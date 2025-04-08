import os

search_term = "document.body.classList"
matches = []

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith((".js", ".html", ".css")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    if search_term in f.read():
                        matches.append(path)
            except Exception as e:
                print(f"Could not read {path}: {e}")

print("\nFiles containing 'document.body.classList':\n")
for match in matches:
    print(match)

if not matches:
    print("No matches found.")