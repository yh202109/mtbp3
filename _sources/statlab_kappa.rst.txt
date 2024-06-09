#############
StatLab/Cohen's Kappa for inter-rater reliability
#############

*************
Background
*************

Cohen's kappa is a statistic used for describing, summarizing, estimating and testing inter-ratter consistency. 


*************
Notation
*************

For two categories rating, assume :math:`Y_{r,i} \in \{A,B\}` for rater :math:`r=1,2` and sample index :math:`i = 1, \ldots, n`.

.. list-table:: Counts for 2 categories
   :widths: 10 10 10 10
   :header-rows: 1

   * - 
     - R2: A
     - R2: B
     - Row Total
   * - R1: A 
     - :math:`N_{11}`
     - :math:`N_{12}` 
     - :math:`N_{1\bullet}` 
   * - R1: B 
     - :math:`N_{21}`
     - :math:`N_{22}` 
     - :math:`N_{2\bullet}` 
   * - Column total
     - :math:`N_{\bullet 1}`
     - :math:`N_{\bullet 2}` 
     - :math:`N_{\bullet\bullet}` 


For three or more categories rating, assume :math:`Y_{r,i} \in \{A,B,C, \ldots \}` 
for rater :math:`r=1,2` and sample index :math:`i = 1, \ldots, n`.

.. list-table:: Counts for 3 or more categories
   :widths: 10 10 10 10 10 10
   :header-rows: 1

   * - 
     - R2: A
     - R2: B
     - R2: C
     - :math:`\ldots` 
     - Row Total
   * - R1: A 
     - :math:`N_{11}`
     - :math:`N_{12}` 
     - :math:`N_{13}` 
     - :math:`\ldots` 
     - :math:`N_{1\bullet}` 
   * - R1: B 
     - :math:`N_{21}`
     - :math:`N_{22}` 
     - :math:`N_{23}` 
     - :math:`\ldots` 
     - :math:`N_{2\bullet}` 
   * - R1: C 
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
   * - Column total
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

with :math:`\sum N_{j \bullet} = \sum N_{\bullet j} = N_{\bullet \bullet}` 
and :math:`\sum p_{r=1,j} = \sum p_{r=2, j} = 1`.

Under independence assumption, the expected number of agreement is estimated by
:math:`\sum_{j=1}^J\hat{E}_{j} = \frac{1}{N_{\bullet \bullet}}\sum_{j=1}^J N_{\bullet j} N_{j\bullet} \equiv N_{\bullet \bullet}p_E`.

The :math:`\kappa` statistic is calculated as

.. math::
  \kappa = \frac{p_O - p_E}{1-p_E}.

The SE of :math:`\kappa` is calculated as

.. math::
  \sqrt{\frac{p_O(1-p_O)}{N_{\bullet \bullet}(1-p_E)^2}}.



