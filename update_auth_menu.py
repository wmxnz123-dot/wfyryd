import glob
import os
import re

files = glob.glob('prototype_ui/admin_*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('授权统计分析', '授权记录')
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file)}")
