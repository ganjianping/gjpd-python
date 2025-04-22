from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()

# Regular FastAPI endpoint
@app.get("/items/{item_id}", operation_id="get_item")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

# Attach MCP server
mcp = FastApiMCP(
    app,
    name="MyAPI-MCP",
    description="MCP server over FastAPI",
    base_url="http://localhost:8000"
)
mcp.mount()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # :contentReference[oaicite:14]{index=14}
