import re

file_path = '/Users/zhanghuimin/Downloads/000潍坊个人数据空间/trae/kxkj/prototype_ui/admin_catalog_add.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's fix the innerHTML for onTableSelectChange and toggleDataType
def fix_tr_innerHTML_1(match):
    original = match.group(0)
    
    # We want to keep the FIRST isPrimaryKey radio, but change the 2nd and 3rd back to <select>
    
    # Split the original string by the radio button pattern
    parts = original.split("""<td class="p-3 text-center">
                            <input type="radio" name="isPrimaryKey" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50" disabled>
                        </td>""")
    
    if len(parts) == 4:
        # There were 3 occurrences. The first one is the real isPrimaryKey.
        # The 2nd and 3rd are the "非空" and "脱敏显示"
        select_html = """<td class="p-3">
                            <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent" disabled>
                                <option value="no" selected>否</option>
                                <option value="yes">是</option>
                            </select>
                        </td>"""
        
        radio_html = """<td class="p-3 text-center">
                            <input type="radio" name="isPrimaryKey" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50" disabled>
                        </td>"""
        
        # Reconstruct:
        new_str = parts[0] + radio_html + parts[1] + select_html + parts[2] + select_html + parts[3]
        return new_str
    return original

# For addFieldRow, the formatting is slightly different (bg-white instead of bg-transparent, and no disabled)
def fix_tr_innerHTML_2(match):
    original = match.group(0)
    
    parts = original.split("""<td class="p-3 text-center">
                <input type="radio" name="isPrimaryKey" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50">
            </td>""")
            
    if len(parts) == 4:
        select_html = """<td class="p-3">
                <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white">
                    <option value="no" selected>否</option>
                    <option value="yes">是</option>
                </select>
            </td>"""
            
        radio_html = """<td class="p-3 text-center">
                <input type="radio" name="isPrimaryKey" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50">
            </td>"""
            
        new_str = parts[0] + radio_html + parts[1] + select_html + parts[2] + select_html + parts[3]
        return new_str
    return original

# Apply the fixes
content = re.sub(r'tr\.innerHTML = `[\s\S]*?`;', lambda m: fix_tr_innerHTML_1(m) if 'bg-transparent' in m.group(0) else fix_tr_innerHTML_2(m), content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML Restored and Fixed!")
