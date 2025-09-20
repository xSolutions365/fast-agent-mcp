from mcp_agent.core.fastagent import FastAgent
from pathlib import Path
import asyncio

fast = FastAgent("Playwright MCP PoC")

@fast.agent(
    instruction="You are a web automation testing agent. Use Playwright MCP server to interact with web pages to perform testing tasks. Testing tasks are provided using BDD/Gherkin format",
    servers=["playwright"],
)

async def test_webapp(usecases: Path):
    async with fast.run() as agent:
        result = await agent.send(f"Test bdd use cases: {usecases}")
        return result

async def main():
    result = await test_webapp(Path("./prompts/bdd_woodmackenzie_prompt.md").read_text())
    print("Test Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
