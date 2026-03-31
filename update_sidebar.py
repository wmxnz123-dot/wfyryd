import glob
import os
import re

files = glob.glob('/Users/zhanghuimin/Downloads/000潍坊个人数据空间/trae/kxkj/prototype_ui/admin_*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 替换个人中心管理和仪表盘配置为一级菜单
    pattern_profile = re.compile(r'<!-- 个人中心管理 -->.*?<li>\s*<div class="flex items-center justify-between px-6 py-3.*?<i class="fa-solid fa-user-gear w-6"></i> <span class="ml-3">个人中心管理</span>.*?<ul class="pl-14 py-2 space-y-3 text-sm hidden bg-gray-800/50">.*?<li><a href="admin_profile_dashboard_config\.html"[^>]*>仪表盘配置</a></li>\s*</ul>\s*</li>', re.DOTALL)
    
    replacement_profile = '''<!-- 仪表盘配置 -->
                <li>
                    <a href="admin_profile_dashboard_config.html" class="flex items-center px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition">
                        <i class="fa-solid fa-chart-pie w-6"></i> <span class="ml-3">仪表盘配置</span>
                    </a>
                </li>'''
    
    content = pattern_profile.sub(replacement_profile, content)

    # 2. 隐藏监管统计菜单
    pattern_monitor = re.compile(r'<!-- 监管统计 -->\s*<li>\s*<a href="admin_monitor_stats\.html" class="flex items-center px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition">')
    replacement_monitor = '''<!-- 监管统计 (Hidden) -->
                <li class="hidden">
                    <a href="admin_monitor_stats.html" class="flex items-center px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition">'''
    
    content = pattern_monitor.sub(replacement_monitor, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {os.path.basename(file)}')
