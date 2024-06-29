..
    #  Copyright (C) 2023-2024 Y Hsu <yh202109@gmail.com>
    #
    #  This program is free software: you can redistribute it and/or modify
    #  it under the terms of the GNU General Public license as published by
    #  the Free software Foundation, either version 3 of the License, or
    #  any later version.
    #
    #  This program is distributed in the hope that it will be useful,
    #  but WITHOUT ANY WARRANTY; without even the implied warranty of
    #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    #  GNU General Public License for more details
    #
    #  You should have received a copy of the GNU General Public license
    #  along with this program. If not, see <https://www.gnu.org/license/>
   
.. role:: red-b

.. role:: red

#############
StatLab/Corr/Kendall's tau 
#############

:red-b:`Disclaimer:`
:red:`This page is provided only for studying and practicing. The author does not intend to promote or advocate any particular analysis method or software.`

*************
Background
*************

Kendall's tau (:math:`\tau`) is a statistic used for measuring rank correlation [1]_ [2]_ . 

*************
Notation 
*************

Let :math:`(Y_{i1}, Y_{i2})` be a pair of random variables corresponding to the :math:`i` th sample where :math:`i = 1, \ldots, n`.

.. list-table:: Observed Value
   :widths: 10 10 10 
   :header-rows: 1
   :name: tbl_count1

   * - 
     - :math:`Y_{i1}`
     - :math:`Y_{i2}`
   * - **Sample:** 1
     - :math:`Y_{11}`
     - :math:`Y_{12}` 
   * - **Sample:** 2
     - :math:`Y_{21}` 
     - :math:`Y_{22}` 
   * - :math:`\vdots` 
     - :math:`\vdots`
     - :math:`\vdots`
   * - **Sample:** :math:`n`
     - :math:`Y_{n1}`
     - :math:`Y_{n2}` 

Let :math:`Z_{ij} \equiv sign(Y_{i1}-Y_{j1})sign(Y_{i2}-Y_{j2})`,
:math:`c = \sum_{i=1}^n \sum_{j < n} I(Z_{ij}=1)`,
:math:`d = \sum_{i=1}^n \sum_{j < n} I(Z_{ij}=-1)`
and :math:`t = \frac{n(n-1)}{2}`.
The coefficient :math:`\tau` (tau-a) can be calculated as 

.. math::
  :label: eq_tau1

  \tau = \frac{ c - d }{t}.

:eq:`eq_tau1` can also be expressed as 

.. math::

  \tau = \frac{2}{n(n-1)} \left( \sum_{i=1}^n \sum_{j < n} Z_{ij} \right),


If there were no ties, the maximum value of :eq:`eq_tau1` is 1 at :math:`c=t`, and the minimum is -1 at :math:`d=t`


*************
Example - Group-1
*************

.. list-table:: Kendall's :math:`\tau = 1.0`
   :widths: 10 10 10 
   :header-rows: 1
   :name: tbl_ex1

   * - 
     - :math:`Y_{i1}`
     - :math:`Y_{i2}`
   * - **Sample:** 1
     - 1
     - 4
   * - **Sample:** 2
     - 3
     - 6
   * - **Sample:** 3
     - 2
     - 5

.. list-table:: Kendall's :math:`\tau = -1.0`
   :widths: 10 10 10 
   :header-rows: 1
   :name: tbl_ex1

   * - 
     - :math:`Y_{i1}`
     - :math:`Y_{i2}`
   * - **Sample:** 1
     - 1
     - 6
   * - **Sample:** 2
     - 3
     - 4
   * - **Sample:** 3
     - 2
     - 5

*************
How-to 
*************

To use ``scipy.stats`` [3]_:

.. code:: python

  from scipy.stats import kendalltau 
  y1 = [1,3,2]
  y2 = [4,6,5]

  tau, p_value = kendalltau(y1, y2)
  print("Kendall's tau:", tau)

*************
Reference
*************

.. [1] Wikipedia. (year). Kendall rank correlation coefficient. https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient
.. [2] Encyclopedia of Mathematics. (yeawr). Kendall tau metric. https://encyclopediaofmath.org/index.php?title=Kendall_tau_metric
.. [2] Scipy. (year). kendalltau. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kendalltau.html

