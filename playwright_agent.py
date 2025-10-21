from mcp_agent.core.fastagent import FastAgent
from pathlib import Path
import asyncio

fast = FastAgent("Playwright MCP PoC", quiet=True)

@fast.agent(
    instruction="You are a web automation testing agent. Use Playwright MCP server to interact with web app. Execute test tasks provided using BDD/Gherkin format. Always take screenshot at the end of each scenario. Screenshot should be saved as {filename}.png and stored in ./artifacts directory. Before each scenario start browser_start_tracing and after each scenario is tested stop browser_stop_tracing then save it to ./artifacts/{filename} directories. Test report should be in the markdown format and saved as {filename}.md in the ./artifacts directory",
    servers=["playwright"]
)

def append_to_report(log_text: str, file_path: str = "./artifacts/report.md"):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(log_text)
        f.write("\n")

async def test_webapp(usecases: str, filename: str):
    async with fast.run() as agent:
        result = await agent.send(f"Test bdd use case from {filename}:\n\n{usecases}")
        return filename, result

async def main():
    prompt_dir = Path("./prompts")

    results = []
    for file in prompt_dir.glob("*.md"):
        text = file.read_text()
        filename, result = await test_webapp(text, file.name)
        results.append((filename, result))

    for filename, result in results:
        print(f"\n=== {filename} ===")
        print("Test Result:", result)
        append_to_report(result, f"./artifacts/{filename}")

if __name__ == "__main__":
    asyncio.run(main())
