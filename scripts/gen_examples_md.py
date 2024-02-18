#!/usr/bin/env python3

import argparse
import os
import glob
from typing import List

def main():
    parser = argparse.ArgumentParser(description="Generate Markdown files for Python scripts.")
    parser.add_argument("--dir", "-d", default="examples", help="Directory to search for Python files.")
    parser.add_argument("--out-dir", "-o", default="docs/examples", help="Directory to output Markdown files.")
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(args.out_dir, exist_ok=True)

    # Get list of *.py files in the specified directory
    python_files = glob.glob(os.path.join(args.dir, "*.py"))
    py_file_name = ""
    md_file_links: List[str] = []

    for py_file in python_files:
        py_file_name = os.path.basename(py_file)
        md_file_name = os.path.splitext(py_file_name)[0] + ".md"
        md_file_path = os.path.join(args.out_dir, md_file_name)

        # Create and write to the corresponding *.md file
        with open(md_file_path, 'w') as md_file:
            md_file.write(f"# {py_file_name}\n\n")
            md_file.write(f"```python\n--8<-- \"./examples/{py_file_name}\"\n```")

        md_file_links.append(md_file_name)

    # Create index.md file
    index_md_path = os.path.join(args.out_dir, "index.md")
    with open(index_md_path, 'w') as index_md_file:
        index_md_file.write("# Examples\n\n")
        index_md_file.write(
            "The following examples are taken from the [`examples/`](https://github.com/openai/openai-python/tree/main/examples) "
            "directory in the root of the [openai/openai-python](https://github.com/openai/openai-python) repository.\n\n"
            )
        for md_link in sorted(md_file_links):
            index_md_file.write(f"- [{md_link.replace('.md', '.py')}](./{md_link})\n")

if __name__ == "__main__":
    main()
