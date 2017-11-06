import unittest
from AVL_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):

  def setUp(self):
    self.__tree = Binary_Search_Tree()
#empty tree  
  def test_empty(self):
    self.assertEqual('[ ]', str(self.__tree))
    self.assertEqual('[ ]', self.__tree.post_order())
    self.assertEqual('[ ]', self.__tree.pre_order())
    self.assertEqual([], self.__tree.to_list()) 
    self.assertEqual(0, self.__tree.get_height())
   
#insertion    
  def test_insert_one_element(self):
    self.__tree.insert_element(10)
    self.assertEqual('[ 10 ]', str(self.__tree))  
    self.assertEqual('[ 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10 ]', self.__tree.pre_order())
    self.assertEqual([10], self.__tree.to_list())
    self.assertEqual(1, self.__tree.get_height())
    
  def test_insert_two_element(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(5)
    self.assertEqual('[ 5, 10 ]', str(self.__tree))  
    self.assertEqual('[ 5, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 5 ]', self.__tree.pre_order())
    self.assertEqual([5, 10], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height())
    
  def test_insert_three_element_balanced(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(5)
    self.__tree.insert_element(15)    
    self.assertEqual('[ 5, 10, 15 ]', str(self.__tree))
    self.assertEqual('[ 5, 15, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 5, 15 ]', self.__tree.pre_order())
    self.assertEqual([5, 10, 15], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height())
        
  def test_insert_three_element_right_heavy_single_rotation(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(15)
    self.__tree.insert_element(20)    
    self.assertEqual('[ 10, 15, 20 ]', str(self.__tree))    	
    self.assertEqual('[ 10, 20, 15 ]', self.__tree.post_order())
    self.assertEqual('[ 15, 10, 20 ]', self.__tree.pre_order())
    self.assertEqual([10, 15, 20], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height())
    
  def test_insert_three_element_left_heavy_single_rotation(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(8)
    self.__tree.insert_element(5)    
    self.assertEqual('[ 5, 8, 10 ]', str(self.__tree))    	
    self.assertEqual('[ 5, 10, 8 ]', self.__tree.post_order())
    self.assertEqual('[ 8, 5, 10 ]', self.__tree.pre_order())     	
    self.assertEqual([5, 8, 10], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height())
    
  def test_insert_four_element_right_heavy_single_rotation(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(15)
    self.__tree.insert_element(20)
    self.__tree.insert_element(5)    
    self.assertEqual('[ 5, 10, 15, 20 ]', str(self.__tree))    	
    self.assertEqual('[ 5, 10, 20, 15 ]', self.__tree.post_order())
    self.assertEqual('[ 15, 10, 5, 20 ]', self.__tree.pre_order())
    self.assertEqual([5, 10, 15, 20], self.__tree.to_list())
    self.assertEqual(3, self.__tree.get_height())
    
  def test_insert_four_element_left_heavy_single_rotation(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(8)
    self.__tree.insert_element(5)
    self.__tree.insert_element(15)    
    self.assertEqual('[ 5, 8, 10, 15 ]', str(self.__tree))    	
    self.assertEqual('[ 5, 15, 10, 8 ]', self.__tree.post_order())
    self.assertEqual('[ 8, 5, 10, 15 ]', self.__tree.pre_order())     	
    self.assertEqual([5, 8, 10, 15], self.__tree.to_list())
    self.assertEqual(3, self.__tree.get_height())
    
  def test_insert_five_element_right_heavy_double_rotation(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(5)
    self.__tree.insert_element(15)
    self.__tree.insert_element(20) 
    self.__tree.insert_element(18)       
    self.assertEqual('[ 5, 10, 15, 18, 20 ]', str(self.__tree))    	
    self.assertEqual('[ 5, 15, 20, 18, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 5, 18, 15, 20 ]', self.__tree.pre_order())
    self.assertEqual([5, 10, 15, 18, 20], self.__tree.to_list())
    self.assertEqual(3, self.__tree.get_height())
    
  def test_insert_five_element_left_heavy_double_rotation(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(8)
    self.__tree.insert_element(15)
    self.__tree.insert_element(5) 
    self.__tree.insert_element(7)       
    self.assertEqual('[ 5, 7, 8, 10, 15 ]', str(self.__tree))    	
    self.assertEqual('[ 5, 8, 7, 15, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 7, 5, 8, 15 ]', self.__tree.pre_order())     	
    self.assertEqual([5, 7, 8, 10, 15], self.__tree.to_list())
    self.assertEqual(3, self.__tree.get_height())
    
#removal 
  def test_remove_from_one_element_tree(self):
    self.__tree.insert_element(10)
    self.__tree.remove_element(10)
    self.assertEqual('[ ]', str(self.__tree))    	
    self.assertEqual('[ ]', self.__tree.post_order())
    self.assertEqual('[ ]', self.__tree.pre_order())     	
    self.assertEqual([], self.__tree.to_list())
    self.assertEqual(0, self.__tree.get_height()) 
    
  def test_remove_root_from_two_element_tree(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(8)    
    self.__tree.remove_element(10)
    self.assertEqual('[ 8 ]', str(self.__tree))    	
    self.assertEqual('[ 8 ]', self.__tree.post_order())
    self.assertEqual('[ 8 ]', self.__tree.pre_order())     	
    self.assertEqual([8], self.__tree.to_list())
    self.assertEqual(1, self.__tree.get_height())   

  def test_remove_leaf_node_from_two_element_tree(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(8)    
    self.__tree.remove_element(8)
    self.assertEqual('[ 10 ]', str(self.__tree))    	
    self.assertEqual('[ 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10 ]', self.__tree.pre_order())     	
    self.assertEqual([10], self.__tree.to_list())
    self.assertEqual(1, self.__tree.get_height()) 

  def test_remove_leaf_node_from_three_element_balanced_tree(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(8)
    self.__tree.insert_element(15)
    self.__tree.remove_element(15)
    self.assertEqual('[ 8, 10 ]', str(self.__tree))    	
    self.assertEqual('[ 8, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 8 ]', self.__tree.pre_order())     	
    self.assertEqual([8,10], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height()) 

  def test_remove_root_from_three_element_balanced_tree(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(8)
    self.__tree.insert_element(15)
    self.__tree.remove_element(10)
    self.assertEqual('[ 8, 15 ]', str(self.__tree))    	
    self.assertEqual('[ 8, 15 ]', self.__tree.post_order())
    self.assertEqual('[ 15, 8 ]', self.__tree.pre_order())     	
    self.assertEqual([8,15], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height()) 
  
  def test_remove_original_root_from_three_element_unbalanced_tree(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(15)
    self.__tree.insert_element(20)
    self.__tree.remove_element(10)
    self.assertEqual('[ 15, 20 ]', str(self.__tree))    	
    self.assertEqual('[ 20, 15 ]', self.__tree.post_order())
    self.assertEqual('[ 15, 20 ]', self.__tree.pre_order())     	
    self.assertEqual([15,20], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height()) 

  def test_remove_new_root_from_three_element_unbalanced_tree(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(15)
    self.__tree.insert_element(20)
    self.__tree.remove_element(15)
    self.assertEqual('[ 10, 20 ]', str(self.__tree))    	
    self.assertEqual('[ 10, 20 ]', self.__tree.post_order())
    self.assertEqual('[ 20, 10 ]', self.__tree.pre_order())     	
    self.assertEqual([10,20], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height()) 

  def test_remove_leaf_node_from_three_element_unbalanced_tree(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(15)
    self.__tree.insert_element(20)
    self.__tree.remove_element(20)
    self.assertEqual('[ 10, 15 ]', str(self.__tree))    	
    self.assertEqual('[ 10, 15 ]', self.__tree.post_order())
    self.assertEqual('[ 15, 10 ]', self.__tree.pre_order())     	
    self.assertEqual([10,15], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height()) 
    
  def test_remove_new_root_from_three_element_unbalanced_tree(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(15)
    self.__tree.insert_element(20)
    self.__tree.remove_element(15)
    self.assertEqual('[ 10, 20 ]', str(self.__tree))    	
    self.assertEqual('[ 10, 20 ]', self.__tree.post_order())
    self.assertEqual('[ 20, 10 ]', self.__tree.pre_order())     	
    self.assertEqual([10,20], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height()) 
    
  def test_remove_four_element_right_heavy(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(15)
    self.__tree.insert_element(20)
    self.__tree.insert_element(5)   
    self.__tree.remove_element(15)
    self.assertEqual('[ 5, 10, 20 ]', str(self.__tree))    	
    self.assertEqual('[ 5, 20, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 5, 20 ]', self.__tree.pre_order())
    self.assertEqual([5, 10, 20], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height())
  
  
  def test_remove_four_element_left_heavy(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(15)
    self.__tree.insert_element(8)
    self.__tree.insert_element(5)   
    self.__tree.remove_element(5)
    self.assertEqual('[ 8, 10, 15 ]', str(self.__tree))    	
    self.assertEqual('[ 8, 15, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 8, 15 ]', self.__tree.pre_order())
    self.assertEqual([8, 10, 15], self.__tree.to_list())
    self.assertEqual(2, self.__tree.get_height())
    
  def test_remove_five_element_right_heavy_double_rotation(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(5)
    self.__tree.insert_element(15)
    self.__tree.insert_element(20) 
    self.__tree.insert_element(18)   
    self.__tree.remove_element(15)    
    self.assertEqual('[ 5, 10, 18, 20 ]', str(self.__tree))    	
    self.assertEqual('[ 5, 20, 18, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 5, 18, 20 ]', self.__tree.pre_order())
    self.assertEqual([5, 10, 18, 20], self.__tree.to_list())
    self.assertEqual(3, self.__tree.get_height())
  
  def test_remove_five_element_left_heavy_double_rotation(self):
    self.__tree.insert_element(10)
    self.__tree.insert_element(8)
    self.__tree.insert_element(15)
    self.__tree.insert_element(5) 
    self.__tree.insert_element(7)       
    self.__tree.remove_element(8)
    self.assertEqual('[ 5, 7, 10, 15 ]', str(self.__tree))    	
    self.assertEqual('[ 5, 7, 15, 10 ]', self.__tree.post_order())
    self.assertEqual('[ 10, 7, 5, 15 ]', self.__tree.pre_order())
    self.assertEqual([5, 7, 10, 15], self.__tree.to_list())
    self.assertEqual(3, self.__tree.get_height())

#special cases     
  def test_remove_from_empty_tree(self):
    with self.assertRaises(ValueError):
      self.__tree.remove_element(13)
    self.assertEqual('[ ]', str(self.__tree))
    self.assertEqual('[ ]', self.__tree.pre_order())
    self.assertEqual('[ ]', self.__tree.post_order())
    self.assertEqual(0, self.__tree.get_height())
    self.assertEqual([], self.__tree.to_list())
    
  def test_insert_duplicate_value(self):
    with self.assertRaises(ValueError):
      self.__tree.insert_element(13)
      self.__tree.insert_element(13)
    self.assertEqual('[ 13 ]', str(self.__tree))
    self.assertEqual('[ 13 ]', self.__tree.pre_order())
    self.assertEqual('[ 13 ]', self.__tree.post_order())
    self.assertEqual(1, self.__tree.get_height())
    self.assertEqual([13], self.__tree.to_list())

  def test_remove_nonexistent_value(self):
    with self.assertRaises(ValueError):
      self.__tree.insert_element(13)
      self.__tree.remove_element(14)
    self.assertEqual('[ 13 ]', str(self.__tree))
    self.assertEqual('[ 13 ]', self.__tree.pre_order())
    self.assertEqual('[ 13 ]', self.__tree.post_order())
    self.assertEqual(1, self.__tree.get_height())
    self.assertEqual([13], self.__tree.to_list())

    
    
if __name__ == '__main__':
  unittest.main()