def merge(arr, left, mid, right):
    # Kích thước của các mảng con
    n1 = mid - left + 1
    n2 = right - mid

    # Tạo mảng tạm thời
    L = arr[left:left + n1]  # Mảng bên trái
    R = arr[mid + 1:right + 1]  # Mảng bên phải

    # Chỉ số cho các mảng tạm thời và mảng gốc
    i = 0  # Chỉ số cho mảng bên trái
    j = 0  # Chỉ số cho mảng bên phải
    k = left  # Chỉ số cho mảng gốc

    # Trộn các phần tử vào mảng gốc
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Sao chép phần còn lại của L nếu có
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Sao chép phần còn lại của R nếu có
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2  # Tìm chỉ số giữa
        merge_sort(arr, left, mid)  # Sắp xếp nửa bên trái
        merge_sort(arr, mid + 1, right)  # Sắp xếp nửa bên phải
        merge(arr, left, mid, right)  # Hợp nhất

# Ví dụ sử dụng
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    merge_sort(arr, 0, len(arr) - 1)
    print("Mảng đã được sắp xếp:", arr)