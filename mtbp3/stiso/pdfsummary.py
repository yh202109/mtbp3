#  Copyright (C) 2023-2024 Y Hsu <yh202109@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public license as published by
#  the Free software Foundation, either version 3 of the License, or
#  any later version.
#j
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details
#
#  You should have received a copy of the GNU General Public license
#  along with this program. If not, see <https://www.gnu.org/license/>

from pypdf import PdfReader
import mtbp3
import os
import pandas as pd

class pdfSummary:
    def __init__(self, path = None):
        
        if not isinstance(path, str) or len(path) == 0:
            self.pdf_path = mtbp3.get_data('attention.pdf')
            self.demo = True
        else:
            self.pdf_path = path
            self.demo = False

        try:
            file = open(self.pdf_path, 'rb')
            self.pp = PdfReader(file)
        except FileNotFoundError:
            raise ValueError("File not found")

        tmp0 = self.pp.get_num_pages()
        tmp1 = [len(self.pp.pages[i].images) for i in range(tmp0)]
        self.summary = {
            'pdf_version': self.pp.pdf_header.split('-')[1],
            'n_page': tmp0,
            'file_size': os.path.getsize(self.pdf_path),
            'n_image_in_page': tmp1,
            'n_image_in_file': sum(tmp1)
        }
        self.summary_label = {
            'pdf_version': "PDF version",
            'n_page': "Number of pages: ",
            'file_size': "File size (byte): ",
            'n_image_in_page': "Number of images in individual pages: ",
            'n_image_in_file': "Number of images total: ",
        }

    def get_summary_string(self):
        return "\n".join([self.summary_label[key] + ": " + str(self.summary[key]) for key in self.summary.keys()])

    def get_summary_df(self):
        data = {
            'Summary Label': list(self.summary_label.values()),
            'Summary Value': list(self.summary.values())
        }
        df = pd.DataFrame(data)
        return df

if __name__ == "__main__":

    pfr = pdfSummary("/Users/yh2020/dt2/proj/mtbp3/mtbp3/data/attention.pdf")
    print('outline',pfr.pp.outline)

