'''
collective communication : 집합 통신
이 통신 방법은 모든 프로세스들이 MPI communicate이 가능한다. -> 모두 통신에 참여한다.
아래와 같은 통신 방법들이 존재한다.
bcast: rank가 root인 프로세스에서 다른 모든 프로세스에 broadCast 
gather : 모든 프로세스에서 value들을 가져와서 root 프로세스에게 전달
reduce : Reduction operation (sum, max, min 등등)을 모든 value들에게 적용하고 root 프로세스에게 보낸다.

'''

# broadcast example
from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        data = {'a': 1, 'b': 2, 'c': 3}
    else:
        data = None

    data = comm.bcast(data, root=0)
    print(f"Process {rank} received data {data}")

if __name__ == "__main__":
    main()
    # mpiexec -n 4 python bcast.py