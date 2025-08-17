# pyright: reportUnusedFunction=false, reportUnusedClass=false
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Node:
    val: int = 0
    next: Optional["Node"] = None
    random: Optional["Node"] = None

__all__ = ["Node", "copyRandomList"]

def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    """Deep clone a linked list with next/random pointers using a hash map."""
    if head is None:
        return None

    old_to_new: Dict[Node, Node] = {}

    # 1) Create clones (values only)
    cur = head
    while cur:
        old_to_new[cur] = Node(cur.val)
        cur = cur.next

    # 2) Wire next/random using the map
    cur = head
    while cur:
        clone = old_to_new[cur]
        clone.next = old_to_new.get(cur.next)
        clone.random = old_to_new.get(cur.random)
        cur = cur.next

    return old_to_new[head]
