"""Entry point for the Clockify MCP server when run as a module."""
import sys
import asyncio

from clockify_mcp.mcp_server import mcp

def main():
    """Run the Clockify MCP server."""
    print("Starting Clockify MCP server in stdio mode", file=sys.stderr)
    asyncio.run(mcp.run_stdio_async())

if __name__ == "__main__":
    main()
