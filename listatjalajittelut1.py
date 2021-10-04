def sort1D(a):
    n = len(a)
    for i in range(n):
        minind = i

        for j in range (i+1, n):
            if (a[minind] > a[j]):
                minind = j

        a[i], a[minind] = a[minind], a[i]
    return a
  