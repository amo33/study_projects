'''
profiling은 bottleneck을 확인하고 MPI program의 performance를 최적화하는데 있어 중요하다.
python에서는 cProfile, line_profiler와 같은 몇 가지 profiling library를 사용하지만, 실제로 MPI program에서는 parallel 실행 때문에 이들을 활용하기 까다롭다.

그렇기에 각각의 프로세스를 따로 profile하는 방법이 있다. 아래는 cProfile을 활용해서 이 방법을 진행한다.

아래 방법처럼 main 함수 자체를 감싸는 profiler를 사용하면 각각의 프로세스마다 독립된 파일로 profile 결과가 나온다. -> SnakeViz를 사용해서 시각화할 수 있다.
'''

import cProfile
from mpi4py import MPI

def main():
    pass # Your own code

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    profiler = cProfile.Profile()
    profiler.enable()
    
    main()
    
    profiler.disable()
    profiler.dump_stats(f"profile_{rank}.out")
'''
MPI 프로그램 최적하는 communication과 computation의 중첩을 대부분 요구한다.
뿐만 아니라 프로세스끼리의 부하 관리, communication 부하 최소화 등등도 포함한다.
'''

# 프로세스 부하관리 예시 in c
'''

#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    int total_work = 100; // 전체 작업량 예시
    int work_per_process = total_work / world_size; // 각 프로세스의 작업량

    // 각 프로세스에 할당된 작업 시작 인덱스 계산
    int start = work_per_process * world_rank;
    int end = start + work_per_process;

    // 마지막 프로세스는 나머지 작업도 처리
    if (world_rank == world_size - 1) {
        end = total_work;
    }

    // 각 프로세스가 수행할 작업
    for (int i = start; i < end; i++) {
        // 여기에 작업 처리 로직 구현
        printf("Process %d doing work %d\n", world_rank, i);
    }

    MPI_Finalize();
    return 0;
}
'''

# communication , computation 중첩 관리 : 비동기 or 동기 통신 전략으로 구현 in c
'''

#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    const int SIZE = 10000;
    int data[SIZE]; // 데이터 버퍼

    MPI_Request request;
    MPI_Status status;

    // 비동기 통신 시작
    if (world_rank == 0) {
        // 다른 프로세스에 데이터 전송
        MPI_Isend(data, SIZE, MPI_INT, 1, 0, MPI_COMM_WORLD, &request);
    } else if (world_rank == 1) {
        // 데이터 수신
        MPI_Irecv(data, SIZE, MPI_INT, 0, 0, MPI_COMM_WORLD, &request);
    }

    // 통신 중에 수행할 계산 작업
    // ...
    // 예를 들어, 복잡한 수학적 계산, 데이터 처리 등을 수행할 수 있습니다.

    // 비동기 통신 완료 대기
    MPI_Wait(&request, &status);

    MPI_Finalize();
    return 0;
}
이 코드는 다음과 같이 동작합니다:

MPI_Isend와 MPI_Irecv를 사용하여 데이터 전송을 시작합니다. 이 함수들은 전송이 완료되기를 기다리지 않고 즉시 제어권을 반환합니다.
통신이 진행되는 동안 다른 계산 작업을 수행할 수 있습니다.
계산 작업 후, MPI_Wait 함수를 호출하여 데이터 전송이 완료될 때까지 기다립니다.
이 방법을 사용하면 통신 대기 시간 동안 유용한 작업을 할 수 있어 전체 프로그램의 효율성을 높일 수 있습니다. 그러나 이러한 중첩이 효과적으로 이루어지려면, 계산과 통신이 서로 방해받지 않도록 잘 설계되어야 합니다.

'''