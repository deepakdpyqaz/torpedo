import numpy as np


def text_to_np(text):
    """
    Convert a text file to a numpy array
    """
    with open(text, "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line]
    lines = np.array(lines)
    return lines
