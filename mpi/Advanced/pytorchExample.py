'''
이전 예제에서 tensorflow와 MPI 사용 예제를 보았는데, 이번에는 pytorch를 사용하는 방법에 대해서 알아보겠다.
pytorch는 torch.distributed package에서 distributed computing 기능을 여러 bakend로 지원한다. 그중 mpi도 포함
현재는 NCCL, GLOO를 backend로 사용한다. MPI는 사실 기능이 앞선 2가지 backend보다 좋지 않다. 그래도 MPI로 사용하고 싶다는 가정으로 진행해보겠다.
'''
import torch.distributed as dist
from mpi4py import MPI

def main():
    # Initialize the distributed environment
    dist.init_process_group('mpi') # use mpi backend
    # 이 코드에서도 dist.send, dist.recv, dist.broadcast 등 실제 mpi4py에서 지원하는 기능들을 dist로 사용가능하다.
    # ... your code here ...

if __name__ == "__main__":
    main()
'''
GLOO :  집합통신 라이브러리. 여러 시스템에서 max, sum, min등의 데이터 집계 작업을 수행한다. Facebook에 개발했으며, 이런 데이터 작업이 활발한 ML training에 적합
NCCL : nvidia gpu와 함께 사용하도록 고안됨. -> cpu + gpu 작업에서도 잘 작동한다.
'''