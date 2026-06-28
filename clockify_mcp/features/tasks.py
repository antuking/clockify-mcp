"""Task tools/resources registration."""
from typing import Dict, List, Optional
from fastmcp import FastMCP

from clockify_mcp.clockify_client import ClockifyClient

def register_tools(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.tool("get_tasks", description="Get all tasks in a workspace")
    def get_tasks(workspace_id: Optional[str] = None, project_id: Optional[str] = None) -> List[Dict]:
        return client.get_tasks(workspace_id=workspace_id, project_id=project_id)

    @mcp.tool("get_task", description="Get a task by ID")
    def get_task(task_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.get_task(task_id, workspace_id=workspace_id)

    @mcp.tool("add_task", description="Add a new task")
    def add_task(
        name: str,
        workspace_id: Optional[str] = None,
        projectId: Optional[str] = None,
        assigneeIds: Optional[List[str]] = None,
        tagIds: Optional[List[str]] = None,
        status: Optional[str] = None,
        billable: Optional[bool] = None,
        estimate: Optional[str] = None,
        userId: Optional[str] = None,
    ) -> Dict:
        return client.add_task(
            workspace_id=workspace_id, name=name, projectId=projectId,
            assigneeIds=assigneeIds, tagIds=tagIds, status=status,
            billable=billable, estimate=estimate, userId=userId
        )

    @mcp.tool("update_task", description="Update an existing task")
    def update_task(
        task_id: str,
        workspace_id: Optional[str] = None,
        name: Optional[str] = None,
        assigneeIds: Optional[List[str]] = None,
        tagIds: Optional[List[str]] = None,
        status: Optional[str] = None,
        archived: Optional[bool] = None,
    ) -> Dict:
        return client.update_task(
            task_id, workspace_id=workspace_id, name=name,
            assigneeIds=assigneeIds, tagIds=tagIds, status=status, archived=archived
        )

    @mcp.tool("delete_task", description="Delete a task")
    def delete_task(task_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.delete_task(task_id, workspace_id=workspace_id)

def register_resources(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.resource("clockify://task/{task_id}")
    def get_task_resource(task_id: str) -> Dict:
        return client.get_task(task_id)
