#Example of how to setup a Breadth-First search (queue)
#First in Last out (FILO)
#Uninformed search algorithm: No knowledge of problem, only initial state and possible actions to take

def remove(self):
    #Checks if frontier (list of nodes) is empty
    if self.isempty():
        raise Exception("Empty frontier")
    else:
        #Saves the first item in the list
        node = self.frontier[0]
        #Removes first item from the list of nodes -- Sets the list of nodes as all items except the first node
        self.frontier = self.frontier[1:]
        #Returns node
        return node