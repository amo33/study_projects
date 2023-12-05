// 2D 3D dimension of Grid and blocks
// Grids와 block들은 3차원까지 선언할 수 있다.
// 다차원으로 선언하는 것이 성능에 영향을 주는 것은 아니다.
// 허나, 2d 행렬과 같은 input data (특정: matrix들)을 다룰 때는 도움이 된다.
// 이 다차원을 선언하기 위해서 cuda에 있는 dim3 형으로 가능하다. 

/*
가령 아래와 같이 선언하면 block 마다 스레드, block의 개수도 dim3형태로 선언되어 사용될 수 있다.
dim3 threads_per_block(16, 16, 1); 
dim3 number_of_blocks(16, 16, 1);
*/
/*
명세서 

This code contains a host function matrixMulCPU which is fully functional.
Your task is to build out the matrixMulGPUCUDA kernel. 
The source code will execute the matrix multiplication with both functions, and compare their answers to verify the correctness of the CUDA kernel you will be writing. 

You will need to create an execution configuration whose arguments are both dim3 values with the x and y dimensions set to greater than 1.
Inside the body of the kernel, you will need to establish the running thread’s unique index within the grid per usual, but you should establish two indices for the thread: 
one for the x axis of the grid, and one for the y axis of the grid.
*/

#include <stdio.h>

#define N  64
#define ROW 16
#define COLUMN 16
__global__ void matrixMulGPU( int * a, int * b, int * c )
{
  /*
   * Build out this kernel.
   */
  int val = 0;
  int row = blockIdx.x * blockDim.x + threadIdx.x;
  int col = blockIdx.y * blockDim.y + threadIdx.y;
  if (row < N && col <N)
  {
    for (int k=0; k < N; ++k)
    {
      val += a[row*N+k] * b[k*N+col];
    }
    c[row*N+col] = val;
  }
}

/*
 * This CPU function already works, and will run to create a solution matrix
 * against which to verify your work building out the matrixMulGPU kernel.
 */

void matrixMulCPU( int * a, int * b, int * c )
{
  int val = 0;

  for( int row = 0; row < N; ++row )
    for( int col = 0; col < N; ++col )
    {
      val = 0;
      for ( int k = 0; k < N; ++k )
        val += a[row * N + k] * b[k * N + col];
      c[row * N + col] = val;
    }
}

int main()
{
  int *a, *b, *c_cpu, *c_gpu; // Allocate a solution matrix for both the CPU and the GPU operations

  int size = N * N * sizeof (int); // Number of bytes of an N x N matrix

  // Allocate memory
  cudaMallocManaged (&a, size);
  cudaMallocManaged (&b, size);
  cudaMallocManaged (&c_cpu, size);
  cudaMallocManaged (&c_gpu, size);

  // Initialize memory; create 2D matrices
  for( int row = 0; row < N; ++row )
    for( int col = 0; col < N; ++col )
    {
      a[row*N + col] = row;
      b[row*N + col] = col+2;
      c_cpu[row*N + col] = 0;
      c_gpu[row*N + col] = 0;
    }

  /*
   * Assign `threads_per_block` and `number_of_blocks` 2D values
   * that can be used in matrixMulGPU above.
   */

  dim3 threads_per_block(ROW, COLUMN, 1);
  dim3 number_of_blocks ((N / threads_per_block.x) + 1, (N / threads_per_block.y) + 1, 1);
  
  matrixMulGPU <<< number_of_blocks, threads_per_block >>> ( a, b, c_gpu );

  cudaDeviceSynchronize();

  // Call the CPU version to check our work
  matrixMulCPU( a, b, c_cpu );

  // Compare the two answers to make sure they are equal
  bool error = false;
  for( int row = 0; row < N && !error; ++row )
    for( int col = 0; col < N && !error; ++col )
      if (c_cpu[row * N + col] != c_gpu[row * N + col])
      {
        printf("FOUND ERROR at c[%d][%d]\n", row, col);
        error = true;
        break;
      }
  if (!error)
    printf("Success!\n");

  // Free all our allocated memory
  cudaFree(a); cudaFree(b);
  cudaFree( c_cpu ); cudaFree( c_gpu );
}