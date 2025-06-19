# JMTS_2403 | Linear Programming Solver via Import-Free Simplex Method

A linear programming solver GUI using the simplex method.

## Overview

This project provides two implementations of the simplex method for solving linear programming problems:

- **simplex.py**: Simplex method in python without imports
- **JMTS_2403A_C01.py**: A GUI application with interactive problem definition

## ✨ Features

### Core Functionality
- Solves linear programming problems in standard form handling both maximization and minimization problems
- Implements the import-free simplex method
- Supports inequity and bounds constraints

### GUI Features
- Interactive problem definition interface
- Interactive constraint and objective function input
- Variable bounds specification


## Installation

No external dependencies required for the core simplex implementation. For the GUI version:

```bash
# The GUI version uses tkinter, which comes with Python by default
python --version  # Ensure Python 3.x is installed
```

## 🔐 Usage

### Command Line Version (simplex.py)

The basic version demonstrates solving a predefined linear programming problem:

```python
# Example problem setup in the code:
# Minimize: -3x₁ - 5x₂
# Subject to:   x₁ ≤ 4
#               2x₂ ≤ 12
#               3x₁ + 2x₂ ≤ 18
#               x₁, x₂ ≥ 0
```

Run:
```bash
python simplex.py
```

### GUI Version 01 (JMTS_2403_C01.py)

Launch the interactive interface:
```bash
python JMTS_2403_C01.py
```

#### Using the GUI:

1. **Define Problem Parameters**:
   - Select objective type (min/max)
   - Set number of variables (n)
   - Set number of constraints (m)
   - Click "Define" to generate input fields

2. **Input Problem Data**:
   - Enter objective function coefficients
   - Define constraint coefficients and right-hand side values
   - Set variable bounds (supports -inf and inf)

3. **Solve**:
   - Click "Solve" to run the simplex algorithm
   - View optimal solution and objective value
   - Review problem formulation in the results panel

## Mathematical Formulation

The solver handles linear programming problems in the form:

```
Minimize (or Maximize): c₁x₁ + c₂x₂ + ... + cₙxₙ

Subject to:
a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ ≤ b₁
a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ ≤ b₂
⋮
aₘ₁x₁ + aₘ₂x₂ + ... + aₘₙxₙ ≤ bₘ

With variable bounds:
lⱼ ≤ xⱼ ≤ uⱼ for j = 1, 2, ..., n
```

## Algorithm Details

### Simplex Method Implementation

1. **Initialization**: Convert to standard form by adding slack variables
2. **Pivot Selection**: Choose entering variable (most negative coefficient) and leaving variable (minimum ratio test)
3. **Pivot Operations**: Perform row operations to maintain tableau form
4. **Optimality Check**: Continue until no negative coefficients remain in objective row
5. **Solution Extraction**: Read optimal values from final tableau

### Key Features

- **Feasibility Checking**: Validates solution against original constraints
- **Unbounded Detection**: Identifies problems with no finite optimum

## 📂 Repository Structure

```
├── simplex.py              # Core simplex implementation
├── JMTS_2403_C01.py      # GUI application
└── README.md              # This documentation
```

## Example Output

### JMTS_2403_C01.py
```
[3, 4, 5, 6]
[1, 4, 5, 6]
[1, 2, 5, 6]
x_optimal: [2.0, 6.0]
f_optimal: 36.0
```

### GUI Interface
The GUI provides a final results display including:
- Optimal variable values & corresponding objective function value
- Coefficients of the objective function
- Constraint matrix representation

## Technical Notes

- **Numerical Precision**: Uses floating-point arithmetic with tolerance checking
- **Memory Efficiency**: Minimal memory footprint with in-place operations
- **Error Handling**: Comprehensive validation and error reporting
- **Platform Independence**: Pure Python implementation, cross-platform compatible

## Purpose

This project is motivated as-is primarily for self-learning purposes, which is an exercise of the simplex method and optimization solver GUI. 
Subsequent improvements, bug fixes, or additional features are expected.

## 📄 License

This package is released under the MIT License.

## ✏️ Author

Created by [@Yunqing-Jia](https://github.com/Yunqing-Jia) as the JMTS_2403 project.