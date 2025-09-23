from mcp_agent.core.fastagent import FastAgent
from pathlib import Path
import asyncio

fast = FastAgent("Playwright MCP PoC")

@fast.agent(
    instruction="You are a web automation testing agent. Use Playwright MCP server to interact with web app. Testing tasks are provided using BDD/Gherkin format. Always take screenshot at the end of each scenario. Screenshot should be saved as {filename}.png and stored in ./artifact directory",
    servers=["playwright"],
)

async def test_webapp(usecases: str, filename: str):
    async with fast.run() as agent:
        result = await agent.send(f"Test bdd use case from {filename}:\n\n{usecases}")
        return filename, result

async def main():
    # result = await test_webapp(Path("./prompts/bdd_woodmackenzie_prompt.md").read_text())
    # print("Test Result:", result)

    prompt_dir = Path("./prompts")

    results = []
    for file in prompt_dir.glob("*.md"):
        text = file.read_text()
        filename, result = await test_webapp(text, file.name)
        results.append((filename, result))

    for filename, result in results:
        print(f"\n=== {filename} ===")
        print("Test Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
