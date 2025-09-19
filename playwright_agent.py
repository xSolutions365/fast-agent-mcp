from mcp_agent.core.fastagent import FastAgent
import asyncio

fast = FastAgent("Playwright MCP PoC")

@fast.agent(
    instruction="Go to the Playwright website and click on the 'Fixtures' link in the sidebar.",
    servers=["playwright"],
)
async def main():
  async with fast.run() as agent:
    await agent()

if __name__ == "__main__":
    asyncio.run(main())
