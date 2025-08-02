import re

import LinkedList as ll

import_expression = re.compile(r'import\s+\'([A-z0-9_\-.\\])\'')

def main():
    list = ll.LinkedList()
    list.append_item("Fat girls are cute!")
    list.append_item("Fat girls are sexy!")
    list.append_item("Fat boobies are hypnotic!")

    node = list.find_parent(lambda val: val == "Fat girls are sexy!")
    list.insert_after(node, "Fat butts are squeezable!")

    for node in list.scan_list():
        print(node.item)

if __name__ == '__main__':
    main()