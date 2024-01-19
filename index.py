print("Calculadora de Ano Bissexto\n")

year = int(input("Qual o ano que deseja checar?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"\n{year} é um ano bissexto")
        else:
            print(f"\n{year} não é um ano bissexto")
    else:
        print(f"\n{year} é um ano bissexto")
else:
    print(f"\n{year} não é um ano bissexto")

enter = input("\nAperte Enter para fechar")