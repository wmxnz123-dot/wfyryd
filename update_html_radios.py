import re

with open('/Users/zhanghuimin/Downloads/000潍坊个人数据空间/trae/kxkj/prototype_ui/admin_catalog_add.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_primary_key_select = """<td class="p-3">
                            <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent" disabled>
                                <option value="no" selected>否</option>
                                <option value="yes">是</option>
                            </select>
                        </td>"""

new_primary_key_radio = """<td class="p-3 text-center">
                            <input type="radio" name="isPrimaryKey" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50" disabled>
                        </td>"""

old_title_display_select = """<td class="p-3 is-title-col hidden">
                            <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent" disabled>
                                <option value="no" selected>否</option>
                                <option value="yes">是</option>
                            </select>
                        </td>"""

new_title_display_radio = """<td class="p-3 is-title-col hidden text-center">
                            <input type="radio" name="isTitleDisplay" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50" disabled>
                        </td>"""

# For onTableSelectChange
content = content.replace(old_primary_key_select, new_primary_key_radio)
content = content.replace(old_title_display_select, new_title_display_radio)

# For toggleDataType
old_primary_key_select_2 = """<td class="p-3">
                        <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent" disabled>
                            <option value="no" selected>否</option>
                            <option value="yes">是</option>
                        </select>
                    </td>"""

new_primary_key_radio_2 = """<td class="p-3 text-center">
                        <input type="radio" name="isPrimaryKey" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50" disabled>
                    </td>"""

old_title_display_select_2 = """<td class="p-3 is-title-col hidden">
                        <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-transparent" disabled>
                            <option value="no" selected>否</option>
                            <option value="yes">是</option>
                        </select>
                    </td>"""

new_title_display_radio_2 = """<td class="p-3 is-title-col hidden text-center">
                        <input type="radio" name="isTitleDisplay" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50" disabled>
                    </td>"""

content = content.replace(old_primary_key_select_2, new_primary_key_radio_2)
content = content.replace(old_title_display_select_2, new_title_display_radio_2)

# For addFieldRow
old_primary_key_select_3 = """<td class="p-3">
                <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white">
                    <option value="no" selected>否</option>
                    <option value="yes">是</option>
                </select>
            </td>"""

new_primary_key_radio_3 = """<td class="p-3 text-center">
                <input type="radio" name="isPrimaryKey" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50">
            </td>"""

old_title_display_select_3 = """<td class="p-3 is-title-col hidden">
                <select class="border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:border-blue-500 bg-white">
                    <option value="no" selected>否</option>
                    <option value="yes">是</option>
                </select>
            </td>"""

new_title_display_radio_3 = """<td class="p-3 is-title-col hidden text-center">
                <input type="radio" name="isTitleDisplay" class="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500 cursor-pointer disabled:opacity-50">
            </td>"""

content = content.replace(old_primary_key_select_3, new_primary_key_radio_3)
content = content.replace(old_title_display_select_3, new_title_display_radio_3)

# Update toggleEditRow function
old_toggle_edit_row_inputs_1 = """inputs.forEach(input => {
                input.removeAttribute('readonly');
                input.classList.remove('bg-transparent');
                input.classList.add('bg-white');
            });"""

new_toggle_edit_row_inputs_1 = """inputs.forEach(input => {
                if (input.type === 'radio') {
                    input.removeAttribute('disabled');
                } else {
                    input.removeAttribute('readonly');
                    input.classList.remove('bg-transparent');
                    input.classList.add('bg-white');
                }
            });"""

old_toggle_edit_row_inputs_2 = """inputs.forEach(input => {
                input.setAttribute('readonly', 'true');
                input.classList.remove('bg-white');
                input.classList.add('bg-transparent');
            });"""

new_toggle_edit_row_inputs_2 = """inputs.forEach(input => {
                if (input.type === 'radio') {
                    input.setAttribute('disabled', 'true');
                } else {
                    input.setAttribute('readonly', 'true');
                    input.classList.remove('bg-white');
                    input.classList.add('bg-transparent');
                }
            });"""

content = content.replace(old_toggle_edit_row_inputs_1, new_toggle_edit_row_inputs_1)
content = content.replace(old_toggle_edit_row_inputs_2, new_toggle_edit_row_inputs_2)

with open('/Users/zhanghuimin/Downloads/000潍坊个人数据空间/trae/kxkj/prototype_ui/admin_catalog_add.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML Updated with radios!")
