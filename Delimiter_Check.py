import sys # for sys.argv, the command-line arguments
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE


def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
  deque = get_deque()
  file = open(filename, 'r')
  content = file.read()
  for char in content:
      a = 0
      if char == "(":
          deque.push_back(char)
          a = 1
      if char == "[":
          deque.push_back(char)
          a = 2
      if char == "{":
          deque.push_back(char)
          a = 3
      if char == ")":
          if a == 2 or a == 3:
              return False
          if deque.peek_back() == "(":
              deque.pop_back()
              a = 0
          else: 
              return False
      if char == "]":
          if a == 1 or a == 3:
              return False
          if deque.peek_back() == "[":
              deque.pop_back()
              a = 0
          else: 
              return False
      if char == "}":
          if a == 1 or a == 2:
              return False
          if deque.peek_back() == "{":
              deque.pop_back()
              a = 0
          else: 
              return False
      if a == 0 is False:
          deque.push_back(char)
  if len(deque) == 0:
      return True
  else:
      return False

      
                  
          


if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


