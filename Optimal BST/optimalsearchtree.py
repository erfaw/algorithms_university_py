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
            ## DEFINE j WITH t AND i (TO MEASURE HOW RADIUS WE MUST CALCULATE)
            j= i+t

            ### LOOP THROUGH ALL POSSIBLE ROOT (k) BETWEEN i AND j TO FOUND BEST
            ## VARIABLE TO STORE EACH k_value
            k_values = {}
            ## LOOP k
            for k in range(i,j+1):
                #      RECURSIVE MUST BE => right_brnach_value + left_branch_value + possibility of i + possibility of j
                ## CALCULATE LEFT AND RIGHT BRANCH BASED ON k 
                sum_of_right_and_left_branch = minavg_matrix[i][k-1] + minavg_matrix[k+1][j]

                ## CALCUALTE POSSIBILITIES FOR EACH i AND j BASED ON 'POSSIBILITY_MATRIX' WHICH ACCEPTED AS AN arg
                sum_possibility = 0
                for p in range(i,j+1):
                    sum_possibility += POSSIBILITY_MATRIX[p]

                ## FIX THE PROBLEM WITH <Floating Point Arithmetic Problem>
                sum_possibility = np.round(sum_possibility, 1)

                ## CALCULATE AND STORE k_value IN k_values
                k_value = np.round(sum_of_right_and_left_branch + sum_possibility, 1)
                k_values.update(
                    {f"{k}": k_value.item(),}
                    )

            ### FILL MATRIXES WITH FOUNDED VALUES
            ## FILL k number of minimum value
            optimal_matrix[i][j] = min(k_values, key= k_values.get)
            
            ## FILL MINIMUM OF k_values INTO 'minavg_matrix'
            minavg_matrix[i][j] = k_values[min(k_values, key= k_values.get)]

            i+=1
        t+=1
    minavg = minavg_matrix[1][num_of_nodes]

    print("\nminavg_matrix(A)")
    print(pd.DataFrame(minavg_matrix))
    print("\nminavg_matrix(R)")
    print(pd.DataFrame(optimal_matrix))
    return [minavg, optimal_matrix]

num_of_nodes = 3
POSSIBILITY_MATRIX = [0, 0.7, 0.2, 0.1]
result = optsearchtree(
    3,
    POSSIBILITY_MATRIX= POSSIBILITY_MATRIX,
)