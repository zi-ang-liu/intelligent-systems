# Random Search

Random search (RS)は最適化問題を解くためにランダムな探索を行うアルゴリズムです。

RSは、探索空間内のランダムな点を評価することで、最適解を探索します。RSは、勾配情報を必要とせず、関数$f$が微分可能である必要もありません。そのため、非常にシンプルで汎用性のある最適化手法となります。

$\mathbf{x} \in \mathbb{R}^n$を探索空間とし、目的関数$f: \mathbb{R}^n \to \mathbb{R}$を最小化する問題を考えます。$x_i$は$i$番目の次元の値を表します。$\mathcal{X}$を探索空間とします。

RSのアルゴリズムは以下の通りです。

```{prf:algorithm} Random Search
:label: random-search-algorithm

**Inputs:** function $f$, number of iterations $N$, search space $\mathcal{X}$     
**Output:** estimate of the minimum $\mathbf{x}$

1. Initialize $\mathbf{x}$ with a point in the search space $\mathcal{X}$
2. For $i = 1, 2, \ldots, N$:
    1. Generate a random point $\mathbf{x}'$ in the search space $\mathcal{X}$
    2. If $f(\mathbf{x}') < f(\mathbf{x})$, then $\mathbf{x} \leftarrow \mathbf{x}'$
3. Return $\mathbf{x}$
```

## Python implementation

### Sphere function

まず、RSの実装を理解するために、Sphere関数を最小化する問題を考えます。Sphere関数は以下のように定義されます。

$$
f(\mathbf{x}) = \sum_{i=1}^{n} x_i^2
$$

$n$次元のSphere関数の最小値は$\mathbf{x} = \mathbf{0}$であり、その値は$f(\mathbf{0}) = 0$です。探索空間は$\mathcal{X} = [-5.12, 5.12]^n$です。

Sphere関数を最小化するRSの実装は以下の通りです。

```python
import numpy as np


def sphere(x):
    """
    Sphere function

    Parameters
    ----------
    x : np.ndarray
        The input vector

    Returns
    -------
    float
        The value of the Sphere function
    """
    return np.sum(x**2)


def random_search(f, num_iter, search_space, num_dim):
    """
    Random Search

    Parameters
    ----------
    f : function
        The objective function
    num_iter : int
        Number of iterations
    search_space : tuple
        The search space
    num_dim : int
        Number of dimensions

    Returns
    -------
    x : np.ndarray
        The estimate of the solution
    """

    x = np.random.uniform(search_space[0], search_space[1], num_dim)

    for _ in range(num_iter):
        x_new = np.random.uniform(search_space[0], search_space[1], num_dim)
        if f(x_new) < f(x):
            x = x_new

    return x


# number of dimensions
n = 2
# search space
search_space = (-5.12, 5.12)
# number of iterations
num_iter = 1000000

x = random_search(sphere, num_iter, search_space, n)
print("Estimated solution:", x)
```

### ナップサック問題

ナップサック問題は、最適化問題の一つで、与えられた重さと価値を持つアイテムの集合から、重さの合計が制限内で価値の合計を最大化するアイテムの集合を見つける問題です。

#### 問題設定

ナップサック問題の設定は以下の通りです。

- $n$: アイテムの数
- $\mathcal{I}$: アイテムの集合, $\mathcal{I} = \{1, 2, \ldots, n\}$
- $w_i$: アイテム$i$の重さ
- $v_i$: アイテム$i$の価値
- $W$: ナップサックの重さの制限
- $x_i$: アイテム$i$をナップサックに入れるかどうかを表すバイナリ変数, $x_i \in \{0, 1\}$

この問題の目的は、アイテムの集合$\mathcal{I}$から選んだアイテムの重さの合計が$W$以下となるようにして、価値の合計を最大化するアイテムの集合を見つけることです。

最適化問題は以下のように定式化されます。

$$
\begin{align*}
\text{maximize} \quad & \sum_{i \in \mathcal{I}} v_i x_i \\
\text{subject to} \quad & \sum_{i \in \mathcal{I}} w_i x_i \leq W \\
& x_i \in \{0, 1\}, \quad \forall i \in \mathcal{I}
\end{align*}
$$

### RSの実装

ナップサック問題を解くためのRSの実装は以下の通りです。

```python
import numpy as np


def knapsack_value(x):
    """
    Calculate the total value of selected items

    Parameters
    ----------
    x : np.ndarray
        The vector with binary values, 1 if the item is selected, 0 otherwise

    Returns
    -------
    float
        The total value
    """
    return np.sum(v * x)


def knapsack_weight(x):
    """
    Calculate the total weight of selected items

    Parameters
    ----------
    x : np.ndarray
        The vector with binary values, 1 if the item is selected, 0 otherwise

    Returns
    -------
    float
        The total weight
    """
    return np.sum(w * x)


def random_search(num_item, num_iter):
    """
    Random Search for Knapsack Problem

    Parameters
    ----------
    num_item : int
        Number of items
    num_iter : int
        Number of iterations

    Returns
    -------
    x : np.ndarray
        The estimate of the solution
    """

    x = np.zeros(num_item)
    
    for _ in range(num_iter):
        x_new = np.random.randint(0, 2, num_item)
        if knapsack_weight(x_new) <= W and knapsack_value(x_new) > knapsack_value(x):
            x = x_new

    return x


# weight of items
w = np.array([7, 5, 3, 2, 8])
# value of items
v = np.array([5, 10, 8, 4, 7])
# knapsack capacity
W = 15
# number of items
num_item = len(w)
# number of iterations
num_iter = 500

x = random_search(num_item, num_iter)
print("Selected items:", np.where(x == 1)[0])
print("Total value:", knapsack_value(x))
print("Total weight:", knapsack_weight(x))
```