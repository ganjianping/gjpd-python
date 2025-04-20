from server import mcp

# Import tools so they get registered via decorators
import tools.csv
import tools.weather

# Entry point to run the server
if __name__ == "__main__":
    mcp.run(transport='stdio')