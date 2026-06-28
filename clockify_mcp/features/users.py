"""User tools/resources registration."""
from typing import Dict, List, Optional
from fastmcp import FastMCP

from clockify_mcp.clockify_client import ClockifyClient

def register_tools(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.tool("get_current_user", description="Get the current authenticated user")
    def get_current_user() -> Dict:
        return client.get_current_user()

    @mcp.tool("get_users", description="Get all users in a workspace")
    def get_users(workspace_id: Optional[str] = None) -> List[Dict]:
        return client.get_users(workspace_id=workspace_id)

    @mcp.tool("get_user", description="Get a user by ID")
    def get_user(user_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.get_user(user_id, workspace_id=workspace_id)

    @mcp.tool("add_user", description="Add a new user to a workspace")
    def add_user(
        name: str,
        email: str,
        workspace_id: Optional[str] = None,
        role: Optional[str] = None,
        status: Optional[str] = None,
        hourly_rate: Optional[Dict] = None,
    ) -> Dict:
        return client.add_user(
            workspace_id=workspace_id, name=name, email=email,
            role=role, status=status, hourly_rate=hourly_rate
        )

    @mcp.tool("update_user", description="Update an existing user")
    def update_user(
        user_id: str,
        workspace_id: Optional[str] = None,
        name: Optional[str] = None,
        email: Optional[str] = None,
        role: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict:
        return client.update_user(
            user_id, workspace_id=workspace_id, name=name,
            email=email, role=role, status=status
        )

    @mcp.tool("delete_user", description="Delete a user from a workspace")
    def delete_user(user_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.delete_user(user_id, workspace_id=workspace_id)

def register_resources(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.resource("clockify://user/{user_id}")
    def get_user_resource(user_id: str) -> Dict:
        return client.get_user(user_id)
