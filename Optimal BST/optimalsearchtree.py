import numpy as np
import pandas as pd
def optsearchtree(
    num_of_nodes,
    POSSIBILITY_MATRIX, # => must be row:num_of_nodes+2 col:num_of_nodes+1
):
    ## define a variable for end result of least average time of searching is possible.
    minavg = None 

    ## define a variable for end result of optimal matrix made from minavg we found during this procedure
    optimal_matrix = None

    ## define a variable fill with a matrix n x (n+1): for do procedure to find 'minavg', using Dynamix Programing
    minavg_matrix = None

    ## build empty matrix in 'minavg_matrix' and 'optimal_matrix' all value 0
    minavg_matrix = np.zeros((num_of_nodes+2, num_of_nodes+1))
    optimal_matrix = np.zeros((num_of_nodes+2, num_of_nodes+1))

    ## fill data in 'minavg_matrix' and 'optimal_matrix'
    i=1 
    while i <= num_of_nodes:
        ## fill possibilities in minavg_matrix
        minavg_matrix[i][i] = POSSIBILITY_MATRIX[i]
        ## fill main diagonal of the matrix, where is i=j
        optimal_matrix[i][i] = i
        i+=1

    ## main Algorithm Optimal BST:
    t=1 
    while t<=num_of_nodes-1:
        i=1
        while i<=num_of_nodes-t:
            j= i+t
            min_value = None
            for k in range(i,j):
                min_value = min(
                    minavg_matrix[i][k-1] , minavg_matrix[k+1][j]
                )
            sum_possibility = 0
            for i in range(i,j):
                sum_possibility += POSSIBILITY_MATRIX[i]
                
            minavg_matrix[i][j] = min_value + sum_possibility
            optimal_matrix[i][j] = k
            i+=1
        t+=1
    minavg = minavg_matrix[1][num_of_nodes]

    print("minavg_matrix(A)\n"+pd.DataFrame(minavg_matrix))
    print("minavg_matrix(R)\n"+pd.DataFrame(optimal_matrix))
    return minavg, optimal_matrix