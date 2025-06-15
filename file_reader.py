import os

SUPPORTED_EXTENSIONS = ['.py', '.js', '.ts', '.java', '.go', '.cpp', '.c', '.rb']


def read_file_content(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception:
        return ""


def extract_code_chunks(repo_dir, max_chunk_size=3000):
    code_chunks = []
    current_chunk = ""
    
    for root, _, files in os.walk(repo_dir):
        for file in files:
            ext = os.path.splitext(file)[-1]
            if ext in SUPPORTED_EXTENSIONS:
                file_path = os.path.join(root, file)
                code = read_file_content(file_path)
                if not code:
                    continue
                
                # Always create header for the file
                header = f"\n\n# File: {file_path}\n"
                file_content = header + code
                
                # Case 1: File content fits in current chunk
                if len(current_chunk) + len(file_content) <= max_chunk_size:
                    current_chunk += file_content
                
                # Case 2: File content too big but can be split
                else:
                    if current_chunk:  # Save existing chunk first
                        code_chunks.append(current_chunk)
                        current_chunk = ""
                    
                    # Split large files into multiple chunks
                    while file_content:
                        chunk_part = file_content[:max_chunk_size]
                        code_chunks.append(chunk_part)
                        file_content = file_content[max_chunk_size:]
    
    if current_chunk:
        code_chunks.append(current_chunk)
    
    return code_chunks
