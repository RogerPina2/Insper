void selection_sort(int v[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int m = i;

        for (int j = i; j < n; j++) {
            if (v[m] > v[j]) {
                m = j;
            }
        }

        if (m != i) {
            int temp = v[m];
            v[m] = v[i];
            v[i] = temp;
        }
    }
}