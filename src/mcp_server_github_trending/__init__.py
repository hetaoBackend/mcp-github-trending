from .server import serve


def main():
    """MCP GitHub Trending Server - Fetch trending repositories and developers from GitHub"""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="Give a model the ability to fetch GitHub trending repositories and developers"
    )

    args = parser.parse_args()
    asyncio.run(serve())

if __name__ == "__main__":
    main()

