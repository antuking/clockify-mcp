"""Time Entry tools/resources registration."""
from typing import Dict, List, Optional
from fastmcp import FastMCP

from clockify_mcp.clockify_client import ClockifyClient

def register_tools(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.tool("get_time_entries", description="Get all time entries in a workspace")
    def get_time_entries(workspace_id: Optional[str] = None, 
                         start: Optional[str] = None, end: Optional[str] = None) -> List[Dict]:
        return client.get_time_entries(workspace_id=workspace_id, start=start, end=end)

    @mcp.tool("get_time_entry", description="Get a time entry by ID")
    def get_time_entry(entry_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.get_time_entry(entry_id, workspace_id=workspace_id)

    @mcp.tool("add_time_entry", description="Add a new time entry")
    def add_time_entry(
        start: str,
        workspace_id: Optional[str] = None,
        end: Optional[str] = None,
        projectId: Optional[str] = None,
        taskId: Optional[str] = None,
        tagIds: Optional[List[str]] = None,
        userId: Optional[str] = None,
        description: Optional[str] = None,
        billable: Optional[bool] = None,
    ) -> Dict:
        return client.add_time_entry(
            workspace_id=workspace_id, start=start, end=end,
            projectId=projectId, taskId=taskId, tagIds=tagIds,
            userId=userId, description=description, billable=billable
        )

    @mcp.tool("update_time_entry", description="Update an existing time entry")
    def update_time_entry(
        entry_id: str,
        workspace_id: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        projectId: Optional[str] = None,
        taskId: Optional[str] = None,
        tagIds: Optional[List[str]] = None,
        description: Optional[str] = None,
    ) -> Dict:
        return client.update_time_entry(
            entry_id, workspace_id=workspace_id, start=start, end=end,
            projectId=projectId, taskId=taskId, tagIds=tagIds, description=description
        )

    @mcp.tool("delete_time_entry", description="Delete a time entry")
    def delete_time_entry(entry_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.delete_time_entry(entry_id, workspace_id=workspace_id)

    @mcp.tool("get_time_entries_for_project", description="Get all time entries for a project")
    def get_time_entries_for_project(project_id: str, workspace_id: Optional[str] = None) -> List[Dict]:
        return client.get_time_entries_for_project(project_id, workspace_id=workspace_id)

def register_resources(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.resource("clockify://time-entry/{entry_id}")
    def get_time_entry_resource(entry_id: str) -> Dict:
        return client.get_time_entry(entry_id)
