import runtime

while True:
    text = input('RUNTIME > ')
    result, error = runtime.run('<stdin>', text)

    if error: print(error)
    else: print(result)