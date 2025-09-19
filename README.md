# 🚀 fast-agent-mcp

> A blazing-fast, configurable agent framework for Python.

---

## 🛠️ Quick Start

1. Install [uv](https://github.com/astral-sh/uv) (Python package manager):
	```sh
	pip install uv
	```
2. Install fast-agent-mcp:
	```sh
	uv pip install fast-agent-mcp
	```
3. Set up your first agent:
	```sh
	fast-agent setup
	```

---

## 🔑 Configuration

1. Add your API keys
	- Edit `fastagent.secrets.yaml` or set environment variables.
	- Verify:
	  ```sh
	  fast-agent check
	  ```
2. Keep your secrets safe
	- Never commit `fastagent.secrets.yaml` to version control.
3. Configure your agent
	- Edit `fastagent.config.yaml` to set your default model (default: `haiku`).

---

## 📄 Files
- `fastagent.secrets.yaml` — API keys and secrets (keep private!)
- `fastagent.config.yaml` — Agent configuration (model, settings, etc.)

---

## 📢 Tips
- Run `fast-agent check` to validate configuration.
- Open issues or view docs in the repo.

---

Enjoy building with fast-agent-mcp! ⚡️