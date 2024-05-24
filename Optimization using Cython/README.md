# Matrix Multiplication Performance Analysis and Optimization

This project analyzes the performance of matrix multiplication using different methods in Python and Cython. The focus is on comparing the custom matrix multiplication function with NumPy's `@` operator and `np.matmul`, and optimizing the custom implementation using Cython. The project includes:

1. **Performance Comparison**:
   - Benchmarking custom matrix multiplication (`matrix_multiply`) against NumPy's `@` operator and `np.matmul` using `%timeit`.
   - Calculation of GFLOPS (Giga Floating Point Operations per Second) for each method to quantify computational efficiency.

2. **Matrix Size Scaling**:
   - Time measurements and performance analysis for varying matrix sizes, visualized using log-log plots.
   - Determining the maximum matrix size that can be processed in under one second using `np.matmul`.

3. **Cython Optimization**:
   - Initial implementation of `matrix_multiply` in Cython (`matrix_multiply_cy`) for performance improvement.
   - Further optimized Cython implementation (`matmul_cy_opt_1`) with type declarations for enhanced speed.

### Key Results:
- Detailed time comparisons and GFLOPS analysis for different matrix sizes.
- Visualization of performance scaling using Matplotlib.
- Significant performance gains observed with Cython-optimized matrix multiplication.

### Requirements:
- Python 3.x
- NumPy
- Matplotlib
- IPython (for `%timeit` and `%matplotlib` magic commands)
- Cython

To reproduce the results and run the analysis, follow the implementation steps provided in the Jupyter Notebook.

---
