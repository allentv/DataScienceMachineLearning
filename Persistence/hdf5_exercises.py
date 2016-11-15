"""
This module has examples for reading and writing from a HDF5 file.
The below code has examples for reading and writing Numpy arrays & Pandas dataframes.

Data in HDF5 files are saved using a key-value format. The keys can be grouped for 
easier access and is not always required. Data is stored in a HDF5 file just like it
is done in the file system with the same hierarchial structure.


References:
-----------
1) https://www.getdatajoy.com/learn/Read_and_Write_HDF5_from_Python
2) http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_hdf.html
3) http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_hdf.html
"""
import h5py
import numpy as np
import pandas as pd


def save_numpy():
    m1 = np.random.random(size=(1000, 20))
    m2 = np.random.random(size=(1000, 200))
    m3 = np.random.random(size=(1000, 200))
    
    with h5py.File("data.h5", "w") as hf:
        group1 = hf.create_group("Group 1")
        group1.create_dataset("grp1_dataset1", data=m1)
        
        group2 = hf.create_group("Group 2")
        group2.create_dataset("grp2_dataset2", data=m2)
        
        hf.create_dataset("dataset3", data=m3)
    
    with h5py.File("data.h5", "r") as hf:
        print("Keys: %s" % list(hf.keys()))
        print("All Items: %s" % list(hf.items()))
        
        group1 = hf.get("Group 1")
        print("Group 1 Items: %s" % list(group1.items()))
        
        m1 = np.array(group1.get("grp1_dataset1"))
        print("Dataset1: %s,  Size: %s" % (type(m1), m1.size))


def save_pandas():
    data = {
        'c1': [1, 2, 3],
        'c2': ['a', 'b', 'c']
    }
    df = pd.DataFrame(data)
    print("\n\nDataFrame\n%r" % df)

    df.to_hdf("data.h5", "dataframe_object")

    df = pd.read_hdf("data.h5", "dataframe_object")
    print("\n\nDataFrame from file\n%r" % df)


if __name__ == "__main__":
    save_numpy()
    save_pandas()
