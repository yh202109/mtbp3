# mtbp3

![PyPI](https://img.shields.io/pypi/v/mtbp3?label=pypi%20package)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mtbp3)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Tests Status](./_static/reports/junit/tests-badge.svg?dummy=8484744)](./_static/reports/junit/report.html)
[![Coverage Status](./_static/reports/coverage/coverage-badge.svg?dummy=8484744)](./_static/reports/coverage/coverage.xml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yh202109/mtbp3supp/main?filepath=binder/example_emt3_appendix.ipynb)

My tool box in Python.

Functions are grouped into:

- Health
  - Data summary: `health.clinical`
  - eCTD: `health.ectd` 
  - MedDRA: `health.emt` 
  - WhoDrug: 
  - ISO: 
- General 
  - Data summary: `util.cdt`
  - Graphs: `util.cdtg`
  - System: `util.lsr`
- Standard: 
  - CDISC: 
- StatLab: 
  - Correlation: `statlab.corr` 
  - Reliability: `statlab.kappa`

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license) 
- [Credits](#credits) 
- [How to Cite](#how-to-cite) 

## Installation

Instructions on how to install the project and its dependencies.

```bash
$ pip install mtbp3
```

## Usage

Below is an example of showing the version of currently installed package:

``` 
import mtbp3
print(mtbp3.__version__)
``` 

Please find more examples from the link [here](https://yh202109.github.io/mtbp3/index.html).

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`mtbp3` was created by Y. Hsu. It is licensed under the terms of the GNU General Public License v3.0 license.

## Credits

Documentation: 

- Documents were initially created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
- Version badges are provided by: https://img.shields.io/pypi
- Tests badges were generated by: https://smarie.github.io/python-genbadge/

## How to Cite 

Hsu, Y. (2024). mtbp3: My tool box in Python [Software]. Retrieved from https://yh202109.github.io/mtbp3/index.html.

```
@software{mtbp3,
  author = {Hsu, Y.},
  title = {mtbp3: My tool box in Python},
  year = {2024},
  url = {https://yh202109.github.io/mtbp3/index.html},
  note = {Software}
}
```