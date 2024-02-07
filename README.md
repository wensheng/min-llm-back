# min-llm-back

Minimal OpenAI compatible API Server

## Usage

After `pip install -r requirements.txt`:

    python main.py

## Testing

From another terminal:

    curl http://localhost:5000/v1/chat/completion -H "Content-Type: application/json"  -d @sample.json



