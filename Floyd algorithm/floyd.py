from math import inf #IMPORT INFINITY CONST 
import pandas as pd #IMPORT PANDAS TO MAKE DF AND PRINT CLEANLY IN CONSOLE
import subprocess; subprocess.call('cls', shell=True)

## MAKE FLOYD ALGORITHM
def floyd(
    node_num:int,
    input_adjacency_matrix:list,    
)-> list:
    """thin function accept a list include adjacency matrix of a particular Graph, and proceed floyd-warshal algorithm on it to find SHORTEST PATHES between nodes, and return a matrix from it as a result."""
    ## STORE ACCEPTED MATRIX IN LOCAL
    matrix = input_adjacency_matrix

    ## FLOYD-WARSHAL ALGORITHM
    k = 0
    while k<= node_num-1:
        i = 0 
        while i<= node_num-1:
            j = 0 
            while j<= node_num-1:
                matrix[i][j] = min(
                    matrix[i][j],
                    matrix[i][k]+matrix[k][j]
                )
                j += 1
            i += 1
        k += 1

    #RETURN THE RESULT
    return matrix 

## MADE INPUT MATRIX FOR FLOYD ALOGIRTHM
input_matrix = [
    [0,1,inf,1,5],
    [9,0,3,2,inf],
    [inf,inf,0,4,inf],
    [inf,inf,2,0,3],
    [3,inf,inf,inf,0],
]

## CALL FLOYD FUNCTION AND STORE SHORTEST PATHES
shortest_path_matrix = floyd(
        node_num= len(input_matrix[0]),
        input_adjacency_matrix= input_matrix
    )

## MAKE DF TO CLEAN PRINTING AND PRINT IT
shortest_pathes_df = pd.DataFrame(
    data= shortest_path_matrix
)
print(shortest_pathes_df)

