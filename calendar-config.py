from datetime import date


def wrong_file():
    print('Desculpe, você deve iniciar o programa principal para isso funcionar! :(')


if __name__ == '__main__':
    wrong_file()
else:
    calendar = date.today()
    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    def show_date():
        print(f'Dia: {calendar.day}')

        if calendar.month == 1:
            print(f'Mês: {months[0]}')

        if calendar.month == 2:
            print(f'Mês: {months[1]}')

        if calendar.month == 3:
            print(f'Mês: {months[2]}')

        if calendar.month == 4:
            print(f'Mês: {months[3]}')

        if calendar.month == 5:
            print(f'Mês: {months[4]}')

        if calendar.month == 6:
            print(f'Mês: {months[5]}')

        if calendar.month == 7:
            print(f'Mês: {months[6]}')

        if calendar.month == 8:
            print(f'Mês: {months[7]}')

        if calendar.month == 9:
            print(f'Mês: {months[8]}')

        if calendar.month == 10:
            print(f'Mês: {months[9]}')

        if calendar.month == 11:
            print(f'Mês: {months[10]}')

        if calendar.month == 12:
            print(f'Mês: {months[11]}')

        print(f'Ano: {calendar.year}')
    show_date()
    special_days = [
        'Ano Novo', 'Dia do Esportista', 'Carnaval', 'Dia Internacional da Mulher', 'Dia do consumidor', 'Páscoa', 'Dia de Tiradentes', 'Dia do Livro', 'Dia do Trabalho', 'Dia das Mães', 'Dia dos Namorados', 'Corpus Christi', 'Dia do Homem', 'Dia dos Pais', 'Dia do Solteiro', 'Dia da Independência do Brasil', 'Dia das Crianças', 'Dia de Nossa Senhora Aparecida', 'Proclamação da República', 'Black Friday', 'Cyber Monday', 'Natal'
        ]
    if calendar.month == 1 and calendar.day == 1:
        print(f'Dia especial: {special_days[0]}')
    if calendar.month == 2 and calendar.day == 19:
        print(f'Dia especial: {special_days[1]}')
    if calendar.month == 3 and calendar.day == 5:
        print(f'Dia especial: {special_days[2]}')
    if calendar.month == 3 and calendar.day == 8:
        print(f'Dia especial: {special_days[3]}')
    if calendar.month == 3 and calendar.day == 15:
        print(f'Dia especial: {special_days[4]}')
    if calendar.month == 4 and calendar.day == 21:
        print(f'Dias especiais: {special_days[5]} e {special_days}')
    if calendar.month == 5 and calendar.day == 23:
        print(f'Dia especial: {special_days[6]}')
    if calendar.month == 6 and calendar.day == 1:
        print(f'Dia especial: {special_days[7]}')
    if calendar.month == 6 and calendar.day == 12:
        print(f'Dia especial: {special_days[8]}')
    if calendar.month == 6 and calendar.day == 12:
        print(f'Dia especial: {special_days[9]}')
    if calendar.month == 7 and calendar.day == 12:
        print(f'Dia especial: {special_days[10]}')
    if calendar.month == 7 and calendar.day == 20:
        print(f'Dia especial: {special_days[11]}')
    if calendar.month == 8 and calendar.day == 15:
        print(f'Dia especial: {special_days[12]}')
    if calendar.month == 9 and calendar.day == 11:
        print(f'Dia especial: {special_days[13]}')
    if calendar.month == 9 and calendar.day == 15:
        print(f'Dia especial: {special_days[14]}')
    if calendar.month == 9 and calendar.day == 7:
        print(f'Dia especial: {special_days[15]}')
    if calendar.month == 10 and calendar.day == 12:
        print(f'Dia especial: {special_days[16]}')
    if calendar.month == 11 and calendar.day == 15:
        print(f'Dia especial: {special_days[17]}')
    if calendar.month == 11 and calendar.day == 29:
        print(f'Dia especial: {special_days[18]}')
    if calendar.month == 12 and calendar.day == 2:
        print(f'Dia especial: {special_days[19]}')
    if calendar.month == 12 and calendar.day == 25:
        print(f'Dia especial: {special_days[20]}')