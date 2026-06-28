"""Shared base client for Clockify API calls."""
import json
from typing import Dict, List, Any, Optional

import requests

class BaseClient:
    """Base Clockify API client with auth and request helpers."""

    def __init__(self, api_key: str, workspace_id: Optional[str] = None):
        """
        Initialize the Clockify API client.

        Args:
            api_key: Your Clockify API key
            workspace_id: Optional default workspace ID
        """
        self.api_key = api_key
        self.workspace_id = workspace_id
        self.base_url = 'https://api.clockify.me/api/v1/'

        self.session = requests.Session()
        self.session.headers.update({
            'X-Api-Key': api_key,
            'Content-Type': 'application/json',
        })

    def _send_request(self, method: str, uri: str, data: Optional[Dict] = None) -> Any:
        """
        Send a request to the Clockify API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            uri: API endpoint URI
            data: Request data for POST/PUT requests

        Returns:
            Response data from Clockify

        Raises:
            Exception: If the request fails
        """
        url = self.base_url + uri

        if method.upper() == 'GET':
            response = self.session.get(url)
        elif method.upper() == 'POST':
            response = self.session.post(url, data=json.dumps(data) if data else None)
        elif method.upper() == 'PUT':
            response = self.session.put(url, data=json.dumps(data) if data else None)
        elif method.upper() == 'DELETE':
            response = self.session.delete(url)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        if response.status_code >= 300:
            try:
                error = response.json()
            except Exception:
                error = response.text
            raise Exception(f"Clockify API returned HTTP {response.status_code}: {error}")

        return response.json() if response.content else {}
