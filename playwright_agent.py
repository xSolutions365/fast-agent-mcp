from mcp_agent.core.fastagent import FastAgent
from pathlib import Path
import asyncio

fast = FastAgent("Playwright MCP PoC", quiet=True)

@fast.agent(
    instruction="You are a web automation testing agent. Your task is to run test based on BDD/Gherkin prompt. Always take screenshot at the end of each bdd scenario and store it as {filename}.png. Before each test run browser_start_tracing and after test run browser_stop_tracing, save it to ./artifacts/{filename}/ directory. Traces need to be saved in each own {filename}-trace directory and not mix up. Test report should be in the markdown format and saved as {filename}.md in the ./artifacts directory",
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
