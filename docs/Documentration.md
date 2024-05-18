# Technical Documentation

This document provides technical details and documentation for the Python implementation of the NBD-Dirichlet model of consumer buying behavior for marketing research.

## Model Description

The NBD-Dirichlet model is a probabilistic model that describes the purchase incidence and brand choice of consumer products. It combines the Negative Binomial Distribution (NBD) for modeling purchase incidence and the Dirichlet distribution for modeling brand choice.

The model estimates several parameters, including:

- `M`: The expected number of purchases per unit time.
- `K`: The heterogeneity parameter of the NBD.
- `S`: The concentration parameter of the Dirichlet distribution.

## Functions

### `dirichlet()`

The `dirichlet()` function estimates the parameters of the NBD-Dirichlet model given the input data. It takes the following arguments:

- `cat_pen`: Category penetration.
- `cat_buyrate`: Category buyer's average purchase rate.
- `brand_share`: Brand's market share.
- `brand_pen_obs`: Brand penetration.
- ...

### `plot_dirichlet()`

The `plot_dirichlet()` function creates plots of the theoretical penetration growth and shopping rate growth over time. It takes the following arguments:

- `x`: An object of the "dirichlet" class.
- `t`: The number of time periods to plot.
- ...

### `print_dirichlet()`

The `print_dirichlet()` function prints a summary of the estimated NBD-Dirichlet model parameters. It takes the following arguments:

- `x`: An object of the "dirichlet" class.
- ...

### `summary_dirichlet()`

The `summary_dirichlet()` function generates various summary statistics based on the estimated model. It takes the following arguments:

- `obj`: An object of the "dirichlet" class.
- `t`: The number of time periods.
- `type`: The type of summary statistics to generate.
- ...

## Usage Examples

Here are some examples of how to use the functions provided by the Python implementation:

```python
# Estimate the NBD-Dirichlet model parameters
dpar = dirichlet(cat_pen, cat_buyrate, brand_share, brand_pen_obs)

# Plot the theoretical penetration growth and shopping rate growth
plot_dirichlet(dpar, t=4)

# Print a summary of the estimated model parameters
print_dirichlet(dpar)

# Generate summary statistics
summary = summary_dirichlet(dpar, t=1, type=['buy', 'freq', 'heavy', 'dup'])
```
