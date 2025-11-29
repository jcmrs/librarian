# AGENTS.md

**Role:** Autonomous Builder
**Tool:** Local Librarian (`ai_ops/librarian.py`)

## ⚡️ ENVIRONMENT SETUP (Critical)
Before starting any task, you must ensure the environment is ready.
* **Install:** `pip install -r ai_ops/requirements.txt`
* **Index:** `python ai_ops/librarian.py --index .`

## 🧠 CONTEXT RETRIEVAL
Do not guess code. Use the Librarian.
* **Command:** `python ai_ops/librarian.py --ask "Find the class definition for User"`

## ✅ DEFINITION OF DONE
* Tests pass.
* Docs updated.
