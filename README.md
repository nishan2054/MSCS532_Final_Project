**Data Locality Performance Experiment**

This repository contains a small Python experiment demonstrating how data locality and vectorized operations affect performance. The project compares two approaches for adding large numerical arrays:

1. A pure Python loop, which processes elements one at a time

2. A NumPy vectorized operation, which performs the same work using optimized low level routines

The goal is to show how memory access patterns and locality influence runtime, even when the algorithm itself does not change.

**Project Context**

This experiment was completed as part of the Algorithms and Data Structures final project for the Master of Science in Computer Science program. It supports a written analysis showing how insights from high performance computing research apply to real computational workloads.

**How to Run the Program**
1. Install Dependencies

This program requires Python 3 and NumPy. Install NumPy with:

 pip install numpy

2. Run the Experiment

Execute the script from your terminal:

 python data_locality_experiment.py
