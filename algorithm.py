def merge_sort(arr):
    def merge(a1, a2):
        l1, l2 = len(a1), len(a2)

        if l1 * l2 == 0:
            return a1 or a2
        else:
            if a1[0] <= a2[0]:
                return a1[:1] + merge(a1[1:], a2)
            else:
                return a2[:1] + merge(a1, a2[1:])
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2

        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
