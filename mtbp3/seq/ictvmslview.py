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

import pandas as pd
import os
from mtbp3 import util
import warnings
import requests

warnings.simplefilter(action='ignore', category=FutureWarning)
    
class ictvmsl:
    """
    A class to handle ICTV Master Species List (MSL) data.
    Attributes:
    -----------
    msl_file_path : str
        Path to the MSL file.
    msl_file_fullpath : str
        Full path to the MSL file.
    msl_version : str
        Version of the MSL.
    msl_column_names : list
        List of column names in the MSL.
    msl : DataFrame
        The MSL data loaded into a pandas DataFrame.
    Methods:
    --------
    update_msl(self, version="current")
        Updates the MSL data by downloading the specified version from the ICTV website.
    make_narrow(msl)
        Converts the MSL DataFrame to a narrower format by combining certain columns.
    find_rows_given_str(self, search_str="", search_rank="Species", color="", narrow=False, outfmt="simple", exact=False, search_within_subset=None)
        Finds rows in the MSL DataFrame that contain the given search string.
    """

    def __init__(self, msl_file_path = ""):
        if not isinstance(msl_file_path, str):
            raise TypeError("msl_file_path must be a string")

        if msl_file_path:
            self.msl_file_path = msl_file_path
            self.msl_file_fullpath = msl_file_path
        else:
            self.msl_file_path = f'supp_seq/ICTV_MSL39v4_example.csv'
            self.msl_file_fullpath = util.get_data(self.msl_file_path)

        self.msl_version = ""
        self.msl_column_names = []
        self.msl = self.__load_list()

        if self.msl is not None:
            self.msl_column_names = self.msl.columns.tolist()
            print(f"File {self.msl_file_path} has been loaded")
            print("Column names:", self.msl_column_names)
            print("Total number of rows:", len(self.msl))

    def update_msl(self, version="current"):
        all_url = {
            "current": "https://ictv.global/msl/current",
            "39.v4": "https://ictv.global/sites/default/files/MSL/ICTV_Master_Species_List_2023_MSL39.v4.xlsx",
            "39.v3": "https://ictv.global/sites/default/files/MSL/ICTV_Master_Species_List_2023_MSL39.v3.xlsx"
        }
        if version in all_url:
            url = all_url[version]
        else:
            raise ValueError(f"Version {version} is not supported. Supported versions are: {', '.join(all_url.keys())}")

        response = requests.get(url)
        if response.status_code == 200:
            with open("temp.xlsx", "wb") as f:
                f.write(response.content)
            self.msl = pd.read_excel("temp.xlsx", sheet_name="MSL")
            os.remove("temp.xlsx")
            self.msl_column_names = self.msl.columns.tolist()
            print(f"File of version {version} has been loaded")
            print("Column names:", self.msl_column_names)
            print("Total number of rows:", len(self.msl))
        else:
            raise Exception(f"Failed to download file from {url}. Status code: {response.status_code}")


    @staticmethod
    def make_narrow(msl, method="concatenation"):
        if method == "full":
            msl = msl.iloc[:, :-4]
            return msl
        elif method == "concatenation":
            for col in msl.columns:
                if col.lower().startswith('sub') and not msl[col].isna().all():
                    index1 = msl.columns.get_loc(col[3:].capitalize())
                    index2 = msl.columns.get_loc(col)
                    msl.iloc[:, index1] = msl.apply(lambda row: f"{row[index1]}; [{col}] {row[index2]}" if pd.notna(row[index2]) else row[index1], axis=1)
            msl = msl.iloc[:, :-4]
            msl = msl.drop(columns=[col for col in msl.columns if col.lower().startswith('sub')])
        elif method == "drop":
            for col in msl.columns:
                if col.lower().startswith('sub') and msl[col].isna().all():
                    msl = msl.drop(columns=[col])
            msl = msl.iloc[:, :-4]
        else: 
            raise ValueError("Unknown method. Supported methods are 'concatenation' and 'drop'")

        return msl

    def __load_list(self):
        #file_path = f'./mtbp3/data/supp_seq/ICTV_MSL39v4_example.csv'
        file_path = self.msl_file_fullpath
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            return df
        else:
            raise FileNotFoundError(f"File not found: {file_path}")

    def find_rows_given_str(self, search_strings=None, search_rank="Species", color="", narrow=False, outfmt="simple", exact=False, search_within_subset=None, tree_style="concatenation"):
        """
        Find rows in the MSL dataframe that match a given search string.
        Parameters:
        search_str (str): The string to search for. Must be a nonempty string.
        search_rank (str): The rank to search within (e.g., "Species"). Must be 'all' or one of the column names in the MSL dataframe.
        color (str): The color to highlight the search string in the results.
        narrow (bool): Whether to narrow the results to a specific format.
        outfmt (str): The output format. Must be 'simple' or 'tree'.
        exact (bool): Whether to search for an exact match.
        search_within_subset (dict): A dictionary specifying a subset of the MSL dataframe to search within.
        Returns:
        pandas.DataFrame or str: The filtered dataframe if outfmt is 'simple', or a tree representation of the results if outfmt is 'tree'.
        Raises:
        TypeError: If search_str is not a string or if search_within_subset is not a dictionary or None.
        ValueError: If search_str is empty, if search_rank is invalid, or if outfmt is invalid.
        """

        if not (isinstance(search_strings, list) or isinstance(search_strings, str)):
            raise TypeError("search_strings must be a list or a string")
        if not search_strings:
            raise ValueError("search_strings must be a nonempty list or a nonempty string")
        if isinstance(search_strings, str):
            search_strings = [search_strings]
        if search_rank and search_rank != "all" and search_rank not in self.msl_column_names:
            raise ValueError(f"search_rank must be 'all' or one of the following: {', '.join(self.msl_column_names)}")
        if outfmt not in ["simple", "tree"]:
            raise ValueError("outfmt must be 'simple' or 'tree'")
        if search_within_subset is not None and not isinstance(search_within_subset, dict):
            raise TypeError("search_subset must be a dictionary or None")

        msl2 = self.msl
        if search_within_subset is not None:
            for key, value in search_within_subset.items():
                if key in msl2.columns and isinstance(value, str) and value:
                    index = msl2.columns.get_loc(key)
                    msl2 = msl2[msl2.iloc[:, index].str.lower() == value.lower()]

        if search_rank == "all":
            if exact:
                filtered_df = msl2[msl2.iloc[:, 1:16].apply(lambda row: any(search_str.lower() == element.lower() for element in row.astype(str).values for search_str in search_strings), axis=1)]
            else:
                filtered_df = msl2[msl2.iloc[:, 1:16].apply(lambda row: any(search_str.lower() in element.lower() for element in row.astype(str).values for search_str in search_strings), axis=1)]
            if color:
                for col in filtered_df[1:16]:
                    filtered_df[col] = filtered_df[col].apply(lambda row: util.cdt.color_str(row, words=search_strings, colors=color, exact=exact) if pd.notna(row) else row)
        else:
            if exact:
                filtered_df = msl2[msl2[search_rank].apply(lambda x: any(search_str.lower() == x.lower() for search_str in search_strings) if pd.notna(x) else False)]
            else:
                filtered_df = msl2[msl2[search_rank].apply(lambda x: any(search_str.lower() in x.lower() for search_str in search_strings) if pd.notna(x) else False)]
            if color:
                index = msl2.columns.get_loc(search_rank)
                filtered_df.iloc[:, index] = filtered_df.iloc[:, index].apply(lambda row: util.cdt.color_str(row, words=search_strings, colors=color, exact=exact))


        if outfmt == "simple":
            if narrow:
                filtered_df = self.make_narrow(filtered_df, method="drop")
            return filtered_df
        elif outfmt == "tree":
            filtered_df = self.make_narrow(filtered_df, method=tree_style)
            filtered_df = filtered_df.fillna("NA")
            filtered_df = filtered_df.iloc[:, 1:-1]
            for col in filtered_df.columns:
                filtered_df[col] = filtered_df[col].apply(lambda x: f"[{col}] {x}" if pd.notna(x) else x)
            tree_list = []

            for i in range(len(filtered_df.columns)):
                tmp = filtered_df.iloc[:, :i].drop_duplicates()
                tmp['concat'] = tmp.apply(lambda row: "/" + "/".join(row.astype(str)) + "/", axis=1)
                tree_list += tmp['concat'].unique().tolist()
            filtered_df['concat'] = filtered_df.apply(lambda row: "/" + "/".join(row.astype(str)), axis=1)
            tree_list += filtered_df['concat'].unique().tolist()
            tree_list = tree_list[1:]
            tree_list = sorted(tree_list)

            out_tree = util.cdt.ListTree(lst=tree_list)
            return out_tree.list_tree()
        else:
            return

if __name__ == "__main__":
    pass
