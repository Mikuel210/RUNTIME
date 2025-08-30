import runtime

file_name = input("Enter the file name: ")

with open(f"./data/{file_name}", 'r') as file:
    text = file.read()

    ## MAKE TOKENS
    #result, error = runtime.make_tokens(file_name, text)

    ## MAKE AST
    #ast = runtime.generate_ast(result)
    #result = ast.node
    #error = ast.error
    
    ## RUN
    result, error = runtime.run(file_name, text)
    if error: print(error)