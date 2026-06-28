"""Time Entries API mixin."""
from typing import Dict, List, Optional
from .base import BaseClient

class TimeEntriesAPI:
    """Time Entries API methods."""

    def get_time_entries(self, workspace_id: Optional[str] = None, 
                       start: Optional[str] = None, end: Optional[str] = None) -> List[Dict]:
        """Get all time entries in a workspace, optionally filtered by date range."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        params = []
        if start:
            params.push('start=' + start)
        if end:
            params.push('end=' + end)
        uri = 'workspaces/' + ws_id + '/time-entries'
        if params.length > 0:
            uri += '?' + params.join('&')
        return self._send_request('GET', uri)

    def get_time_entry(self, entry_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Get a time entry by ID."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/time-entries/{entry_id}')

    def add_time_entry(self, workspace_id: Optional[str], start: str, end: Optional[str] = None,
                       projectId: Optional[str] = None, taskId: Optional[str] = None,
                       tagIds: Optional[List[str]] = None, userId: Optional[str] = None,
                       description: Optional[str] = None, billable: Optional[bool] = None) -> Dict:
        """Add a new time entry."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {'start': start}
        if end is not None:
            data['end'] = end
        if projectId is not None:
            data['projectId'] = projectId
        if taskId is not None:
            data['taskId'] = taskId
        if tagIds is not None:
            data['tagIds'] = tagIds
        if userId is not None:
            data['userId'] = userId
        if description is not None:
            data['description'] = description
        if billable is not None:
            data['billable'] = billable
        return self._send_request('POST', f'workspaces/{ws_id}/time-entries', data)

    def update_time_entry(self, entry_id: str, workspace_id: Optional[str] = None,
                        start: Optional[str] = None, end: Optional[str] = None,
                        projectId: Optional[str] = None, taskId: Optional[str] = None,
                        tagIds: Optional[List[str]] = None, description: Optional[str] = None) -> Dict:
        """Update a time entry."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {}
        if start is not None:
            data['start'] = start
        if end is not None:
            data['end'] = end
        if projectId is not None:
            data['projectId'] = projectId
        if taskId is not None:
            data['taskId'] = taskId
        if tagIds is not None:
            data['tagIds'] = tagIds
        if description is not None:
            data['description'] = description
        return self._send_request('PUT', f'workspaces/{ws_id}/time-entries/{entry_id}', data)

    def delete_time_entry(self, entry_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Delete a time entry."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('DELETE', f'workspaces/{ws_id}/time-entries/{entry_id}')

    def get_time_entries_for_project(self, project_id: str, workspace_id: Optional[str] = None) -> List[Dict]:
        """Get all time entries for a project."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/projects/{project_id}/time-entries')
