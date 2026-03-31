import glob
import os
import re

files = glob.glob('prototype_ui/admin_*.html')

pattern = re.compile(r'<!-- 自有数据管理 -->\s*<li>\s*<div.*?<i class="fa-solid fa-folder-open w-6"></i> <span class="ml-3">自有数据管理</span>.*?</div>\s*<ul.*?</ul>\s*</li>', re.DOTALL)

new_menu = '''<!-- 自有数据管理 -->
            <li>
                <a href="admin_own_data_catalog.html" class="flex items-center px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition">
                    <i class="fa-solid fa-folder-open w-6"></i> <span class="ml-3">自有数据管理</span>
                </a>
            </li>'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = pattern.sub(new_menu, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file)}")
