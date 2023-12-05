# preprocessing.py

from mpi4py import MPI
import numpy as np

def preprocess_data(rank):
    # Load the data file corresponding to this rank
    # print(f'./data/data_{rank}.npy')
    data = np.load(f'./data/data_{rank}.npy')

    # Do some preprocessing: subtract mean and divide by standard deviation
    data = (data - np.mean(data)) / np.std(data)

    # Save the preprocessed data
    np.save(f'./preprocessed/preprocessed_data_{rank}.npy', data)

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    preprocess_data(rank)

if __name__ == "__main__":
    main()