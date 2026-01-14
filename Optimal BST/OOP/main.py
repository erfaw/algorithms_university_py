from OBST import OBST
## BUILD OBJECT FROM 'OBST' CLASS
# obst = OBST(
#     num_of_nodes = 4,
#     POSSIBILITY_LIST= [0, 0.3, 0.4, 0.2, 0.1]
# )
obst = OBST(
    num_of_nodes = 3,
    POSSIBILITY_LIST= [0, 0.7, 0.2, 0.1]
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
