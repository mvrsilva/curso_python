ano = int(input("Digite o ano de seu nascimento: "))


if ano <= 1964:
    print("Geração Baby boomer")

elif ano >= 1965 and ano <= 1979:
    print("Geração X")

elif ano >= 1980 and ano <= 1994:
    print("Geração Y") 

else: 
        print("Geracação Z")

