from mcp_agent.core.fastagent import FastAgent
import asyncio

fast = FastAgent("Playwright MCP PoC")

@fast.agent(
    instruction="You are a web automation testing agent. Use Playwright MCP server to interact with web pages to perform testing tasks.",
    servers=["playwright"],
)

async def test_webapp(usecases: str):
    async with fast.run() as agent:
        result = await agent.send(f"Test this web application: {usecases}")
        return result

async def main():
    usecases = "Go to wood mackenzie web app. Find report and add the report to the cart."
    result = await test_webapp(usecases)
    print("Test Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
