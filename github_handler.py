import os
import shutil
import tempfile
import subprocess

def clone_repo(repo_url):
    temp_dir = tempfile.mkdtemp()
    repo_name = repo_url.rstrip('/').split('/')[-1].replace('.git', '')
    dest_path = os.path.join(temp_dir, repo_name)

    try:
        subprocess.run(["git", "clone", repo_url, dest_path], check=True)
    except subprocess.CalledProcessError:
        raise RuntimeError("[!] Failed to clone the repository.")

    return dest_path