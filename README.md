# min-llm-back

Minimal OpenAI compatible API Server

## Existing OpenAI Compatible API servers

The easiest way to run a OpenAI compatible server is to use
[Ollama](https://ollama.com/),
[FastChat](https://github.com/lm-sys/FastChat) or 
[Llama.cpp-python](https://github.com/abetlen/llama-cpp-python)

## Ollama

Install [Ollama](https://ollama.com/).

From one terminal:

    OLLAMA_HOST=0.0.0.0:5000 ollama serve 

From another terminal:

    OLLAMA_HOST=0.0.0.0:5000 ollama run openchat

Replace openchat with any model you want to use, see [available models](https://ollama.com/library).


### FastChat

Install FastChat:

    pip install fschat[model_worker] honcho

Run:

    honcho -f Procfile.fschat start

The API server runs on port 5000

Create a new Profile and replace `model_path` if you want to use a different model.

### llama-cpp-python

Install llama-cpp-python:

    pip install llama-cpp-python[server]

For good experience, use acceleration options specific for your hardware, for example, cuda/cublas:

    CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python[server]

Find models on huggingface, and download (or get with curl or wget) them into folder models/:

    mkdir models
    cd models
    https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF/resolve/main/deepseek-coder-6.7b-instruct.Q5_K_M.gguf

Run:

    python -m llama_cpp.server --host 0.0.0.0 --port 5000 --model models/deepseek-coder-6.7b/deepseek-coder-6.7b-instruct.Q5_K_M.gguf

The API server runs on port 5000


## min-llm-back Usage

After `pip install -r requirements.txt`:

    python main.py

## Testing

From another terminal:

    curl http://localhost:5000/v1/chat/completions -H "Content-Type: application/json"  -d @sample.json

Test streaming:

    curl http://localhost:5000/v1/chat/completions -H "Content-Type: application/json"  -d @sample_streaming.json



