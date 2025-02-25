#include <iostream>
#include <chrono>
#include <vector>

using namespace std;
using namespace std::chrono;

// Hàm Merge Sort đã được cài đặt
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Gọi đệ quy hàm Merge Sort
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Ghép hai mảng lại
        // (Thêm mã ghép mảng ở đây)
    }
}

int main() {
    // Tạo mảng ngẫu nhiên
    vector<int> arr = {5, 2, 9, 1, 5, 6};
    
    // Bắt đầu đo thời gian
    auto start = high_resolution_clock::now();

    // Gọi thuật toán Merge Sort
    mergeSort(arr, 0, arr.size() - 1);

    // Kết thúc đo thời gian
    auto end =