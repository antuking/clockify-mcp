"""Composable Clockify API client."""
from clockify_mcp.client.base import BaseClient
from clockify_mcp.client.workspaces import WorkspacesAPI
from clockify_mcp.client.projects import ProjectsAPI
from clockify_mcp.client.tasks import TasksAPI
from clockify_mcp.client.clients import ClientsAPI
from clockify_mcp.client.tags import TagsAPI
from clockify_mcp.client.users import UsersAPI
from clockify_mcp.client.time_entries import TimeEntriesAPI
from clockify_mcp.client.reports import ReportsAPI

class ClockifyClient(
    BaseClient,
    WorkspacesAPI,
    ProjectsAPI,
    TasksAPI,
    ClientsAPI,
    TagsAPI,
    UsersAPI,
    TimeEntriesAPI,
    ReportsAPI,
):
    """Clockify API client composed of feature mixins."""

__all__ = ["ClockifyClient"]
