def inverte_string(string):
    nova_string = ""
    for char in string:
        nova_string = char + nova_string
    return nova_string

string_original = input("Digite uma string: ")
string_invertida = inverte_string(string_original)
print("String invertida:", string_invertida)
