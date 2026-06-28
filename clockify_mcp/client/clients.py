"""Clients API mixin."""
from typing import Dict, List, Optional
from .base import BaseClient

class ClientsAPI:
    """Clients API methods."""

    def get_clients(self, workspace_id: Optional[str] = None) -> List[Dict]:
        """Get all clients in a workspace."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/clients')

    def get_client(self, client_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Get a client by ID."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('GET', f'workspaces/{ws_id}/clients/{client_id}')

    def add_client(self, workspace_id: Optional[str], name: str, 
                   billable: Optional[bool] = None) -> Dict:
        """Add a new client to a workspace."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {'name': name}
        if billable is not None:
            data['billable'] = billable
        return self._send_request('POST', f'workspaces/{ws_id}/clients', data)

    def update_client(self, client_id: str, workspace_id: Optional[str] = None,
                      name: Optional[str] = None, billable: Optional[bool] = None) -> Dict:
        """Update a client."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        data = {}
        if name is not None:
            data['name'] = name
        if billable is not None:
            data['billable'] = billable
        return self._send_request('PUT', f'workspaces/{ws_id}/clients/{client_id}', data)

    def delete_client(self, client_id: str, workspace_id: Optional[str] = None) -> Dict:
        """Delete a client."""
        ws_id = workspace_id or self.workspace_id
        if not ws_id:
            raise ValueError('workspace_id is required')
        return self._send_request('DELETE', f'workspaces/{ws_id}/clients/{client_id}')
