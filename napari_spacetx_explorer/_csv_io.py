import numpy as np
import pandas as pd


class CSVIO:
    """Read data from csv file

    Parameters
    ----------
    file_path : str
        Path to the csv file

    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.y_col_names = ["yc", "y", "axis-0"]
        self.x_col_names = ["xc", "x", "axis-1"]
        self.tgt_col_names = ["target", "gene", "name"]

    def is_compatible(self):
        if self.file_path.endswith('.csv'):
            return True
        return False

    def read(self):
        df = pd.read_csv(self.file_path)
        df = df.fillna('None')
        print(df.columns)
        y_col_candidates = [c for c in df.columns if c.lower() in self.y_col_names]
        x_col_candidates = [c for c in df.columns if c.lower() in self.x_col_names]
        tgt_col_candidates = [c for c in df.columns if c.lower() in self.tgt_col_names]

        assert len(y_col_candidates) == 1 and len(x_col_candidates) == 1, "Found multiple candidate columns for Y and/or X axes"
        assert len(tgt_col_candidates) == 1, "Found multiple candidate columns for gene names"

        y_col, x_col, tgt_col = y_col_candidates[0], x_col_candidates[0], tgt_col_candidates[0]
        self.total_data = (df[[y_col, x_col]].to_numpy(), df[tgt_col])
