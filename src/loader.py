import os
import glob

def load_documents_from_folder(folder_path: str = "docs") -> list[dict]:
    documents = []

# simple file load of all files in /docs defined by folder_path above
    for file_path in glob.glob(os.path.join(folder_path, "*")):
        if file_path.endswith(".txt") or file_path.endswith(".md"): #can do markdown or text files and ignores .png etc
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                chunks = chunk_text(content)

                for idx, chunk in enumerate(chunks):
                    documents.append({
                        "text": chunk,
                        "source": os.path.basename(file_path),
                        "chunk_id": f"{os.path.basename(file_path)}_chunk{idx}"
                    })

    return documents

def chunk_text(text: str) -> list[str]:
    # Split on double newlines (paragraphs/blocks) so chucking is done per infomation section 
    paragraphs = text.split("\n\n")
    return [p.strip() for p in paragraphs if p.strip()]
