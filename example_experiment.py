## File to create hdf5 experiment file

import numpy as np
import h5py

with h5py.file('example_file.hdf5', 'w') as f:
    dset = f.create_dataset('dataset',(100,), dtype = 'i')