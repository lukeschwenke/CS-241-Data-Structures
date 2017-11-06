class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.val = val
      self.next = None
      self.prev = None
      

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
      self.__header = self.__Node(None)
      self.__trailer = self.__Node(None)
      self.__size = 0
      self.__header.next = self.__trailer
      self.__trailer.prev = self.__header
      self.__header.prev = None
      self.__trailer.next = None
      

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    # TODO replace pass with your implementation
    return self.__size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    new_node = Linked_List.__Node(val)
    new_node.next = self.__trailer
    self.__trailer.prev.next = new_node
    new_node.prev = self.__trailer.prev
    self.__trailer.prev = new_node
    self.__size = self.__size + 1
    
    

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    # TODO replace pass with your implementation
    new_node = Linked_List.__Node(val)
    if index >= self.__size or index < 0: #If size is 0 index error will be raised.
      raise IndexError 
    current = self.__header
    for i in range(index):
      current = current.next
    new_node.next = current.next
    current.next = new_node
    new_node.next.prev = new_node
    new_node.prev = current
    self.__size = self.__size + 1

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    if index >= self.__size or index < 0:
      raise IndexError
    current = self.__header.next
    for i in range(index):  
      current = current.next
    current.prev.next = current.next
    current.next.prev = current.prev
    current.next = None
    current.prev = None
    self.__size = self.__size - 1
    return current.val
    
  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    # TODO replace pass with your implementation
    if index >= self.__size or index < 0:
      raise IndexError
    current = self.__header.next
    for i in range(index):
      current = current.next
    return current.val
    
  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    
    if self.__size > 1: #If size is 1 it would not change the list. 
      head = self.__header.next
      self.__header.next = head.next
      head.next.prev = self.__header
      head.next = self.__trailer
      head.prev = self.__trailer.prev
      self.__trailer.prev.next = head
      self.__trailer.prev = head
    
  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    if self.__size == 0:
      return("[ ]")
    else:
      current = self.__header.next
      str_1 = "[ " + str(current.val) 
      current = current.next
      for i in range(self.__size - 1):
        str_1 = str_1 + ", " + str(current.val)
        current = current.next
      str_1 += " ]" 
      return(str_1)
      
  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    self.__iter_Node = self.__header.next
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    if self.__iter_Node is self.__trailer:
      raise StopIteration
    to_return = self.__iter_Node.val
    self.__iter_Node = self.__iter_Node.next
    return to_return

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
  
  Test_1 = Linked_List() #Testing empty Linked List
  print(len(Test_1))
  print(Test_1)
  try:
    Test_1.insert_element_at(5, 3)
  except IndexError:
    print("Good")
  try:
    Test_1.insert_element_at(4, 0)
  except IndexError:
    print("Good")
  try:
    Test_1.insert_element_at(3, -1)
  except IndexError:
    print("Good")
  try:
    Test_1.remove_element_at(2)
  except IndexError:
    print("Good")
  try:
    Test_1.remove_element_at(0)
  except IndexError:
    print("Good")
  try:
    Test_1.remove_element_at(-7)
  except IndexError:
    print("Good")
  try:
    Test_1.get_element_at(3)
  except IndexError:
    print("Good")
  try:
    Test_1.get_element_at(0)
  except IndexError:
    print("Good")
  try:
    Test_1.get_element_at(-4)
  except IndexError:
    print("Good")
  try:
    Test_1.rotate_left()
  except IndexError:
    print("Bad")
  print(len(Test_1))
  print(Test_1)
  
  #testing Linked_List of one element 
  try:
    Test_1.append_element(3)
  except IndexError:
    print("Bad")
  try:
    Test_1.insert_element_at(5, 3)
  except IndexError:
    print("Good")
  try:
    Test_1.insert_element_at(4, 0)
  except IndexError:
    print("Bad")
  try:
    Test_1.insert_element_at(3, -1)
  except IndexError:
    print("Good")
  try:
    Test_1.remove_element_at(2)
  except IndexError:
    print("Good")
  try:
    Test_1.remove_element_at(0)
  except IndexError:
    print("Bad")
  try:
    Test_1.remove_element_at(-7)
  except IndexError:
    print("Good")
  try:
    Test_1.get_element_at(3)
  except IndexError:
    print("Good")
  try:
    Test_1.get_element_at(0)
  except IndexError:
    print("Bad")
  try:
    Test_1.get_element_at(-4)
  except IndexError:
    print("Good")
  try:
    Test_1.rotate_left()
  except IndexError:
    print("Bad")
  print(len(Test_1))
  print(Test_1)

  #testing Linked_List of multiple elements
  try:
    Test_1.append_element(16)
    Test_1.append_element(92)
    Test_1.append_element(7)
  except IndexError:
    print("Bad")  
  try:
    Test_1.insert_element_at(5, 7)
  except IndexError:
    print("Good")
  try:
    Test_1.insert_element_at(4, 3)
  except IndexError:
    print("Bad")
  try:
    Test_1.insert_element_at(4, 0)
  except IndexError:
    print("Bad")
  try:
    Test_1.insert_element_at(3, -1)
  except IndexError:
    print("Good")
  try:
    Test_1.remove_element_at(7)
  except IndexError:
    print("Good")
  try:
    Test_1.remove_element_at(2)
  except IndexError:
    print("Bad")
  try:
    Test_1.remove_element_at(0)
  except IndexError:
    print("Bad")
  try:
    Test_1.remove_element_at(-7)
  except IndexError:
    print("Good")
  try:
    Test_1.get_element_at(12)
  except IndexError:
    print("Good")
  try:
    Test_1.get_element_at(3)
  except IndexError:
    print("Bad")
  try:
    Test_1.get_element_at(0)
  except IndexError:
    print("Bad")
  try:
    Test_1.get_element_at(-4)
  except IndexError:
    print("Good")
  try:
    Test_1.rotate_left()
  except IndexError:
    print("Bad")
  print(len(Test_1))
  print(Test_1)
  
  #testing iterating through multiple element Linked_List
  try:
    for element in Test_1:
      print(element)
  except IndexError:
    print("Bad")