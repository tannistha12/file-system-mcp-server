from mcp.server.fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("hello-server")

@mcp.tool()
def hello_server() -> str:
    """A simple greeting tool that returns a hello message."""
    return "Hello from server"

if __name__ == "__main__":
    # Run the server with default transport (stdio)
    mcp.run(transport="stdio")