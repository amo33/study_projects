'''
MPI에서 점대점 통신 방법으로 'sending and receiving messages' 방법이 있다고 알고 있다. 
Here's a simple example of the MPI send and recv (receive) methods.
'''

from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0: # if rank is 0 send the data
        data = {'a': 1, 'b': 2, 'c': 3}
        comm.send(data, dest=1)
    elif rank == 1: # if rank is 1 receiv the data sent from rank 0
        data = comm.recv(source=0)
        print(f"Received data {data} from process 0") 

if __name__ == "__main__":
    main()
    # mpiexec -n 2 python send_recv.py

