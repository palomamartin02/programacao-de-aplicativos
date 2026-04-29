n = float(input("Nota: "))
x = int(input("Anos XP: "))
c = input("Certificado (s/n): ")


def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    if possui_certificacao == "s" or (nota_teste > 80 and anos_xp > 2):
        return True
    else:
        return False

if verificar_aprovacao(n, x, c):
    print("Contratar")
else:
    print("Descartar")