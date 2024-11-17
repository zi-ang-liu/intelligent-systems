# Installation

## Install Gurobi Optimizer for Python

### Conda

To install Gurobi Optimizer for Python using conda, use the following command:

```bash
conda install -c gurobi gurobi
```

To specify a version, use the following command:

```bash
conda install -c gurobi gurobi=10.0.1
```

### Pip

To install Gurobi Optimizer for Python using pip, use the following command:

```bash
python -m pip install gurobipy
```

To specify a version, use the following command:

```bash
python -m pip install gurobipy==11.0.0
```

### Setup License

To use Gurobi Optimizer, you need to obtain a license. If you are an academic user, you can request an academic license for free from the Gurobi website.

In the website, you can find a specific license (e.g., `grbgetkey 253e22f3-...`). Run this command in the terminal to set up the license.

## Using Google Colab

### Install Gurobi

To use Gurobi Optimizer in Google Colab, you need to install Gurobi in the Colab environment. Run the following commands in the Colab notebook:

```python
!pip install gurobipy  # install gurobipy, if not already installed
import gurobipy as gp  # import the installed package
```

This will install the Size-limited Trial License version of Gurobi Optimizer, which can solve at most 2000 variables and 2000 constraints.

The following code creates a `model_size_limited` object of the `Model` class:

```python
model_size_limited = gp.Model()
```

The following output indicates that the size-limited Gurobi Optimizer is installed:

```python
Restricted license - for non-production use only - expires 2025-11-24
```

## The Example

The following is a linear programming problem:

$$
\begin{align*}
\max &\quad 5x_1 + 4x_2 \\
\text{s.t.} &\quad x_1 + 2x_2 \leq 80 \\
&\quad 4x_1 + 4x_2 \leq 180 \\
&\quad 3x_1 + x_2 \leq 90 \\
&\quad x_1, x_2 \geq 0
\end{align*}
$$

Here, $x_1$ and $x_2$ are the decision variables. The objective is to find so