# CLAUDE.md (AI Context OS Anchor)

## 🗺️ SYSTEM ONTOLOGY
1. **The Librarian:** Local tool (`ai_ops/librarian.py`). The ONLY interface for code/docs.
2. **TEARS Protocol:** Output format (Target, Evidence, Association, Restriction, Skill).
3. **The Commons:** Shared scripts in `ai_ops/commons/`.

## 🛠 TOOL USAGE
* **Fetch Context:** `python ai_ops/librarian.py --ask "Project" "Question"`
* **Learn Code:** `python ai_ops/librarian.py --index "Project" "Path"`

## 📂 KNOWLEDGE REPOSITORY
* **Strategy:** `ai_ops/PRD/PRD-Visionary.md`
* **Specs:** `ai_ops/PRD/PRD-Architect.md`
* **Memory:** `ai_ops/PRD/PRD-Librarian.md`
