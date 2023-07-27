# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 20:13:37 2023

@author: mahmoud
"""

##### Function to get matrix from input
##### O(n2)
def getMatrixFromInput(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter value for element ({i}, {j}): "))
            row.append(element)
        matrix.append(row)
    return matrix


##### Function to add two matrices and display them
def addMatrices(matrix1, matrix2):
    print("\nEnter dimensions for the first matrix:")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix1 = getMatrixFromInput(m, n)


    print("\nEnter dimensions for the second matrix:")
    p = int(input("Enter number of rows: "))
    q = int(input("Enter number of columns: "))
    matrix2 = getMatrixFromInput(p, q)

    if m != p or n != q:
        print("Matrices cannot be added. Dimensions are not compatible.")
    else:
        result_matrix = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result_matrix.append(row)
    return result_matrix


##### Function to check rotation
def areMatricesEqual(matrix1, matrix2):
    """
    Check if two matrices are equal.
    """
    return matrix1 == matrix2

def checkRotation():
    
    print("\nEnter dimensions for the first matrix:")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix1 = getMatrixFromInput(m, n)


    print("\nEnter dimensions for the second matrix:")
    p = int(input("Enter number of rows: "))
    q = int(input("Enter number of columns: "))
    matrix2 = getMatrixFromInput(p, q)
    """
    Check if matrix1 is a rotation of matrix2 or vice versa.
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False

    # Check if matrix2 is a rotation of matrix1
    for _ in range(4):  # We check all possible rotations (0, 90, 180, 270 degrees)
        if areMatricesEqual(matrix1, matrix2):
            return True

        # Manually rotate matrix2
        matrix2 = [[matrix2[j][i] for j in range(len(matrix2))] for i in range(len(matrix2[0]) - 1, -1, -1)]

    return False


##### Function to invert dictionary
def invertDictionary():
    def invert_dict(d):
        return {v: k for k, v in d.items()}

    original_dict = eval(input("Enter a dictionary (in the format {'key': 'value'}): "))
    inverted_dict = invert_dict(original_dict)
    print("Inverted Dictionary:", inverted_dict)



##### Function to convert matrix to dictionary
def convertMatrixToDictionary():
    def matrix_to_dict(matrix):
        dictionary = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dictionary[(i, j)] = matrix[i][j]
        return dictionary

    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    matrix = []

    print(f"Enter {rows} rows with {cols} elements in each row:")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    dictionary = matrix_to_dict(matrix)
    print("Dictionary representation of the matrix:", dictionary)


##### Function to check palindrome
def checkPalindrome():
    def is_palindrome(word):
        return word == word[::-1]

    word = input("Enter a word: ")
    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")

##### Function to search for an element
##### time complexity o(NlogN)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr
def searchAndSortElement():
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    arr = list(map(int, input("Enter space-separated integers for the list: ").split()))
    target = int(input("Enter the element to search for: "))

    arr = mergeSort(arr)
    index = binary_search(arr, target)

    if index != -1:
        print(f"Element {target} found at index {index}.")
        print("Sorted list using merge sort:", arr)
    else:
        print(f"Element {target} not found in the list.")

    
# Main program
def main():
    name = input("Enter your name: ")
    print(f"Welcome {name} I'm here to assist you :)")

    while True: # I use it to go out(break) when choice is Exit
        print("\nMenu:")
        print("1. Add Matrices")
        print("2. Check Rotation")
        print("3. Invert Dictionary")
        print("4. Convert Matrix to Dictionary")
        print("5. Check Palindrome")
        print("6. Search for an Element") #(BONUS: Search, if element found then sort using merge sort algorithm)
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            print("\nResultant matrix after addition:")
            result_matrix = addMatrices([[1,2],[3,4]],[[1,2],[3,4]])
            print(result_matrix)
        elif choice == 2:
            result = checkRotation()
            if result:
                print("The matrices are rotations of each other.")
            else:
                print("The matrices are not rotations of each other.")
        elif choice == 3:
            invertDictionary()
        elif choice == 4:
            convertMatrixToDictionary()
        elif choice == 5:
            checkPalindrome()
        elif choice == 6:
            searchAndSortElement()
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7).")

main()