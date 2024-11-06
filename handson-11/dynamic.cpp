#include <iostream>

class DynamicArray {
private:
    int *arr;      // Pointer to the dynamically allocated array
    int capacity;  // Current capacity of the array
    int size;      // Current number of elements in the array

public:
    // Constructor
    DynamicArray() {
        capacity = 10; // Initial capacity
        size = 0;
        arr = new int[capacity];
    }

    // Destructor
    ~DynamicArray() {
        delete[] arr;
    }

    // Function to add an element to the array
    void push_back(int element) {
        if (size == capacity) {
            // If the array is full, double the capacity
            capacity *= 2;
            int *newArr = new int[capacity];
            for (int i = 0; i < size; ++i) {
                newArr[i] = arr[i];
            }
            delete[] arr;
            arr = newArr;
        }
        arr[size++] = element;
    }

    // Function to get the element at a given index
    int at(int index) {
        if (index < 0 || index >= size) {
            std::cerr << "Index out of bounds\n";
            exit(1);
        }
        return arr[index];
    }

    // Function to get the current size of the array
    int getSize() {
        return size;
    }

    // Function to get the current capacity of the array
    int getCapacity() {
        return capacity;
    }

    // Function to clear the array
    void clear() {
        delete[] arr;
        size = 0;
        capacity = 10;
        arr = new int[capacity];
    }
};

int main() {
    // Example usage
    DynamicArray dynArray;

    // Pushing elements into the dynamic array
    for (int i = 0; i < 15; ++i) {
        dynArray.push_back(i * 10);
    }

    // Accessing elements using at() function
    std::cout << "Elements in the dynamic array:\n";
    for (int i = 0; i < dynArray.getSize(); ++i) {
        std::cout << dynArray.at(i) << " ";
    }
    std::cout << std::endl;

    // Displaying the size and capacity
    std::cout << "Current size: " << dynArray.getSize() << "\n";
    std::cout << "Current capacity: " << dynArray.getCapacity() << "\n";

    return 0;
}
