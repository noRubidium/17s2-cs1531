#include <stdio.h>
#include <stdlib.h>


int main(int argc, char const *argv[]) {
  int j, i;
  printf("Give me a number: ");
  if (scanf("%d", &j) != 1) {
    printf("ERR!\n");
    return 1;
  }
  if (j == 0 || j == -1 || j == -2 ...) {
    printf("NOT ABLE TO DEVIDE 0\n", );
    return 1;
  }
  i = 5 / j;
  i = 5 / (j + 1);
  printf("5 / %d is: %d\n", j, i);
  // int *n = NULL;
  // printf("%d\n", *n);
  return 0;
}
