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

.. role:: bg-ltsteelblue



#############
StatLab/Cohen's Kappa 
#############

:red-b:`Disclaimer:`
:red:`This page is provided only for studying and practicing. The author does not intend to promote or advocate any particular analysis method or software.`

*************
Background
*************

Cohen's kappa (:math:`\kappa`) is a statistic used for describing inter-ratter reliability of two ratters (or intra-rater) with categorical rating outcomes [1]_. 
Please note that there are also additional considerations for the use of :math:`\kappa` for quantifying agreement [2]_ [3]_ .

*************
Notation 
*************

For two ratters and two categories rating, let :math:`Y_{r,i} \in \{v_j; j=1,2\}` represent rating
from rater :math:`r=1,2` for sample :math:`i = 1, \ldots, n`.
Let :math:`N_{j_1,j_2}` represent the total number of sample received ratings :math:`(v_{j_1}, v_{j_2})` from two raters, where :math:`j_1,j_2 \in \{1,2\}`.

.. list-table:: Counts for 2 categories
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: :math:`v_1`
     - Ratter 2: :math:`v_2`
     - Row Total
   * - **Ratter 1:** :math:`v_1`
     - :math:`N_{11}`
     - :math:`N_{12}` 
     - :math:`N_{1\bullet}` 
   * - **Ratter 1:**  :math:`v_2`
     - :math:`N_{21}`
     - :math:`N_{22}` 
     - :math:`N_{2\bullet}` 
   * - **Column Total**
     - :math:`N_{\bullet 1}`
     - :math:`N_{\bullet 2}` 
     - :math:`n`

For two ratters and three or more categories rating, let :math:`Y_{r,i} \in \{v_1,v_2,v_3, \ldots, v_J \}` represent rating 
from rater :math:`r=1,2` for sample :math:`i = 1, \ldots, n`.
Let :math:`N_{j_1,j_2}` represent the total number of sample received ratings :math:`(v_{j_1}, v_{j_2})` from two raters, where :math:`j_1,j_2 \in \{1,\ldots,J\}`.

.. list-table:: Counts for 3 or more categories
   :widths: 10 10 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: :math:`v_1`
     - Ratter 2: :math:`v_2`
     - Ratter 2: :math:`v_3`
     - :math:`\ldots` 
     - Row Total
   * - **Ratter 1:** :math:`v_1`
     - :math:`N_{11}`
     - :math:`N_{12}` 
     - :math:`N_{13}` 
     - :math:`\ldots` 
     - :math:`N_{1\bullet}` 
   * - **Ratter 1:** :math:`v_2`
     - :math:`N_{21}`
     - :math:`N_{22}` 
     - :math:`N_{23}` 
     - :math:`\ldots` 
     - :math:`N_{2\bullet}` 
   * - **Ratter 1:** :math:`v_3`
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
   * - **Column Total**
     - :math:`N_{\bullet 1}`
     - :math:`N_{\bullet 2}` 
     - :math:`N_{\bullet 3}` 
     - :math:`\ldots` 
     - :math:`n` 

The observed raw percentage of agreement is defined as 

.. math::

  p_O = \sum_{j=1}^J N_{jj} / n

where :math:`J \geq 2` is the size of value set.

Assume that 

.. math::
  (N_{1\bullet}, \ldots N_{J\bullet}) \sim multi(n, (p_{r=1,1}, \ldots, p_{r=1,J})), 

and

.. math::
  (N_{\bullet 1}, \ldots N_{\bullet J}) \sim multi(n, (p_{r=2,1}, \ldots, p_{r=2,J})), 

with :math:`\sum_j N_{j \bullet} = \sum_j N_{\bullet j} = n` 
and :math:`\sum_j p_{r=1,j} = \sum_j p_{r=2, j} = 1`.

Under independence assumption, the expected number of agreement is estimated by
:math:`\sum_{j=1}^J\hat{E}_{j} = \frac{1}{n}\sum_{j=1}^J N_{\bullet j} N_{j\bullet} \equiv n p_E`.

The Cohen's :math:`\kappa` statistic is calculated as

.. math::
  \kappa = \frac{p_O - p_E}{1-p_E}.

The SE of :math:`\kappa` is calculated as

.. math::
  \sqrt{\frac{p_O(1-p_O)}{n(1-p_E)^2}}.

*************
Interpretation of Cohen's Kappa Suggested in Literature
*************


Cohen (1960) [4]_ suggested the Kappa result be interpreted as follows: 

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

Interpretation suggested by McHugh (2012) [5]_:

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

As discussed by Sim and Wright [6]_ , biases and other factors could have impact on the interpretation.

*************
Example - Group-1
*************

.. list-table:: Cohen's :math:`\kappa = 0`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: :math:`v_1`
     - Ratter 2: :math:`v_2`
     - Row Total
   * - **Ratter 1:** :math:`v_1`
     - 9
     - 21
     - 30
   * - **Ratter 1:** :math:`v_2`
     - 21
     - 49
     - 70
   * - **Column Total**
     - 30
     - 70
     - 100

.. list-table:: Cohen's :math:`\kappa = 0`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: :math:`v_1`
     - Ratter 2: :math:`v_2`
     - Row Total
   * - **Ratter 1:** :math:`v_1`
     - 49
     - 21
     - 70
   * - **Ratter 1:** :math:`v_2`
     - 21
     - 9
     - 30
   * - **Column Total**
     - 70
     - 30
     - 100

.. list-table:: Cohen's :math:`\kappa = 1`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: :math:`v_1`
     - Ratter 2: :math:`v_2`
     - Row Total
   * - **Ratter 1:** :math:`v_1`
     - 30
     - 0
     - 30
   * - **Ratter 1:** :math:`v_2`
     - 0
     - 70
     - 70
   * - **Column Total**
     - 30
     - 70
     - 100

.. list-table:: Cohen's :math:`\kappa = 1`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: :math:`v_1`
     - Ratter 2: :math:`v_2`
     - Row Total
   * - **Ratter 1** :math:`v_1`
     - 50
     - 0
     - 50
   * - **Ratter 1:** :math:`v_2`
     - 0
     - 50
     - 50
   * - **Column Total**
     - 50
     - 50
     - 100

.. list-table:: Cohen's :math:`\kappa = -1`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: :math:`v_1` 
     - Ratter 2: :math:`v_2`
     - Row Total
   * - **Ratter 1:** :math:`v_1`
     - 0
     - 50
     - 50
   * - **Ratter 1:** :math:`v_2`
     - 50
     - 0
     - 50
   * - **Column Total**
     - 50
     - 50
     - 100

.. list-table:: Cohen's :math:`\kappa = -0.7241379310344827`
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - Ratter 2: :math:`v_1`
     - Ratter 2: :math:`v_2`
     - Row Total
   * - **Ratter 1:** :math:`v_1`
     - 0
     - 30
     - 30
   * - **Ratter 1:** :math:`v_2`
     - 70
     - 0
     - 70
   * - **Column Total**
     - 70
     - 30
     - 100


*************
How-to 
*************

To use ``sklearn.metrics`` (stable):

.. code:: python

   from sklearn.metrics import cohen_kappa_score
   y1 = ['v2'] * 70 + ['v1'] * 30
   y2 = ['v1'] * 70 + ['v2'] * 30
   print("Cohen's kappa:", cohen_kappa_score(y1, y2))

To use ``mtbp3.statlab`` (testing):

.. code:: python

   from mtbp3.statlab import kappa
   y1 = ['v2'] * 70 + ['v1'] * 30
   y2 = ['v1'] * 70 + ['v2'] * 30
   kappa = kappa.KappaCalculator([y1,y2])
   print("Cohen's kappa:", kappa.cohen_kappa)

=============
Bootstrap CI
=============

To use ``mtbp3.statlab``:

.. testsetup:: *

   from mtbp3.statlab import kappa
   y1 = ['v2'] * 70 + ['v1'] * 30
   y2 = ['v1'] * 70 + ['v2'] * 30
   kappa = kappa.KappaCalculator(y1,y2)

.. testcode::

   print( kappa.bootstrap_cohen_ci(n_iterations=1000, confidence_level=0.95, out_digits=6) )

Output:

.. testoutput::

   Cohen's kappa: -0.724138
   Confidence Interval (95.0%): [-0.907669, -0.496558]


Note that examples of using ``SAS/PROC FREQ`` and ``R`` package ``vcd`` for calculating :math:`\kappa` can be found in reference [7]_ .

=============
Bubble Plot
=============

To create a bubble plot using ``mtbp3.statlab``:

.. code:: python

   from mtbp3.statlab import kappa

    r1 = ['Apple'] * 10 + ['Orange'] * 50 + ['Pear'] * 40
    r2 = ['Apple'] * 20 + ['Pear'] * 60 + ['Orange'] * 20

    kappa = KappaCalculator([r1,r2], stringna='NA')

    print("Cohen's kappa (mtbp3.statlab): "+str(kappa.cohen_kappa))
    print("Number of raters per sample: "+str(kappa.n_rater))
    print("Number of rating categories: "+str(kappa.n_category))
    print("Number of sample: "+str(kappa.y_count.shape[0]))

    kappa.create_bubble_plot()

Output:

.. testoutput::

    Cohen's kappa (mtbp3.statlab): -0.09375
    Number of raters per sample: 2.0
    Number of rating categories: 3
    Number of sample: 100

.. figure:: /_static/fig/statlab_kappa_fig1.svg
    :scale: 70%
    :align: center
    :alt: bubble plot

To create a bubble plot within individual raters summary using ``mtbp3.statlab``:

.. code:: python

    kappa.create_bubble_plot(hist=True)

.. figure:: /_static/fig/statlab_kappa_fig2.svg
    :scale: 70%
    :align: center
    :alt: bubble plot with hist

*************
Extensions
*************

Some scenarios discussed by Hallgren (2012) [9]_ include:

- the **prevalence** problem: one category has much higher percentage than other categories and causes :math:`\kappa` to be low.
- the **bias** problem: there are substantial differences in marginal distributions and causes :math:`\kappa` tend to be high.
- unequal importance

(Please note that this is not an exhaustive list.)

*************
Weighted :math:`\kappa`
*************

Let :math:`w_{j_1,j_2}` represent the weight given to total number of sample received ratings :math:`(v_{j_1}, v_{j_2})` from two raters, where :math:`j_1,j_2 \in \{1,\ldots,J\}`.
The weighted :math:`\kappa` is calculated as

.. math::
  \kappa = 1- \frac{\sum_{j_1=1}^J\sum_{j_2=1}^J w_{j_1,j_2}N_{j_1,j_2}}{\sum_{j_1=1}^J\sum_{j_2=1}^J w_{j_1,j_2}\hat{E}_{j_1, j_2}}.

*************
Reference
*************

.. [1] Wikipedia. (year). Cohen's kappa. https://en.wikipedia.org/wiki/Cohen%27s_kappa.
.. [2] Uebersax, J. (year). Kappa Coefficients: A Critical Appraisal. https://www.john-uebersax.com/stat/kappa.htm#procon.
.. [3] Brennan, R. L., & Prediger, D. J. (1981). Coefficient Kappa: Some Uses, Misuses, and Alternatives. Educational and Psychological Measurement, 41(3), 687-699. https://doi.org/10.1177/0013164481041003070
.. [4] Cohen, J. (1960). A Coefficient of Agreement for Nominal Scales. Educational and Psychological Measurement, 20(1), 37-46. https://doi.org/10.1177/001316446002000104 
.. [5] McHugh M. L. (2012). Interrater reliability: the kappa statistic. Biochemia medica, 22(3), 276-282. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3900052/
.. [6] Sim, J., Wright, C. C. (2005). The Kappa Statistic in Reliability Studies: Use, Interpretation, and Sample Size Requirements, Physical Therapy, Volume 85, Issue 3, Pages 257-268, https://doi.org/10.1093/ptj/85.3.257
.. [7] PSU. STAT504: Measure of Agreement: Kappa. https://online.stat.psu.edu/stat504/lesson/11/11.2/11.2.4
.. [8] Basu, S., Banerjee, M., & Sen, A. (2000). Bayesian inference for kappa from single and multiple studies. Biometrics, 56(2), 577–582. https://doi.org/10.1111/j.0006-341x.2000.00577.x
.. [9] Hallgren K. A. (2012). Computing Inter-Rater Reliability for Observational Data: An Overview and Tutorial. Tutorials in quantitative methods for psychology, 8(1), 23–34. https://doi.org/10.20982/tqmp.08.1.p023
.. [10] Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. Biometrics, 33(1), 159–174.