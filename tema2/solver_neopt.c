/*
 * Tema 2 ASC
 * 2023 Spring
 */
#include "utils.h"

/*
 * Add your unoptimized implementation here
 */
void print_matrix(int N, double *matrix) {
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      printf("%f ", matrix[i * N + j]);
    }
    printf("\n");
  }
}

void matrix_transpose(int N, double *transposed, double *to_transpose) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      transposed[i * N + j] = to_transpose[j * N + i];
    }
  }
}

double *my_solver(int N, double *A, double *B) {
  double *At = calloc(N * N, sizeof(double));
  double *Bt = calloc(N * N, sizeof(double));
  double *AxB = calloc(N * N, sizeof(double));
  double *AxBxAt = calloc(N * N, sizeof(double));
  double *BtxBt = calloc(N * N, sizeof(double));
  double *result = calloc(N * N, sizeof(double));

  matrix_transpose(N, At, A);
  matrix_transpose(N, Bt, B);

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      for (int k = i; k < N; k++) {
        AxB[i * N + j] += A[i * N + k] * B[k * N + j];
      }
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      for (int k = j; k < N; k++) {
        AxBxAt[i * N + j] += AxB[i * N + k] * At[k * N + j];
      }
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < N; k++) {
        BtxBt[i * N + j] += Bt[i * N + k] * Bt[k * N + j];
      }
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      result[i * N + j] = AxBxAt[i * N + j] + BtxBt[i * N + j];
    }
  }

  free(At);
  free(Bt);
  free(AxB);
  free(AxBxAt);
  free(BtxBt);

  return result;
}
