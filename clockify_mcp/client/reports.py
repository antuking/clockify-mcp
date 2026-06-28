"""Reports API mixin."""
from typing import Dict, List, Optional
from .base import BaseClient

class ReportsAPI:
    """Reports API methods."""

    def __init__(self):
        # Reports API uses a different base URL
        pass

    def get_reports_summary(self, workspace_id: str, start_date: str, end_date: str) -> Dict:
        """Get time entry summary report for a workspace."""
        # Reports API endpoint
        url = f'https://reports.clockify.me/v1/reports/summary'
        headers = {
            'X-Api-Key': self.api_key,
            'Content-Type': 'application/json',
        }
        params = {
            'workspaceId': workspace_id,
            'startDate': start_date,
            'endDate': end_date,
        }
        response = self.session.get(url, params=params, headers=headers)
        if response.status_code >= 300:
            try:
                error = response.json()
            except Exception:
                error = response.text
            raise Exception(f"Clockify Reports API returned HTTP {response.status_code}: {error}")
        return response.json() if response.content else {}

    def get_reports_detailed(self, workspace_id: str, start_date: str, end_date: str) -> List[Dict]:
        """Get detailed time entry report for a workspace."""
        url = f'https://reports.clockify.me/v1/reports/detailed'
        headers = {
            'X-Api-Key': self.api_key,
            'Content-Type': 'application/json',
        }
        params = {
            'workspaceId': workspace_id,
            'startDate': start_date,
            'endDate': end_date,
        }
        response = self.session.get(url, params=params, headers=headers)
        if response.status_code >= 300:
            try:
                error = response.json()
            except Exception:
                error = response.text
            raise Exception(f"Clockify Reports API returned HTTP {response.status_code}: {error}")
        return response.json().get('timeentries', []) if response.content else []
