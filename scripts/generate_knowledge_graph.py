import os
import re

# --- CONFIG ---
KNOWLEDGE_DIR = "memory/knowledge"
OUTPUT_FILE = "memory/knowledge/GRAPH.md"
EXCLUDE_DIRS = ["Tools", ".git", "state"]  # Folders to skip

# --- LOGIC ---
def scan_knowledge():
    print(f"🔍 Scanning knowledge base: {KNOWLEDGE_DIR}...")
    nodes = []
    edges = []
    tags_map = {}

    for root, dirs, files in os.walk(KNOWLEDGE_DIR):
        # Filter excluded dirs
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file.endswith(".md") and file != "GRAPH.md":
                path = os.path.join(root, file)
                category = os.path.basename(root) # AI, Philosophy, etc.
                
                # Parse File
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Extract Title (First # Headline or File Name)
                title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip()
                    # Clean title (remove "📌 HEADLINE REWRITE" etc)
                    title = title.replace("📌 HEADLINE REWRITE", "").strip()
                    if title.startswith(">"): title = title[1:].strip()
                else:
                    title = file.replace(".md", "").replace("_", " ")

                # Shorten Title for Graph
                short_title = (title[:30] + "..") if len(title) > 30 else title
                file_id = re.sub(r"[^a-zA-Z0-9]", "", file) # Safe ID
                
                # Add Node
                nodes.append(f'    {file_id}["📄 {short_title}"]')
                
                # Extract Tags
                tags = re.findall(r"#(\w+)", content)
                for tag in tags:
                    tag = tag.lower()
                    if tag in ["headline", "core", "analysis", "bottom", "follow"]: continue # Skip structural tags
                    
                    if tag not in tags_map:
                        tags_map[tag] = f"tag_{tag}"
                    
                    # Add Edge (File -> Tag)
                    edges.append(f"    {file_id} -.-> {tags_map[tag]}")

    # Generate Mermaid
    mermaid = ["# 🕸️ Knowledge Graph", "", "```mermaid", "graph LR"]
    
    # Styles
    mermaid.append("    classDef file fill:#e1f5fe,stroke:#01579b,stroke-width:2px;")
    mermaid.append("    classDef tag fill:#fff3e0,stroke:#ff6f00,stroke-width:1px,stroke-dasharray: 5 5;")
    
    # Nodes (Files)
    mermaid.extend(nodes)
    
    # Nodes (Tags)
    for tag, tag_id in tags_map.items():
        mermaid.append(f'    {tag_id}("#{tag}"):::tag')
    
    # Edges
    mermaid.extend(edges)
    
    # Styling
    file_ids = [n.split("[")[0].strip() for n in nodes]
    if file_ids:
        mermaid.append(f"    class {','.join(file_ids)} file;")

    mermaid.append("```")
    
    # Write Output
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(mermaid))
    
    print(f"✅ Graph generated at: {OUTPUT_FILE}")
    print(f"📊 Stats: {len(nodes)} Files, {len(tags_map)} Tags")

if __name__ == "__main__":
    scan_knowledge()
