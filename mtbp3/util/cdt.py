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

import pandas as pd

def diff_two_columns(df, col1='ARM', col2='ACTARM'):
    """
    Calculate the difference between two columns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the columns to compare.
        col1 (str): The name of the first column to compare. Default is 'ARM'.
        col2 (str): The name of the second column to compare. Default is 'ACTARM'.

    Returns:
        pandas.DataFrame or str: If there is a difference between the two columns, 
        a DataFrame is returned with the unique combinations of values in col1 and col2,
        along with a 'diff' column indicating whether the values are different ('True') or not ('').
        If there is no difference between the two columns, the string "The two columns are the same." is returned.
    """

    if not col1 or not col2:
        return "Both col1 and col2 must be provided."
    if not isinstance(df, pd.DataFrame):
        return "Input is not a DataFrame."
    if col1 not in df.columns:
        return f"Column '{col1}' does not exist in the DataFrame."
    if col2 not in df.columns:
        return f"Column '{col2}' does not exist in the DataFrame."
    if col1 == col2:
        return f"Columns should be different."
    
    diff = df[col1].ne(df[col2]).any()
    if diff:
        out = df.groupby([col1, col2]).size().reset_index()
        out['diff'] = (out[col1] != out[col2]).map(lambda x: "" if x==False else "True")
        return out
    else:
        return "The two columns are the same."
        
