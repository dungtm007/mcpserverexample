from mcp.server.fastmcp import FastMCP 

mcp = FastMCP("Demo")

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

