from mcp.server.fastmcp import FastMCP
from client import search_papers, get_paper_by_id

mcp = FastMCP("arxiv-digest")

@mcp.tool()
def get_paper(id: str) -> dict:
    """Retrieves arXiv paper by ID and returns a dict with keys: id, title, authors, summary"""
    try:
        return get_paper_by_id(id)
    except Exception as e:
        return {"error": f"Could not retrieve paper by ID"}
    pass

@mcp.tool()
def search_arxiv(query: str, max_results: int = 5) -> list:
    """Search arXiv papers by keyword and return matching results."""
    try:
        return search_papers(query, max_results)
    except Exception as e:
        return [{"error": f"Search failed: {str(e)}"}]

mcp.run(transport="stdio")