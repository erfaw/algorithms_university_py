from OBST import OBST
import subprocess; subprocess.call('cls', shell=True)
## SOME EXAMPLES TO INPUT
#     num_of_nodes = 3,
#     POSSIBILITY_LIST= [0, 0.7, 0.2, 0.1]
#   --------
#     num_of_nodes = 4,
#     POSSIBILITY_LIST= [0, 0.3, 0.4, 0.2, 0.1]

## GET ENTRY VALUES FROM USER
nodes_number = int(input("insert 'num_of_nodes'=\t"))
possibility_list = []
print("Please insert possibilities carefully: ")
for node in range(nodes_number+1):
    if node == 0: 
        possibility_list.append(0)
    else:
        possibility_list.append(None)
        possibility_list[node] = float(input(f"\tnode [{node}]=\t"))

## BUILD OBJECT FROM 'OBST' CLASS BASED ON ENTRY VALUES
obst = OBST(
    num_of_nodes = nodes_number,
    POSSIBILITY_LIST= possibility_list
)

## CALCULATE BEST OPTIONS
obst.result_cal = obst.calculate_matrices()

## MAKE OPTIMAL BST FROM BEST OPTIONS
obst.result_tree = obst.build_optimal_bst(
    i=1,
    j= obst.num_of_nodes,
    R= obst.result_cal[1],
    keys= obst.possibility_list
)

## PRINT TREE
print("\nOptimal BST should be like this:")
obst.print_inorder(
    obst.result_tree
)

print()
