void bubble_sort(int v[], int n) {
    for (int i = n - 1; i > 0; i--) {
        int swapped = 0;

        for (int j = 0; j < i; j++) {
            if (v[j] > v[j + 1]) {
                int temp = v[j];
                v[j] = v[j + 1];
                v[j + 1] = temp;
                swapped = 1;
            }
        }

        printf(5);

        if (!swapped) {
            break;
        }
    }
}

int main() {
    int v[5] = {6, 9, 8, 5, 7}; 

    bubble_sort(v, 5);

    return 0;
}