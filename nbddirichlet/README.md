# NBD-Dirichlet Model of Consumer Buying Behavior for Marketing Research (Python Version)

This repository contains a Python implementation of the NBD-Dirichlet model of consumer buying behavior for marketing research. The code is translated from the original R version of the package "NBDdirichlet" developed by Feiming Chen.

## Acknowledgment

We would like to acknowledge and express our gratitude to Feiming Chen for developing the original R version of the "NBDdirichlet" package. The Python implementation in this repository is based on their work and aims to provide similar functionality in the Python programming language.

The original R package details are as follows:

```
Package: NBDdirichlet
Type: Package
Title: NBD-Dirichlet Model of Consumer Buying Behavior for Marketing Research
Version: 1.4
Date: 2022-05-26
Author: Feiming Chen
Maintainer: Feiming Chen <feimingchen@yahoo.com>
URL: https://ani.stat.fsu.edu/~fchen/statistics/R-package-NBDdirichlet/how-to-use-Dirichlet-marketing-model.html
Description: The Dirichlet (aka NBD-Dirichlet) model describes the purchase incidence and brand choice of consumer products. We estimate the model and summarize various theoretical quantities of interest to marketing researchers. Also provides functions for making tables that compare observed and theoretical statistics.
License: GPL (>= 3)
NeedsCompilation: no
Packaged: 2022-05-27 13:36:17 UTC; fchen
Repository: CRAN
Date/Publication: 2022-05-29 14:00:02 UTC
```

## Overview

The NBD-Dirichlet model is a powerful tool for analyzing consumer buying behavior in marketing research. It describes the purchase incidence and brand choice of consumer products. This Python implementation provides functions to estimate the model parameters and summarize various theoretical quantities of interest to marketing researchers.

## Installation

To use the Python version of the NBD-Dirichlet model, you need to have Python installed on your system. You can download and install Python from the official website: [https://www.python.org](https://www.python.org)

Additionally, you need to install the required dependencies listed in the `requirements.txt` file. You can install them using the following command:

```
pip install -r requirements.txt
```

## Usage

The main functions provided by this Python implementation are:

- `dirichlet`: Estimates the parameters of the NBD-Dirichlet model.
- `plot_dirichlet`: Plots the theoretical penetration growth and shopping rate growth over time.
- `print_dirichlet`: Prints a summary of the estimated NBD-Dirichlet model parameters.
- `summary_dirichlet`: Generates various summary statistics based on the estimated model.

For detailed usage instructions and examples, please refer to the documentation and example notebooks provided in this repository.

## Contributing

Contributions to this Python implementation of the NBD-Dirichlet model are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This Python implementation is released under the [GNU General Public License (GPL) version 3](https://www.gnu.org/licenses/gpl-3.0.en.html) or later, consistent with the original R package.

## Contact

If you have any questions or inquiries regarding this Python implementation, please contact Massimiliano Marinucci at mmarinucci@numinate.com.
