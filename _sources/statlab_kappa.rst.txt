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

