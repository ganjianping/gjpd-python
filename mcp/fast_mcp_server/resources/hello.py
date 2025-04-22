from server import mcp

@mcp.resource("greeting://{name}")
def greet(name: str) -> str:
    return f"Hello, {name}!"