import numpy as np
import pandas as pd
from utils import text_to_np
import os
import re


class Model:
    procedure = [
        "cause",
        "quantity",
        "color",
        "odour",
        "consistency",
        "complaints",
        "frequency",
        "urgency",
        "floating",
        "other_complaints",
        "duration",
    ]

    def __init__(self, data_path="data"):
        for files in os.listdir(data_path):
            if files.endswith(".txt"):
                setattr(
                    self,
                    files.split(".")[0],
                    text_to_np(os.path.join(data_path, files)),
                )
            else:
                setattr(
                    self,
                    files.split(".")[0],
                    pd.read_csv(os.path.join(data_path, files)),
                )

    def predict(self, terms, indices=True):
        search_terms = []
        if indices:
            for idx, prop in enumerate(terms):
                search_terms.extend(np.take(getattr(self, procedure[idx])))
        else:
            search_terms = terms
        search_terms = list(filter(lambda x: x != "", search_terms))
        search_terms = list(map(lambda x: x.strip(), search_terms))
        search_term = "|".join(search_terms)
        return self.master[
            self.master["Search Term for Feature of pureesha"].str.contains(
                search_term, regex=True, case=False
            )
        ].reset_index(drop=True)


model = Model("data")
