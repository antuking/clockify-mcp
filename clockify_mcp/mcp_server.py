"""MCP server implementation for Clockify."""
from fastmcp import FastMCP

from clockify_mcp.clockify_client import ClockifyClient
from clockify_mcp.config import CLOCKIFY_API_KEY, CLOCKIFY_WORKSPACE_ID, validate_config
from clockify_mcp.features import (
    workspaces,
    projects,
    tasks,
    clients,
    tags,
    users,
    time_entries,
    reports,
)

class ClockifyMCPServer(FastMCP):
    """MCP server for Clockify integration using FastMCP."""

    def __init__(self):
        """Initialize the Clockify MCP server."""
        super().__init__(name="Clockify MCP Server", version="0.1.0")
        self.client = ClockifyClient(
            api_key=CLOCKIFY_API_KEY or "placeholder",
            workspace_id=CLOCKIFY_WORKSPACE_ID,
        )
        self._register_features()

    async def run_stdio_async(self):
        """Run the server in stdio mode asynchronously, validating config first."""
        validate_config()
        await super().run_stdio_async()

    def run_stdio(self):
        """Run the server in stdio mode, validating config first."""
        validate_config()
        super().run_stdio()

    def _register_features(self) -> None:
        """Register all Clockify features (tools and resources) with the MCP server."""
        features = (
            workspaces,
            projects,
            tasks,
            clients,
            tags,
            users,
            time_entries,
            reports,
        )
        for module in features:
            if hasattr(module, "register_tools"):
                module.register_tools(self, self.client)
            if hasattr(module, "register_resources"):
                module.register_resources(self, self.client)

# Create a global instance for use as an entrypoint (e.g., clockify_mcp.mcp_server:mcp)
mcp = ClockifyMCPServer()
