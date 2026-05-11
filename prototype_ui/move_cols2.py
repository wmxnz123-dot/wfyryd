import re

file_path = '/Users/zhanghuimin/Downloads/000潍坊个人数据空间/trae/kxkj/prototype_ui/admin_catalog_add.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_thead = """<th class="p-3 font-medium w-16 text-center">序号</th><th class="p-3 font-medium w-12"></th>
<th class="p-3 font-medium">字段英文名</th>
<th class="p-3 font-medium">字段中文名</th>
<th class="p-3 font-medium">是否为主键</th>
<th class="p-3 font-medium is-title-col hidden">是否为标题展示</th>
<th class="p-3 font-medium">类型</th>
<th class="p-3 font-medium">长度</th>
<th class="p-3 font-medium">显示类型</th>
<th class="p-3 font-medium">字典类型</th>
<th class="p-3 font-medium">非空</th>
<th class="p-3 font-medium">脱敏显示</th>
<th class="p-3 font-medium">脱敏规则</th>
<th class="p-3 font-medium">显示状态</th>
<th class="p-3 font-medium">操作</th>"""

new_thead = """<th class="p-3 font-medium w-16 text-center">序号</th><th class="p-3 font-medium w-12"></th>
<th class="p-3 font-medium">字段英文名</th>
<th class="p-3 font-medium">字段中文名</th>
<th class="p-3 font-medium">类型</th>
<th class="p-3 font-medium">长度</th>
<th class="p-3 font-medium">显示类型</th>
<th class="p-3 font-medium">字典类型</th>
<th class="p-3 font-medium">非空</th>
<th class="p-3 font-medium">脱敏显示</th>
<th class="p-3 font-medium">脱敏规则</th>
<th class="p-3 font-medium">显示状态</th>
<th class="p-3 font-medium">是否为主键</th>
<th class="p-3 font-medium is-title-col hidden">是否为标题展示</th>
<th class="p-3 font-medium">操作</th>"""

content = content.replace(old_thead, new_thead)

def move_cols_in_template(template):
    is_primary_key_pattern = r'(\s*<td class="p-3 text-center">\s*<input type="radio" name="isPrimaryKey"[^>]*>\s*</td>)'
    is_title_display_pattern = r'(\s*<td class="p-3 is-title-col hidden text-center">\s*<input type="radio" name="isTitleDisplay"[^>]*>\s*</td>)'
    
    primary_key_match = re.search(is_primary_key_pattern, template)
    title_display_match = re.search(is_title_display_pattern, template)
    
    if primary_key_match and title_display_match:
        primary_key_str = primary_key_match.group(1)
        title_display_str = title_display_match.group(1)
        
        template = template.replace(primary_key_str, '')
        template = template.replace(title_display_str, '')
        
        actions_pattern = r'(\s*<td class="p-3">\s*<div class="flex items-center justify-center space-x-2">)'
        
        template = re.sub(actions_pattern, primary_key_str + title_display_str + r'\1', template)
        
    return template

matches = list(re.finditer(r'tr\.innerHTML = `([\s\S]*?)`;', content))
for match in reversed(matches):
    original_inner = match.group(1)
    if 'arrows-up-down-left-right' in original_inner:
        new_inner = move_cols_in_template(original_inner)
        content = content[:match.start(1)] + new_inner + content[match.end(1):]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Moved columns to the end!")
