# client.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import CreateMessageResult, TextContent

async def run():
    # 1. Define how to launch the server
    server_params = StdioServerParameters(
        command="python",
        args=["../fast_mcp_server/server.py"],  # Adjust path if needed
        env=None
    )

    # 2. Connect via stdio transport
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            # 3. List and invoke tools/resources
            tools = await session.list_tools()
            print("Available tools:", tools)

            result = await session.call_tool("add", {"a": 5, "b": 7})
            print("add(5, 7) →", result)         # :contentReference[oaicite:16]{index=16}

            greeting, _ = await session.read_resource("greeting://World")
            print(greeting)                     # :contentReference[oaicite:17]{index=17}

if __name__ == "__main__":
    asyncio.run(run())
