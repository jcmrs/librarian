import os
import sys
import asyncio
import cognee
from litellm import completion

# --- CONFIGURATION (Embedded Mode for Jules) ---
# We use os.environ to get the key from GitHub Secrets/Environment
os.environ["LLM_PROVIDER"] = "gemini"
os.environ["LLM_MODEL"] = "gemini/gemini-2.5-flash"

# Force Embedded DBs (No Docker required)
# This prevents Jules/GitHub Actions from crashing
os.environ["GRAPH_DATABASE_PROVIDER"] = "networkx"
os.environ["VECTOR_DATABASE_PROVIDER"] = "lancedb"
os.environ["RELATIONAL_DATABASE_PROVIDER"] = "sqlite"
os.environ["COGNEE_ROOT_DIR"] = "./.cognee_memory"

async def ingest(target):
    """
    Reads local files and builds the graph.
    Supports recursive directory scanning.
    """
    print(f"📚 Indexing Target: {target}")
    
    if os.path.isfile(target):
        # Single file ingestion
        with open(target, 'r', encoding='utf-8') as f:
            await cognee.add(f.read(), dataset_name="session")
            
    elif os.path.isdir(target):
        # Directory recursion
        for root, _, files in os.walk(target):
            for file in files:
                # Filter for relevant code/text files
                if file.endswith(('.py', '.js', '.ts', '.md', '.json', '.txt', '.html', '.css')):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            await cognee.add(f.read(), dataset_name="session")
                    except Exception as e:
                        print(f"⚠️ Skipping {file}: {e}")

    # Build the graph (Cognify)
    print("🧠 Cognifying (Building Relationships)...")
    await cognee.cognify(datasets=["session"])
    print("✅ Indexing Complete")

async def ask(query):
    """
    Searches the graph and synthesizes an answer.
    """
    print(f"🤔 Thinking: {query}")
    
    # 1. Search the graph
    results = await cognee.search(query, datasets=["session"])
    
    if not results:
        print("❌ No context found in the graph.")
        return

    # 2. Synthesize using Gemini 2.5 Flash
    # We ask it to format the data cleanly
    prompt = f"Analyze this context and extract the answer/snippet. Format as Markdown:\n{results}"
    
    response = completion(
        model="gemini/gemini-2.5-flash",
        api_key=os.environ.get("LLM_API_KEY"),
        messages=[{"role": "user", "content": f"{prompt}\n\nUSER QUERY: {query}"}]
    )
    
    print("\n" + "="*40)
    print("      LIBRARIAN PRESCRIPT      ")
    print("="*40 + "\n")
    print(response.choices[0].message.content)
    print("\n" + "="*40)

async def main():
    if len(sys.argv) < 2:
        print("Usage: python librarian.py --index <path> OR python librarian.py --ask <query>")
        return

    mode = sys.argv[1]
    
    if mode == "--index":
        if len(sys.argv) < 3:
            # Default to current directory if no path provided
            await ingest(".")
        else:
            await ingest(sys.argv[2])
            
    elif mode == "--ask":
        if len(sys.argv) < 3:
            print("Error: Please provide a query.")
            return
        query = " ".join(sys.argv[2:])
        await ask(query)

if __name__ == "__main__":
    asyncio.run(main())
