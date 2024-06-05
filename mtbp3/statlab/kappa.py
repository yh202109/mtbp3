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


        observed = [[x, y] for x, y in zip(y1, y2)]

        y1_observed = [x[0] for x in observed]
        y2_observed = [x[1] for x in observed]

        kappa = cohen_kappa_score(y1_observed, y2_observed)


        from sklearn.metrics import cohen_kappa_score

    import numpy as np
    from sklearn.utils import resample

    # Bootstrap resampling
    n_iterations = 1000
    kappa_values = []
    for _ in range(n_iterations):
        # Perform bootstrap resampling
        r1_resampled = resample(r1)
        r2_resampled = resample(r2)
        
        # Calculate kappa for resampled data
        kappa = cohen_kappa_score(r1_resampled, r2_resampled)
        kappa_values.append(kappa)

    # Calculate confidence interval
    confidence_level = 0.95
    lower_percentile = (1 - confidence_level) / 2
    upper_percentile = 1 - lower_percentile
    lower_bound = np.percentile(kappa_values, lower_percentile * 100)
    upper_bound = np.percentile(kappa_values, upper_percentile * 100)

    print("Cohen's kappa:", cohen_kappa_score(r1, r2))
    print("Confidence Interval ({}%): [{}, {}]".format(confidence_level * 100, lower_bound, upper_bound))k
    return kappa