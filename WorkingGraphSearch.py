def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    print ("Start:", problem.getStartState())
    print ("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print ("Start's successors:", problem.getSuccessors(problem.getStartState()))
    state=problem.getStartState()
    path=[]
    closed=[]
    fringe=[]
    path.append(state)
    fringe.append(state)

    while True:
        if not path:
            print("The path is empty")
        if not fringe:
            print("The fringe is empty")

        node=fringe.pop()

        if problem.isGoalState(node):
            path.append(node)
            print("Reached the goal. it is ",node)
            return path
        if node not in closed:
            closed.append(node)
            for child in  problem.getSuccessors(node):
                # print(child[0])
                fringe.append(child[0])


        # if
        #     for nextOption in problem.getSuccessors(problem.getStartState()):
        #         if problem.isGoalState(nextOption):
        #             path.append(nextOption)
        #             return path

    util.raiseNotDefined()



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print ("Start:", problem.getStartState())
    # print ("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print ("Start's successors:", problem.getSuccessors(problem.getStartState()))
    state=problem.getStartState()
    path=[]
    closedbehind=[] # Nodes we don't want to return to
    closedahead=[] #Never revisit these
    current=[] #The current node we are looking at
    current.append(state)
    print(state)

    while True:
        if not current:
            print("The current is empty")
        # input('Press enter to continue: ')
        node=current.pop()
        closedbehind.append(node) # So we dont go back to this node, unless it has no further options

        if problem.isGoalState(node):
            current.append(node)
            # print("Reached the goal. it is ",node)
            # print("so its successors are: ",problem.getSuccessors(node))
            return path

        bothclosedlists=closedahead+closedbehind
        # print("Closed Ahead: ", closedahead)
        # print("Closed Behind: ",closedbehind)
        availablenodes = [anodes for anodes in problem.getSuccessors(node) if anodes[0] not in bothclosedlists]
        # print("availablenodes",availablenodes)
        #   check if there are any possible successors

        if not availablenodes:
            # There is no successor to this node, and it is not the goal
            # Undo the last move, and add this node onto the do not visit list
            # print("Removing move from path ")
            path.pop() #Removes last move from history
            closedahead.append(node)
            closedbehind.pop()
            current.append(closedbehind.pop())
            # print("Current type: ",type(current))

        else :

            # nextnode,nextmove,_= random.choice(availablenodes)
            # print("availablenodes",availablenodes)
            # print("availablenodes[0]",availablenodes[0])
            nextnode,nextmove,_= availablenodes[0]
            # print("nextnode",nextnode)
            # print("nextmove",nextmove)
            # input('Press enter to continue: ')
            # This chooses a random next move out of the successors that aren't in the No Go list
            # print("nextnode,nextmove",nextnode,nextmove)
            path.append(nextmove) #Add this move to the path taken
            current.append(nextnode) #This is now the current position


    util.raiseNotDefined()
