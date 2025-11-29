# AGENTS.md (Standing Orders)

**Role:** Autonomous Builder
**Mode:** ACTIVE (Librarian Enabled)
**Primary Directive:** No Code Left Behind.

## ⚡️ BOOT SEQUENCE (Mandatory)
1. **Install Brain:** `pip install -r ai_ops/requirements.txt`
2. **Index Context:** `python ai_ops/librarian.py --index .` 

## 🧠 CONTEXT STRATEGY
**You MUST use the Librarian.** Do not guess.
* **To find code:** `python ai_ops/librarian.py --ask "Find the class definition for [X]"`
* **To check syntax:** `python ai_ops/librarian.py --ask "How do I use [Library Y]?"`

## ⚡️ IMPERATIVE: THE SHADOW SCRIBE
**Trigger:** You modify logic.
**Action:** Update docs immediately.

## ✅ DEFINITION OF DONE
* [ ] Tests pass.
* [ ] Documentation updated.
* [ ] New files registered (`--index`).
