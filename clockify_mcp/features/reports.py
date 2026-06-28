"""Report tools registration."""
from typing import Dict, List, Optional
from fastmcp import FastMCP

from clockify_mcp.clockify_client import ClockifyClient

def register_tools(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.tool("get_reports_summary", description="Get time entry summary report for a workspace")
    def get_reports_summary(
        workspace_id: str,
        start_date: str,
        end_date: str,
    ) -> Dict:
        return client.get_reports_summary(workspace_id, start_date, end_date)

    @mcp.tool("get_reports_detailed", description="Get detailed time entry report for a workspace")
    def get_reports_detailed(
        workspace_id: str,
        start_date: str,
        end_date: str,
    ) -> List[Dict]:
        return client.get_reports_detailed(workspace_id, start_date, end_date)

def register_resources(mcp: FastMCP, client: ClockifyClient) -> None:
    pass
