#include <stdio.h>

/*
 * Currently, `initializeElementsTo`, if executed in a thread whose
 * `i` is calculated to be greater than `N`, will try to access a value
 * outside the range of `a`. -> 주어진 execution configuration <<a,b>> 보다 더 많은 영역을 접근하려고 하면 애초에 맞지 않는다. -> 따라서 initializElementsTO에서 해당 idx 위치가 N보다 작으면 값을 할당해줘야 한다. 
 *
 * Refactor the kernel defintition to prevent our of range accesses.
 */

__global__ void initializeElementsTo(int initialValue, int *a, int N)
{
  int i = threadIdx.x + blockIdx.x * blockDim.x;
  if (i < N)
  {
    a[i] = initialValue;
  }
  
}

int main()
{
  /*
   * Do not modify `N`.
   */

  int N = 1000;

  int *a;
  size_t size = N * sizeof(int);

  cudaMallocManaged(&a, size);

  /*
   * Assume we have reason to want the number of threads
   * fixed at `256`: do not modify `threads_per_block`.
   */

  size_t threads_per_block = 256;

  /*
   * Assign a value to `number_of_blocks` that will
   * allow for a working execution configuration given
   * the fixed values for `N` and `threads_per_block`.
   */

  // Ensure there are at least `N` threads in the grid, but only 1 block's worth extra
  size_t number_of_blocks = (N+ threads_per_block -1) / threads_per_block;

  int initialValue = 6;

  initializeElementsTo<<<number_of_blocks, threads_per_block>>>(initialValue, a, N);
  cudaDeviceSynchronize();

  /*
   * Check to make sure all values in `a`, were initialized.
   */

  for (int i = 0; i < N; ++i)
  {
    if(a[i] != initialValue)
    {
      printf("FAILURE: target value: %d\t a[%d]: %d\n", initialValue, i, a[i]);
      exit(1);
    }
  }
  printf("SUCCESS!\n");

  cudaFree(a); // host 와 device에서 모두 접근할 수 있는 a는 cudaFree를 통해서 free한다.
}