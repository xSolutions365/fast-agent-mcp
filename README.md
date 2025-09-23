# 🚀 fast-agent-mcp

> A blazing-fast, configurable agent framework for Python using 

---

## 🛠️ Quick Start

1. The project assumes you are using uv for managing Python packages.Install [uv](https://github.com/astral-sh/uv) (Python package manager):

	```sh
	curl -Ls https://astral.sh/uv/install.sh
	```

---

## 🔑 Configuration

1. **Add your API keys**

   Export your `OPENAI_API_KEY` in the console:

   ```sh
   export OPENAI_API_KEY=your-key-here
   ```

   Verify your setup:

   ```sh
   fast-agent check
   ```
2. Keep your secrets safe
	- Never commit `fastagent.secrets.yaml` to version control.
3. Configure your agent
	- Edit `fastagent.config.yaml` to set your default model (default: `gpt-4.1`).

---

## 📄 Files
- `fastagent.secrets.yaml` — API keys and secrets (keep private!)
- `fastagent.config.yaml` — Agent configuration (model, settings, etc.)

---

## 📢 Tips
- Run `fast-agent check` to validate configuration.
- Open issues or view docs in the repo.

---

## ▶️ Run your agent

```sh
uv run playwright_agent.py
```
