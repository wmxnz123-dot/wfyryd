import os
import glob
import re

html_files = glob.glob('prototype_ui/admin_*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find and remove the global search div
    pattern = r'<div class="relative">\s*<input type="text" placeholder="全局搜索\.\.\."[^>]*>\s*<i class="fa-solid fa-search absolute[^>]*><\/i>\s*<\/div>'
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, '', content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed global search from {file}")
