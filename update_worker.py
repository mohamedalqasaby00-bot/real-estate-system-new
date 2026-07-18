import re, json

# Read the HTML file
with open('public/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Read the existing worker.js
with open('worker.js', 'r', encoding='utf-8') as f:
    worker_content = f.read()

# Find the const HTML declaration and the first line after it
# There should be a pattern: const HTML = "...";
# We'll replace everything between const HTML = and the semicolon/next statement

# Escape the html content for including as a JS string
escaped = html_content.replace('\\', '\\\\').replace("'", "\\'").replace("\n", "\\n")

# Replace the HTML content in worker.js
# Worker pattern: const HTML = "..." or const HTML = '...'
new_worker = re.sub(
    r"(const HTML = )'(?:[^'\\]|\\.)*'",
    lambda m: m.group(1) + "'" + escaped + "'",
    worker_content,
    count=1
)

if new_worker == worker_content:
    # '...' failed, try "..."
    new_worker = re.sub(
        r'const HTML = "(?:[^"\\]|\\.)*"',
        lambda m: 'const HTML = "' + escaped.replace('"', '\\"') + '"',
        worker_content,
        count=1
    )

with open('worker.js', 'w', encoding='utf-8') as f:
    f.write(new_worker)

print("Done. worker.js updated.")
