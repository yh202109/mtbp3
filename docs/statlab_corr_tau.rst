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
StatLab/Corr/Kendall's tau coefficient 
#############

:red-b:`Disclaimer:`
:red:`This page is provided only for studying and practicing. The author does not intend to promote or advocate any particular analysis method or software.`

*************
Background
*************

Kendall's tau (:math:`\tau`) is a statistic used for measuring rank correlation [1]_. 

*************
Notation 
*************

Let :math:`Y_{i1}` and :math:`Y_{i2}` be a pair of independent random variables corresponding to the :math:`i` th sample where :math:`i = 1, \ldots, n`.

.. list-table:: Count of Ratings
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

The coefficient :math:`\tau` can be calculated as 

.. math::
  :label: eq_tau1

  \tau = \frac{2}{n(n-1)} \left(2\sum_{i=1}^n \sum_{j < n} I(sign(Y_{i1}-Y_{j1})sign(Y_{i2}-Y_{j2})==1) - \frac{n(n-1)}{2}\right).

*************
Reference
*************

.. [1] Wikipedia. (year). Kendall rank correlation coefficient. https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient

