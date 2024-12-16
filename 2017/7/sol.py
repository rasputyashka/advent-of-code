from __future__ import annotations
from dataclasses import dataclass, field
from re import compile
from pprint import pprint
from collections import deque, Counter

pattern = compile(r'(\w+) \((\d+)\)( -> )?(.*)')

all_nodes = {}

@dataclass
class Node:
    name: str
    value: int = 0
    total_value: int = 0
    children: list[str] = field(default_factory=list)
    parent: None|Node = None

    def __repr__(self):
        return f"{self.name} {str(self.value)} {str(self.children)} {str(self.parent)} {self.total_value}"


for line in open(0).readlines():
    find = pattern.search(line)
    name = find.group(1)
    value = int(find.group(2))
    children = find.group(4)
    if name not in all_nodes:
        cur_node = Node(name=name, value=value)
    else:
        cur_node = all_nodes[name]
        cur_node.value = value
    if children:
        for child in children.split(", "):
            if child not in all_nodes:
                child_node = Node(name=child, parent=cur_node, value=1000000)
            else:
                child_node = all_nodes[child]
                child_node.parent = cur_node
            cur_node.children.append(child)
            all_nodes[child] = child_node
    all_nodes[name] = cur_node

def get_total(node):
    res = node.value
    for child in node.children:
        child_node = all_nodes[child]
        if child_node.children == []:
            res += child_node.value
        else:
            res += get_total(child_node)
    return res

def get_root():
    for k, v in all_nodes.items():
        if v.parent is None:
            return v

for node in all_nodes.values():
    node.total_value = get_total(node)

root_node = get_root()

cursum = -1
while True:
    subnodes = [all_nodes[node] for node in root_node.children]
    subnodes_values = [subnode.total_value for subnode in subnodes]
    if len(set(subnodes_values)) == 2:
        counter = Counter(subnodes_values)
        for subnode in subnodes:
            if counter[subnode.total_value] == 1:
                root_node = subnode
                print(set(subnodes_values))
                break
    else:
        print(root_node.value)
        exit(0)
