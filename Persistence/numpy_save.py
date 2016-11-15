"""
Save and restore numpy data
"""
import numpy as np


def save_data():
    data = np.matrix((
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ))
    with open("numpy_obj.npy", "wb") as npy_file:
        np.save(npy_file, data)
        print("\n\nSave data to file : 'numpy_obj.npy'")

def load_data():
    data = np.load("numpy_obj.npy")
    print("\n\nNumpy Array from file: %r" % data)


if __name__ == "__main__":
    save_data()
    load_data()
