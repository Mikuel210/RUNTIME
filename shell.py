import runtime
from sys import exit

while True:
    file_name = '<stdin>'

    try:
        text = input('RUNTIME > ')

        if text.strip() == '':
            continue
    except KeyboardInterrupt:
        exit(0)

    ## MAKE TOKENS
    #result, error = runtime.make_tokens(file_name, text)

    ## MAKE AST
    # ast = runtime.generate_ast(result)
    # result = ast.node
    # error = ast.error
    
    ## RUN
    result, error = runtime.run(file_name, text)

    if error: print(error)
    else:
        if isinstance(result, runtime.List) and len(result.value) == 1:
            print(repr(result.value[0]))
        else:
            print(repr(result))