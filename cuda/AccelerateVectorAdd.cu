#include <stdio.h>
/*

이 코드는 CPU로만 작동하는 벡터 더하기 어플리케이션이다. 여기 있는 addVectorsInto 함수를 CUDA kernel로 만들어 GPU 병렬 연산을 할 수 있게 만들어보자. 다음을 유의해서 코드를 짜보자.

addVectorsInto를 CUDA kernel로 만들기
addVectorsInto가 CUDA kernel로 작동하는 적절한 execution configuration을 찾고 실행하기
메모리 할당과 해제를 적절히 해서 a, b, result 벡터가 CPU/GPU에서 모두 접근 가능하도록 하기
addVectorsInto를 리팩토링하자: it will be launched inside of a single thread, and only needs to do one thread’s worth of work on the input vectors. Be certain the thread will never try to access elements outside the range of the input vectors, and take care to note whether or not the thread needs to do work on more than one element of the input vectors.
CUDA 코드가 잘못될 수 있는 부분에 적절히 error handling을 하자.

*/
// inline 이란 : ?????????????????????????????????????????????
// fprintf란: fprintf를 사용하면 문자열이 파일에 출력된다는 뜻이다.
// -> int fprintf(FILE *stream, const char* format, ...)
// stderr stream : 주로 에러 메시지를 출력하기 위해 만들어진 stream
inline cudaError_t checkCuda(cudaError_t result)
{
  if (result != cudaSuccess)
  {
    fprintf(stderr, "CUDA Runtime Error: %s\n", cudaGetErrorString(result));
    assert(result == cudaSuccess);
  }
  return result;
}

void initWith(float num, float *a, int N)
{
  for(int i = 0; i < N; ++i)
  {
    a[i] = num;
  }
}

__global__
void addVectorsInto(float *result, float *a, float *b, int N)
{
  int idx = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = gridDim.x*blockDim.x;
  for(int i = idx; i < N; i+=stride)
  {
    result[i] = a[i] + b[i];
  }
}

void checkElementsAre(float target, float *array, int N)
{
  for(int i = 0; i < N; i++)
  {
    if(array[i] != target)
    {
      printf("FAIL: array[%d] - %0.0f does not equal %0.0f\n", i, array[i], target);
      exit(1);
    }
  }
  printf("SUCCESS! All values added correctly.\n");
}

int main()
{
  const int N = 2<<20; // Don't change
  size_t size = N * sizeof(float);

  float *a;
  float *b;
  float *c;
  cudaError_t mallocCheck, syncError, asyncError;
  size_t threads_per_block = 1024; // block에 존재할 수 있는 thread의 개수는 최대 1024이다!
  size_t number_of_blocks;
  number_of_blocks = (N + threads_per_block - 1) / threads_per_block;

  checkCuda(cudaMallocManaged(&a, size));
  checkCuda(cudaMallocManaged(&b, size));
  checkCuda(cudaMallocManaged(&c, size));
  mallocCheck = cudaGetLastError();
  if(mallocCheck != cudaSuccess)
  {
    printf("Malloc failed");
    return -1;
  }
  initWith(3, a, N);
  initWith(4, b, N);
  initWith(0, c, N);

  addVectorsInto<<<number_of_blocks, threads_per_block>>>(c, a, b, N);
  syncError = cudaGetLastError();
  asyncError = cudaDeviceSynchronize();
  if(syncError != cudaSuccess){
    printf("Error: %s\n", cudaGetErrorString(syncError));
  }
  if(asyncError != cudaSuccess)
  {
    printf("Error: %s\n", cudaGetErrorString(asyncError));
  }
  checkElementsAre(7, c, N);
  
  cudaFree(a);
  cudaFree(b);
  cudaFree(c);
}
