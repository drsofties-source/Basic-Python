print("NOT")
a = True
b = not a 
c = True
d = False
print(f"Nilai b = {b}", "\n")
print("OR (|)")
print(f"True Or False = {a|b}")
print(f"False Or True = {a|b}")
print(f"True Or True = {a|c}")
print(f"False Or False = {d|b}","\n")
print("AND")
print(f'True & True = {a&c}')
print(f'True & False = {a&b}')
print(f'False & True = {b&a}')
print(f'False & False = {b&d}')
print("XOR")
print(f'True ^ True = {a ^ c}')
print(f'True ^ False = {a ^ b}')
print(f'False ^ True = {b ^ a}')
print(f'False ^ False = {b ^ d}')

        #==> Kenapa tidak menggunakan &,  digunakan pada operasi bitwise
        # and lebih cocok untuk digunakan pada operasi logika