#include <iostream>
using namespace std;

// 알고리즘은 먼저 손으로 해보세요
// Select unsorted front, switch with minimum
// O(n*n), but one swap

int main(void) {
    int to_sort[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
    int i, j, min, index, temp;
    int arr_size = sizeof(to_sort)/sizeof(int);
    
    for (i = 0; i < arr_size; i++) {
        min = 9999;
        for (j = i; j < arr_size; j++){
            if (to_sort[j] < min) {
                min = to_sort[j];
                index = j;
            }
        }
        temp = to_sort[i];
        to_sort[i] = min;
        to_sort[index] = temp;
    }
    for(i = 0; i < arr_size; i++) {
        printf("%d\n", to_sort[i]); 
    }
    
}