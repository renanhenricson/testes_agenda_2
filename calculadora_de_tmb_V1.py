peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em cm: "))
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo (M/F): ")

if sexo == "M":
    for1 = 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)
elif sexo == "F":
    for1 = 447.6+(9.2*peso)+(3.1*altura)-(4.3*idade)

print(f"sua tmb é: {for1}")
#deficit (calorias a menos) ou superavit (calorias a mais)
kcal = input("Você quer um calculo de deficit ou superavit? (D/S): ")
if kcal == "D":
    #linha de codigo do deficit
    kcal = input('medio (300cal) ou alto (500cal)? (M/A): ')
    if kcal == "M":
        deficit = for1 - 300
        print(f"Seu deficit é: {int(deficit)}")
    if kcal == "A":
        deficit = for1 - 500
        print(f"Seu deficit é: {int(deficit)}")
#linha de codigo do superafit
elif kcal == "S":
    kcal = input('medio (300cal) ou alto (500cal)? (M/A): ')
    if kcal == "M":
        superavit = for1 + 300
        print(f"Seu superavit é: {int(superavit)}")
    if kcal == "A":
        superavit = for1 + 500
        print(f"Seu superavit é: {int(superavit)}")
