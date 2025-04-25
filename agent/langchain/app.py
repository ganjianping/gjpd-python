from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
from langchain_core.messages import AIMessage, HumanMessage
from agent import create_agent
from typing import Dict, Any, List
from pydantic import BaseModel, Field

# 1. Define simple models for input/output
class Message(BaseModel):
    type: str = Field(..., description="Message type, e.g. 'human' or 'ai'")
    content: str = Field(..., description="Message content")

class ChatRequest(BaseModel):
    messages: List[Message] = Field(..., description="List of conversation messages")

# 2. Create FastAPI app
app = FastAPI(
    title="LangChain Agent API",
    version="1.0",
    description="POST to /agent/invoke to interact with your AI agent"
)

# 3. Initialize your LangChain agent executor
agent_executor = create_agent()

# 4. Custom route to handle agent invocation with explicit schema
@app.post("/agent/invoke", response_model=Dict[str, Any])
async def agent_invoke(request: ChatRequest):
    """
    Invoke the agent with a list of messages.
    
    Example:
    ```json
    {
        "messages": [
            {"type": "human", "content": "What's the weather in San Francisco?"}
        ]
    }
    ```
    """
    # Convert the request to the format expected by LangChain
    formatted_messages = []
    for msg in request.messages:
        if msg.type == "human":
            formatted_messages.append(HumanMessage(content=msg.content))
        elif msg.type == "ai":
            formatted_messages.append(AIMessage(content=msg.content))
    
    # Invoke the agent
    result = agent_executor.invoke({"messages": formatted_messages})
    return result

# 5. Simple async root endpoint
@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the LangChain Agent API. "
                   "Send POST requests to /agent/invoke to chat with the agent."
    }

# 6. Example endpoint with explicit schema to test if OpenAPI works
@app.post("/echo")
async def echo(message: Dict[str, Any]):
    """Simple echo endpoint to test if API is working"""
    return {"received": message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
