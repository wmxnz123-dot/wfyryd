import os
import glob

html_files = glob.glob('prototype_ui/admin_*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if 'admin_search_config.html' not in line:
            new_lines.append(line)
            
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
