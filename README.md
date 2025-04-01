# mcp-github-trending MCP Server

A MCP server that provides access to GitHub trending repositories and developers data through a simple API interface.

[![smithery badge](https://smithery.ai/badge/@hetaoBackend/github-trending-mcp-server)](https://smithery.ai/server/@hetaoBackend/github-trending-mcp-server)

## Features

- Access GitHub trending repositories and developers data
- Filter by programming language
- Filter by time period (daily, weekly, monthly)
- Filter by spoken language
- Returns well-formatted JSON responses

## Tools

The server implements the following tools:

### get_github_trending_repositories

Gets trending repositories from GitHub with the following parameters:

- `language` (optional): Programming language to filter repositories by (e.g. "python", "javascript")
- `since` (optional): Time period to filter repositories by ("daily", "weekly", "monthly"). Defaults to "daily"
- `spoken_language` (optional): Spoken language to filter repositories by

Example response:
```json
[
  {
    "name": "repository-name",
    "fullname": "owner/repository-name",
    "url": "https://github.com/owner/repository-name",
    "description": "Repository description",
    "language": "Python",
    "stars": 1000,
    "forks": 100,
    "current_period_stars": 50
  }
]
```

### get_github_trending_developers

Gets trending developers from GitHub with the following parameters:

- `language` (optional): Programming language to filter by (e.g. "python", "javascript")
- `since` (optional): Time period to filter by ("daily", "weekly", "monthly"). Defaults to "daily"

Example response:
```json
[
  {
    "username": "developer",
    "name": "Developer Name",
    "url": "https://github.com/developer",
    "avatar": "https://avatars.githubusercontent.com/u/123456",
    "repo": {
      "name": "repository-name",
      "description": "Repository description",
      "url": "https://github.com/developer/repository-name"
    }
  }
]
```

## Installation

### Prerequisites

- Python 3.12

### Install Steps

Install the package:
```bash
pip install mcp-github-trending
```

### Claude Desktop Configuration

On MacOS:
```bash
~/Library/Application\ Support/Claude/claude_desktop_config.json
```

On Windows:
```bash
%APPDATA%/Claude/claude_desktop_config.json
```

<details>
 <summary>Development/Unpublished Servers Configuration</summary>

```json
{
  "mcpServers": {
    "mcp-github-trending": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-github-trending",
        "run",
        "mcp-github-trending"
      ]
    }
  }
}
```
</details>

<details>
 <summary>Published Servers Configuration</summary>

```json
{
  "mcpServers": {
    "mcp-github-trending": {
      "command": "uvx",
      "args": [
        "mcp-github-trending"
      ]
    }
  }
}
```
</details>

## Development

### Building and Publishing

1. Sync dependencies and update lockfile:
```bash
uv sync
```

2. Build package distributions:
```bash
uv build
```

3. Publish to PyPI:
```bash
uv publish
```

Note: Set PyPI credentials via environment variables or command flags:
- Token: `--token` or `UV_PUBLISH_TOKEN`
- Username/password: `--username`/`UV_PUBLISH_USERNAME` and `--password`/`UV_PUBLISH_PASSWORD`

### Debugging

For the best debugging experience, use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector).

Launch the MCP Inspector via [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm):

```bash
npx @modelcontextprotocol/inspector uv --directory /path/to/mcp-github-trending run mcp-github-trending
```

The Inspector will display a URL that you can access in your browser to begin debugging.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
