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

import requests
import os
import pandas as pd

class accessLib:
    """
    A class for accessing the CDISC library using an input file and API key.

    Attributes:
        input_file (str): The path to the input file containing the API key.

    Raises:
        FileNotFoundError: If the input file is not found.
        ValueError: If the API key is empty.
    """

    def __init__(self, input_file):
        self.input_file = input_file
        if not os.path.isfile(self.input_file):
            raise FileNotFoundError(f"Input file '{self.input_file}' not found.")
        with open(self.input_file, 'r') as file:
            self.api_key = file.read().strip()
        if not self.api_key:
            raise ValueError("API key is empty.")

        self.baseURL = "https://library.cdisc.org/api"

    def get_ct_list(self):
        """
        Retrieves a DataFrame containing information about CDISC library packages.

        This method sends a GET request to the CDISC library API to retrieve information about CDISC library packages.
        It returns a DataFrame containing package information, including the title, package series, effective date, path, and type of each package.

        Returns:
            dict: A dictionary containing the DataFrame with package information and a set of unique package titles.
                - 'ct': pandas.DataFrame: The DataFrame containing package information.
                - 'title': set: A set of unique package titles.
        """
        ep = "/mdr/products"
        pp = "/Terminology"
        req = requests.get(
            self.baseURL + ep + pp, 
            headers={'api-key': self.api_key, 'Accept': 'application/json'}
        )
        req.close()
        if req.status_code == 200:
            data = req.json()
            packages = data['_links']['packages']
            df = pd.DataFrame()
            for package in packages:
                title = package['title']
                t1, t2 = title.split(" Controlled Terminology Package ")
                t2, t3 = t2.split(" Effective ")
                df = df._append({'Title': t1, 'PkgSeries': t2, 'Effective': t3, 'Path': package['href'], 'Type': package['type']}, ignore_index=True)
            df['Newest'] = df['Effective'] == df.groupby('Title')['Effective'].transform('max')
        return {'ct': df, 'title': set(df['Title'])}

if __name__ == "__main__":
    cl = accessLib("/Users/yh2020/cdisc.txt")
    out = cl.get_ct_list()
    print(out['ct'])
