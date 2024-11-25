class Node:
  def __init__(self,key):
    self.data = key
    self.right = None
    self.left = None

def max_height(A):
  if(A==None):
    return 0
  else
    ldepth = max_height(A.left)
    Rdepth = max_height(A.left)
    if(ldepth>Rdepth):
      return (1 + ldepth)
    else
      return (1+ Rdepth)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)

max_height(root)
  
