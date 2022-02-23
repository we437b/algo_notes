#include <stdio.h>

// 알고리즘은 먼저 손으로 해보세요
// Insert only when needed, so faster but still O(n^2) cuz worst case

int main(void) {
    int to_sort[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
    int j, temp;
    int arr_size = sizeof(to_sort)/sizeof(int);
    
    for (int i = 0; i < arr_size-1;i++) {
        j = i;
        while (j >= 0 && (to_sort[j] > to_sort[j+1])) {
            temp = to_sort[j];
            to_sort[j] = to_sort[j+1];
            to_sort[j+1] = temp;
            // because we need to make sure everything before i is sorted
            // Are You Dumb Eugene
            j--;
        }
    }
    for(int i = 0; i < arr_size; i++) {
        printf("%d\n", to_sort[i]); 
    }
    
}