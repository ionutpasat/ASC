/*
 * Tema 2 ASC
 * 2023 Spring
 */
#include "utils.h"

extern inline void matrix_transpose(register int N,
                                    register double *restrict transposed,
                                    register double *restrict to_transpose) {
  register int i, j;
  for (j = 0; j < N; j += 4) {
    for (i = 0; i < N; ++i) {
      register double *to_tr = &to_transpose[i * N + j];
      register double *tr = &transposed[j * N + i];
      tr[0] = to_tr[0];
      tr[N] = to_tr[1];
      tr[2 * N] = to_tr[2];
      tr[3 * N] = to_tr[3];
    }
  }
}

double *my_solver(register int N, register double *A, register double *B) {
  int i, j, k;
  register double *restrict At = calloc(N * N, sizeof(double));
  register double *restrict Bt = calloc(N * N, sizeof(double));
  register double *restrict AxB = calloc(N * N, sizeof(double));
  register double *restrict AxBxAt = calloc(N * N, sizeof(double));
  register double *restrict BtxBt = calloc(N * N, sizeof(double));
  register double *restrict result = calloc(N * N, sizeof(double));

  matrix_transpose(N, At, A);
  matrix_transpose(N, Bt, B);

  for (i = 0; i < N; ++i) {
    for (k = i; k < N; ++k) {
      register double *pB = &B[k * N];
      for (j = 0; j + 3 < N; j += 4) {
        register double aux = A[i * N + k];
        AxB[i * N + j] += aux * pB[j];
        AxB[i * N + j + 1] += aux * pB[j + 1];
        AxB[i * N + j + 2] += aux * pB[j + 2];
        AxB[i * N + j + 3] += aux * pB[j + 3];
      }
    }
  }

  for (j = 0; j < N; ++j) {
    for (i = 0; i < N; ++i) {
      register double sum = 0.0;
      for (k = j; k + 3 < N; k += 4) {
        register double tmp1 = AxB[i * N + k] * At[k * N + j];
        register double tmp2 = AxB[i * N + k + 1] * At[(k + 1) * N + j];
        register double tmp3 = AxB[i * N + k + 2] * At[(k + 2) * N + j];
        register double tmp4 = AxB[i * N + k + 3] * At[(k + 3) * N + j];
        sum += tmp1 + tmp2 + tmp3 + tmp4;
      }
      for (; k < N; ++k) {
        register double tmp = AxB[i * N + k] * At[k * N + j];
        sum += tmp;
      }
      AxBxAt[i * N + j] = sum;
    }
  }

  for (j = 0; j < N; ++j) {
    for (i = 0; i < N; ++i) {
      register double *orig_pa = &Bt[i * N];
      double *pa = orig_pa;
      double *pb = &Bt[j];
      register double sum1 = 0.0;
      register double sum2 = 0.0;
      register double sum3 = 0.0;
      register double sum4 = 0.0;
      for (k = 0; k + 3 < N; k += 4) {
        sum1 += *pa * *pb;
        sum2 += *(pa + 1) * *(pb + N);
        sum3 += *(pa + 2) * *(pb + 2 * N);
        sum4 += *(pa + 3) * *(pb + 3 * N);
        pa += 4;
        pb += 4 * N;
      }
      BtxBt[i * N + j] += sum1 + sum2 + sum3 + sum4;
    }
  }

  for (i = 0; i < N; ++i) {
    register int index = i * N;
    register double *res = &result[index];
    register double *src1 = &AxBxAt[index];
    register double *src2 = &BtxBt[index];
    for (j = 0; j + 3 < N; j += 4) {
      *res = *src1 + *src2;
      *(res + 1) = *(src1 + 1) + *(src2 + 1);
      *(res + 2) = *(src1 + 2) + *(src2 + 2);
      *(res + 3) = *(src1 + 3) + *(src2 + 3);
      res += 4;
      src1 += 4;
      src2 += 4;
    }
  }

  free(At);
  free(Bt);
  free(AxB);
  free(AxBxAt);
  free(BtxBt);

  return result;
}
