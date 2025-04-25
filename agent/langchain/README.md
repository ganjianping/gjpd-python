# Langchain Agent

This is a Langchain agent implementation that uses OpenAI models and exposes the agent functionality through a FastAPI service.

## Setup

### Dependencies
Install the required packages:
```bash
# Using uv package manager
uv add langchain openai fastapi uvicorn langchain-community langgraph langserve duckduckgo-search
uv pip compile requirements.in --quiet --output-file requirements.txt
uv pip sync requirements.txt


# Or using pip
pip install langchain openai fastapi uvicorn langchain-community langgraph langserve duckduckgo-search
```

### API Keys
Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

For Tavily search functionality (optional):
```bash
export TAVILY_API_KEY="your-tavily-api-key-here"
```
If TAVILY_API_KEY is not set, the system will fallback to using DuckDuckGo search.

## Usage

### Running the Agent API
Start the FastAPI server:
```bash
cd agent/langchain
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`:
- API documentation: `http://localhost:8000/docs`
- Agent endpoint: `http://localhost:8000/agent`

### Making Requests
You can interact with the agent using HTTP requests:

```python
import requests
import json

response = requests.post(
    "http://localhost:8000/agent/invoke",
    json={
        "messages": [
            {"type": "human", "content": "What's the weather in San Francisco?"}
        ]
    }
)
print(json.dumps(response.json(), indent=2))
```

### Testing the Agent
You can directly test the agent by running:
```bash
python agent.py
```

## Implementation Details

### Agent Components
- **Tools**: Uses the Tavily search tool for web queries
- **Model**: OpenAI's GPT-4 model
- **Framework**: LangGraph React agent for reasoning and action
- **API**: FastAPI with LangServe for HTTP endpoints

### Code Structure
- `agent.py`: Core agent implementation
- `app.py`: FastAPI application that exposes the agent