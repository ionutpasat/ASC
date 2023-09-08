// TODO
// Inmultirea matricelor

#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdint.h>     // provides int8_t, uint8_t, int16_t etc.
#include <stdlib.h>
#include <sys/time.h>

#define N 1200
double a[N][N], b[N][N], c[N][N];

int main(int argc, char* argv[])
{
    int i, j, k, bi, bj, bk;
    int blockSize = 50; 
    struct timeval start, end;
    float elapsed;

    if(argc > 2)
    {
        printf("apelati cu %s <n>\n", argv[0]);
        return -1;
    }
    if(argc == 2)
        blockSize = atoi(argv[1]);

    srand(0); //to repeat experiment
    //srand(time(NULL)); // if you want random seed

    // reset c matrix and initialize a and b matrix
    for (i = 0; i < N; i++){
        for (j = 0; j < N; j++){
            c[i][j] = 0.0;
            a[i][j] = (double)rand() / RAND_MAX * 2.0 - 1.0; //double in range -1 to 1
            b[i][j] = (double)rand() / RAND_MAX * 2.0 - 1.0; //double in range -1 to 1
        }
    }

    gettimeofday(&start, NULL);

    // BMM - block method and pointer to line optimization
    for (bi = 0; bi < N; bi += blockSize) {
        for (bj = 0; bj < N; bj += blockSize) {
            for (bk = 0; bk < N; bk += blockSize) {
                for (i = bi; i < bi + blockSize && i < N; i++) {
                    double *orig_pa = &a[i][bk];
                    for (j = bj; j < bj + blockSize && j < N; j++) {
                        double *pa = orig_pa;
                        double *pb = &b[bk][j];
                        register double suma = 0;
                        for (k = bk; k < bk + blockSize && k < N; k++) {
                            suma += *pa * *pb;
                            pa++;
                            pb += N;
                        }
                        c[i][j] += suma;
                    }
                }
            }
        }
    }

    gettimeofday(&end, NULL);

    elapsed = ((end.tv_sec - start.tv_sec) * 1000000.0f + end.tv_usec - start.tv_usec) / 1000000.0f;

    printf("TIME (BMM-optimize): %12f\n", elapsed);

    return 0;
}
