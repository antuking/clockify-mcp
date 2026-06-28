"""Users API mixin."""
from typing import Dict, List, Optional
from .base import BaseClient

class UsersAPI:
    """Users API methods."""

    def get_current_user(self) -> Dict:
        """Get the current authenticated user."""
        return self._send_request('GET', 'user')

    def get_users(self, workspace_id: Optional[str] = None) -> List[Dict]:
        """Get all users in a workspace."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/users')

    def get_user(self, user_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Get a user by ID."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/users/{user_id}')

    def add_user(self, workspace_id: Optional[str], name: str, email: str,
                 role: Optional[str] = None, status: Optional[str] = None,
                 hourly_rate: Optional[Dict] = None) -> Dict:
        """Add a new user to a workspace."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {'name': name, 'email': email}
        if role is not None:
            data['role'] = role
        if status is not None:
            data['status'] = status
        if hourly_rate is not None:
            data['hourlyRate'] = hourly_rate
        return self._send_request('POST', f'workspaces/{ws_id}/users', data)

    def update_user(self, user_id: str, workspace_id: Optional[str] = None,
                    name: Optional[str] = None, email: Optional[str] = None,
                    role: Optional[str] = None, status: Optional[str] = None) -> Dict:
        """Update a user."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {}
        if name is not None:
            data['name'] = name
        if email is not None:
            data['email'] = email
        if role is not None:
            data['role'] = role
        if status is not None:
            data['status'] = status
        return self._send_request('PUT', f'workspaces/{ws_id}/users/{user_id}', data)

    def delete_user(self, user_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Delete a user from a workspace."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('DELETE', f'workspaces/{ws_id}/users/{user_id}')
