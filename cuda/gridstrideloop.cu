#include <stdio.h>

void init(int *a, int N)
{
  int i;
  for (i = 0; i < N; ++i)
  {
    a[i] = i;
  }
}

/*
 * In the current application, `N` is larger than the grid.
 * Refactor this kernel to use a grid-stride loop in order that
 * each parallel thread work on more than one element of the array.
 */

__global__
void doubleElements(int *a, int N)
{
  int idx = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = gridDim.x * blockDim.x; // stride를 계산해서 한 grid마다 여러 개의 데이터를 for문으로 작업하는 방법이 있다.
  int i = 0;
  for (i = idx; i < N; i += stride)
  {
    a[i] *= 2;
  }
}

bool checkElementsAreDoubled(int *a, int N)
{
  int i;
  for (i = 0; i < N; ++i)
  {
    if (a[i] != i*2) return false;
  }
  return true;
}

int main()
{
  /*
   * `N` is greater than the size of the grid (see below).
   */

  int N = 10000;
  int *a;
  cudaError_t error;
  size_t size = N * sizeof(int);
  error = cudaMallocManaged(&a, size); // error 를 다룬다면 cudaMalloc의 경우 이 방법을 쓴다.
  if (error != cudaSuccess)
  {
    printf("Error: %s\n", cudaGetErrorString(error)); // `cudaGetErrorString` is provided by CUDA.
  }
  init(a, N);

  /*
   * The size of this grid is 256*32 = 8192.
   */

  size_t threads_per_block = 256;
  size_t number_of_blocks = 32;

  doubleElements<<<number_of_blocks, threads_per_block>>>(a, N);
  cudaDeviceSynchronize();

  bool areDoubled = checkElementsAreDoubled(a, N);
  printf("All elements were doubled? %s\n", areDoubled ? "TRUE" : "FALSE");

  cudaFree(a);
}