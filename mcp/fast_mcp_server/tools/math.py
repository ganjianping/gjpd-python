# This is a simple math tool for the MCP server.
from server import mcp

# Expose a simple addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
