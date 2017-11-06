from AVL_Tree import Binary_Search_Tree
class Fraction:

  def __init__(self, numerator, denominator):
    # use caution here... In most languages, it is not a good idea to
    # raise an exception from a constructor. Python is a bit different
    # and it shouldn't cause a problem here.
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    #TODO replace pass with your implementation,
    #returning True if self is less than other and
    #False otherwise.
    self_n = self.__n * other.__d
    other_n = other.__n * self.__d
    
    temp = self.__d * other.__d
    
    other_d = temp
    self_d = temp
    
    
    if self_n < other_n:
      return True
    else:
      return False
    
    
    

  def __gt__(self, other):
    #TODO replace pass with your implementation,
    #returning True if self is greater than other and
    #False otherwise.
    
    self_n = self.__n * other.__d
    other_n = other.__n * self.__d
    
    temp = self.__d * other.__d
    
    other_d = temp
    self_d = temp
    
    if self_n > other_n:
      return True
    else:
      return False

  def __eq__(self, other):
    #TODO replace pass with your implementation,
    #returning True if self equal to other and
    #False otherwise. Note that fractions are
    #stored in reduced form.
    if self.__n == other.__n and self.__d == other.__d:
      return True
    else:
      return False

  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  # the __repr__ method is similar to __str__, but is called
  # when Python wants to display these objects in a container like
  # a Python list.
  def __repr__(self):
    return str(self)

if __name__ == '__main__':
  #TODO create a bunch of fraction objects and store them in an array.
  #Then insert each item from the array into a balanced BST.
  #Then get the in-order array representation of the BST using
  #the new to_list() method, which you must implement.
  #print the original and in-order traversal arrays to show that
  #the fractions have been sorted.
  tree = Binary_Search_Tree()
  a = Fraction(1,2)
  b = Fraction(2,3)
  c = Fraction(3,4)
  d = Fraction(5,6)
  e = Fraction(1,3)
  f = Fraction(1,4)
  g = Fraction(5,7)
  h = Fraction(5,9)
  i = Fraction(17,29)
  j = Fraction(30,61)
  k = Fraction(7,48)
  l = Fraction(2,28)
  
  fraction_list = [a,b,c,d,e,f,g,h,i,j,k,l]
  
  for i in fraction_list:
    tree.insert_element(i)
  print(tree.to_list())
  print(tree.in_order())
  
  
