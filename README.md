# Clockify MCP Server

A Model Context Protocol (MCP) server for Clockify that allows interaction with Clockify's time tracking entities through a standardized protocol.

## Features

- **Full CRUD Support**: Comprehensive Create, Read, Update, and Delete operations for all core Clockify entities.
- **Access to Clockify entities**:
  - Workspaces
  - Projects
  - Tasks
  - Clients
  - Tags
  - Users
  - Time Entries
  - Reports
- **Time Tracking**: Start/stop timers, log time manually, and manage time entries.
- **Full MCP Support**: Standardized protocol for use with any MCP client (Claude Desktop, Cursor, Windsurf, etc.).

## Quick Start (Local Setup)

### 1. Prerequisites
- [uv](https://github.com/astral-sh/uv) installed on your system.
- Clockify API key (get it from [Clockify Profile Settings](https://clockify.me/user/settings)).

### 2. Installation
```bash
git clone https://github.com/yourusername/clockify-mcp.git
cd clockify-mcp
uv sync
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
CLOCKIFY_API_KEY=your-api-key
CLOCKIFY_WORKSPACE_ID=your-workspace-id  # optional
```

### 4. Running the Server
```bash
uv run clockify-mcp
```

### 5. Using with MCP Clients (Local)

#### Codex CLI
```bash
codex mcp add clockify_mcp \
  --env CLOCKIFY_API_KEY=<CLOCKIFY_API_KEY> \
  --env CLOCKIFY_WORKSPACE_ID=<CLOCKIFY_WORKSPACE_ID> \
  -- uv --directory <REPO_PATH> run clockify-mcp
```

#### Claude Desktop
```json
{
  "mcpServers": {
    "clockify": {
      "command": "uv",
      "args": ["--directory", "<REPO_PATH>", "run", "clockify-mcp"],
      "env": {
        "CLOCKIFY_API_KEY": "your-api-key",
        "CLOCKIFY_WORKSPACE_ID": "your-workspace-id"
      }
    }
  }
}
```

#### Cursor / Windsurf
```json
{
  "name": "Clockify MCP",
  "command": "uv",
  "args": ["--directory", "<REPO_PATH>", "run", "clockify-mcp"],
  "env": {
    "CLOCKIFY_API_KEY": "your-api-key",
    "CLOCKIFY_WORKSPACE_ID": "your-workspace-id"
  }
}
```

## API Coverage

This server implements the following Clockify API endpoints:

### Workspaces
- `get_workspaces` - List all workspaces
- `get_workspace` - Get workspace by ID

### Projects
- `get_projects` - List all projects in a workspace
- `get_project` - Get project by ID
- `add_project` - Create a new project
- `update_project` - Update an existing project
- `delete_project` - Delete a project

### Tasks
- `get_tasks` - List all tasks
- `get_task` - Get task by ID
- `add_task` - Create a new task
- `update_task` - Update an existing task
- `delete_task` - Delete a task

### Clients
- `get_clients` - List all clients
- `get_client` - Get client by ID
- `add_client` - Create a new client
- `update_client` - Update an existing client
- `delete_client` - Delete a client

### Tags
- `get_tags` - List all tags
- `get_tag` - Get tag by ID
- `add_tag` - Create a new tag
- `update_tag` - Update an existing tag
- `delete_tag` - Delete a tag

### Users
- `get_current_user` - Get the authenticated user
- `get_users` - List all users in a workspace
- `get_user` - Get user by ID
- `add_user` - Add a user to a workspace
- `update_user` - Update a user
- `delete_user` - Remove a user from a workspace

### Time Entries
- `get_time_entries` - List time entries (with optional date range)
- `get_time_entry` - Get time entry by ID
- `add_time_entry` - Create a new time entry
- `update_time_entry` - Update an existing time entry
- `delete_time_entry` - Delete a time entry
- `get_time_entries_for_project` - Get time entries for a project

## Development

This server is built using:
- [FastMCP](https://github.com/jlowin/fastmcp) - A Python framework for building MCP servers
- [Requests](https://requests.readthedocs.io/) - For HTTP communication
- [python-dotenv](https://github.com/theskumar/python-dotenv) - For environment management
