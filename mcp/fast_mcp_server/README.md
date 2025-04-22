# GJPD MCP Server

A Model Context Protocol (MCP) server implementation for Claude that extends its capabilities with custom tools.

## Setup

### Prerequisites
- Python 3.9+
- [uv](https://github.com/astral-sh/uv) package manager
- Claude for Desktop application

### Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

## Development

### Managing Dependencies
```bash
# Add new packages
uv add "mcp[cli]" pandas

# Update dependencies
uv pip freeze > requirements.txt
```

### Running the Server Locally
```bash
# Start the server with uv
uv run main.py   
```

### Run in development mode
```bash
uv run main.py --dev
uv run mcp dev server.py
```


## Claude for Desktop Integration

### Configuration
1. Edit Claude for Desktop configuration file:
   ```bash
   nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. Add the MCP server configuration:
   ```json
   {
     "mcpServers": {
       "GJPD": {
         "command": "/full/path/to/uv",
         "args": [
           "--directory", 
           "~/Code/gjp-demo/gjpd-python/mcp/fast_mcp_server",
           "run",
           "main.py"
         ],
         "transportType": "stdio"
       }
     }
   }
   ```

   > **Note:** Replace `/full/path/to/uv` with your actual uv path (find it using `which uv`).

3. Restart Claude for Desktop to apply changes

### Troubleshooting

#### Viewing Logs
```bash
# View MCP-related logs
tail -n 20 -f ~/Library/Logs/Claude/mcp*.log

# Use the MCP inspector for debugging
npx @modelcontextprotocol/inspector
```

#### Common Issues
- **"spawn uv ENOENT" error**: The `uv` command can't be found. Use the full path from `which uv`.
- **Connection failures**: Ensure the server name matches between the config and your code.
- **Runtime errors**: Check the logs for Python exceptions and error messages.

## Available Tools

### Weather Tool
Fetches current weather data and forecasts.

Example queries:
- "What's the weather in Sacramento?"
- "What are the active weather alerts in Texas?"

### CSV Tool
Provides CSV file parsing and analysis capabilities.

Example queries:
- "Analyze this CSV file for trends"
- "Create a summary of this dataset"

## Contributing

1. Create feature branches for new tools
2. Add new tools in the `tools/` directory 
3. Import tools in `main.py` to register them
4. Update this README with documentation for new tools