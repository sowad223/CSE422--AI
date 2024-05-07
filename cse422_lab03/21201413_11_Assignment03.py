import random
tree = [[]]
student_id = input("Enter your student id: ")
health_point_range = input(" Minimum and Maximum value for the range of negative HP: ").split(' ')
minimum_health_point = int(health_point_range[0])
maximum_health_point= int(health_point_range[1])
turns_taken = int(student_id[0])

sub_branch = int(student_id[2])
initial_health_point = int(student_id[7] + student_id[6])

for val in range(((turns_taken * 2) + 1)):
    for colums in range(sub_branch ** val):
        tree[val].append(0)
    if val < ((turns_taken * 2) + 1) - 1:
        tree.append([])
index = len(tree) - 1
for q in range(len(tree[index])):
    tree[index][q] = random.randint(minimum_health_point, maximum_health_point)
current_level = index

for values in range(turns_taken * 2):
    starting_index = 0
    if (values + 1) % 2 != 0:
        for m_values in range(int((sub_branch ** current_level) / sub_branch)):
            temporary_values = tree[current_level][starting_index:(starting_index + sub_branch - 1) + 1]
            tree[current_level - 1][m_values] = min(temporary_values)
            starting_index = (starting_index + sub_branch - 1) + 1
    else:
        for j in range(int((sub_branch ** current_level) / sub_branch)):
            temporary_values = tree[current_level][starting_index:(starting_index + sub_branch - 1) + 1]
            tree[current_level - 1][j] = max(temporary_values)
            starting_index = (starting_index + sub_branch - 1) + 1
    current_level -= 1
leaf_nodes = tree[index]
alpha_value = min(leaf_nodes[:sub_branch])
comparison_count = sub_branch
k_index = sub_branch
for i in range(int((len(leaf_nodes) / sub_branch) - 1)):
    iterator = 0
    while iterator < sub_branch:
        if alpha_value > leaf_nodes[k_index]:
            comparison_count += 1
            k_index += sub_branch - iterator
            break
        else:
            comparison_count += 1
        k_index += 1
        iterator += 1
    if iterator == sub_branch:
        starting_index = (i + 1) * sub_branch
        alpha_value = min(leaf_nodes[starting_index:k_index])
print()
depth = turns_taken * 2
print("Depth and Branches ratio is ", depth, ":", sub_branch)
print("Terminal States (leaf node values) are ", tree[index])
print("Left life(HP) of the defender after maximum damage caused by the attacker is ", (initial_health_point - tree[0][0]))
print("After Alpha-Beta Pruning Leaf Node Comparisons", comparison_count)
