from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP('Python-MCP-Server')

@mcp.tool()
def get_info_about(name: str) -> str:
    employee_info = {
        "name": "Badr JLIL",
        "email": "badr.jlil@company.com",
        "phone_number": "+212 6 41 84 56 49",
        "job_title": "Data Scientist",
        "salary": 42500,
        "contract_type": "CDI",
        "hire_date": "2022-09-01",
        "status": "Active",
        "address": "Casablanca, Morocco",
    }
    return json.dumps(employee_info)
