"""Project tools/resources registration."""
from typing import Dict, List, Optional
from fastmcp import FastMCP

from clockify_mcp.clockify_client import ClockifyClient

def register_tools(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.tool("get_projects", description="Get all projects in a workspace")
    def get_projects(workspace_id: Optional[str] = None) -> List[Dict]:
        return client.get_projects(workspace_id=workspace_id)

    @mcp.tool("get_project", description="Get a project by ID")
    def get_project(project_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.get_project(project_id, workspace_id=workspace_id)

    @mcp.tool("add_project", description="Add a new project to a workspace")
    def add_project(
        name: str,
        workspace_id: Optional[str] = None,
        color: Optional[str] = None,
        billable: Optional[bool] = None,
        client_id: Optional[str] = None,
        hourly_rate: Optional[Dict] = None,
    ) -> Dict:
        return client.add_project(
            workspace_id=workspace_id, name=name, color=color,
            billable=billable, client_id=client_id, hourly_rate=hourly_rate
        )

    @mcp.tool("update_project", description="Update an existing project")
    def update_project(
        project_id: str,
        workspace_id: Optional[str] = None,
        name: Optional[str] = None,
        color: Optional[str] = None,
        billable: Optional[bool] = None,
        archived: Optional[bool] = None,
    ) -> Dict:
        return client.update_project(
            project_id, workspace_id=workspace_id, name=name,
            color=color, billable=billable, archived=archived
        )

    @mcp.tool("delete_project", description="Delete a project")
    def delete_project(project_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.delete_project(project_id, workspace_id=workspace_id)

def register_resources(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.resource("clockify://project/{project_id}")
    def get_project_resource(project_id: str) -> Dict:
        return client.get_project(project_id)
