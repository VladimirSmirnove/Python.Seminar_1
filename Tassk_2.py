# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
result = True
for X in True, False:
    for Y in True, False:
        for Z in True, False:
            print(f"{X = } {Y = } {Z = }     Result: {not (X or Y or Z) == (not X and not Y and not Z)}")
            