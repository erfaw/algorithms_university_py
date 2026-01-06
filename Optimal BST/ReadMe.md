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