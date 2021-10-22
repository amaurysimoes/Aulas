peso=float(input("Qual o teu peso: "))
h=float(input("qual tua altura:  "))
sexo = str(input("sexo M-Masculino, F- feminino "))

if(sexo == "M"):
    pesoIdHom = ((72.7 * h) - 58)
    print("Seu peso Ideal é: %.2f"%pesoIdHom)
    if(peso >= pesoIdHom):
        print("voce esta acima do seu peso ideal")
    else:
        print("Voce esta abaixo do seu peso ideal")

if(sexo == "F"):
    pesoIdmulh = ((62.1 * h) - 44.7)
    print("Seu peso Ideal é: %.2f"%pesoIdmulh)
    if(peso >= pesoIdmulh):
        print("voce esta acima do seu peso ideal")
    else:
        print("Voce esta abaixo do seu peso ideal")