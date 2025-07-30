import runtime
from sys import exit

while True:
    file_name = '<stdin>'

    try:
        text = input('RUNTIME > ')
    except KeyboardInterrupt:
        exit(0)

    ## MAKE TOKENS
    # result, error = runtime.make_tokens(file_name, text)

    ## MAKE AST
    # ast = runtime.generate_ast(tokens)
    # result = ast.node
    # error = ast.error
    
    ## RUN
    result, error = runtime.run(file_name, text)

    if error: print(error)
    else: print(result)