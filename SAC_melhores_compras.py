usuario = input("Informe o e-mail cadastrado: ")
nota = int(input("Avalie, de 1 a 100, o seu nível de satisfação com o atendimento prestado: "))

if nota < 70:
    print("O atendimento foi insatisfatório")
elif 70 <= nota <= 89:
    print("O atendimento foi neutro")
else:  # nota >= 90
    print("O atendimento foi de qualidade")