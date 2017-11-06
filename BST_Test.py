import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):

  def setUp(self):
    self.__tree = Binary_Search_Tree()
    
  def test_empty(self):
    self. assertEqual('[ ]', str(self.__tree))
	
  def test_insert_one_element(self):
    self.__tree.insert_element(3)
    self.assertEqual('[ 3 ]', str(self.__tree))

  def test_insert_two_elements(self):
    self.__tree.insert_element(3)
    self.__tree.insert_element(5)
    self.assertEqual('[ 3, 5 ]', str(self.__tree))
    self.assertEqual('[ 5, 3 ]', self.__tree.post_order())
    self.assertEqual('[ 3, 5 ]', self.__tree.pre_order())

  def test_insert_three_elements_decreasing(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(6)
    self.__tree.insert_element(1)
    self.assertEqual('[ 1, 6, 10 ]', str(self.__tree))
    self.assertEqual('[ 10, 6, 1 ]', self.__tree.pre_order())
    self.assertEqual('[ 1, 6, 10 ]', self.__tree.post_order())

  def test_get_height_balanced_three_elements(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(1)
    self.assertEqual(2, self.__tree.get_height())

  def test_get_height_left_heavy_three_elements(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(6)
    self.__tree.insert_element(1)
    self.assertEqual(3, self.__tree.get_height())

  def test_get_height_right_heavy_three_elements(self):
    self.__tree.insert_element(1)
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.assertEqual(3, self.__tree.get_height())

  def test_remove_root_from_singular_tree(self):
    self.__tree.insert_element(6)
    self.__tree.remove_element(6)
    self.assertEqual('[ ]', str(self.__tree))
    self.assertEqual(0, self.__tree.get_height())

  def test_remove_root_with_one_left_child(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(3)
    self.__tree.remove_element(6)
    self.assertEqual('[ 3 ]', str(self.__tree))
    self.assertEqual(1, self.__tree.get_height())

  def test_remove_root_with_one_right_child(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(8)
    self.__tree.remove_element(6)
    self.assertEqual('[ 8 ]', str(self.__tree))
    self.assertEqual(1, self.__tree.get_height())

  def test_remove_root_with_two_children(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(1)
    self.__tree.remove_element(6)
    self.assertEqual('[ 1, 10 ]', str(self.__tree))
    self.assertEqual('[ 1, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 1 ]', self.__tree.pre_order())
    self.assertEqual(2, self.__tree.get_height())

  def test_remove_right_node_with_no_children(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(1)
    self.__tree.remove_element(10)
    self.assertEqual('[ 1, 6 ]', str(self.__tree))
    self.assertEqual('[ 1, 6 ]', self.__tree.post_order())
    self.assertEqual('[ 6, 1 ]', self.__tree.pre_order())
    self.assertEqual(2, self.__tree.get_height())

  def test_remove_right_node_with_one_right_child(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(1)
    self.__tree.insert_element(15)
    self.__tree.remove_element(10)
    self.assertEqual('[ 1, 6, 15 ]', str(self.__tree))
    self.assertEqual('[ 6, 1, 15 ]', self.__tree.pre_order())
    self.assertEqual('[ 1, 15, 6 ]', self.__tree.post_order())
    self.assertEqual(2, self.__tree.get_height())

  def test_remove_right_node_with_one_left_child(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(1)
    self.__tree.insert_element(8)
    self.__tree.remove_element(10)
    self.assertEqual('[ 1, 6, 8 ]', str(self.__tree))
    self.assertEqual('[ 6, 1, 8 ]', self.__tree.pre_order())
    self.assertEqual('[ 1, 8, 6 ]', self.__tree.post_order())
    self.assertEqual(2, self.__tree.get_height())
    
  def test_remove_right_node_with_two_children(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(8)
    self.__tree.insert_element(13)    
    self.__tree.remove_element(10)
    self.assertEqual('[ 6, 8, 13 ]', str(self.__tree))
    self.assertEqual('[ 6, 13, 8 ]', self.__tree.pre_order())
    self.assertEqual('[ 8, 13, 6 ]', self.__tree.post_order())
    self.assertEqual(3, self.__tree.get_height())
    
  def test_remove_left_node_with_no_children(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(1)
    self.__tree.remove_element(1)
    self.assertEqual('[ 6, 10 ]', str(self.__tree))
    self.assertEqual('[ 6, 10 ]', self.__tree.pre_order())
    self.assertEqual('[ 10, 6 ]', self.__tree.post_order())
    self.assertEqual(2, self.__tree.get_height())
    
  def test_remove_left_node_with_one_right_child(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(1)
    self.__tree.insert_element(4)
    self.__tree.remove_element(1)
    self.assertEqual('[ 4, 6, 10 ]', str(self.__tree))
    self.assertEqual('[ 6, 4, 10 ]', self.__tree.pre_order())
    self.assertEqual('[ 4, 10, 6 ]', self.__tree.post_order())
    self.assertEqual(2, self.__tree.get_height())

  def test_remove_left_node_with_one_left_child(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(2)
    self.__tree.insert_element(1)
    self.__tree.remove_element(2)
    self.assertEqual('[ 1, 6, 10 ]', str(self.__tree))
    self.assertEqual('[ 6, 1, 10 ]', self.__tree.pre_order())
    self.assertEqual('[ 1, 10, 6 ]', self.__tree.post_order())
    self.assertEqual(2, self.__tree.get_height())
    
  def test_remove_left_node_with_two_children(self):	
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(1)
    self.__tree.insert_element(8)
    self.__tree.insert_element(13)
    self.__tree.remove_element(10)
    self.assertEqual('[ 1, 6, 8, 13 ]', str(self.__tree))
    self.assertEqual('[ 6, 1, 13, 8 ]', self.__tree.pre_order())
    self.assertEqual('[ 1, 8, 13, 6 ]', self.__tree.post_order())
    self.assertEqual(3, self.__tree.get_height())
    
  def test_remove_node_not_affecting_height(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(13)
    self.__tree.insert_element(8)
    self.__tree.remove_element(13)
    self.assertEqual('[ 6, 8, 10 ]', str(self.__tree))
    self.assertEqual('[ 6, 10, 8 ]', self.__tree.pre_order())
    self.assertEqual('[ 8, 10, 6 ]', self.__tree.post_order())
    self.assertEqual(3, self.__tree.get_height())
    
  def test_remove_node_affecting_height(self):
    self.__tree.insert_element(6)
    self.__tree.insert_element(10)
    self.__tree.insert_element(13)
    self.__tree.insert_element(8)
    self.__tree.remove_element(13)
    self.__tree.remove_element(8)
    self.assertEqual('[ 6, 10 ]', str(self.__tree))
    self.assertEqual('[ 6, 10 ]', self.__tree.pre_order())
    self.assertEqual('[ 10, 6 ]', self.__tree.post_order())
    self.assertEqual(2, self.__tree.get_height())    

#special cases     
  def test_remove_from_empty_tree(self):
    with self.assertRaises(ValueError):
      self.__tree.remove_element(13)
    self.assertEqual('[ ]', str(self.__tree))
    self.assertEqual('[ ]', self.__tree.pre_order())
    self.assertEqual('[ ]', self.__tree.post_order())
    self.assertEqual(0, self.__tree.get_height())
  def test_insert_duplicate_value(self):
    with self.assertRaises(ValueError):
      self.__tree.insert_element(13)
      self.__tree.insert_element(13)
    self.assertEqual('[ 13 ]', str(self.__tree))
    self.assertEqual('[ 13 ]', self.__tree.pre_order())
    self.assertEqual('[ 13 ]', self.__tree.post_order())
    self.assertEqual(1, self.__tree.get_height())
  def test_remove_nonexistent_value(self):
    with self.assertRaises(ValueError):
      self.__tree.insert_element(13)
      self.__tree.remove_element(14)
    self.assertEqual('[ 13 ]', str(self.__tree))
    self.assertEqual('[ 13 ]', self.__tree.pre_order())
    self.assertEqual('[ 13 ]', self.__tree.post_order())
    self.assertEqual(1, self.__tree.get_height())
    
  def test_huge_tree(self):
    self.assertEqual(0, self.__tree.get_height())
    self.__tree.insert_element(10)
    self.assertEqual(1, self.__tree.get_height())    
    self.__tree.insert_element(8)
    self.assertEqual(2, self.__tree.get_height())
    self.__tree.insert_element(12)
    self.assertEqual(2, self.__tree.get_height())
    self.__tree.insert_element(6)
    self.assertEqual(3, self.__tree.get_height())
    self.__tree.insert_element(14)
    self.assertEqual(3, self.__tree.get_height())
    self.__tree.insert_element(11)
    self.assertEqual(3, self.__tree.get_height())
    self.__tree.insert_element(9)
    self.assertEqual(3, self.__tree.get_height())
    self.__tree.insert_element(7)
    self.assertEqual(4, self.__tree.get_height())
    self.assertEqual('[ 6, 7, 8, 9, 10, 11, 12, 14 ]', str(self.__tree))
    self.assertEqual('[ 10, 8, 6, 7, 9, 12, 11, 14 ]', self.__tree.pre_order())
    self.assertEqual('[ 7, 6, 9, 8, 11, 14, 12, 10 ]', self.__tree.post_order())    
    self.__tree.remove_element(8)
    self.assertEqual(4, self.__tree.get_height())
    self.assertEqual('[ 6, 7, 9, 10, 11, 12, 14 ]', str(self.__tree))
    self.assertEqual('[ 10, 9, 6, 7, 12, 11, 14 ]', self.__tree.pre_order())
    self.assertEqual('[ 7, 6, 9, 11, 14, 12, 10 ]', self.__tree.post_order())    
    self.__tree.remove_element(7)  
    self.assertEqual(3, self.__tree.get_height())
    self.assertEqual('[ 6, 9, 10, 11, 12, 14 ]', str(self.__tree))
    self.assertEqual('[ 10, 9, 6, 12, 11, 14 ]', self.__tree.pre_order())
    self.assertEqual('[ 6, 9, 11, 14, 12, 10 ]', self.__tree.post_order())    
    self.__tree.remove_element(10)  
    self.assertEqual(3, self.__tree.get_height())
    self.assertEqual('[ 6, 9, 11, 12, 14 ]', str(self.__tree))
    self.assertEqual('[ 11, 9, 6, 12, 14 ]', self.__tree.pre_order())
    self.assertEqual('[ 6, 9, 14, 12, 11 ]', self.__tree.post_order())  
    
if __name__ == '__main__':
  unittest.main()

