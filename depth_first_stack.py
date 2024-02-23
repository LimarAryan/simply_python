#Example of how to setup a Depth-First Search (stack)
#Uninformed search algorithm: No knowledge of problem, only initial state and possible actions to take

def remove(self):
    #Checks if frontier (list of nodes) is empty, no solution
    if self.isempty():
        raise Exception("Empty frontier")
    else:
        #Saves the last item in the list, which is the newest node added
        node = self.frontier[-1]
        #Removes last item from the list of nodes -- Sets the list of nodes as all items except the last node
        self.frontier = self.frontier[:-1]
        #Returns node
        return node