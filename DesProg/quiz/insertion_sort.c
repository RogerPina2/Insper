void insertion_sort(int v[], int n) {
    for (int i = 1; i < n; i++) {
        int temp = v[i];

        int h = i;
        while (h > 0 && temp < v[h - 1]) {
            v[h] = v[h - 1];
            h--;
        }

        v[h] = temp;
    }
}