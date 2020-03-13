#Input To The Programm Initial And Goal State
initial=(1," ", 5,
         3,2,4,
         6, 7, 8)

goal_st=(" ", 1, 2,
         3,4,5,
         6, 7, 8)

#To Find The Heuristic Cost( No Of Misplaced Tiles )
def h(Node):
    Node=tuple(Node)
    c=0
    for i in range(9):
        if Node[i]!=goal_st[i]:
            c=c+1;
    if(Node==initial or Node==goal_st):
        return c
    else:
        return c-1

#To Print The Path Traversed
def printChilds(A):
    node=initial
    level=1
    for j in range(len(A)):

        print("<-----Level {}------->".format(depth_holder[j]))
        for i in range(0,9,3):
            print(A[j][i],A[j][i+1],A[j][i+2])
        print(moves[j])
        print("{}(f) = {}(g) + {}(h)\n".format(depth_holder[j]+heuristic[j],depth_holder[j],heuristic[j]))
        

#To Hold Various Moves And Function For Movements Of Empty Tile
moves=[]
def up(A,i):
    A=list(A)
    A[i],A[i-3]=A[i-3],A[i]
    move.append("Move Up\n")
    return A
def down(A,i):
    A=list(A)
    A[i],A[i+3]=A[i+3],A[i]
    move.append("Move Down\n")
    return A
def left(A,i):
    A=list(A)
    A[i],A[i-1]=A[i-1],A[i]
    move.append("Move Left\n")
    return A
def right(A,i):
    A=list(A)
    A[i],A[i+1]=A[i+1],A[i]
    move.append("Move Right\n")
    return A

#To Finds Childs Of A Parent Node        
def findChilds(Node):
    index=Node.index(" ")
    childs=[]
    if((index+1 in range(0,9)) and (index % 3 != 2)):
        c1=right(Node,index)
        childs.append(c1)
        
    if(index+3 in range(0,9)):
        c2=down(Node,index)
        childs.append(c2)
    
    if(index-3 in range(0,9)):
        c3=up(Node,index)
        childs.append(c3)

    if((index-1 in range(0,9)) and (index % 3 !=0)):
        c4=left(Node,index)
        childs.append(c4)
    return childs
explored=[]
depth_holder=[]
move=[]
heuristic=[]
#BFS Traversal Of Nodes
def bfs_connected_component(start,goal):
    start=list(start)
    goal=list(goal)
    queue = [start]
    depth=[0]
    heu=[h(start)]
    d=0
    prev_d=d
    index=0
    move.append("Start Node")
        
    while queue:
        min_cost=(h(queue[0])+depth[0])
        for i in queue:
            if(h(i)+depth[queue.index(i)]<min_cost):
                min_cost=h(i)+depth[queue.index(i)]
                index=queue.index(i)
        node = queue.pop(index)
        d=depth.pop(index)
        mo=move.pop(index)
        he=heu.pop(index)
        
        if node not in explored:
            explored.append(node)
            print(node)
            depth_holder.append(d)
            moves.append(mo)
            heuristic.append(he)
            #COST+=1
            if node==goal:
                moves.append("Goal State")
                #print("\nTotal Cost:- ",h(node))
                return explored
            
            neighbours = findChilds(node)
            for neighbour in neighbours:
                queue.append(neighbour)
                depth.append(d+1)
                heu.append(h(neighbour))
             
      
rest=bfs_connected_component(initial,goal_st) 
printChilds(rest)


