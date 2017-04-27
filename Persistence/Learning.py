
import pickle
import h5py
import numpy as np

m1 = np.random.random(size=(1000, 2000))

def save_hdf5(RandomData):
    # Save the data in HDF5 format
    with h5py.File("TEST.h5", "w") as hf:
        group1 = hf.create_group("M1Test")
        group1.create_dataset("M1TestData", data = RandomData)    
        print("Saving object to file hdf5")


def save_binary(RandomData):
    # Save the data in binary format
    with open("TEST.obj", "wb") as file:
        print("Saving object to binary file")
        pickle.dump(RandomData, file)


def save_text(RandomData):
    # Save the data in Text format
    with open("TEST.txt", "w") as file:
        print("Saving object to file as text")
        np.savetxt("TEST.txt", RandomData, delimiter=",")


if __name__ == "__main__":

    save_hdf5(m1)
    save_binary(m1)
    save_text(m1)