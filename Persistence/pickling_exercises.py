"""
This module has examples of pickling in python.

Pickling is the process in which a python object is written to file in
binary format. Reading the object back from file is called "Unpickling"


References:
-----------
1) https://docs.python.org/3/library/pickle.html
"""
import pickle


def save():
    some_data = {'key': [1, 2, 3, ['a', 'b']]}
    
    # Save the data in binary format
    with open("pickle_data.obj", "wb") as file:
        print("Saving object to file...")
        pickle.dump(some_data, file)
    
    with open("pickle_data.obj", "rb") as file:
        pickled_obj = pickle.load(file)
        print("Load pickled object: %s" % pickled_obj)


if __name__ == "__main__":
    save()
