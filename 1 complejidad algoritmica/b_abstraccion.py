def f(x):
    respuesta = 0             # -> 1
    for i in range(1000):     # -> 1000
        respuesta += 1

    for i in range(x):        # -> x
        respuesta += x

    for i in range(x):        # -> x^2
        for j in range(x):
            respuesta += 1
            respuesta += 1
    return respuesta          # -> 1

                              # --- total ---
                              # -> 1002 + x + 2x^2

# print(f(100000)) # 300001000
# print(f(10000)) # 300001000
# print(f(1000)) # 3001000