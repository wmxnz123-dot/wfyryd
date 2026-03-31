import glob
import os
import re

files = glob.glob('prototype_ui/admin_*.html')

new_lis = '''
                    <li><a href="admin_dashboard.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">数据检索</a></li>
                    <li><a href="admin_dashboard_results.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">组合检索</a></li>
                    <li><a href="admin_tag_search.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">标签检索</a></li>
                    <li><a href="admin_data_map.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">数图分析</a></li>
'''

pattern = re.compile(r'(<!-- 数据检索管理 -->\s*<li>\s*<div.*?</div>\s*<ul[^>]*>)(.*?)(</ul>)', re.DOTALL)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- 数据检索管理 -->' in content:
        new_content = pattern.sub(lambda m: m.group(1) + "\n" + new_lis + "                " + m.group(3), content)
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(file)}")
