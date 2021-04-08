#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
#include <math.h>
/*
#define DO_STAGE(num, cond) do {\
    printf("Stage " #num ": ");\
    scanf("%lu", &converter.uint);\
    x = converter.dbl;\
    if(cond) {\
        puts("Stage " #num " passed!");\
    } else {\
        puts("Stage " #num " failed!");\
        return num;\
    }\
} while(0);
*/
union cast {
    uint64_t uint;
    double dbl;
};

// sparc
//inf  : 9218868437227405312 fftff
//-inf : 18442240474082181120 fftff
//nan  : 9221120237041090559 ftfft

// x86
//inf  : 2146435072 fffff
//-inf : 4293918720 fffff
//nan  : 18446744071561543679 ftfft

// デカい数(infの1/4くらい)　9209861237972664320 ffftf
int main(void) {
    union cast converter;
    double x;

    scanf("%lu", &converter.uint);
    x = converter.dbl;

    printf("%lu\n", converter.uint);
    printf("%lf\n", x);
    printf("%lf\n", x+1);
    printf("%lf\n", x*2);
    if(x == -x){puts("True");}else{puts("False");}
    if(x != x){puts("True");}else{puts("False");}
    if(x + 1 == x && x * 2 == x){puts("True");}else{puts("False");}
    if(x + 1 == x && x * 2 != x){puts("True");}else{puts("False");}
    if((1 + x) - 1 != 1 + (x - 1)){puts("True");}else{puts("False");}

    //DO_STAGE(1, x == -x);
    //DO_STAGE(2, x != x);
    //DO_STAGE(3, x + 1 == x && x * 2 == x);
    //DO_STAGE(4, x + 1 == x && x * 2 != x);
    //DO_STAGE(5, (1 + x) - 1 != 1 + (x - 1));

    //print_flag();

    return 0;
}