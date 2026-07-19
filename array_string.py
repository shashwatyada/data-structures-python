# String Operations
def string_demo():
    print("-----String Operations-----")

    text = "LeetCode"
    print("Original String:", text)

    # 1. Indexing (Accessing characters by index)
    print("Character at index 4 = 'C':", text[4])
    print("Charater at index -1 = 'e':", text[-1])
    print("Character at index 0 = 'L':", text[0])

    # Slicing [start:end] -> end index is excluded
    print("Slice from index 0 to 4:", text[0:4], " || ", text[4:])

    # Reversing the string
    reversed_text = text[::-1]
    print("Reverse String : ", reversed_text)

    # Built-in Method
    print(" Upper Case :", text.upper() , " || Lower Case :", text.lower(), len(text))


# Array (List) Operations
def array_demo():
    print("-----Array (List)------")

    #Array Defination
    arr = [10, 20, 30, 40]
    print("Original Array : ", arr)

    # Insertion 
    arr.append(50) # Adds to the end
    print(" After 50 : ", arr)

    arr.insert(1, 15) # Add 15 at index 1
    print(" After Insertion : ", arr)

    arr.pop() # Remove from the end
    print("After pop : ", arr)

    arr.remove(20)
    print(" After Remove : ", arr)
    
    print(" Slice : ", arr[1:3])

    for num in arr:
        print("Element : ", num)

# Execution Block
if __name__ == "__main__":
    string_demo()
    array_demo()