def bin_search(a, key):
    low = 0
    high = len(a) - 1
    while low < high:
        mid = (low + high) // 2
        if a[mid] == key:
            return True
        elif a[mid] > key:
            high = high -1
        elif a[mid] < key:
            low = low + 1
    return False
def recur_bin_search(a, low, high, key):
    if high >= low:
        mid = low + (high - low) // 2
        if a[mid] == key:
            return True
        elif a[mid] > key:
            return recur_bin_search(a, low, mid - 1, key)
        return recur_bin_search(a, mid + 1, high, key)
    else:
        return False


a = list(range(1, 100, 1))
# print(bin_search(a, 101))
print(recur_bin_search(a, 0, len(a)-1, 101))