from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__size = 0
    self.__contents = [None] * self.__capacity
    self.__headnumber = 0
    self.__tailnumber = 0
    # TODO replace pass with any additional initializations you need.
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    if self.__size == 0:
        return "[ ]"
    else:
        string = "[ " + str(self.__contents[self.__headnumber])
        for val in range(self.__size - 1):
            string = string + ", " + str(self.__contents[((self.__headnumber + 1 + val)%self.__capacity)])
        return string + " ]"
            

            


    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    temparr = [None] * (self.__capacity * 2)
    for node in range(self.__size):
        temparr[node] = self.__contents[(self.__headnumber + node)%self.__capacity]
    self.__contents = temparr
    self.__headnumber = 0
    self.__tailnumber = self.__size - 1
    self.__capacity = self.__capacity * 2
    


    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary
    if self.__size == self.__capacity:
        self.__grow()
    if self.__size == 0:
        self.__contents[self.__headnumber] = val
        self.__size = self.__size + 1
    else: 
        self.__headnumber = ((self.__headnumber - 1 + self.__capacity)%self.__capacity)
        self.__contents[self.__headnumber] = val
        self.__size = self.__size + 1
  
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    val = self.__contents[self.__headnumber]
    self.__contents[self.__headnumber] = None
    self.__headnumber = (((self.__headnumber + 1)%self.__capacity))
    self.__size = self.__size - 1
    return val
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    return self.__contents[self.__headnumber]
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == self.__capacity:
        self.__grow()
    self.__tailnumber  = ((self.__tailnumber + 1)%self.__capacity)
    self.__contents[self.__tailnumber]  = val
    self.__size = self.__size + 1

  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    val = self.__contents[self.__tailnumber]
    self.__contents[self.__tailnumber] = None
    self.__tailnumber = ((self.__tailnumber - 1)%self.__capacity)
    self.__size = self.__size - 1
    return val

  def peek_back(self):
    # TODO replace pass with your implementation.
    return self.__contents[self.__tailnumber]


# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':

    