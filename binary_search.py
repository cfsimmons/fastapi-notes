def binary_search(arr, input_val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if (arr[mid] == input_val):
            return mid
        elif (arr[mid] < input_val):
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    array = [2, 3, 4, 10, 40]
    my_val = 40

    result = binary_search(array, my_val)
    if result != -1:
        print(f"Element is present at index: {result}")
    else:
        print("Element is not present in array")


if __name__ == "__main__":
    main()
