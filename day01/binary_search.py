def binary_search(arr, input_val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"mid = ({low} + {high}) // 2")
        print(f"\nmid: {mid}")
        if (arr[mid] == input_val):
            print("Success")
            return mid
        elif (arr[mid] < input_val):
            low = mid + 1
            print(f"low: {low}")
        else:
            high = mid - 1
            print(f"high: {high}")
    return -1


def main():
    array = [1, 3, 5, 7]
    my_val = 7

    result = binary_search(array, my_val)
    if result != -1:
        print(f"Element is present at index: {result}")
    else:
        print("Element is not present in array")


if __name__ == "__main__":
    main()
