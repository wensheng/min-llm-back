# min-llm-back

Minimal OpenAI compatible API Server

## Existing OpenAI Compatible API servers

The easiest way to run a OpenAI compatible server is to use
[FastChat](https://github.com/lm-sys/FastChat) or 
[Llama.cpp-python](https://github.com/abetlen/llama-cpp-python)

### FastChat

Install FastChat:

    pip install fschat[model_worker] honcho

Run:

    honcho -f Procfile.fschat start

The API server runs on port 8080

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

    python -m llama_cpp.server --host 0.0.0.0 --port 18080 --model models/deepseek-coder-6.7b/deepseek-coder-6.7b-instruct.Q5_K_M.gguf

The API server runs on port 18080


## min-llm-back Usage

After `pip install -r requirements.txt`:

    python main.py

## Testing

From another terminal:

    curl http://localhost:5000/v1/chat/completion -H "Content-Type: application/json"  -d @sample.json



