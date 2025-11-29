# JULES.md (Standing Orders)

**Role:** Autonomous Builder
**Memory Strategy:** Just-In-Time (JIT) Indexing
**Primary Directive:** No Code Left Behind. Code and Documentation are a single atomic unit.

## ⚡️ BOOT SEQUENCE (Mandatory)
Since you run in an ephemeral environment, you must initialize your brain at the start of every task:
1. **Install Brain:** `pip install -r ai_ops/requirements.txt`
2. **Index Context:** `python ai_ops/librarian.py --index .` 
   *(This learns the current state of the repo in seconds)*

## 🧠 TOOL USE (The Librarian)
You are forbidden from guessing code context. You must look it up.
* **To find code/classes:** `python ai_ops/librarian.py --ask "Find the class definition for [X] and show me the file path"`
* **To check syntax:** `python ai_ops/librarian.py --ask "How do I use [Library Y]? Show examples."`

## ⚡️ IMPERATIVE 1: THE SHADOW SCRIBE (Doc-as-Code)
**Trigger:** You modify any logic in a `.py` or `.js` file.
**Action:** You MUST immediately check the corresponding documentation.
* Use the Librarian to find the docstring or README section.
* If docstrings are outdated -> Update them.
* If the `ATOMIC-SPEC.md` logic was changed -> Append a "Change Log" note.

## ⚡️ IMPERATIVE 2: THE LIBRARIAN HANDSHAKE
**Trigger:** You create a NEW file.
**Action:** You MUST register it so you can see it in your next query.
* **Command:** `python ai_ops/librarian.py --index [NewFilePath]`

## ✅ DEFINITION OF DONE
* [ ] All tests passed.
* [ ] Documentation updated to match code changes.
* [ ] New files registered with Librarian.
