# CLRS P3 S12 Binary Search Trees

from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    p :Node
    key: int
    left: Node
    right: Node

def inorder_tree_walk(tree: Node) -> None:
    if tree != Nil: 
        inorder_tree_walk(tree.left)
        print(tree.key)
        inorder_tree_walk(tree.right)

def tree_search(tree: Node, k: int) -> Node:
    if tree == Nil or tree.key == k:
        return tree
    elif tree.key > k:
        return tree_search(tree.left,k)
    else:
        return tree_search(tree.right,k)

def tree_search_interative(tree: Node, k: int) -> Node:
    while tree != Nil and tree.key != k:
        tree = tree.right if tree.key < k else tree.left
    return tree

def tree_min(tree: Node) -> Node:
    while tree != Nil and tree.left != Nil:
        tree = tree.left
    return tree

def tree_max(tree: Node) -> Node:
    while tree != Nil and tree.right != Nil:
        tree = tree.left
    return tree

def tree_successor(n: Node) -> Node:
    if n == Nil:
        return Nil 
    if n.right != Nil:
        return tree_min(tree.right)
    else:
        curr = n
        while curr.p != Nil and curr.p.left != curr: # same as curr.p.right == curr
            curr = curr.p
        return curr.p

def tree_predecessor(n: Node) -> Node:
    if n == Nil:
        return Nil 
    if n.left != Nil:
        return tree_max(tree.left)
    else:
        curr = n
        while curr.p != Nil and curr.p.right != curr:
            curr = curr.p
        return curr.p

def tree_insert(tree: Node, n: Node) -> None:
    if tree == Nil:
        return n
    prev = Nil
    while tree != Nil:
        prev = tree
        tree = tree.right if tree.key < n.key else tree.left
    n.p = prev
    if prev.key < n.key:
        prev.right = n 
    else: 
        prev.left = n

# leave both out, in's children untouched, it's up to caller to decide
def transplant(tree: Node, out: Node, In: Node) -> None:
    if tree == Nil or out == Nil:
        return
    if out.p == Nil:
        tree = In
    elif out == out.p.right:
        out.p.right = In
    else:
        out.p.left = In
    if In != Nil:
        In.p = out.p
    
def tree_delete(tree: Node, n: Node) -> None:
    if tree == Nil or n == Nil:
        return
    if n.left == Nil and n.right == Nil:
        transplant(tree, n, Nil)
    elif n.left != nil:
        transplant(tree, n, n.left)
    elif n.right != nil:
        transplant(tree, n, n.right)
    else:
        successor = tree_min(n.right)
        if successor.p == n: # or n.right == successor
            transplant(tree, n, successor)
        else:
            transplant(tree, successor, successor.right)
            successor.right = n.right
            successor.right.p = successor
            transplant(tree, n, successor)
            successor.left = n.left
            successor.left.p = successor

