import heapq
input_file_graph=open("graph_data.txt","r")

def heuristic_values(input_file_graph):
    values_of_heuristics={}
    for values in input_file_graph:
        print(values)
        line_strip=values.strip().split()
        print(line_strip)
        values_of_heuristics[line_strip[0]]=int(line_strip[1])
    return values_of_heuristics

values_of_heuristics=heuristic_values(input_file_graph)
print(values_of_heuristics)

input_file_graph=open("graph_data.txt","r")

parents_graph={}
child_graph={}
for val in input_file_graph:
    print(val)
    line_strip=val.strip().split()
    for j in range(2, len(line_strip),2):
        child_graph[line_strip[j]]=int(line_strip[j+1])
    print(child_graph)
    parents_graph[line_strip[0]]=child_graph
    child_graph={}
    print(parents_graph)

def A_star_algorithm(start_node,parents_graph,values_of_heuristics,goal_node):
    bounding_line=[(0,start_node)]
    matrix=[]
    heapq.heappush(matrix,(0,start_node))
    parents={}
    costing={}
    parents[start_node]=None
    costing[start_node]=0
    q_list=[]

    while matrix:
        current_value=heapq.heappop(matrix)[1]
        if current_value==goal_node:
            break
        for i in parents_graph[current_value]:
            new_costing=costing[current_value] + parents_graph[current_value][i]
            if i not in costing or new_costing < costing[i]:
                costing[i]=new_costing
                queue=new_costing + values_of_heuristics[i]
                q_list.append((queue,i))
                heapq.heappush(matrix,(queue,i))
                parents[i]=current_value
    return parents, costing


start_node=input("enter the starting node:")
goal_node=input("enter the goal node:")

if start_node not in values_of_heuristics or goal_node not  in values_of_heuristics :
    print("there is no such start_node or Goal_node")
else:

    path_list_to_goal=[]
    parents,costing=A_star_algorithm(start_node,parents_graph,values_of_heuristics,goal_node)
    path_list_to_goal.append(goal_node)
    temp=goal_node
    while temp!=start_node:
        temp=parents[temp]
        path_list_to_goal.append(temp)
    path_list_to_goal.reverse()
    if len(path_list_to_goal)==1 and path_list_to_goal[0]!=start_node:
        print("NO path found")
    else:
        print("PATH: ", end="")
        for i,j in enumerate(path_list_to_goal):
            if i<len(path_list_to_goal)-1:
                print(j, end="-->")
            else:
                print(j)
        print("Total Distance:",costing[goal_node], 'km')





