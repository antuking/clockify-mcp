"""Workspace tools/resources registration."""
from typing import Dict, List
from fastmcp import FastMCP

from clockify_mcp.clockify_client import ClockifyClient

def register_tools(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.tool("get_workspaces", description="Get all workspaces for the authenticated user")
    def get_workspaces() -> List[Dict]:
        return client.get_workspaces()

    @mcp.tool("get_workspace", description="Get a workspace by ID")
    def get_workspace(workspace_id: str) -> Dict:
        return client.get_workspace(workspace_id)

def register_resources(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.resource("clockify://workspace/{workspace_id}")
    def get_workspace_resource(workspace_id: str) -> Dict:
        return client.get_workspace(workspace_id)
