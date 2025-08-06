# 📂 Segment Trees

This folder contains my learning and implementation journey of **Segment Trees** – a powerful data structure for efficient range queries and updates. It is part of my larger goal to master Data Structures and Algorithms (DSA) for coding interviews and real-world problem solving.

---

## ✅ What are Segment Trees?

Segment Trees are binary trees used to:
- Perform **range queries** (e.g., sum, min, max, gcd) in `O(log n)` time.
- Perform **point or range updates** in `O(log n)` time.

They are especially useful when:
- The data is **static or semi-static**, and
- Frequent **queries and updates** are needed.

---

## ✍️ Implementations Covered

| # | Topic | Description |
|---|-------|-------------|
| 1 | `segment_tree_build.py` | Basic implementation of segment tree construction |
| 2 | `segment_tree_query.py` | Range sum/min/max queries on a segment tree |
| 3 | `segment_tree_update.py` | Updating values in the array and tree |
| 4 | `segment_tree_lazy.py` | Lazy propagation for efficient range updates |
| 5 | `segment_tree_gcd.py` | Segment tree for range GCD queries |
| 6 | `segment_tree_custom.py` | Custom segment tree for more complex use-cases |

> 📌 Each file is commented, with examples and explanations to help in understanding both logic and implementation.

---

## 🧠 Key Concepts Learned

- Efficient tree representation using arrays/lists
- Recursive construction and traversal
- Querying sub-ranges with pruning
- Propagating updates lazily (Lazy Propagation)
- Custom merge functions for different problems

---

## 🚀 Applications of Segment Trees

- Competitive programming problems involving frequent range queries/updates
- Online gaming systems (leaderboard calculations)
- Range minimum/maximum/sum product problems
- Interval-based algorithms
- Heavy use in platforms like Codeforces, AtCoder, and LeetCode

---

## 🧩 Sample Problems Solved

- ✅ Range Sum Queries
- ✅ Range Minimum Queries
- ✅ Range GCD Queries
- ✅ Range XOR Queries
- ✅ Dynamic Array with Point Updates
- ✅ Range Update with Lazy Propagation

---

## 📚 Resources Used

- [CP Algorithms - Segment Trees](https://cp-algorithms.com/data_structures/segment_tree.html)
- [GeeksforGeeks - Segment Tree](https://www.geeksforgeeks.org/segment-tree-data-structure/)
- [Neetcode & Codeforces Editorials]
- My handwritten notes and dry-run logs

---

## 🗂️ How to Use

Each file contains:
- Python implementation of a specific segment tree variation
- Sample test cases
- Function docstrings for clarity

To run a file:
```bash
python3 segment_tree_xxx.py