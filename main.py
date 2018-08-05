import sys
sys.path.insert(0, 'C:/Users/sidd/Desktop/Binary_Search_Tree/')
import binary_search_tree


mybst = binary_search_tree.binary_search_tree()
mybst.insert_node(20)
mybst.insert_node(25)
mybst.insert_node(22)
mybst.insert_node(18)
mybst.insert_node(17)
mybst.insert_node(100)
mybst.insert_node(105)
mybst.insert_node(140)

#mybst.minimum_element(mybst.root)
#mybst.maximum_element(mybst.root)
mybst.preorder(mybst.root)
print("\n*****")
print()
mybst.delete_a_node(22)
mybst.preorder(mybst.root)
print("\n*****")
print()
#mybst.delete_a_node(31)
#mybst.preorder(mybst.root)
print()
print("\n*****")
#print(mybst.height_BST(mybst.root))
