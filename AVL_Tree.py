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

  def __init__(self):
    self.__root = None
    
    
    
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
      if t.right != None and t.left != None:
        t.depth = 1 + max(t.left.depth, t.right.depth)
      elif t.right != None and t.left == None:
        t.depth = 1 + t.right.depth
      elif t.right == None and t.left != None:
        t.depth = 1 + t.left.depth
        
      return self.__balance(t)
    elif value < t.value:
      t.left = self.recursive_insert(value, t.left)

      if t.right != None and t.left != None:
        t.depth = 1 + max(t.left.depth, t.right.depth)
      elif t.right != None and t.left == None:
        t.depth = 1 + t.right.depth
      elif t.right == None and t.left != None:
        t.depth = 1 + t.left.depth
        
      return self.__balance(t)
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
        
      return self.__balance(t)
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
        
      return self.__balance(t)
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
          
        return self.__balance(t)
      elif (t.left == None) and (t.right != None):
        return t.right
      elif (t.left != None) and (t.right == None):
        return t.left
  
  def __balance(self, t):
    if t.left == None and t.right == None:
      #new leaf nodes aren't checked because they are balanced
      return t
    else:
      if t.left == None:
        balance = t.right.depth
      elif t.right == None:
         balance = 0 - t.left.depth
      else:
         balance = t.right.depth - t.left.depth
         
      #print('node ' + str(t.value) + ' balance is ' + str(balance))
      if balance == 0:
        return t
      elif balance == 1:
        return t
      elif balance == -1:
        return t
      elif balance == 2:
      
        right_balance = 0
        if t.right.right == None and t.right.left == None:
          right_balance = 0
        elif t.right.right == None:
          right_balance = 0 - t.right.left.depth
        elif t.right.left == None:
          right_balance = t.right.right.depth
        else:
          right_balance = (t.right.right.depth - t.right.left.depth)
          
        if right_balance == (0 or 1):
          #print('single rotation left around ' + str(t.value))
          temp = t.right.left
          new_root = t.right
          
          new_root.left = t
          t.right = temp
          #print(new_root.value)
          #print(new_root.left.value)
          #print(new_root.right.value)
                   
          
          if t.right == None and t.left == None:
            t.depth = 1
          elif t.right != None and t.left != None:
            t.depth = 1 + max(t.left.depth, t.right.depth)
          elif t.right != None and t.left == None:
            t.depth = 1 + t.right.depth
          elif t.right == None and t.left != None:
            t.depth = 1 + t.left.depth
            
          if new_root.right == None and new_root.left == None:
            new_root.depth = 1
          elif new_root.right != None and new_root.left != None:
            new_root.depth = 1 + max(new_root.left.depth, new_root.right.depth)
          elif new_root.right != None and new_root.left == None:
            new_root.depth = 1 + new_root.right.depth
          elif new_root.right == None and new_root.left != None:
            new_root.depth = 1 + new_root.left.depth
            
          return new_root
          
          
        if right_balance == -1:
          ##print('single rotation right around ' + str(t.right.value))
          #print('single rotation left around ' + str(t.value))
          sub_temp = t.right.left.right
          old_sub_root = t.right
          new_sub_root = t.right.left
          new_sub_root.right = old_sub_root
          t.right = new_sub_root
          old_sub_root.left = sub_temp
          
          if old_sub_root.right == None and old_sub_root.left == None:
            old_sub_root.depth = 1
          elif old_sub_root.right != None and old_sub_root.left != None:
            old_sub_root.depth = 1 + max(old_sub_root.left.depth, old_sub_root.right.depth)
          elif old_sub_root.right != None and old_sub_root.left == None:
            old_sub_root.depth = 1 + old_sub_root.right.depth
          elif old_sub_root.right == None and old_sub_root.left != None:
            old_sub_root.depth = 1 + old_sub_root.left.depth
          
          if new_sub_root.right == None and new_sub_root.left == None:
            new_sub_root.depth = 1
          elif new_sub_root.right != None and new_sub_root.left != None:
            new_sub_root.depth = 1 + max(new_sub_root.left.depth, new_sub_root.right.depth)
          elif new_sub_root.right != None and new_sub_root.left == None:
            new_sub_root.depth = 1 + new_sub_root.right.depth
          elif new_sub_root.right == None and new_sub_root.left != None:
            new_sub_root.depth = 1 + new_sub_root.left.depth
          
          
          
          #print(old_sub_root.depth)
          #print(new_sub_root.depth)
          temp = new_sub_root.left
          new_sub_root.left = t
          t.right = temp
          
          
          if t.right == None and t.left == None:
            t.depth = 1
          elif t.right != None and t.left != None:
            t.depth = 1 + max(t.left.depth, t.right.depth)
          elif t.right != None and t.left == None:
            t.depth = 1 + t.right.depth
          elif t.right == None and t.left != None:
            t.depth = 1 + t.left.depth
          
          if new_sub_root.right == None and new_sub_root.left == None:
            new_sub_root.depth = 1
          elif new_sub_root.right != None and new_sub_root.left != None:
            new_sub_root.depth = 1 + max(new_sub_root.left.depth, new_sub_root.right.depth)
          elif new_sub_root.right != None and new_sub_root.left == None:
            new_sub_root.depth = 1 + new_sub_root.right.depth
          elif new_sub_root.right == None and new_sub_root.left != None:
            new_sub_root.depth = 1 + new_sub_root.left.depth
          
          
          
          return new_sub_root
        
        
      elif balance == -2:
        
        left_balance = 0
        if t.left.right == None and t.left.left == None:
          left_balance = 0
        elif t.left.right == None:
          left_balance = 0 - t.left.left.depth
        elif t.left.left == None:
          left_balance = t.left.right.depth
        else:
          left_balance = (t.left.right.depth - t.left.left.depth)
          
        if left_balance == (0 or -1):
          #print('single rotation right around ' + str(t.value))
          temp = t.left.right
          new_root = t.left
          new_root.right = t
          t.left = temp
                
          
          if t.right == None and t.left == None:
            t.depth = 1
          elif t.right != None and t.left != None:
            t.depth = 1 + max(t.left.depth, t.right.depth)
          elif t.right != None and t.left == None:
            t.depth = 1 + t.right.depth
          elif t.right == None and t.left != None:
            t.depth = 1 + t.left.depth
            
          if new_root.right == None and new_root.left == None:
            new_root.depth = 1
          elif new_root.right != None and new_root.left != None:
            new_root.depth = 1 + max(new_root.left.depth, new_root.right.depth)
          elif new_root.right != None and new_root.left == None:
            new_root.depth = 1 + new_root.right.depth
          elif new_root.right == None and new_root.left != None:
            new_root.depth = 1 + new_root.left.depth
          
          return new_root
          
        if left_balance == 1:
          #print('single rotation left around ' + str(t.right.value))
          #print('single rotation right around ' + str(t.value))
          sub_temp = t.left.right.left
          old_sub_root = t.left
          new_sub_root = t.left.right
          new_sub_root.left = old_sub_root
          t.left = new_sub_root
          old_sub_root.right = sub_temp
          
          
          if old_sub_root.right == None and old_sub_root.left == None:
            old_sub_root.depth = 1
          elif old_sub_root.right != None and old_sub_root.left != None:
            old_sub_root.depth = 1 + max(old_sub_root.left.depth, old_sub_root.right.depth)
          elif old_sub_root.right != None and old_sub_root.left == None:
            old_sub_root.depth = 1 + old_sub_root.right.depth
          elif old_sub_root.right == None and old_sub_root.left != None:
            old_sub_root.depth = 1 + old_sub_root.left.depth
            
          if new_sub_root.right == None and new_sub_root.left == None:
            new_sub_root.depth = 1
          elif new_sub_root.right != None and new_sub_root.left != None:
            new_sub_root.depth = 1 + max(new_sub_root.left.depth, new_sub_root.right.depth)
          elif new_sub_root.right != None and new_sub_root.left == None:
            new_sub_root.depth = 1 + new_sub_root.right.depth
          elif new_sub_root.right == None and new_sub_root.left != None:
            new_sub_root.depth = 1 + new_sub_root.left.depth
          
          temp = new_sub_root.right
          new_sub_root.right = t
          t.left = temp

          
          if t.right == None and t.left == None:
            t.depth = 1
          elif t.right != None and t.left != None:
            t.depth = 1 + max(t.left.depth, t.right.depth)
          elif t.right != None and t.left == None:
            t.depth = 1 + t.right.depth
          elif t.right == None and t.left != None:
            t.depth = 1 + t.left.depth
          
          if new_sub_root.right == None and new_sub_root.left == None:
            new_sub_root.depth = 1
          elif new_sub_root.right != None and new_sub_root.left != None:
            new_sub_root.depth = 1 + max(new_sub_root.left.depth, new_sub_root.right.depth)
          elif new_sub_root.right != None and new_sub_root.left == None:
            new_sub_root.depth = 1 + new_sub_root.right.depth
          elif new_sub_root.right == None and new_sub_root.left != None:
            new_sub_root.depth = 1 + new_sub_root.left.depth
          
          return new_sub_root
        
      

  
        
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
      
  def to_list(self):
    return self.recursive_to_list(self.__root)
    
  def recursive_to_list(self, t):
    if t == None:
      return []
    elif t.left != None and t.right != None:
      list_to_return = self.recursive_to_list(t.left)
      list_to_return.append(t.value)
      for i in self.recursive_to_list(t.right):
        list_to_return.append(i)
      return list_to_return
    elif t.left == None and t.right != None:
      list_to_return = [t.value]
      for i in self.recursive_to_list(t.right):
        list_to_return.append(i)
      return list_to_return
    elif t.left == None and t.right == None:           
      return [t.value]
    elif t.left != None and t.right == None:
      list_to_return = self.recursive_to_list(t.left)
      list_to_return.append(t.value)
      return list_to_return

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

if __name__ == '__main__':
  test = Binary_Search_Tree()
  
  test.insert_element(25)
  test.insert_element(30)
  test.insert_element(31)
  test.insert_element(50)
  test.insert_element(45)
  test.insert_element(55)
  test.insert_element(34)
  
  print(test.in_order())
  print(test.pre_order())
  print(test.post_order())
  print(test.to_list())
