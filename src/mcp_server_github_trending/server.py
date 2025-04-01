from enum import Enum
import json
from typing import Sequence

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from gtrending import fetch_repos, fetch_developers


class ToolName(Enum):
    GET_REPOSITORIES = "get_github_trending_repositories"
    GET_DEVELOPERS = "get_github_trending_developers"


async def serve() -> None:
    server = Server("mcp-github-trending")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        """List available github trending tools."""
        return [
            Tool(
                name=ToolName.GET_REPOSITORIES.value,
                description="Get trending repositories on github",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "language": {
                            "type": "string",
                            "description": "Language to filter repositories by",
                        },
                        "since": {
                            "type": "string",
                            "description": "Time period to filter repositories by",
                            "enum": ["daily", "weekly", "monthly"],
                        },
                        "spoken_language": {
                            "type": "string",
                            "description": "Spoken language to filter repositories by",
                        },
                    },
                },
            ),
            Tool(
                name=ToolName.GET_DEVELOPERS.value,
                description="Get trending developers on github",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "language": {
                            "type": "string",
                            "description": "Language to filter repositories by",
                        },
                        "since": {
                            "type": "string",
                            "description": "Time period to filter repositories by",
                            "enum": ["daily", "weekly", "monthly"],
                        },
                        "spoken_language": {
                            "type": "string",
                            "description": "Spoken language to filter repositories by",
                        },
                    },
                },
            ),
        ]

    @server.call_tool()
    async def call_tool(
        name: str, arguments: dict
    ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
        """Handle tool calls for github trending queries."""
        try:
            match name:
                case ToolName.GET_REPOSITORIES.value:
                    # Get parameters from arguments
                    language = arguments.get("language")
                    since = arguments.get("since", "daily")
                    spoken_language = arguments.get("spoken_language")
                    
                    # Fetch trending repositories
                    repos = fetch_repos(
                        language=language,
                        spoken_language_code=spoken_language,
                        since=since
                    )
                    
                    # Format the response
                    formatted_repos = []
                    for repo in repos:
                        formatted_repo = {
                            "name": repo["name"],
                            "fullname": repo["fullname"],
                            "url": repo["url"],
                            "description": repo["description"],
                            "language": repo["language"],
                            "stars": repo["stars"],
                            "forks": repo["forks"],
                            "current_period_stars": repo["currentPeriodStars"]
                        }
                        formatted_repos.append(formatted_repo)
                    
                    return [
                        TextContent(type="text", text=json.dumps(formatted_repos, indent=2))
                    ]

                case ToolName.GET_DEVELOPERS.value:
                    # Get parameters from arguments
                    language = arguments.get("language")
                    since = arguments.get("since", "daily")
                    
                    # Fetch trending developers
                    developers = fetch_developers(
                        language=language,
                        since=since
                    )
                    
                    # Format the response
                    formatted_devs = []
                    for dev in developers:
                        formatted_dev = {
                            "username": dev["username"],
                            "name": dev["name"],
                            "url": dev["url"],
                            "avatar": dev["avatar"],
                            "repo": {
                                "name": dev["repo"]["name"],
                                "description": dev["repo"]["description"],
                                "url": dev["repo"]["url"]
                            }
                        }
                        formatted_devs.append(formatted_dev)
                    
                    return [
                        TextContent(type="text", text=json.dumps(formatted_devs, indent=2))
                    ]

                case _:
                    raise ValueError(f"Unknown tool: {name}")

        except Exception as e:
            raise ValueError(f"Error processing mcp-server-github-trending query: {str(e)}")

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options)