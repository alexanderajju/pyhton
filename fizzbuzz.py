def fizzbuzz():
    for fizzbuzz in range(1,101):
        if fizzbuzz % 2 == 0 and fizzbuzz % 7 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 2 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 7 == 0:
            print("buzz")
            continue
        print(fizzbuzz)

fizzbuzz()