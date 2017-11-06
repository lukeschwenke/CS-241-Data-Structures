import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    # Run your tests with each deque type to ensure that
    # they behave identically.
    self.__deque = get_deque(ARR_DEQUE_TYPE)
    self.__stack = Stack()
    self.__queue = Queue()
  
  def test_empty_stack_string(self):
    self.assertEqual('[ ]', str(self.__stack))
    
  def test_filled_stack_string(self):
    self.__stack.push('A')
    self.__stack.push('B')
    self.assertEqual('[ B, A ]', str(self.__stack))       
    
  def test_push_empty_stack(self):
    self.__stack.push('A')
    self.assertEqual('[ A ]', str(self.__stack))

  def test_push_onto_filled_stack(self):
    self.__stack.push('A')
    self.__stack.push('B')
    self.assertEqual('[ B, A ]', str(self.__stack))
 
  def test_pop_empty_stack(self):
    with self.assertRaises(IndexError):
        returned = self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_filled_stack_returned_value(self):
    self.__stack.push('A')
    returned = self.__stack.pop()
    self.assertEqual('A', returned)
    
  def test_pop_filled_stack_remaining(self):
    self.__stack.push('A')
    returned = self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))
  
  def test_pop_two_value_stack_returned_value(self):
    self.__stack.push('A')
    self.__stack.push('B')
    returned = self.__stack.pop()
    self.assertEqual('B', returned)
    
  def test_pop_two_value_stack_remaining(self):
    self.__stack.push('A')
    self.__stack.push('B')
    returned = self.__stack.pop()
    self.assertEqual('[ A ]', str(self.__stack))
  
  def test_peek_empty_stack(self):
    with self.assertRaises(IndexError):
        self.__stack.peek()
    self.assertEqual('[ ]', str(self.__stack))
    
  def test_peek_one_value_stack(self):
    self.__stack.push('A')
    returned = self.__stack.peek()
    self.assertEqual('A', returned)
  
  def test_peek_two_value_stack(self):
    self.__stack.push('A')
    self.__stack.push('B')
    returned = self.__stack.peek()
    self.assertEqual('B', returned)
  
  def test_empty_queue_string(self):
    self.assertEqual('[ ]', str(self.__queue))
    
  def test_filled_queue_string(self):
    self.__queue.enqueue('A')
    self.__queue.enqueue('B')
    self.assertEqual('[ A, B ]', str(self.__queue))       
    
  def test_enqueue_empty_queue(self):
    self.__queue.enqueue('A')
    self.assertEqual('[ A ]', str(self.__queue))

  def test_enqueue_onto_filled_queue(self):
    self.__queue.enqueue('A')
    self.__queue.enqueue('B')
    self.assertEqual('[ A, B ]', str(self.__queue))
 
  def test_dequeue_empty_queue(self):
    with self.assertRaises(IndexError):
        returned = self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_filled_queue_returned_value(self):
    self.__queue.enqueue('A')
    returned = self.__queue.dequeue()
    self.assertEqual('A', returned)
    
  def test_dequeue_filled_queue_remaining(self):
    self.__queue.enqueue('A')
    returned = self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))
  
  def test_dequeue_two_value_queue_returned_value(self):
    self.__queue.enqueue('A')
    self.__queue.enqueue('B')
    returned = self.__queue.dequeue()
    self.assertEqual('A', returned)
    
  def test_dequeue_two_value_queue_remaining(self):
    self.__queue.enqueue('A')
    self.__queue.enqueue('B')
    returned = self.__queue.dequeue()
    self.assertEqual('[ B ]', str(self.__queue))

  def test_empty_deque_string(self):
    self.assertEqual('[ ]', str(self.__deque))
    
  def test_filled_deque_string_front(self):
    self.__deque.push_front('A')
    self.__deque.push_front('B')
    self.assertEqual('[ B, A ]', str(self.__deque))

  def test_filled_deque_string_back(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    self.assertEqual('[ A, B ]', str(self.__deque))       
    
  def test_push_empty_deque_front(self):
    self.__deque.push_front('A')
    self.assertEqual('[ A ]', str(self.__deque))

  def test_push_onto_filled_deque_front(self):
    self.__deque.push_front('A')
    self.__deque.push_front('B')
    self.assertEqual('[ B, A ]', str(self.__deque))
    
  def test_push_empty_deque_back(self):
    self.__deque.push_back('A')
    self.assertEqual('[ A ]', str(self.__deque))

  def test_push_onto_filled_deque_back(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    self.assertEqual('[ A, B ]', str(self.__deque))
 
  def test_pop_empty_deque_front(self):
    with self.assertRaises(IndexError):
        returned = self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_filled_deque_returned_value_front(self):
    self.__deque.push_front('A')
    returned = self.__deque.pop_front()
    self.assertEqual('A', returned)
    
  def test_pop_filled_deque_remaining_front(self):
    self.__deque.push_front('A')
    returned = self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_pop_two_value_deque_returned_value_front(self):
    self.__deque.push_front('A')
    self.__deque.push_front('B')
    returned = self.__deque.pop_front()
    self.assertEqual('B', returned)
    
  def test_pop_two_value_deque_remaining_front(self):
    self.__deque.push_front('A')
    self.__deque.push_front('B')
    returned = self.__deque.pop_front()
    self.assertEqual('[ A ]', str(self.__deque))

  def test_pop_empty_deque_back(self):
    with self.assertRaises(IndexError):
        returned = self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_filled_deque_returned_value_back(self):
    self.__deque.push_back('A')
    returned = self.__deque.pop_back()
    self.assertEqual('A', returned)
    
  def test_pop_filled_deque_remaining_back(self):
    self.__deque.push_back('A')
    returned = self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_pop_two_value_deque_returned_value_back(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    returned = self.__deque.pop_back()
    self.assertEqual('B', returned)
    
  def test_pop_two_value_deque_remaining_back(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    returned = self.__deque.pop_back()
    self.assertEqual('[ A ]', str(self.__deque))
  
  def test_peek_empty_deque_front(self):
    with self.assertRaises(IndexError):
        self.__deque.peek_front()
    self.assertEqual('[ ]', str(self.__deque))
    
  def test_peek_one_value_deque_front(self):
    self.__deque.push_front('A')
    returned = self.__deque.peek_front()
    self.assertEqual('A', returned)
  
  def test_peek_two_value_deque_front(self):
    self.__deque.push_front('A')
    self.__deque.push_front('B')
    returned = self.__deque.peek_front()
    self.assertEqual('B', returned)      

  def test_peek_empty_deque_back(self):
    with self.assertRaises(IndexError):
        self.__deque.peek_back()
    self.assertEqual('[ ]', str(self.__deque))
    
  def test_peek_one_value_deque_back(self):
    self.__deque.push_back('A')
    returned = self.__deque.peek_back()
    self.assertEqual('A', returned)
  
  def test_peek_two_value_deque_back(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    returned = self.__deque.peek_back()
    self.assertEqual('B', returned)   
    

  
  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

if __name__ == '__main__':
  unittest.main()
  

        

