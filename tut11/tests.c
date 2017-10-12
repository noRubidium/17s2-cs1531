#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int add(int a, int b) {
  return 0;
}


int addTests() {
  assert(add(0, 0) == 0);
  assert(add(5, 3) == 8);
  assert(add(3, 3) == 6);
  assert(add(5.5, 3) == 8);
}


int main(int argc, char const *argv[]) {
  addTests();
  return 0;
}
