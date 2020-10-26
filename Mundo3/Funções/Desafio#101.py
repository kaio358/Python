
def voto(anos):
    from datetime import date
    atual = date.today().year
    idade = atual - anos
    if idade < 16 :
        return f'A idade {idade} insuficiente, NEGADO !!'
    if 16 <= idade <18 or idade>69:
        return f'A idade {idade} é OPICIONAL'
    if 18 <= idade <= 69:
        return f'A idade {idade} é OBRIGATORIO'
print(voto(int(input('Informe o ano de nascimento : '))))