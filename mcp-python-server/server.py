from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP('Python-MCP-Server')

@mcp.tool()
def get_info_about(name: str) -> str:
    employee_info = {
        "name": "Badr",
        "salary": 75500,
    }
    return json.dumps(employee_info)
