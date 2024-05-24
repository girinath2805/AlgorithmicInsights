# Circuit Analysis

This README file provides a detailed explanation of the algorithm implemented in the provided Python code. The code is designed for analyzing electrical circuits specified in SPICE format to find nodal voltages and currents through voltage and current sources. The README will cover the following topics:

1. **[Introduction](#1-introduction)**
2. **[Algorithm Overview](#2-algorithm-overview)**
3. **[Code Explanation](#3-code-explanation)**
4. **[Handling Exceptional Cases](#4-handling-exceptional-cases)**
5. **[Usage](#5-usage)**


---

## 1. Introduction

The code is designed to read a SPICE circuit file and perform nodal analysis. Nodal analysis is a fundamental technique used in electrical engineering to solve for unknown node voltages and currents in a circuit. The algorithm supports basic circuit elements: Resistors, Voltage sources, and Current sources.

## 2. Algorithm Overview

The algorithm follows these main steps:

1. **Parsing the Circuit File**: The code reads the SPICE circuit file, extracts circuit components (nodes, voltage sources, current sources, and resistors), and stores them in relevant data structures.

2. **Matrix Initialization**: It initializes two matrices, $G$ (conductance matrix) and $I$ (current matrix), to set up the equations for nodal analysis.$$GV = I$$
where $V$ is nodal voltage matrix.

3. **Node Mapping**: It maps each node in the circuit to a unique index and stores this mapping in a dictionary.

4. **Resistor Handling**: For each resistor, it calculates the conductance and updates the G matrix accordingly.

5. **Voltage Source Handling**: For each voltage source, it updates the G and I matrices based on the source value and connection to nodes.

6. **Current Source Handling**: For each current source, it updates the I matrix based on the source value and connection to nodes.

7. **Solving Linear Equations**: The algorithm solves the linear equations represented by the G and I matrices using NumPy's linear algebra functions.

8. **Mapping Results**: It maps the computed nodal voltages and source currents back to their respective nodes and sources.

## 3. Code Explanation

Let's break down the code step by step:

- **Parsing Circuit File**: The code reads the SPICE circuit file line by line and extracts relevant components within the circuit block.

- **Node and Component Tracking**: It tracks nodes, voltage sources, current sources, and resistors while parsing the circuit.

- **Matrix Initialization**: The code initializes two matrices, G and I, with the appropriate dimensions based on the number of nodes and sources.

- **Node Mapping**: Nodes are mapped to unique indices in the `node_dict` dictionary.

- **Resistor Handling**: For each resistor, the conductance is calculated, and the appropriate values are updated in the G matrix.

- **Voltage Source Handling**: The code processes voltage sources, updating G and I matrices based on source values and connections to nodes.

- **Current Source Handling**: Current sources are handled by updating the I matrix based on source values and connections to nodes.

- **Solving Linear Equations**: Linear equations are solved using NumPy's `linalg.solve` function, resulting in nodal voltages and source currents.

- **Mapping Results**: Nodal voltages are mapped back to their corresponding nodes, and source currents are stored in the `current` dictionary.

## 4. Handling Exceptional Cases

The code includes robust handling of exceptional cases:

- **File Validation**: It checks if the provided file name is empty or nonexistent and raises a `FileNotFoundError` if necessary.

- **Empty Circuit File**: It detects if the circuit file is empty and raises a `FileNotFoundError` with an appropriate message.

- **Malformed Circuit**: The code ensures that the circuit file contains both `.circuit` and `.end` directives and raises a `ValueError` if they are missing.

- **Missing 'GND' Node**: It checks for the presence of a 'GND' node in the circuit and raises a `ValueError` if it's missing.

- **Circuit Error**: The code verifies that there is a solvable circuit and raises a `ValueError` if no solution can be found.


## 5. Usage

To use this code, follow these steps:

1. Ensure you have a valid SPICE circuit file.
2. Call the `evalSpice(filename)` function with the filename as the argument.
3. The function will return two dictionaries: `node_dict` (containing nodal voltages) and `current` (containing source currents).

Example usage:

```python
voltage, current = evalSpice("path_to_file")
print("Nodal Voltages:", voltage)
print("Source Currents:", current)
```

