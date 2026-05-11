import re

file_path = '/Users/zhanghuimin/Downloads/000潍坊个人数据空间/trae/kxkj/prototype_ui/app_my_data.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove from initial HTML
old_html_dot = """<button id="tabUnclaimed" class="flex-1 py-3 text-sm text-center tab-inactive transition relative" onclick="switchTab('unclaimed')">
            未认领数据
            <span class="absolute top-2 right-6 w-2 h-2 bg-red-500 rounded-full"></span>
        </button>"""

new_html_dot = """<button id="tabUnclaimed" class="flex-1 py-3 text-sm text-center tab-inactive transition relative" onclick="switchTab('unclaimed')">
            未认领数据
        </button>"""

content = content.replace(old_html_dot, new_html_dot)

# Try with a different indentation if first replace failed
old_html_dot_2 = """<button id="tabUnclaimed" class="flex-1 py-3 text-sm text-center tab-inactive transition relative" onclick="switchTab('unclaimed')">\n            未认领数据\n            <span class="absolute top-2 right-6 w-2 h-2 bg-red-500 rounded-full"></span>\n        </button>"""
content = content.replace(old_html_dot_2, new_html_dot)

# Remove from JS logic
old_js_dot = "tabUnclaimed.innerHTML = '未认领的数据<span class=\"absolute top-2 right-6 w-2 h-2 bg-red-500 rounded-full\"></span>';"
new_js_dot = "tabUnclaimed.innerHTML = '未认领数据';"
content = content.replace(old_js_dot, new_js_dot)

old_js_dot_2 = "tabUnclaimed.innerHTML = '未认领数据<span class=\"absolute top-2 right-6 w-2 h-2 bg-red-500 rounded-full\"></span>';"
content = content.replace(old_js_dot_2, new_js_dot)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Red dot removed!")
