#  Copyright (C) 2023 Y Hsu <yh202109@gmail.com>
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

import numpy as np

def calculate_kappa(y1, y2, remove_nan=False):
    assert len(y1) == len(y2), "y1 and y2 must have the same length"
    assert all(isinstance(x, (int, float)) for x in y1), "y1 must contain numerical values"
    assert all(isinstance(x, (int, float)) for x in y2), "y2 must contain numerical values"
    idx_nan = np.isnan(y1) | np.isnan(y2)
    total_nan = np.count_nonzero(idx_nan)
    if total_nan > 0:
        if remove_nan:
            print(f"Total number of incomplete paired observations is: {total_nan}")
            y1 = np.array(y1)[~idx_nan]
            y2 = np.array(y2)[~idx_nan]
        else:
            pass


    return kappa

