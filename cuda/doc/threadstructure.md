# CUDA thread 구조
- cuda의 grid 내부 모든 스레드는 같은 커널 함수를 수행한다. 
- 그 스레드들은 서로 구별하고 처리하기 위해 자체 좌표를 수행한다.   
- 좌표의 특징을 갖는 2-level 구조계층을 쓴다.
- 보통은 blockIdx로 grid 내부 몇 번째 block인지, threadIdx로 block 내부 몇 번째 thread인지의 정보를 요구한다.   
- gridDim는 grid내 block의 개수를 반환한다.

- dimGrid와 dimBlock이라는 변수는 dim3 type인 3차원까지 받을 수 있다.

https://junstar92.tistory.com/245