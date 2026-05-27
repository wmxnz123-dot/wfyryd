import glob
import re

files = glob.glob('/Users/zhanghuimin/Downloads/000潍坊个人数据空间/trae/kxkj/prototype_ui/admin_*.html')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match the hidden list item for monitor stats
    # Looks like:
    # <li class="hidden">
    #     <a href="admin_monitor_stats.html" ...>
    #     <i class="fa-solid fa-chart-line w-6"></i> <span class="ml-3">监管统计</span>
    # </a>
    # </li>
    
    # Use a simpler regex
    # Replace `<li class="hidden">\s*<a href="admin_monitor_stats.html"` with `<li>\n<a href="admin_monitor_stats.html"`
    new_content = re.sub(
        r'<li class="hidden">(\s*<a href="admin_monitor_stats\.html")', 
        r'<li>\1', 
        content
    )
    
    # Replace text "监管统计" only within the admin_monitor_stats link block
    new_content = re.sub(
        r'(<a href="admin_monitor_stats\.html"[\s\S]*?)监管统计(</span>)',
        r'\1平台运营分析\2',
        new_content
    )
    
    new_content = new_content.replace('<!-- 监管统计 (Hidden) -->', '<!-- 平台运营分析 -->')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")

print("Done")
