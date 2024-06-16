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
:red:`This page is provided only for study purposes. The author does not intend to promote or advocate any particular analysis method or software.`

*************
Background
*************

Fleiss's kappa (:math:`\kappa`) is a statistic used for describing inter-ratter reliability of multiple independent ratters 
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
     - :math:`\vdots`
     - :math:`\ddots` 
     - :math:`\vdots` 
   * - **Sample:** :math:`n`
     - :math:`N_{N1}`
     - :math:`N_{N2}` 
     - :math:`\ldots` 
     - :math:`N_{NJ}` 
     - :math:`R` 
   * - **Column total**
     - :math:`N_{\bullet 1}`
     - :math:`N_{\bullet 2}` 
     - :math:`\ldots` 
     - :math:`N_{\bullet J}` 
     - :math:`nR` 
   * - **Ratio to ** :math:`nR`
     - :math:`p_1 = \frac{N_{\bullet 1}}{nR}`
     - :math:`p_2 = \frac{N_{\bullet 2}}{nR}` 
     - :math:`\ldots` 
     - :math:`p_J = \frac{N_{\bullet J}}{nR}` 
     - :math:`1` 

The observed averaged agreement is calculated as 

.. math::

  \bar{p}_O = \frac{1}{n} \sum_{i=1}^N p_{O,i},

where :math:`p_{O,i} = \frac{1}{R(R-1)} \left(\sum_{j=1}^J N_{ij}(N_{ij}-1)\right)= \frac{1}{R(R-1)} \left(\sum_{j=1}^J N_{ij}^2 - R\right)`.

The expected agreement category :math:`j` is calculated as 

.. math::

  \bar{p}_E = \sum_{j=1}^J p_{E,j}^2,

where :math:`p_{E,j} = \frac{N_{\bullet j}}{nR}`

The Fleiss's :math:`\kappa` statistic is calculated as

.. math::
  \kappa = \frac{\bar{p}_O - \bar{p}_E}{1-\bar{p}_E}.

*************
Example 
*************

TBA

*************
How-to 
*************

TBA

*************
Reference
*************

.. [1] Wikipedia. (year). Fleiss's kappa. https://en.wikipedia.org/wiki/Fleiss%27_kappa 
.. [2] Fleiss, J. L. (1971). Measuring nominal scale agreement among many raters. Psychological Bulletin, 76(5), 378-382. https://doi.org/10.1037/h0031619