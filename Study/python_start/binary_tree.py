from readline import insert_text
import sys 

input = sys.stdin.readline 

class treenode:

    def __init__(self , a):
        self.node = a 
        self.leftnode = None
        self.rightnode = None


class nodeop:
    def __init__(self, head):
        self.current_node = head  

    def insert_node(self,k):
        print("test",k)
        if self.current_node != None:
            print(self.current_node.node, "::", k)
            if self.current_node.node > k:
                self.current_node = self.current_node.leftnode
                print("left")
                self.insert_node(k)
            elif self.current_node.node <= k:
                print("right")
                self.current_node = self.current_node.rightnode 
                self.insert_node(k)
        elif self.current_node == None:
            self.current_node = treenode(k)
            
        # while True:
 
        #         if self.current_node.node > k:
        #             if self.current_node.leftnode != None:
        #                 self.current_node = self.current_node.leftnode 
        #             else:
        #                 self.current_node.leftnode = treenode(k)
        #                 break 
        #         elif self.current_node.node <= k:
        #             if self.current_node.rightnode != None:
        #                 self.current_node = self.current_node.rightnode 
        #             else:
        #                 self.current_node.rightnode = treenode(k)
        #                 break 
                


root_node = treenode(4)
top_node = nodeop(root_node)
for i in range(2, 6):
    top_node.insert_node(i)
    top_node.current_node = root_node
    #print("root", root_node)
    if top_node.current_node.leftnode != None:
        print("root left",top_node.current_node.leftnode)
    if top_node.current_node.rightnode != None:
        print("root right",top_node.current_node.rightnode)

def print_node(node):
    if node != None:
        print(node.node)
        if node.leftnode != None:
            print("root left",node.leftnode.node)
        if node.rightnode != None:
            print("root right",node.rightnode.node)
    
print_node(root_node)
print(root_node.leftnode)
print(root_node.rightnode)
#print_node(root_node.leftnode.rightnode)
