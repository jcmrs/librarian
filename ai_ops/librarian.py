import os
import sys
import asyncio
import cognee
from litellm import completion

# --- CONFIGURATION (Jules-Safe Embedded Mode) ---
# 1. API Key: Pulled from Environment (GitHub Secrets)
os.environ["LLM_PROVIDER"] = "gemini"
os.environ["LLM_MODEL"] = "gemini/gemini-2.5-flash"

# 2. Database: Embedded Files (No Docker/Server required)
os.environ["GRAPH_DATABASE_PROVIDER"] = "networkx"
os.environ["VECTOR_DATABASE_PROVIDER"] = "lancedb"
os.environ["RELATIONAL_DATABASE_PROVIDER"] = "sqlite"
os.environ["COGNEE_ROOT_DIR"] = "./.cognee_memory"

async def ingest(target):
    """Recursive file ingestion"""
    print(f"📚 Indexing Target: {target}")
    if os.path.isfile(target):
        with open(target, 'r', encoding='utf-8') as f:
            await cognee.add(f.read(), dataset_name="session")
    elif os.path.isdir(target):
        for root, _, files in os.walk(target):
            for file in files:
                if file.endswith(('.py', '.js', '.md', '.txt', '.json')):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            await cognee.add(f.read(), dataset_name="session")
                    except Exception: pass

    print("🧠 Building Graph...")
    await cognee.cognify(dataset_name="session")
    print("✅ Indexing Complete")

async def ask(query):
    """Search and Synthesize"""
    print(f"🤔 Thinking: {query}")
    # Fix: Ensure correct argument type for search
    results = await cognee.search(query, dataset_name="session")
    
    if not results:
        print("❌ No context found.")
        return

    prompt = f"Analyze this context and extract the answer/snippet. Format as Markdown:\n{results}"
    response = completion(
        model="gemini/gemini-2.5-flash",
        api_key=os.environ.get("LLM_API_KEY"),
        messages=[{"role": "user", "content": f"{prompt}\n\nUSER QUERY: {query}"}]
    )
    print("\n--- PRESCRIPT ---\n")
    print(response.choices[0].message.content)
    print("\n-----------------\n")

async def main():
    if len(sys.argv) < 2: return
    mode = sys.argv[1]
    if mode == "--index":
        path = sys.argv[2] if len(sys.argv) > 2 else "."
        await ingest(path)
    elif mode == "--ask":
        query = " ".join(sys.argv[2:])
        await ask(query)

if __name__ == "__main__":
    asyncio.run(main())
