# Drills - Linked List Basics
# Follow the instructions in the comments. Write your code directly below the comment.
# ----------------------------------------------------------------------------------

# Drill 1: Create a Node class with data and next attributes
from __future__ import annotations

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None

# Drill 2: Create a LinkedList class with head attribute
# Drill 3: Implement append(), display methods
from typing import Any

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data)-> Any:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node