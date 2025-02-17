# -*- coding: utf-8 -*-
import os

# Directory containing your markdown files
directory = "content/blog"

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        file_path = os.path.join(directory, filename)
        
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Replace only the first occurrence of "url:" with "slug:"
        for i, line in enumerate(lines):
            if line.strip().startswith("url:"):
                lines[i] = line.replace("url:", "slug:", 1)
                break  # Ensure only the first occurrence is replaced

        # Write the changes back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(lines)

print("✅ Replacement complete: 'url:' → 'slug:' in first occurrence for all .md files in content/blog/")