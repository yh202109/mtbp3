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
    
class ictvmsl:
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
        self.msl2 = pd.DataFrame()
        self.msl = self.__load_list()

        if self.msl is not None:
            self.msl_column_names = self.msl.columns.tolist()
            print(f"File {self.msl_file_path} has been loaded")
            print("Column names:", self.msl.columns.tolist())
            print("Total number of rows:", len(self.msl))

    @staticmethod
    def make_narrow(msl):
        if 'Realm' in msl.columns and 'Subrealm' in msl.columns:
            msl['Realm'] = msl.apply(lambda row: f"{row['Realm']}(Subrealm:{row['Subrealm']})" if pd.notna(row['Subrealm']) else row['Realm'], axis=1)
        if 'Kingdom' in msl.columns and 'Subkingdom' in msl.columns:
            msl['Kingdom'] = msl.apply(lambda row: f"{row['Kingdom']}(Subkingdom:{row['Subkingdom']})" if pd.notna(row['Subkingdom']) else row['Kingdom'], axis=1)
        if 'Phylum' in msl.columns and 'Subphylum' in msl.columns:
            msl['Phylum'] = msl.apply(lambda row: f"{row['Phylum']}(Subphylum:{row['Subphylum']})" if pd.notna(row['Subphylum']) else row['Phylum'], axis=1)
        if 'Class' in msl.columns and 'Subclass' in msl.columns:
            msl['Class'] = msl.apply(lambda row: f"{row['Class']}(Subclass:{row['Subclass']})" if pd.notna(row['Subclass']) else row['Class'], axis=1)
        if 'Order' in msl.columns and 'Suborder' in msl.columns:
            msl['Order'] = msl.apply(lambda row: f"{row['Order']}(Suborder:{row['Suborder']})" if pd.notna(row['Suborder']) else row['Order'], axis=1)
        if 'Family' in msl.columns and 'Subfamily' in msl.columns:
            msl['Family'] = msl.apply(lambda row: f"{row['Family']}(Subfamily:{row['Subfamily']})" if pd.notna(row['Subfamily']) else row['Family'], axis=1)
        if 'Genus' in msl.columns and 'Subgenus' in msl.columns:
            msl['Genus'] = msl.apply(lambda row: f"{row['Genus']}(Subgenus:{row['Subgenus']})" if pd.notna(row['Subgenus']) else row['Genus'], axis=1)
        msl = msl.iloc[:, :-4]
        msl2 = msl.drop(columns=[col for col in msl.columns if col.lower().startswith('sub')])
        return msl2

    def __load_list(self):
        #file_path = f'./mtbp3/data/supp_seq/ICTV_MSL39v4_example.csv'
        file_path = self.msl_file_fullpath
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            return df
        else:
            raise FileNotFoundError(f"File not found: {file_path}")

    def find_rows_given_str(self, search_str="", search_rank="Species", color="", narrow=False, outfmt="simple", exact=False):
        """
        Find rows in the DataFrame that contain the given search string.
        Parameters:
        search_str (str): The string to search for in the DataFrame. Must be a nonempty string.
        search_rank (str): The column name to search within. Must be 'all' or one of the column names in the DataFrame. Default is "Species".
        neighbor_rank (str): (Unused parameter, can be removed or implemented in future versions).
        Returns:
        DataFrame: A DataFrame containing rows that match the search criteria.
        Raises:
        TypeError: If search_str is not a string.
        ValueError: If search_str is an empty string.
        ValueError: If search_rank is not 'all' and not a valid column name in the DataFrame.
        """

        if not isinstance(search_str, str):
            raise TypeError("search_str must be a string")
        if not search_str:
            raise ValueError("search_str must be a nonempty string")
        if search_rank and search_rank != "all" and search_rank not in self.msl_column_names:
            raise ValueError(f"search_rank must be 'all' or one of the following: {', '.join(self.msl_column_names)}")
        if outfmt not in ["simple", "tree"]:
            raise ValueError("outfmt must be 'simple' or 'tree'")

        if search_rank == "all":
            if exact:
                filtered_df = self.msl[self.msl.iloc[:, 1:16].apply(lambda row: search_str.lower() == row.astype(str).str.lower().values, axis=1)]
                if color:
                    for col in filtered_df[1:16]:
                        filtered_df[col] = filtered_df[col].apply(lambda row: util.cdt.color_str(row, words=search_str, colors=color, exact=exact) if pd.notna(row) else row)
            else:
                filtered_df = self.msl[self.msl.iloc[:, 1:16].apply(lambda row: search_str.lower() in row.astype(str).str.lower().values, axis=1)]
                if color:
                    for col in filtered_df[1:16]:
                        filtered_df[col] = filtered_df[col].apply(lambda row: util.cdt.color_str(row, words=search_str, colors=color, exact=exact) if pd.notna(row) else row)
            if narrow:
                filtered_df = self.make_narrow(filtered_df)
        else:
            if exact:
                filtered_df = self.msl2[self.msl2[search_rank].str.lower() == search_str.lower()]
            else:
                filtered_df = self.msl[self.msl[search_rank].str.contains(search_str, case=False, na=False)]

            if color:
                filtered_df[search_rank] = filtered_df[search_rank].apply(lambda row: util.cdt.color_str(row, words=search_str, colors=color, exact=exact))

            if narrow:
                filtered_df = self.make_narrow(filtered_df)

        if outfmt == "simple":
            return filtered_df
        elif outfmt == "tree" and not narrow:
            filtered_df = self.make_narrow(filtered_df)

            tree_list = filtered_df['Realm'].unique().tolist()
            tree_list = [f"/{item}/" for item in tree_list]
            tmp = filtered_df[['Realm', 'Kingdom']].drop_duplicates()
            tmp['string'] = tmp.apply(lambda row: f"/{row['Realm']}/{row['Kingdom']}/", axis=1)
            tree_list = tree_list + tmp['string'].unique().tolist()
            tmp = filtered_df[['Realm', 'Kingdom', 'Phylum']].drop_duplicates()
            tmp['string'] = tmp.apply(lambda row: f"/{row['Realm']}/{row['Kingdom']}/{row['Phylum']}/", axis=1)
            tree_list = tree_list + tmp['string'].unique().tolist()
            tmp = filtered_df[['Realm', 'Kingdom', 'Phylum', 'Class']].drop_duplicates()
            tmp['string'] = tmp.apply(lambda row: f"/{row['Realm']}/{row['Kingdom']}/{row['Phylum']}/{row['Class']}/", axis=1)
            tree_list = tree_list + tmp['string'].unique().tolist()
            tmp = filtered_df[['Realm', 'Kingdom', 'Phylum', 'Class', 'Order']].drop_duplicates()
            tmp['string'] = tmp.apply(lambda row: f"/{row['Realm']}/{row['Kingdom']}/{row['Phylum']}/{row['Class']}/{row['Order']}/", axis=1)
            tree_list = tree_list + tmp['string'].unique().tolist()
            tmp = filtered_df[['Realm', 'Kingdom', 'Phylum', 'Class', 'Order', 'Family']].drop_duplicates()
            tmp['string'] = tmp.apply(lambda row: f"/{row['Realm']}/{row['Kingdom']}/{row['Phylum']}/{row['Class']}/{row['Order']}/{row['Family']}/", axis=1)
            tree_list = tree_list + tmp['string'].unique().tolist()
            tmp = filtered_df[['Realm', 'Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus']].drop_duplicates()
            tmp['string'] = tmp.apply(lambda row: f"/{row['Realm']}/{row['Kingdom']}/{row['Phylum']}/{row['Class']}/{row['Order']}/{row['Family']}/{row['Genus']}/", axis=1)
            tree_list = tree_list + tmp['string'].unique().tolist()
            tmp = filtered_df[['Realm', 'Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']].drop_duplicates()
            tmp['string'] = tmp.apply(lambda row: f"/{row['Realm']}/{row['Kingdom']}/{row['Phylum']}/{row['Class']}/{row['Order']}/{row['Family']}/{row['Genus']}/{row['Species']}", axis=1)
            tree_list = tree_list + tmp['string'].unique().tolist()
            out_tree = util.cdt.ListTree(lst=tree_list)
            return out_tree.list_tree()
        else:
            return

if __name__ == "__main__":
    pass
