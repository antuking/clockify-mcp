"""Client tools/resources registration."""
from typing import Dict, List, Optional
from fastmcp import FastMCP

from clockify_mcp.clockify_client import ClockifyClient

def register_tools(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.tool("get_clients", description="Get all clients in a workspace")
    def get_clients(workspace_id: Optional[str] = None) -> List[Dict]:
        return client.get_clients(workspace_id=workspace_id)

    @mcp.tool("get_client", description="Get a client by ID")
    def get_client(client_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.get_client(client_id, workspace_id=workspace_id)

    @mcp.tool("add_client", description="Add a new client to a workspace")
    def add_client(
        name: str,
        workspace_id: Optional[str] = None,
        billable: Optional[bool] = None,
    ) -> Dict:
        return client.add_client(
            workspace_id=workspace_id, name=name, billable=billable
        )

    @mcp.tool("update_client", description="Update an existing client")
    def update_client(
        client_id: str,
        workspace_id: Optional[str] = None,
        name: Optional[str] = None,
        billable: Optional[bool] = None,
    ) -> Dict:
        return client.update_client(
            client_id, workspace_id=workspace_id, name=name, billable=billable
        )

    @mcp.tool("delete_client", description="Delete a client")
    def delete_client(client_id: str, workspace_id: Optional[str] = None) -> Dict:
        return client.delete_client(client_id, workspace_id=workspace_id)

def register_resources(mcp: FastMCP, client: ClockifyClient) -> None:
    @mcp.resource("clockify://client/{client_id}")
    def get_client_resource(client_id: str) -> Dict:
        return client.get_client(client_id)
