from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    print(f"This is process {rank} speaking.")

if __name__ == "__main__":
    main()