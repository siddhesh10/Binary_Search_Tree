import sys
sys.path.insert(0, 'C:/Users/sidd/Desktop/Binary_Search_Tree/')
import node

class binary_search_tree(object):

    def __init__(self):
        self.root=None

    def insert_node(self,data):
        new_node=node.node(data)
        if self.root==None:
            self.root=new_node
        else:
            current_node=self.root
            while True:
                if data<current_node.data:
                    if current_node.leftchild==None:
                        current_node.leftchild=new_node
                        break
                    else:
                        current_node=current_node.leftchild
                else:
                    if current_node.rightchild==None:
                        current_node.rightchild=new_node
                        break
                    else:
                        current_node=current_node.rightchild

    def preorder(self,node):
        if node ==None :
            return
        else:

            print(node.data,end="--")
            self.preorder(node.leftchild)
            self.preorder(node.rightchild)

    def postorder(self,node):
        if node ==None :
            return
        else:
            self.preorder(node.leftchild)
            self.preorder(node.rightchild)
            print(node.data,end="--")

    def inorder(self,node):
        if node ==None :
            return
        else:
            self.preorder(node.leftchild)
            print(node.data,end="--")
            self.preorder(node.rightchild)

    def delete_a_node(self,data):
        if self.root==None:
            print("Empty BST")
        else:
            parent=None
            node=self.root
            replace_node=None
            while(node!=None and node.data!=data):
                parent=node
                if data>=node.data:
                    node=node.rightchild
                    flag=1
                else:
                    node=node.leftchild
                    flag=0


            if node is None:
                print("node not in BST.")

            else:


                if (node.leftchild==None) and (node.rightchild==None):
                    if (flag):
                        parent.rightchild=None
                    else:
                        parent.leftchild=None
                    del node

                elif (node.leftchild==None) or (node.rightchild==None):
                    if node.leftchild==None:
                        if(flag):
                            parent.rightchild=node.rightchild
                        else:
                            parent.leftchild=node.rightchild
                    else  :
                        if(flag):
                            parent.rightchild==node.leftchild
                        else:
                            parent.leftchild=node.leftchild

                    del node


                else:
                     replace_node=self.minimum_element(node.rightchild)
                     temp=replace_node.data
                     self.delete_a_node(replace_node.data)
                     node.data=temp

    def minimum_element(self,node):
        if self.root==None:
            print("Empty BST")
        else:
            while(node.leftchild!=None):
                node=node.leftchild
            print(node.data)
            return (node)

    def maximum_element(self,node):
        if self.root==None:
            print("Empty BST")
        else:
            while(node.rightchild!=None):
                node=node.rightchild
            print(node.data)

    def height_BST(self,node):
        if node==None:
            return -1
        else:
            lh=self.height_BST(node.leftchild)
            rh=self.height_BST(node.rightchild)
            return max(lh,rh) + 1
