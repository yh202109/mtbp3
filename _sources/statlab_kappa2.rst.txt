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
StatLab/Fleiss's Kappa  
#############

:red-b:`Disclaimer:`
:red:`This page is provided only for studying and practicing. The author does not intend to promote or advocate any particular analysis method or software.`

*************
Background
*************

Fleiss's kappa (:math:`\kappa`) is a statistic used for describing inter-rater reliability of multiple independent raters 
with categorical rating outcomes [1]_ [2]_. 

*************
Notation 
*************

Assume there are the same :math:`R+N_0 \geq 2+N_0` raters and each of :math:`n` samples were rated by :math:`R` randomly selected raters and were not rated by the rest of :math:`N_0` raters.
For :math:`J` categories rating, let :math:`Y_{r,i} \in \{v_0, v_1,v_2,\ldots, v_J \}` represent rating 
from rater :math:`r=1,2,\ldots,R+N_0` for sample :math:`i = 1, \ldots, n`.
Let :math:`N_{ij}` represent the total number of raters gave rating :math:`(v_j)` to sample :math:`i`, where :math:`j \in \{0, 1,\ldots,J\}`.
The value :math:`v_0` represent raters did not rate the sample :math:`i` and :math:`N_{i0}=N_0` is a fixed number for all :math:`i`.
Therefore, :math:`v_0` will not be included in the discussion below.

.. list-table:: Count of Ratings
   :widths: 10 10 10 10 10 10
   :header-rows: 1
   :name: tbl_count1

   * - 
     - :math:`v_1`
     - :math:`v_2`
     - :math:`\ldots` 
     - :math:`v_J`
     - Row Total
   * - **Sample:** 1
     - :math:`N_{11}`
     - :math:`N_{12}` 
     - :math:`\ldots` 
     - :math:`N_{1J}` 
     - :math:`R` 
   * - **Sample:** 2
     - :math:`N_{21}` 
     - :math:`N_{22}` 
     - :math:`\ldots` 
     - :math:`N_{2J}` 
     - :math:`R` 
   * - **Sample:** 3
     - :math:`N_{31}`
     - :math:`N_{32}` 
     - :math:`\ldots` 
     - :math:`N_{3J}` 
     - :math:`R` 
   * - :math:`\vdots` 
     - :math:`\vdots`
     - :math:`\vdots`
     - :math:`\ddots` 
     - :math:`\vdots`
     - :math:`\vdots` 
   * - **Sample:** :math:`n`
     - :math:`N_{n1}`
     - :math:`N_{n2}` 
     - :math:`\ldots` 
     - :math:`N_{nJ}` 
     - :math:`R` 
   * - **Column total**
     - :math:`N_{\bullet 1}`
     - :math:`N_{\bullet 2}` 
     - :math:`\ldots` 
     - :math:`N_{\bullet J}` 
     - :math:`nR` 

The observed averaged agreement is calculated as 

.. math::
  :label: eq_obs1

  \bar{p}_O = \frac{1}{n} \sum_{i=1}^n p_{O,i},

where :math:`p_{O,i} = \frac{1}{R(R-1)} \left(\sum_{j=1}^J N_{ij}(N_{ij}-1)\right)= \frac{1}{R(R-1)} \left(\sum_{j=1}^J N_{ij}^2 - R\right)`.

The expected agreement is calculated as 

.. math::
  :label: eq_exp1

  \bar{p}_E = \sum_{j=1}^J p_{E,j}^2,

where :math:`p_{E,j} = \frac{N_{\bullet j}}{nR}`.

The Fleiss's :math:`\kappa` statistic is calculated from :eq:`eq_obs1` and :eq:`eq_exp1` as

.. math::
  :label: eq_kappa1

  \kappa = \frac{\bar{p}_O - \bar{p}_E}{1-\bar{p}_E}.

*************
Example - Group-1
*************

.. list-table:: Fleiss's :math:`\kappa = 1.0`
   :widths: 10 10 10 10 10
   :header-rows: 1

   * - 
     - :math:`v_1`
     - :math:`v_2`
     - :math:`v_3`
     - :math:`v_4`
   * - **Sample 1**
     - 12
     - 0
     - 0
     - 0
   * - **Sample 2**
     - 0
     - 12
     - 0
     - 0
   * - **Sample 3**
     - 0
     - 0
     - 12 
     - 0
   * - **Sample 4**
     - 0
     - 0
     - 12 
     - 0
   * - **Sample 5**
     - 0
     - 0
     - 0
     - 12 
   * - **Column Total**
     - 12 
     - 12 
     - 24 
     - 12


.. list-table:: Fleiss's :math:`\kappa` = -0.0909090909090909
   :widths: 10 10 10 10 10
   :header-rows: 1

   * - 
     - :math:`v_1`
     - :math:`v_2`
     - :math:`v_3`
     - :math:`v_4`
   * - **Sample 1**
     - 3
     - 3
     - 3
     - 3
   * - **Sample 2**
     - 3
     - 3
     - 3
     - 3
   * - **Sample 3**
     - 3
     - 3
     - 3 
     - 3
   * - **Sample 4**
     - 3
     - 3
     - 3 
     - 3
   * - **Sample 5**
     - 3
     - 3
     - 3
     - 3 
   * - **Column Total**
     - 15 
     - 15 
     - 15
     - 15

*************
How-to 
*************

To use both ``statsmodels.stats.inter_rater`` and ``mtbp3.statlab``:

.. testcode::

   import statsmodels.stats.inter_rater as ir
   from mtbp3.statlab import kappa

   r1 = ['NA'] * 20 + ['B'] * 50 + ['A'] * 30
   r2 = ['A'] * 20 + ['NA'] * 20 + ['B'] * 60
   r3 = ['A'] * 40 + ['NA'] * 20 + ['B'] * 30 + ['C'] * 10
   r4 = ['B'] * 60 + ['NA'] * 20 + ['C'] * 10 + ['A'] * 10
   r5 = ['C'] * 60 + ['A'] * 10 + ['B'] * 10 + ['NA'] * 20
   data = [r1, r2, r3, r4, r5]
   kappa = KappaCalculator(data, stringna='NA')

   print("Fleiss's kappa (stasmodels.stats.inter_rater): "+str(ir.fleiss_kappa(kappa.y_count)))
   print("Fleiss's kappa (mtbp3.statlab): "+str(kappa.fleiss_kappa))
   print("Number of raters per sample: "+str(kappa.n_rater))
   print("Number of rating categories: "+str(kappa.n_category))
   print("Number of sample: "+str(kappa.y_count.shape[0]))

Output:

.. testoutput::

   Fleiss's kappa (stasmodels.stats.inter_rater): -0.14989733059548255
   Fleiss's kappa (mtbp3.statlab): -0.14989733059548255
   Number of raters per sample: 4.0
   Number of rating categories: 3
   Number of sample: 100

*************
Lab Exercise
*************

1. Find Bootstrap CI of Fleiss's kappa. (see the function of Cohen's kappa CI)

*************
More Details
*************

:eq:`eq_obs1` corresponds to the observed 
probability of having agreement for a sample from two randomly selected raters estimated from :numref:`Tabel %s <tbl_count1>`.
:eq:`eq_exp1` corresponds to the expected 
probability of having agreement for a sample from two randomly selected raters under the assumption of no agreement, 
which corresponds to the assumption of :math:`(N_{i1},\ldots, N_{iJ}) \sim multi(n, (p_1,\ldots, p_J))`.
Note that the notations in this page did not use conventional 'hat' to represent estimated :math:`p_j`.

The equation :eq:`eq_kappa1` can be expressed as [2]_ :sup:`(Eq. 9)`,

.. math::

  \kappa = \frac{\sum_{i=1}^{n}\sum_{j=1}^J N_{ij}^2 - nR\left(1+(R-1)\sum_{j=1}^J p_j^2\right)}{nR(R-1)(1-\sum_{j=1}^J p_j^2)}


Note that Fleiss (1971) assumed large :math:`n` and fixed :math:`p_j` while deriving variance of kappa.
Please see the Fleiss (1971) for more discussions.
The variance of :math:`\kappa` under the assumption of no agreement beyond chance can be approximated as:

.. math::

  var(\kappa) = c(n,R,\{p_j\}) var\left(\sum_{j=1}^J N_{1j}^2 \right),

where

.. math::

  c(n,R,\{p_j\}) = n^{-1}\left(R(R-1)\left(1-\sum_{j=1}^J p_j^2\right)\right)^{-2},

and 

.. math::
  :label: eq_kappa2_vn2

  var\left(\sum_{j} N_{ij}^2 \right) 
  =& E\left( \left(\sum_{j} N_{ij}^2\right)^2\right) - \left(E\left(\sum_{j} N_{ij}^2\right)\right)^2 \\
  =& E\left(\sum_{j} N_{ij}^4\right) + E\left(\sum_j\sum_{k \neq j} N_{ij}^2 N_{ik}^2 \right) - \left(E\left(\sum_{j} N_{ij}^2\right)\right)^2.


:eq:`eq_kappa2_vn2` can be calculated as [2]_ :sup:`(Eq. 15)`

.. math::

  var\left(\sum_{j} N_{ij}^2 \right) 
  =& 2R(R-1)\left(\sum_j p_j^2 - (2R-3)\left(\sum_j p_j^2\right)^2 + 2(R-2)\sum_j p_j^3\right),

*************
Lab Exercise
*************

2. Find :math:`Cov(N_{i1},N_{i2})` under no agreement assumption.

*************
Reference
*************

.. [1] Wikipedia. (year). Fleiss's kappa. https://en.wikipedia.org/wiki/Fleiss%27_kappa 
.. [2] Fleiss, J. L. (1971). Measuring nominal scale agreement among many raters. Psychological Bulletin, 76(5), 378-382. https://doi.org/10.1037/h0031619

