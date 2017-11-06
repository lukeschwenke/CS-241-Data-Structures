class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      #depth is actually the height of the tree rooted at a node
      self.depth = 0
      self.left = None
      self.right = None
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None
    # TODO complete initialization
    
    
    
  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.recursive_insert(value, self.__root)
  
  def recursive_insert(self, value, t):
    #BASE CASE
    if t == None:
      new_node = self.__BST_Node(value)
      new_node.depth = 1
      return new_node
    #RECURSIVE
    elif value > t.value:
      t.right = self.recursive_insert(value, t.right)
      #THIS FIRST STATEMENT IS USELESS
      if t.right != None and t.left != None:
        t.depth = 1 + max(t.left.depth, t.right.depth)
      elif t.right != None and t.left == None:
        t.depth = 1 + t.right.depth
      elif t.right == None and t.left != None:
        t.depth = 1 + t.left.depth
        
      return t
    elif value < t.value:
      t.left = self.recursive_insert(value, t.left)

      if t.right != None and t.left != None:
        t.depth = 1 + max(t.left.depth, t.right.depth)
      elif t.right != None and t.left == None:
        t.depth = 1 + t.right.depth
      elif t.right == None and t.left != None:
        t.depth = 1 + t.left.depth
        
      return t
    elif value == t.value:
      raise ValueError
  
  
  

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.recursive_remove(value, self.__root)
    
  def recursive_remove(self, value, t):
    if t == None:
      raise ValueError
    #RECURSIVE
    elif value > t.value:
      t.right = self.recursive_remove(value, t.right)
      
      if t.right == None and t.left == None:
        t.depth = 1
      elif t.right != None and t.left != None:
        t.depth = 1 + max(t.left.depth, t.right.depth)
      elif t.right != None and t.left == None:
        t.depth = 1 + t.right.depth
      elif t.right == None and t.left != None:
        t.depth = 1 + t.left.depth
        
      return t
    elif value < t.value:
      t.left = self.recursive_remove(value, t.left)
      
      if t.right == None and t.left == None:
        t.depth = 1
      elif t.right != None and t.left != None:
        t.depth = 1 + max(t.left.depth, t.right.depth)
      elif t.right != None and t.left == None:
        t.depth = 1 + t.right.depth
      elif t.right == None and t.left != None:
        t.depth = 1 + t.left.depth
        
      return t
    #BASE
    elif value == t.value:
      if (t.left == None) and (t.right == None):
        t = None
      elif (t.left != None) and (t.right != None):
        t.value = self.min_on_right(t)
        t.right = self.recursive_remove(t.value, t.right)
        
        if t.right == None and t.left == None:
          t.depth = 1
        elif t.right != None and t.left != None:
          t.depth = 1 + max(t.left.depth, t.right.depth)
        elif t.right != None and t.left == None:
          t.depth = 1 + t.right.depth
        elif t.right == None and t.left != None:
          t.depth = 1 + t.left.depth
          
        return t
      elif (t.left == None) and (t.right != None):
        return t.right
      elif (t.left != None) and (t.right == None):
        return t.left
        
        
  def min_on_right(self, t):
    min = t.right
    while(min.left != None):
      min = min.left
    return min.value

    
    
  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    str = "[ "
    str = str + self.recursive_in_order(self.__root)
    str = str[:-2] + " ]" 
    return str
    
  def recursive_in_order(self, t):
    if t == None:
      return " "
    elif t.left != None and t.right != None:
      return self.recursive_in_order(t.left) + str(t.value) + ", " + self.recursive_in_order(t.right)
    elif t.left == None and t.right != None:
      return str(t.value) + ", " + self.recursive_in_order(t.right)
    elif t.left == None and t.right == None:
      return str(t.value) + ", "
    elif t.left != None and t.right == None:
      return self.recursive_in_order(t.left) + str(t.value) + ", "

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    str = "[ "
    str = str + self.recursive_pre_order(self.__root)
    str = str[:-2] + " ]" 
    return str
    
  def recursive_pre_order(self, t):
    if t == None:
      return " "
    elif t.left != None and t.right != None:
      return str(t.value) + ", " + self.recursive_pre_order(t.left) + self.recursive_pre_order(t.right)
    elif t.left == None and t.right != None:
      return str(t.value) + ", " + self.recursive_pre_order(t.right)
    elif t.left == None and t.right == None:
      return str(t.value) + ", "
    elif t.left != None and t.right == None:
      return str(t.value) + ", " + self.recursive_pre_order(t.left)

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    str = "[ "
    str = str + self.recursive_post_order(self.__root)
    str = str[:-2] + " ]" 
    return str
    
  def recursive_post_order(self, t):
    if t == None:
      return " "
    elif t.left != None and t.right != None:
      return self.recursive_post_order(t.left) + self.recursive_post_order(t.right)+ str(t.value) + ", "
    elif t.left == None and t.right != None:
      return self.recursive_post_order(t.right) + str(t.value) + ", "
    elif t.left == None and t.right == None:
      return str(t.value) + ", "
    elif t.left != None and t.right == None:
      return self.recursive_post_order(t.left) + str(t.value) + ", "

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root == None:
      return 0
    else:
      return self.__root.depth
    
  def __str__(self):
    return self.in_order()

#if __name__ == '__main__':
  """test = Binary_Search_Tree()
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(1)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(2)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(3)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(4)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(101)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(102)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(103)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(104)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(99)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(98)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(97)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  test.insert_element(96)
  print(test.get_height())
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())"""
