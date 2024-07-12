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
StatLab/Corr/NP/Spearman's Rho  
#############

:red-b:`Disclaimer:`
:red:`This page is provided only for studying and practicing. The author does not intend to promote or advocate any particular analysis method or software.`

*************
Background
*************

Spearman's rho (:math:`\rho`) is a statistic used for measuring rank correlation [1]_ [2]_. 

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

Let :math:`(R_{i1}, R_{i2})` be the rank of :math:`Y_{i1}` and the rank of :math:`Y_{i2}`.
In the case of ties, one method is to assign the tied group with the average of unique ranks corresponding the tied group.
For the :math:`i` th sample, let 
:math:`s_1` be the number of observed values less than :math:`Y_{i1}`,
:math:`s_2` be the number of observed values equal to :math:`Y_{i1}`,
and :math:`s_3` be the number of observed values greater to :math:`Y_{i1}`.
We can calculate the rank of a single sample as 

.. math::
  :label: eq_rank

  R_{i^*1} = s1 + \frac{s2+1}{2} = n - s3 - \frac{s-1}{2}.

For a vector, ``pandas.DataFrame`` has the ``rank`` function with ``method='average'`` option to calculate rank as defined in :eq:`eq_rank`. 
In ``R``, that can be calculated using the ``rank`` function with ``ties.method='average'`` option.
See reference [2]_ for ranking in ``Julia``.

The Spearman's :math:`\rho` can be calculated as:

.. math::
  :label: eq_rho

  \rho = \frac{\frac{1}{n}\sum_i R_{i1}R_{i2} - \frac{1}{4}(n+1)^2}{s_1 s_2},

where :math:`s_1 = \sum_i Y_{i1}^2 - \frac{1}{4}(n+1)^2`,
and :math:`s_2 = \sum_i Y_{i2}^2 - \frac{1}{4}(n+1)^2`.

*************
Example - Group-1
*************

.. list-table:: Spearman's :math:`\rho = 1.0`
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

.. list-table:: Spearman's :math:`\rho = -1.0`
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

  from scipy.stats import spearmanr

  y1 = [1, 3, 2]
  y2 = [4, 6, 5]

  rho, p_value = spearmanr(y1, y2)
  print("Spearman's rho:", rho)



*************
Reference
*************

.. [1] Wikipedia. (year). Spearman's rank correlation coefficient. https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient
.. [2] https://discourse.julialang.org. (2022). Ranking of elements of a vector. https://discourse.julialang.org/t/ranking-of-elements-of-a-vector/88293/4
.. [3] scipy.org. (year). spearmanr. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html

