#include <iostream>
using namespace std;

// compare two, send to front (send max to back)
// Very inefficient O(n * n), but slower due to 3 swaps

int main(void) {
    int to_sort[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
    int i, j, temp;
    int arr_size = sizeof(to_sort)/sizeof(int)-1;
    
    for(i = 0; i < arr_size; i++) {
       for (j = 0; j < arr_size-i; j++) {
           if (to_sort[j] > to_sort[j+1]) {
               temp = to_sort[j];
               to_sort[j] = to_sort[j+1];
               to_sort[j+1] = temp;
           }
       }
    }
    for(i = 0; i < arr_size; i++) {
        printf("%d\n", to_sort[i]); 
    }
    
}