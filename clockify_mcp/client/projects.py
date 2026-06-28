"""Projects API mixin."""
from typing import Dict, List, Optional
from .base import BaseClient

class ProjectsAPI:
    """Projects API methods."""

    def get_projects(self, workspace_id: Optional[str] = None) -> List[Dict]:
        """Get all projects in a workspace."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/projects')

    def get_project(self, project_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Get a project by ID."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/projects/{project_id}')

    def add_project(self, workspace_id: Optional[str], name: str, 
                   color: Optional[str] = None, 
                   billable: Optional[bool] = None,
                   client_id: Optional[str] = None,
                   hourly_rate: Optional[Dict] = None,
                   memberships: Optional[List[Dict]] = None) -> Dict:
        """Add a new project to a workspace."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {'name': name}
        if color is not None:
            data['color'] = color
        if billable is not None:
            data['billable'] = billable
        if client_id is not None:
            data['clientId'] = client_id
        if hourly_rate is not None:
            data['hourlyRate'] = hourly_rate
        if memberships is not None:
            data['memberships'] = memberships
        return self._send_request('POST', f'workspaces/{ws_id}/projects', data)

    def update_project(self, project_id: str, workspace_id: Optional[str] = None, 
                       name: Optional[str] = None, color: Optional[str] = None,
                       billable: Optional[bool] = None, archived: Optional[bool] = None) -> Dict:
        """Update a project."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {}
        if name is not None:
            data['name'] = name
        if color is not None:
            data['color'] = color
        if billable is not None:
            data['billable'] = billable
        if archived is not None:
            data['archived'] = archived
        return self._send_request('PUT', f'workspaces/{ws_id}/projects/{project_id}', data)

    def delete_project(self, project_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Delete a project."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('DELETE', f'workspaces/{ws_id}/projects/{project_id}')
