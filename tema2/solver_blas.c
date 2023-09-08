/*
 * Tema 2 ASC
 * 2023 Spring
 */
// #include "cblas.h"
#include "utils.h"
#include <stdio.h>
#include <string.h>

// /*
//  * Add your BLAS implementation here
//  */
double *my_solver(int N, double *A, double *B) {
//   double *res1 = calloc(N * N, sizeof(double));
//   double *res2 = calloc(N * N, sizeof(double));

//   cblas_dcopy(N*N, B, 1, res1, 1);
//   cblas_dtrmm(CblasRowMajor, CblasLeft, CblasUpper, CblasNoTrans, CblasNonUnit,
//               N, N, 1.0, A, N, res1, N);
//   cblas_dtrmm(CblasRowMajor, CblasRight, CblasUpper, CblasTrans, CblasNonUnit,
//               N, N, 1.0, A, N, res1, N);
//   cblas_dgemm(CblasRowMajor, CblasTrans, CblasTrans, N, N, N, 1.0, B, N,
//               B, N, 1.0, res2, N);

//   cblas_daxpy(N*N, 1.0, res1, 1, res2, 1);

//   free(res1);
//   return res2;
return 0;
}

