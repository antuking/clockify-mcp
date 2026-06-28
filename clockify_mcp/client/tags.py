"""Tags API mixin."""
from typing import Dict, List, Optional
from .base import BaseClient

class TagsAPI:
    """Tags API methods."""

    def get_tags(self, workspace_id: Optional[str] = None, project_id: Optional[str] = None) -> List[Dict]:
        """Get all tags (optionally filtered by project)."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        if project_id:
            return self._send_request('GET', f'workspaces/{ws_id}/projects/{project_id}/tags')
        return self._send_request('GET', f'workspaces/{ws_id}/tags')

    def get_tag(self, tag_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Get a tag by ID."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/tags/{tag_id}')

    def add_tag(self, workspace_id: Optional[str], name: str, color: Optional[str] = None,
                projectId: Optional[str] = None) -> Dict:
        """Add a new tag."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {'name': name}
        if color is not None:
            data['color'] = color
        if projectId is not None:
            data['projectId'] = projectId
        return self._send_request('POST', f'workspaces/{ws_id}/tags', data)

    def update_tag(self, tag_id: str, workspace_id: Optional[str] = None,
                   name: Optional[str] = None, color: Optional[str] = None) -> Dict:
        """Update a tag."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {}
        if name is not None:
            data['name'] = name
        if color is not None:
            data['color'] = color
        return self._send_request('PUT', f'workspaces/{ws_id}/tags/{tag_id}', data)

    def delete_tag(self, tag_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Delete a tag."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('DELETE', f'workspaces/{ws_id}/tags/{tag_id}')
