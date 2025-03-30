import os

CONTENT_DIR = './content/blog'

def fix_double_dot_in_blog_paths():
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    contents = f.read()

                if 'blog../images/' in contents:
                    fixed_contents = contents.replace('blog../images/', 'blog/images/')
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(fixed_contents)
                    print(f"✅ Fixed: {path}")

if __name__ == "__main__":
    fix_double_dot_in_blog_paths()