# 🔍 Backtracking

Backtracking is a general algorithmic technique that builds up solutions incrementally and abandons paths (“backtracks”) as soon as it determines the path cannot lead to a valid solution.

---

## 📚 What’s Inside This Folder

This folder includes classic and advanced backtracking problems in Python, such as:

- ✅ **N-Queens Problem**
- ✅ **Sudoku Solver**
- ✅ **Combination & Permutation Generation**
- ✅ **Subset / Power Set Problems**
- ✅ **Word Search**
- ✅ **Palindrome Partitioning**
- ✅ **Expression Add Operators**

---

## 🧠 Core Concepts

| Concept          | Description                                                        |
|------------------|--------------------------------------------------------------------|
| Decision Tree    | Each recursive call represents a decision at a node in the tree.   |
| Pruning          | Invalid paths are discarded early using `if` checks.               |
| Revert Steps     | After each recursive call, we undo the last choice to explore new options. |

---

## 🛠️ How to Use

Each solution follows the pattern:
1. Define a helper recursive function
2. Base case to store the result
3. Loop to explore choices
4. Recurse and backtrack

---

## 🧪 Pro Tips

- Use sorting or visited arrays to handle duplicates.
- Debug by printing the recursive call path.
- Practice designing recursion trees on paper.

---

## 🧩 Use Cases

- Solving puzzles (e.g. Sudoku)
- Combinatorics (e.g. k-combinations)
- Constraint Satisfaction Problems (e.g. N-Queens)

---

Enjoy solving puzzles with backtracking! 🧩🚀