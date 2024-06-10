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
   

.. raw:: html

    <style> .red-b {color:#aa0060; font-weight:bold} .red {color:#aa0060} </style>

.. role:: red-b
.. role:: red

#############
StatLab/Cohen's Kappa 
#############

:red-b:`Disclaimer:`
:red:` This page is for study purpose. The author does not intend to promote or advocate any particular method or software.`

*************
Background
*************

Cohen's kappa (:math:`\kappa`) is a statistic used for describing inter-ratter reliability of two ratters (or intra-rater) with categorical rating outcomes [1]_. 
Please note that there are also concerns of the use of :math:`\kappa` for quantifying agreement [2]_ [3]_ [4]_.

Fleiss' kappa is also a statistic used for inter-ratter reliability and that can be applied to cases with more then two ratters.
Fleiss' kappa is not yet being included in the ``statlab`` module.

*************
Notation 
*************

For two ratters and two categories rating, let :math:`Y_{r,i} \in \{A,B\}` represent rate
for rater :math:`r=1,2` and sample index :math:`i = 1, \ldots, n`.

.. list-table:: Counts for 2 categories
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: A
     - Ratter 2: B
     - Row Total
   * - **Ratter 1: A** 
     - :math:`N_{11}`
     - :math:`N_{12}` 
     - :math:`N_{1\bullet}` 
   * - **Ratter 1: B** 
     - :math:`N_{21}`
     - :math:`N_{22}` 
     - :math:`N_{2\bullet}` 
   * - **Column total**
     - :math:`N_{\bullet 1}`
     - :math:`N_{\bullet 2}` 
     - :math:`N_{\bullet\bullet}` 

For two ratters and three or more categories rating, let :math:`Y_{r,i} \in \{A,B,C, \ldots \}` represent rate 
for rater :math:`r=1,2` and sample index :math:`i = 1, \ldots, n`.

.. list-table:: Counts for 3 or more categories
   :widths: 10 10 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: A
     - Ratter 2: B
     - Ratter 2: C
     - :math:`\ldots` 
     - Row Total
   * - **Ratter 1: A**
     - :math:`N_{11}`
     - :math:`N_{12}` 
     - :math:`N_{13}` 
     - :math:`\ldots` 
     - :math:`N_{1\bullet}` 
   * - **Ratter 1: B**
     - :math:`N_{21}`
     - :math:`N_{22}` 
     - :math:`N_{23}` 
     - :math:`\ldots` 
     - :math:`N_{2\bullet}` 
   * - **Ratter 1: C**
     - :math:`N_{31}`
     - :math:`N_{32}` 
     - :math:`N_{33}` 
     - :math:`\ldots` 
     - :math:`N_{3\bullet}` 
   * - :math:`\vdots` 
     - :math:`\vdots`
     - :math:`\vdots`
     - :math:`\vdots`
     - :math:`\ddots` 
     - :math:`\vdots` 
   * - **Column total**
     - :math:`N_{\bullet 1}`
     - :math:`N_{\bullet 2}` 
     - :math:`N_{\bullet 3}` 
     - :math:`\ldots` 
     - :math:`N_{\bullet\bullet}` 

The observed raw percentage of agreement is defined as 

.. math::

  p_O = \sum_{j=1}^J N_{jj} / N_{\bullet\bullet}

where :math:`J \geq 2` is the size of value set.

Assume that 

.. math::
  (N_{1\bullet}, \ldots N_{J\bullet}) \sim multi(N_{\bullet \bullet}, (p_{r=1,1}, \ldots, p_{r=1,J})), 

and

.. math::
  (N_{\bullet 1}, \ldots N_{\bullet J}) \sim multi(N_{\bullet \bullet}, (p_{r=2,1}, \ldots, p_{r=2,J})), 

with :math:`\sum_j N_{j \bullet} = \sum_j N_{\bullet j} = N_{\bullet \bullet}` 
and :math:`\sum_j p_{r=1,j} = \sum_j p_{r=2, j} = 1`.

Under independence assumption, the expected number of agreement is estimated by
:math:`\sum_{j=1}^J\hat{E}_{j} = \frac{1}{N_{\bullet \bullet}}\sum_{j=1}^J N_{\bullet j} N_{j\bullet} \equiv N_{\bullet \bullet}p_E`.

The Cohen's :math:`\kappa` statistic is calculated as

.. math::
  \kappa = \frac{p_O - p_E}{1-p_E}.

The SE of :math:`\kappa` is calculated as

.. math::
  \sqrt{\frac{p_O(1-p_O)}{N_{\bullet \bullet}(1-p_E)^2}}.

*************
Interpretation of Cohen's Kappa Suggested in Literature
*************

Cohen (1960) [5]_ suggested the Kappa result be interpreted as follows: 

.. list-table:: Cohen's Kappa Interpretation (Cohen, 1960)
   :widths: 10 10 
   :header-rows: 1

   * - Value of :math:`\kappa`
     - Interpretation
   * - :math:`-1 \leq \kappa \leq 0`
     - indicating no agreement
   * - :math:`0 < \kappa \leq 0.2`
     - none to slight
   * - :math:`0.2 < \kappa \leq 0.4`
     - fair
   * - :math:`0.4 < \kappa \leq 0.6`
     - moderate
   * - :math:`0.6 < \kappa \leq 0.8` 
     - substantial
   * - :math:`0.8 < \kappa \leq 1`
     - almost perfect agreement 

Interpretation suggested by McHugh (2012) [6]_:

.. list-table:: Cohen's Kappa Interpretation (McHugh, 2012)
   :widths: 10 10 10
   :header-rows: 1

   * - Value of :math:`\kappa`
     - Level of Agreement
     - % of Data That Are Reliable
   * - :math:`-1 \leq \kappa \leq 0`
     - Disagreement
     - NA
   * - :math:`0-.20`
     - None
     - :math:`0-4%`
   * - :math:`.21-.39`
     - Minimal
     - :math:`4-15%`
   * - :math:`.40-.59`
     - Weak
     - :math:`15-35%`
   * - :math:`.60-.79`
     - Moderate
     - :math:`35-63%`
   * - :math:`.80-.90`
     - Strong
     - :math:`64-81%`
   * - Above.90
     - Almost Perfect
     - :math:`82-100%`

*************
Example - Group-1
*************

.. list-table:: Cohen's :math:`\kappa = 0`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: A
     - Ratter 2: B
     - Row Total
   * - **Ratter 1: A**
     - 9
     - 21
     - 30
   * - **Ratter 1: B** 
     - 21
     - 49
     - 70
   * - **Column total**
     - 30
     - 70
     - 100

.. list-table:: Cohen's :math:`\kappa = 0`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: A
     - Ratter 2: B
     - Row Total
   * - **Ratter 1: A**
     - 49
     - 21
     - 70
   * - **Ratter 1: B**
     - 21
     - 9
     - 30
   * - **Column total**
     - 70
     - 30
     - 100

.. list-table:: Cohen's :math:`\kappa = 1`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: A
     - Ratter 2: B
     - Row Total
   * - **Ratter 1: A**
     - 30
     - 0
     - 30
   * - **Ratter 1: B**
     - 0
     - 70
     - 70
   * - **Column total**
     - 30
     - 70
     - 100

.. list-table:: Cohen's :math:`\kappa = 1`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: A
     - Ratter 2: B
     - Row Total
   * - **Ratter 1: A**
     - 50
     - 0
     - 50
   * - **Ratter 1: B**
     - 0
     - 50
     - 50
   * - **Column total**
     - 50
     - 50
     - 100

.. list-table:: Cohen's :math:`\kappa = -1`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: A
     - Ratter 2: B
     - Row Total
   * - **Ratter 1: A** 
     - 0
     - 50
     - 50
   * - **Ratter 1: B**
     - 50
     - 0
     - 50
   * - **Column total**
     - 50
     - 50
     - 100

.. list-table:: Cohen's :math:`\kappa = -0.7241379310344827`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: A
     - Ratter 2: B
     - Row Total
   * - **Ratter 1: A**
     - 0
     - 30
     - 30
   * - **Ratter 1: B**
     - 70
     - 0
     - 70
   * - **Column total**
     - 70
     - 30
     - 100


*************
How-to 
*************

To use ``sklearn.metrics`` (stable):

.. code:: python

   from sklearn.metrics import cohen_kappa_score
   r1 = ['B'] * 70 + ['A'] * 30
   r2 = ['A'] * 70 + ['B'] * 30
   print("Cohen's kappa:", cohen_kappa_score(r1, r2))

To use ``mtbp3.statlab`` (testing):

.. code:: python

   from mtbp3.statlab import kappa
   r1 = ['B'] * 70 + ['A'] * 30
   r2 = ['A'] * 70 + ['B'] * 30
   kappa = kappa.KappaCalculator([r1,r2])
   print("Cohen's kappa:", kappa.cohen_kappa)

=============
Bootstrap CI
=============

To use ``mtbp3.statlab``:

.. testsetup:: *

   from mtbp3.statlab import kappa
   r1 = ['B'] * 70 + ['A'] * 30
   r2 = ['A'] * 70 + ['B'] * 30
   kappa = kappa.KappaCalculator(r1,r2)

.. testcode::

   print( kappa.bootstrap_cohen_ci(n_iterations=1000, confidence_level=0.95) )

Output:

.. testoutput::

   Cohen's kappa: -0.724
   Confidence Interval (95.0%): [-0.144, 0.135]




*************
Reference
*************

.. [1] Wikipedia. (year). Cohen's kappa. https://en.wikipedia.org/wiki/Cohen%27s_kappa.
.. [2] Uebersax, J. (year). Kappa Coefficients: A Critical Appraisal. https://www.john-uebersax.com/stat/kappa.htm#procon.
.. [3] Brennan, R. L., & Prediger, D. J. (1981). Coefficient Kappa: Some Uses, Misuses, and Alternatives. Educational and Psychological Measurement, 41(3), 687-699. https://doi.org/10.1177/0013164481041003070
.. [4] Sim, J., Wright, C. C. (2005). The Kappa Statistic in Reliability Studies: Use, Interpretation, and Sample Size Requirements, Physical Therapy, Volume 85, Issue 3, Pages 257-268, https://doi.org/10.1093/ptj/85.3.257
.. [5] Cohen, J. (1960). A Coefficient of Agreement for Nominal Scales. Educational and Psychological Measurement, 20(1), 37-46. https://doi.org/10.1177/001316446002000104 
.. [6] McHugh M. L. (2012). Interrater reliability: the kappa statistic. Biochemia medica, 22(3), 276-282. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3900052/