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

Kendall's tau (:math:`\tau`) is a statistic used for measuring rank correlation [1]_ [2]_. 

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

Let :math:`Z_{ij1} \equiv sign(Y_{i1}-Y_{j1})`, :math:`Z_{ij2} \equiv sign(Y_{i2}-Y_{j2})`,
:math:`c = \sum_{i=1}^n \sum_{j < i} I(Z_{ij1}Z_{ij2}=1)`,
:math:`d = \sum_{i=1}^n \sum_{j < i} I(Z_{ij1}Z_{ij2}=-1)`
and :math:`t = \frac{n(n-1)}{2}`.
The coefficient :math:`\tau` (tau-a) can be calculated as 

.. math::
  :label: eq_tau1

  \tau = \frac{ c - d }{t}.

If there are no ties, the maximum value of :eq:`eq_tau1` is 1 at :math:`c=t`, 
and the minimum is -1 at :math:`d=t`.

:eq:`eq_tau1` can also be expressed as 

.. math::
  :label: eq_tau2

  \tau =& \frac{2}{n(n-1)} \left( \sum_{i=1}^n \sum_{j < i} Z_{ij1}Z_{ij2} \right) \\
  =& \frac{1}{n(n-1)} \left( \sum_{i=1}^n \sum_{j=1}^n Z_{ij1}Z_{ij2} \right).

Under independent sample assumption, for a fixed :math:`n`, we know that 
:math:`E(Z_{ij1})=E(Z_{ij2})=0` and 
:math:`Var(Z_{ij1})=Var(Z_{ij2})=1-\frac{1}{n}`. 
From :eq:`eq_tau2`, we can see that :math:`\tau` is a type of correlation coefficient.

If there are ties, the maximum value of :eq:`eq_tau1` becomes less then 1. 
Consider the scenario that there are :math:`n_{t1}` groups of ties in :math:`\{Y_{i1}\}`,
and there are :math:`n_{t2}` groups of ties in :math:`\{Y_{i2}\}`.
Let :math:`n_{t1,k}` be the number of ties within the :math:`k` th group of ties in :math:`\{Y_{i1}\}`,
and :math:`n_{t2,k}` be the number of ties within the :math:`k` th group of ties in :math:`\{Y_{i2}\}`
The adjusted :math:`\tau` (tau-b) is calculated by replacing :math:`t` in :eq:`eq_tau1` with 
:math:`t^* = \sqrt{\frac{1}{2}n(n-1)-\sum_{k=1}^{n_{t1}} \frac{1}{2}n_{t1,k}(n_{t1,k}-1)}\sqrt{\frac{1}{2}n(n-1)-\sum_{k=1}^{n_{t2}} \frac{1}{2}n_{t2,k}(n_{t2,k}-1)}`

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
Lab Exercise  
*************

1. Show :math:`E(Z_{ij})=0`.

*************
Algorithm 
*************

**WARNING: FOR SMALL SAMPLE SIZES ONLY**

Note that the algorithm in this section is implement in ``mtbp3.stalab`` for demonstration only.
Although the matrix presentation is easier to understand, 
the calculation time increases greatly when the sample size increases.
More practical algorithms can be found in references.

Let :math:`Y_{1} = (Y_{11}, \ldots, Y_{n1})` and :math:`Y_{2} = (Y_{12}, \ldots, Y_{n2})`.
Let :math:`\times` represent the matrix product, 
:math:`\times_{car}` represent the Cartesian product, 
:math:`\times_{ele}` represent the element-wise product, 
:math:`g([(a,b)]) = [sign(a-b)]`.
and :math:`h(X_n) = 1_n \times X_n \times 1_n^T`
where :math:`X_n` is a size :math:`n` by :math:`n` matrix, and :math:`1_n` is a length :math:`n` one vector.
Both tau-a and tau-b can be calculated as 

  .. math::
    \tau_1 &= g(Y_{1} \times_{car} Y_{1}) \\
    \tau_2 &= g(Y_{2} \times_{car} Y_{2}) \\
    \tau &= \frac{h(\tau_1 \times_{ele} \tau_2) }{ \sqrt{h(abs(\tau_1))}\sqrt{h(abs(\tau_2))} }


*************
How-to 
*************

To use ``mtbp3.corr``:

.. code:: python

  import numpy as np

  size = 100
  y1 = np.random.randint(1, size+1, size=size).tolist()
  y2 = np.subtract(np.random.randint(1, size+1, size=size),y1).tolist()
  t = CorrCalculator([y1,y2])
  print("Kendall's tau (mtbp3.corr):", c.calculate_kendall_tau())

To create a scatter plot of ``y1`` and ``y2``:

.. code:: python

  c.plot_y_list(axis_label=['y1','y2'])

*************
Reference
*************

.. [1] Wikipedia. (year). Kendall rank correlation coefficient. https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient
.. [2] Encyclopedia of Mathematics. (yeawr). Kendall tau metric. https://encyclopediaofmath.org/index.php?title=Kendall_tau_metric
.. [3] Scipy. (year). kendalltau. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kendalltau.html

