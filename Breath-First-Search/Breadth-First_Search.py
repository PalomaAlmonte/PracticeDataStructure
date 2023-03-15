# example of data structure breath first search

# will iterate through the whole data until it has visited every node
#in BFS there is a node and an edge
#node- has data
#edge - connects nodes and sees who is child of which node

class Node:
    def __init__(self, name):
        #name-data , adject_list- the nodes that are children of the current node
        #visited- neeeded to keep track of which nodes have been visited
        self.name = name
        self.adject_list = []
        self.visited = False


def Breath_first_search(start_node):
    node = [start_node]
    start_node.visited = True

    #will iterate until there is no node in the list
    while node:
        nod = node.pop(0)
        print(nod.name)
        for i in nod.adject_list:
            if not i.visited:
                node.append(i)
                i.visited = True


if __name__ == '__main__':
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')

    node1.adject_list.append(node2)
    node1.adject_list.append(node3)
    node2.adject_list.append(node4)
    node3.adject_list.append(node4)

    Breath_first_search(node1)



