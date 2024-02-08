"""
Minimal OpenAI compatible API server using Hugging Face's transformers
"""
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForCausalLM, AutoTokenizer
from models import (
    OAIChatCompletionResponse,
    OAIErrorResponse,
    OAIChatCompletionRequest,
)


device = "cuda"

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen1.5-7B-Chat-AWQ",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-7B-Chat-AWQ")

app = FastAPI(title="Minimal OpenAI compatible API Server")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return {"message": "Hello World"}


@app.post('/v1/chat/completions',
          response_model=Union[OAIChatCompletionResponse, OAIErrorResponse])
async def chat_completion(request: Request, body: OAIChatCompletionRequest):
    """
    Request body:
      {
        'model': 'whatever',
        'messages': [
          {'role': 'system', 'content': 'You are a helpful assistant.'},
          {'role': 'user', 'content': 'Give me a short introduction to LLM.'}
        ],
        'temperature': 0.8,
        'top_p': 0.95,
        'min_p': 0.05,
        'top_k': 40,
        'repeat_penalty': 0,
      }
    """
    rdict = body.dict()
    textin = tokenizer.apply_chat_template(
        rdict['messages'],
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([textin], return_tensors="pt").to(device)
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    async def stream_response():
        yield response.encode()

    return StreamingResponse(stream_response(), media_type="text/plain")
