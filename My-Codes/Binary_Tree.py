## use node.leftchild / node.rightchild for CLASS calling instead of (self.leftchild)


class Node:
  def __init__(self, value):
      self.value = value
      self.leftchild = None
      self.rightchild = None


class BinaryTree:
  def __init__(self):
      self.root = None

  def insert(self, value): ## ## Insert function specifically for EMPTY mother class
      if self.root is None:
          self.root = Node(value)
      else:
          self._insert(value, self.root) ## redirects to _insert

  def _insert(self, value, node): ## "node" over here is the self.root (current_mothernode)
      if value < node.value: ## compares with the root node and later with the redirected node(Continueing)
          if node.leftchild is None: 
              node.leftchild = Node(value)
          else:
              self._insert(value, node.leftchild) ## now it will compare with the leftchild class and proceeed 
      else:
          if node.rightchild is None:
              node.rightchild = Node(value)
          else:
              self._insert(value,node.rightchild)
  def delete(self, value):
    if self.root is not None:
        self.root = self._delete(value, self.root)

  def _delete(self, value, node):
    if node is None:
        return node

    if value < node.value:
        node.left_child = self._delete(value, node.left_child)
    elif value > node.value:
        node.right_child = self._delete(value, node.right_child)
    else:
        if node.left_child is None:
            return node.right_child
        elif node.right_child is None:
            return node.left_child

        node.value = self._min_value(node.right_child)
        node.right_child = self._delete(node.value, node.right_child)

    return node

  def _min_value(self, node):
    while node.left_child is not None:
        node = node.left_child
    return node.value
          
