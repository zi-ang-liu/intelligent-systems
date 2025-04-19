# The Economic Order Quantity Model

The *Economic Order Quantity* (EOQ) model is one of the most foundamental inventory models. 

## Problem Definition

## Formulation

- $K$: fixed cost per order
- $h$: holding cost per unit per year
- $\lambda$: demand rate (units per year)
- $Q$: order quantity

````{prf:theorem} Economic Order Quantity
:label: eoq
The optimal order quantity $Q^*$ that minimizes the total cost in the EOQ model is given by:

$$
Q^* = \sqrt{\frac{2KD}{h}}$$
$$

The total cost $g(Q)$ is given by:

$$
g(Q^*) = \sqrt{2K \lambda h}
$$

````

## Implementation


```python
def eoq(K, h, demand):
    """
    Calculate the Economic Order Quantity (EOQ) and the total cost.

    Parameters:
    K (float): Fixed cost per order
    h (float): Holding cost per unit per year
    demand (float): Demand rate (units per year)

    Returns:
    tuple: Optimal order quantity (Q*) and total cost (g(Q*))
    """
    Q_optimal = (2 * K * demand / h) ** 0.5
    total_cost = (2 * K * demand * h) ** 0.5
    return Q_optimal, total_cost


# Example usage
K = 8  # Fixed cost per order
h = 0.225  # Holding cost per unit per year
demand = 1300  # Demand rate (units per year)
optimal_order_quantity, total_cost = eoq(K, h, demand)
print(f"Optimal Order Quantity (Q*): {optimal_order_quantity}")
print(f"Total Cost (g(Q*)): {total_cost}")
```