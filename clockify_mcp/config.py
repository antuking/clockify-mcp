"""Configuration module for Clockify MCP server."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Clockify configuration
CLOCKIFY_API_KEY = os.getenv('CLOCKIFY_API_KEY')
CLOCKIFY_WORKSPACE_ID = os.getenv('CLOCKIFY_WORKSPACE_ID')

def validate_config():
    """Validate that all required environment variables are set."""
    if not CLOCKIFY_API_KEY:
        raise ValueError(
            "Missing Clockify configuration. Please set CLOCKIFY_API_KEY "
            "and optionally CLOCKIFY_WORKSPACE_ID environment variables."
        )
