"""Tag tools/resources registration."""
from typing import Dict, List, Optional
from fastmcp import FastMCP

from clockify_mcp.clockify_client import ClockifyClient

def register_tools(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.tool("get_tags", description="Get all tags in a workspace")
    def get_tags(workspace_id: Optional[str] = None, project_id: Optional[str] = None) -> List[Dict]:
        return client.get_tags(workspace_id=workspace_id, project_id=project_id)

    @mcp.tool("get_tag", description="Get a tag by ID")
    def get_tag(tag_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.get_tag(tag_id, workspace_id=workspace_id)

    @mcp.tool("add_tag", description="Add a new tag to a workspace")
    def add_tag(
        name: str,
        workspace_id: Optional[str] = None,
        color: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict:
        return client.add_tag(
            workspace_id=workspace_id, name=name, color=color, projectId=projectId
        )

    @mcp.tool("update_tag", description="Update an existing tag")
    def update_tag(
        tag_id: str,
        workspace_id: Optional[str] = None,
        name: Optional[str] = None,
        color: Optional[str] = None,
    ) -> Dict:
        return client.update_tag(tag_id, workspace_id=workspace_id, name=name, color=color)

    @mcp.tool("delete_tag", description="Delete a tag")
    def delete_tag(tag_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.delete_tag(tag_id, workspace_id=workspace_id)

def register_resources(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.resource("clockify://tag/{tag_id}")
    def get_tag_resource(tag_id: str) -> Dict:
        return client.get_tag(tag_id)
