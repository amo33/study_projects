'''
unhandled exceptions들은 deadlock을 유발할 수 있다.
모든 exception들이 잘 처리되어 구현해야 한다.

'''

from mpi4py import MPI

def risky_operation(rank):
    if rank == 1:
        raise Exception(f"An error occurred in process {rank}")

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    try:
        risky_operation(rank)
    except Exception as e:
        print(e)
        comm.Abort()

if __name__ == "__main__":
    main()

'''
위 코드에서 process 1은 exception을 내뱉는다.
그래서 comm.Abort() 을 호출해서 모든 프로세스를 죽인다.
debugging 방법으로는 print문을 출력하거나, built-in debugger pdb를 사용, 혹은 TotalView나 DDT 같은 MPI 지원 툴을 사용한다.
'''

