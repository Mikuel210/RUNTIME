import runtime

file_name = input("Enter the file name: ")

with open(f"./data/{file_name}", 'r') as file:
    text = file.read()

    result, error = runtime.run(file_name, text)

    if error: print(error)
    else: 
        if len(result.elements) == 1:
            print(result.elements[0])
        else:
            print(result)