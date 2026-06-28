"""Tasks API mixin."""
from typing import Dict, List, Optional
from .base import BaseClient

class TasksAPI:
    """Tasks API methods."""

    def get_tasks(self, workspace_id: Optional[str] = None, project_id: Optional[str] = None) -> List[Dict]:
        """Get all tasks (optionally filtered by project)."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        if project_id:
            return self._send_request('GET', f'workspaces/{ws_id}/projects/{project_id}/tasks')
        return self._send_request('GET', f'workspaces/{ws_id}/tasks')

    def get_task(self, task_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Get a task by ID."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/tasks/{task_id}')

    def add_task(self, workspace_id: Optional[str], name: str,
                 projectId: Optional[str] = None, assigneeIds: Optional[List[str]] = None,
                 tagIds: Optional[List[str]] = None, status: Optional[str] = None,
                 billable: Optional[bool] = None, estimate: Optional[str] = None,
                 userId: Optional[str] = None) -> Dict:
        """Add a new task."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {'name': name}
        if projectId is not None:
            data['projectId'] = projectId
        if assigneeIds is not None:
            data['assigneeIds'] = assigneeIds
        if tagIds is not None:
            data['tagIds'] = tagIds
        if status is not None:
            data['status'] = status
        if billable is not None:
            data['billable'] = billable
        if estimate is not None:
            data['estimate'] = estimate
        if userId is not None:
            data['userId'] = userId
        return self._send_request('POST', f'workspaces/{ws_id}/tasks', data)

    def update_task(self, task_id: str, workspace_id: Optional[str] = None,
                    name: Optional[str] = None, assigneeIds: Optional[List[str]] = None,
                    tagIds: Optional[List[str]] = None, status: Optional[str] = None,
                    archived: Optional[bool] = None) -> Dict:
        """Update a task."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {}
        if name is not None:
            data['name'] = name
        if assigneeIds is not None:
            data['assigneeIds'] = assigneeIds
        if tagIds is not None:
            data['tagIds'] = tagIds
        if status is not None:
            data['status'] = status
        if archived is not None:
            data['archived'] = archived
        return self._send_request('PUT', f'workspaces/{ws_id}/tasks/{task_id}', data)

    def delete_task(self, task_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Delete a task."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('DELETE', f'workspaces/{ws_id}/tasks/{task_id}')

    def get_task_assignees(self, task_id: str, workspace_id: Optional[str] = None) -> List[Dict]:
        """Get assignees for a task."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/tasks/{task_id}/assignees')
