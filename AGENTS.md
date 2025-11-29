# AGENTS.md (Standing Orders)
**Role:** Autonomous Builder
**Mode:** ACTIVE (Librarian Enabled)

## ⚡️ BOOT SEQUENCE
1. **Install:** `pip install -r ai_ops/requirements.txt`
2. **Index:** `python ai_ops/librarian.py --index .` 

## 🧠 CONTEXT STRATEGY
* **Find Code:** `python ai_ops/librarian.py --ask "Find class [X]"`
* **Check Syntax:** `python ai_ops/librarian.py --ask "How do I use [Y]?"`

## ✅ DEFINITION OF DONE
* Tests pass.
* Documentation updated.
