"""Workspaces API mixin."""
from typing import Dict, List
from .base import BaseClient

class WorkspacesAPI:
    """Workspaces API methods."""

    def get_workspaces(self) -> List[Dict]:
        """Get all workspaces for the authenticated user."""
        return self._send_request('GET', 'workspaces')

    def get_workspace(self, workspace_id: str) -> Dict:
        """Get a workspace by ID."""
        return self._send_request('GET', f'workspaces/{workspace_id}')

    def get_users_in_workspace(self, workspace_id: str) -> List[Dict]:
        """Get all users in a workspace."""
        return self._send_request('GET', f'workspaces/{workspace_id}/users')
