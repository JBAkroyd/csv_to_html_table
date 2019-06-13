import os
import csv


op_name = 'Operational Reports'
trans_name = 'Transaction Reports'
op_filename = 'operationalCSV.csv'
trans_filename = 'transactionCSV.csv'
op_desc = 'These reports are triggered manually or through subscriptions and provide an insight into past trends and ' \
          'current state of affairs. They make use of data warehouses as they don\'t require live data. ' \
          'Usual renders are lists, graphs etc.'
trans_desc = 'Usually triggered by systems (automated scripts, workflow updates ' \
             'etc.) and generally rely on live transactional data. The usual renders includes Forms, letters, ' \
             'certificates, invoices etc.'


def heading_html(header_size, header_id, header_content):
    return '<{0} id="{1}">{2}</{0}>'.format(header_size, header_id, header_content)


def single_tag(_html_tag, *args):
    return '<{} %s>'.format(_html_tag) % ' '.join(args)


def main():
    html = heading_html('h1', 'toggleHeader', op_name)
    html += heading_html('h4', 'toggleText', op_desc)
    html += ('\n'
             '    <script>\n'
             '    function toggleTable(){\n'
             '        var t1 = document.getElementById(\'table1\');\n'
             '        var t2 = document.getElementById(\'table2\');\n'
             '        var toggleButton = document.getElementById(\'toggleButton\');\n'
             '        var toggleHeader = document.getElementById(\'toggleHeader\');\n'
             '        var toggleText = document.getElementById(\'toggleText\');\n'
             '        if(t1.style.display === \'block\'){\n'
             '        t1.style.display = \'none\';\n'
             '        t2.style.display = \'block\';\n' +
             '        toggleButton.value = "Switch to {}";\n'.format(op_name) +
             '        toggleHeader.innerHTML = "{}";\n'.format(trans_name) +
             '        toggleText.innerHTML = "{}";\n'.format(trans_desc) +
             '        }\n'
             '        else{\n'
             '        t1.style.display = \'block\';\n'
             '        t2.style.display = \'none\';\n' +
             '        toggleButton.value = "Switch to {}";\n'.format(trans_name) +
             '        toggleHeader.innerHTML = "{}";\n'.format(op_name) +
             '        toggleText.innerHTML = "{}";\n'.format(op_desc) +
             '        }\n'
             '    }\n'
             '    </script>\n'
             '    <style>\n'
             '    #toggleButton {\n'
             '        font-family: \'Gustan book\'; \n'
             '        font-size: 11px;\n'
             '    }\n'
             '    \n'
             '    #toggleText {\n'
             '        width: 40vw;\n'
             '        word-wrap: break-word;\n'
             '        padding-left: 1vw;\n'
             '        font-family: \'Gustan book\'; \n'
             '        font-size: 16px;\n'
             '        padding-bottom: 4vh;\n'
             '    }\n'
             '            \n'
             '    </style>\n')
    html += single_tag('input', 'id="toggleButton"', 'type="button"', 'value="Switch to {}"'.format(trans_name),
                     'onclick="toggleTable()"')
    html += single_tag('div', 'id="table1"', 'style="display:block"')
    html += load(op_filename, "1")
    html += "</div>"
    html += single_tag('div', 'id="table2"', 'style="display:none"')
    html += load(trans_filename, "2")
    html += "</div>"
    os.system("echo '%s' | pbcopy" % html)
    print(html)
    # format csv as html


def load(filename, number):
    table_id = "csv{}".format(number) + "Table"
    search_id = "csv{}".format(number) + "Search"
    js_fn_name = "csv{}".format(number) + "Script"
    html = ('<script>\n'
            'function $$$$() {\n'
            '  var input, filter, table, tr, td, i, txtValue;\n'
            '  input = document.getElementById("$$$$$");\n'
            '  filter = input.value.toUpperCase();\n'
            '  table = document.getElementById("$$$$$$");\n'
            '  tr = table.getElementsByTagName("tr");\n'
            '\n'
            '  for (i = 1; i < tr.length; i++) {\n'
            '	txtValue = "";\n'
            '	for (j = 0; j < tr[i].getElementsByTagName("td").length; j++){\n'
            '		td = tr[i].getElementsByTagName("td")[j];\n'
            '		if (td) {\n'
            '		  txtValue += td.textContent ||  td.innerText;\n'
            '		} \n'
            '	  }\n'
            '      if (txtValue.toUpperCase().indexOf(filter) > -1) {\n'
            '      check = document.getElementById("toggleCheckBox$$$$$$");\n'
            '      if(check.checked == false){\n'
            '        tr[i].style.display = "";\n'
            '      }\n'
            '      else {\n'
            '        status = tr[i].getElementsByTagName("td")[0].textContent || tr[i].getElementsByTagName("td")[0].innerText;\n'
            '        if(status.toUpperCase() === "ACTIVE"){\n'
            '            tr[i].style.display = "";\n'
            '        }\n'
            '        else{\n'
            '        tr[i].style.display = "none";\n'
            '        }\n'
            '      }\n'
            '    }\n'
            '    else {\n'
            '        tr[i].style.display = "none";\n'
            '      }\n'
            '  }\n'
            '}\n'
            '\n'
            'function toggleCheck$$$$$$(){\n'
            ' checkBox = document.getElementById("toggleCheckBox$$$$$$");\n'
            '  table = document.getElementById("$$$$$$");\n'
            '  tr = table.getElementsByTagName("tr");\n'
            '  for (i = 1; i < tr.length; i++) {\n'
            '	txtValue = "";\n'
            '	td = tr[i].getElementsByTagName("td")[0];\n'
            '	if (td) {\n'
            '	  txtValue += td.textContent ||  td.innerText;\n'
            '	} \n'
            '    if (txtValue.toUpperCase() != "ACTIVE" && checkBox.checked == true) {\n'
            '        tr[i].style.display = "none";\n'
            '    } else {\n'
            '      tr[i].style.display = "";\n'
            '    }\n'
            '    }  \n'
            '}\n'
            '</script>\n'
            '\n'
            '<style>\n'
            '* {\n'
            '    font-family: \'Gustan book\';\n'
            '    font-size: 13px;\n'
            '}\n'
            '\n'
            '#$$$$$ {\n'
            'font-family: \'Gustan book\';\n'
            '}\n'
            '\n'
            '#$$$$$ {\n'
            '  width: 20vw%;\n'
            '  font-weight: bold;\n'
            '  padding: 12px 20px 12px 40px;\n'
            '  border: 1px solid #ddd;\n'
            '  margin-bottom: 12px;\n'
            '}\n'
            '\n'
            '#$$$$$$ {\n'
            '  border-collapse: collapse;\n'
            '  width: 100%;\n'
            '  border: 1px solid #ddd;\n'
            '}\n'
            '\n'
            '#$$$$$$ td {\n'
            '  text-align: left;\n'
            '  padding: 12px;\n'
            '}\n'
            '\n'
            '#$$$$$$ tr {\n'
            '  border-bottom: 1px solid #ddd; \n'
            '  color: #000000;\n'
            '}\n'
            '\n'
            'th.tinyWidth {\n'
            '  text-align: left;\n'
            '  padding: 12px;\n'
            '  min-width: 7vw;\n'
            '}\n'
            '\n'
            'th.smallWidth {\n'
            '  text-align: left;\n'
            '  padding: 12px;\n'
            '  min-width: 10vw;\n'
            '}\n'
            '\n'
            'th.largeWidth {\n'
            '  text-align: left;\n'
            '  padding: 12px;\n'
            '  min-width: 40vw;\n'
            '}\n'
            '#$$$$$$ tr.header, #$$$$$$ tr:hover {\n'
            '  background-color: #006272;\n'
            '  color: #d6e4e8;\n'
            '}\n'
            '\n'
            '</style>\n'
            '\n'
            '<input type="text" id="$$$$$" onkeyup="$$$$()" placeholder="Search for names..">\n'
            'Active: <input type="checkbox" id="toggleCheckBox$$$$$$" onclick="toggleCheck$$$$$$()">\n'
            '<table id="$$$$$$">\n').replace("$$$$$$", table_id).replace("$$$$$", search_id).replace("$$$$", js_fn_name)
    reader = csv.reader(open(filename, newline=''), quotechar='|')
    for idx, row in enumerate(reader):
        # print("{}{}".format(idx, row))
        if idx == 0:
            html += header(row)
        else:
            html += reg_row(row)
    html += "</table>"
    return html


def double_tag(_html_tag, _html_contents, *args):
    return '<{0} %s>{1}</{0}>\n'.format(_html_tag, _html_contents) % ' '.join(args)


def header(row):
    html = single_tag('thead') + single_tag('tr', 'class="header"')
    for item in row:
        header_class = 'smallWidth'
        if item == 'Description' or item == 'Record Type':
            header_class = 'largeWidth'
        elif item == 'Report Status' or item == "Modified Date":
            header_class = 'tinyWidth'
        html += double_tag('th', item.replace('ÿ', ' '), 'class="{}"'.format(header_class))
    html += "</tr></thead>"
    return html


def reg_row(row):
    return double_tag('tr', ''.join(
        double_tag('td', item.replace('ÿ', ' '))
        for item in row))


if __name__ == '__main__':
    main()
