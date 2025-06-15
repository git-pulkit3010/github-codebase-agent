import os
import argparse
from github_handler import clone_repo
from file_reader import extract_code_chunks
from summarizer import ask_deepseek
from utils import colored_print, pretty_print


def run_cli():
    parser = argparse.ArgumentParser(description="AI Codebase Explorer")
    parser.add_argument('--repo', type=str, required=True, help='GitHub repo URL')
    args = parser.parse_args()

    repo_url = args.repo
    repo_dir = clone_repo(repo_url)

    colored_print("[✓] Repository cloned successfully.", "green")
    colored_print("[~] Reading code files...", "yellow")

    chunks = extract_code_chunks(repo_dir)
    
    
    colored_print("Included files in chunks:", "cyan")
    for chunk in chunks:
        for line in chunk.splitlines():
            if line.startswith("# File: "):
                print(line)


    colored_print("[✓] Files loaded and chunked.", "green")

    while True:
        try:
            query = input("\n> Your question (type 'exit' to quit): ")
            if query.lower() in ['exit', 'quit']:
                break
            colored_print("[~] Thinking...", "yellow")
            response = ask_deepseek(query, chunks)
            colored_print("[✓] Response:", "green")
            pretty_print(response)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
