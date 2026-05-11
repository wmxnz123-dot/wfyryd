import re

file_path = '/Users/zhanghuimin/Downloads/000潍坊个人数据空间/trae/kxkj/prototype_ui/admin_catalog_add.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We only want to replace the ones that contain "arrows-up-down-left-right"

matches = list(re.finditer(r'tr\.innerHTML = `([\s\S]*?)`;', content))
filtered_matches = [m for m in matches if 'arrows-up-down-left-right' in m.group(1)]

print("Found", len(filtered_matches), "matches")

if len(filtered_matches) == 3:
    correct_tr_inner_disabled = """
                        <td class="p-3 text-center text-gray-500 index-cell"></td>
                        <td class="p-3 text-gray-400 hover:text-blue-500 cursor-grab" onmousedown="this.parentElement.setAttribute('draggable', true)" onmouseup="this.parentElement.removeAttribute('draggable')"><i class="fa-solid fa-arrows-up-down-left-right"></i></td>
                        <td class="p-3"><input type="text" class="w-full border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none bg-gray-100 text-gray-500 text-center" value="${f.engName}" readonly data-non-editable="true"></td>
                        <td class="p-3"><input type="text" class="w-full border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent text-center" value="${f.chName}" readonly></td>
                        <td class="p-3 text-center">
                            <input type="radio" name="isPrimaryKey" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50" disabled>
                        </td>
                        <td class="p-3 is-title-col hidden text-center">
                            <input type="radio" name="isTitleDisplay" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50" disabled>
                        </td>
                        <td class="p-3">
                            <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none bg-gray-100 text-gray-500" disabled data-non-editable="true">
                                <option value="varchar" ${f.type === 'varchar' ? 'selected' : ''}>varchar</option>
                                <option value="int" ${f.type === 'int' ? 'selected' : ''}>int</option>
                                <option value="datetime" ${f.type === 'datetime' ? 'selected' : ''}>datetime</option>
                            </select>
                        </td>
                        <td class="p-3"><input type="number" class="w-16 border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none bg-gray-100 text-gray-500 text-center" value="${f.length}" readonly data-non-editable="true"></td>
                        <td class="p-3">
                            <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent" disabled>
                                <option value="text" selected>文本</option>
                                <option value="cascade">级联</option>
                                <option value="select">下拉框</option>
                            </select>
                        </td>
                        <td class="p-3"><input type="text" class="w-16 border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent text-center" value="-" readonly></td>
                        <td class="p-3">
                            <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent" disabled>
                                <option value="no" selected>否</option>
                                <option value="yes">是</option>
                            </select>
                        </td>
                        <td class="p-3">
                            <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent" disabled>
                                <option value="no" selected>否</option>
                                <option value="yes">是</option>
                            </select>
                        </td>
                        <td class="p-3"><input type="text" class="w-16 border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent text-center" value="-" readonly></td>
                        <td class="p-3 text-center">
                            <button class="text-blue-600 hover:text-blue-800 transition" onclick="toggleVisibility(this)">
                                <i class="fa-solid fa-eye" title="显示状态"></i>
                            </button>
                        </td>
                        <td class="p-3">
                            <div class="flex items-center justify-center space-x-2">
                                <button class="text-blue-600 hover:text-blue-800 transition" onclick="toggleEditRow(this)">编辑</button>
                                <button class="text-red-500 hover:text-red-700 transition" onclick="deleteRow(this)"><i class="fa-solid fa-trash-can"></i></button>
                            </div>
                        </td>
"""

    correct_tr_inner_enabled = """
            <td class="p-3 text-center text-gray-500 index-cell"></td>
            <td class="p-3 text-gray-400 hover:text-blue-500 cursor-grab" onmousedown="this.parentElement.setAttribute('draggable', true)" onmouseup="this.parentElement.removeAttribute('draggable')"><i class="fa-solid fa-arrows-up-down-left-right"></i></td>
            <td class="p-3"><input type="text" class="w-full border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white text-center" placeholder="英文名"></td>
            <td class="p-3"><input type="text" class="w-full border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white text-center" placeholder="中文名"></td>
            <td class="p-3 text-center">
                <input type="radio" name="isPrimaryKey" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50">
            </td>
            <td class="p-3 is-title-col hidden text-center">
                <input type="radio" name="isTitleDisplay" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50">
            </td>
            <td class="p-3">
                <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white">
                    <option value="varchar" selected>varchar</option>
                    <option value="int">int</option>
                    <option value="datetime">datetime</option>
                </select>
            </td>
            <td class="p-3"><input type="number" class="w-16 border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white text-center" value="255"></td>
            <td class="p-3">
                <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white">
                    <option value="text" selected>文本</option>
                    <option value="cascade">级联</option>
                    <option value="select">下拉框</option>
                </select>
            </td>
            <td class="p-3"><input type="text" class="w-16 border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white text-center" value="-"></td>
            <td class="p-3">
                <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white">
                    <option value="no" selected>否</option>
                    <option value="yes">是</option>
                </select>
            </td>
            <td class="p-3">
                <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white">
                    <option value="no" selected>否</option>
                    <option value="yes">是</option>
                </select>
            </td>
            <td class="p-3"><input type="text" class="w-16 border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white text-center" value="-"></td>
            <td class="p-3 text-center">
                <button class="text-blue-600 hover:text-blue-800 transition" onclick="toggleVisibility(this)">
                    <i class="fa-solid fa-eye" title="显示状态"></i>
                </button>
            </td>
            <td class="p-3">
                <div class="flex items-center justify-center space-x-2">
                    <button class="text-blue-600 hover:text-blue-800 transition" onclick="toggleEditRow(this)">保存</button>
                    <button class="text-red-500 hover:text-red-700 transition" onclick="deleteRow(this)"><i class="fa-solid fa-trash-can"></i></button>
                </div>
            </td>
"""

    # We need to build the new content piecemeal
    new_content = ""
    last_end = 0
    for i, match in enumerate(filtered_matches):
        new_content += content[last_end:match.start(1)]
        if i == 0:
            new_content += "\n" + correct_tr_inner_disabled.strip() + "\n                    "
        elif i == 1:
            # Need to adjust indentation for the second one slightly if needed, but it's fine
            new_content += "\n" + correct_tr_inner_disabled.replace('                        <td', '                    <td').strip() + "\n                "
        elif i == 2:
            new_content += "\n" + correct_tr_inner_enabled.strip() + "\n        "
        last_end = match.end(1)
    
    new_content += content[last_end:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed HTML successfully!")
