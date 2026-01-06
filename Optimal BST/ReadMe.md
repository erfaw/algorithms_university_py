for persian|فارسی readme [clickme](https://github.com/erfaw/algorithms_university_py/blob/main/Optimal%20BST/ReadME-per.md)
# 🌳 Optimal Binary Search Tree (OBST) Solver

A professional Python implementation of the **Optimal Binary Search Tree** algorithm using **Dynamic Programming**.

---

## 📝 Project Overview
This project solves the OBST problem, which aims to construct a Binary Search Tree that minimizes the **Average Search Cost** based on the access probabilities of each key. 



## 🛠 Key Engineering Features
- **Floating Point Fix:** Implements `np.round()` to handle the "Binary Floating Point Arithmetic Problem," ensuring high precision in probability sums.
- **Data Compatibility:** Uses the `.item()` method to convert NumPy scalars into native Python types for seamless serialization.
- **Visual Analysis:** Leverages `Pandas DataFrames` to output the Min-Avg (A) and Root (R) matrices in a clean, tabular format.
- **Modular Design:** Cleanly separates initialization, probability summation, and the core DP logic.

## 🚀 Quick Start

### Prerequisites
Install the required libraries:
```bash
pip install numpy pandas

# Execution Example
## Number of keys/nodes
num_of_nodes = 3

## Probability array (Index 0 is a placeholder)
POSSIBILITY_MATRIX = [0, 0.7, 0.2, 0.1] 

## Run the algorithm
min_cost, root_matrix = optsearchtree(num_of_nodes, POSSIBILITY_MATRIX)

# 📊 Output Matrices

The algorithm generates two critical matrices:

    1. MinAvg Matrix (A): Stores the minimum search cost for every sub-tree combination.

    2. Root Matrix (R): Identifies the optimal root node for the range [i, j], allowing for tree reconstruction.

# 🔍 Complexity Analysis
    * Time Complexity: O(n3) due to the three nested loops (diagonal, row, and root-selection k).

    * Space Complexity: O(n2) for storing the DP tables.