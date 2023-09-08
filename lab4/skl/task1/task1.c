#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdint.h>     // provides int8_t, uint8_t, int16_t etc.
#include <stdlib.h>

struct particle
{
    int8_t v_x, v_y, v_z;
};

int main(int argc, char* argv[])
{
    if(argc < 2)
    {
        printf("apelati cu %s <n>\n", argv[0]);
        return -1;
    }

    long n = atol(argv[1]);

    // TODO
    // alocati dinamic o matrice de n x n elemente de tip struct particle
    // verificati daca operatia a reusit

    // TODO
    // populati matricea alocata astfel:
    // *liniile pare contin particule cu toate componentele vitezei pozitive
    //   -> folositi modulo 128 pentru a limita rezultatului lui rand()
    // *liniile impare contin particule cu toate componentele vitezi negative
    //   -> folositi modulo 129 pentru a limita rezultatului lui rand()

    // TODO
    // scalati vitezele tuturor particulelor cu 0.5
    //   -> folositi un cast la int8_t* pentru a parcurge vitezele fara
    //      a fi nevoie sa accesati individual componentele v_x, v_y, si v_z

    struct particle *matrix = malloc(n * n * sizeof(struct particle));

    if (matrix == NULL)
    {
        printf("failed to allocate memory for matrix\n");
        return -1;
    }

    // populate matrix
    for (long i = 0; i < n; i++)
    {
        for (long j = 0; j < n; j++)
        {
            if (i % 2 == 0)
            {
                matrix[i * n + j].v_x = rand() % 128 + 1;
                matrix[i * n + j].v_y = rand() % 128 + 1;
                matrix[i * n + j].v_z = rand() % 128 + 1;
            }
            else
            {
                matrix[i * n + j].v_x = -1 * (rand() % 129 + 1);
                matrix[i * n + j].v_y = -1 * (rand() % 129 + 1);
                matrix[i * n + j].v_z = -1 * (rand() % 129 + 1);
            }
        }
    }

    // scale speeds of all particles by 0.5
    int8_t *speed_ptr = (int8_t*)matrix;
    for (long i = 0; i < n * n * 3; i++)
    {
        speed_ptr[i] *= 0.5;
    }


    // compute max particle speed
    float max_speed = 0.0f;
    for (long i = 0; i < n * n; i++)
    {
        float speed = sqrt(pow(matrix[i].v_x, 2) + pow(matrix[i].v_y, 2) + pow(matrix[i].v_z, 2));
        if (max_speed < speed) max_speed = speed;
    }


    // print result
    printf("viteza maxima este: %f\n", max_speed);

    free(matrix);

    return 0;
}

