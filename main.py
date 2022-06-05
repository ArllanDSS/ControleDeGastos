from datetime import datetime

despesas = [{
    "ID": 1000,
    "Data": '05/06/2022',
    "Horario": '02:43',
    "Despesa": 'UBER BLACK VIP EE',
    "Valor": 1.00,
    "Descricao": 'Lorem ipsum dolor sit amet. '
}, {
    "ID": 1000,
    "Data": '05/06/2022',
    "Horario": '02:43',
    "Despesa": 'UBER',
    "Valor": 10.00,
    "Descricao": 'Lorem ipsum dolor sit amet. '
}, {
    "ID": 1000,
    "Data": '05/06/2022',
    "Horario": '02:43',
    "Despesa": 'UBER BLACK VIP',
    "Valor": 100.00,
    "Descricao": 'Lorem ipsum dolor sit amet. '
}, {
    "ID": 1000,
    "Data": '05/06/2022',
    "Horario": '02:43',
    "Despesa": 'UBER BLACK VIP',
    "Valor": 1000.00,
    "Descricao": 'Lorem ipsum dolor sit amet. '
}, {
    "ID": 1000,
    "Data": '05/06/2022',
    "Horario": '02:43',
    "Despesa": 'UBER BLACK VIP',
    "Valor": 10000.00,
    "Descricao": 'Lorem ipsum dolor sit amet. '
}]
tabela = [
    '---------------------------------------------------------------',
    '                      RELATÓRIO DE DESPESAS                    ',
    '---------------------------------------------------------------',
    ' ID       Data       Horário        Despesa            Valor   ',
    '----  ------------  ---------  -----------------  -------------'
]


def addDespesa():
    id, dt, time, desp, val, desc = 0, str(), str(), str(), str(), str()
    # Entrada e Validação da data

    res = False
    while res == False:
        dt = input('Data e Hora (dd/mm/aaaa hh:mm): ')
        format = "%d/%m/%Y %H:%M"
        try:
            res = bool(datetime.strptime(dt, format))
            break
        except ValueError:
            print(
                'Erro: Data ou Horário inválido. (Tente     dd/mm/aaaa hh/mm)')
            res = False
    dt, time = dt.split()
    # Entrada e Validação da despesa.

    res = False
    while res == False:
        desp = input('Despesa: ')
        if len(desp) > 15:
            print('Erro: Limite de caracteres excedido. (Max.15)')
        else:
            res = True

    # Entrada e Validação de valor.
    res = False
    while res == False:
        val = input('Valor: ')
        try:
            res = float(val) // 1
            break
        except ValueError:
            print('Erro: Valor inválido! (Tente 0.0)')

    desc = input('Descrição: ')

    if len(despesas) == 0:
        id = 1
    else:
        id = len(despesas) + 1

    despesas.append({
        "ID": id,
        "Data": dt,
        "Horario": time,
        "Despesa": desp,
        "Valor": f'{float(val):.2f}',
        "Descricao": desc
    })


def mostrarTabela():

    for n in tabela:
        print(n)
    for i in despesas:
        tooString = str()
        cont = 0
        v_aux = 0
        for j in i:
            if cont == 0:
                tooString += str(i[j]).ljust(7)
            elif cont == 1:
                tooString += str(i[j]).rjust(10)
            elif cont == 2:
                tooString += str(i[j]).rjust(10)
            elif cont == 3:
                tooString += str(i[j]).rjust(13 + len(i[j]) // 2)
                v_aux = (17 - (len(i[j]))) // 2
            elif cont == 4:
                v = f'R$ {i[j]:.2f}'
                v_len = len(v) - 7 // 2 + 7
                v_aux += v_len
                tooString += f'{v:>{v_aux}}'
                break
            cont += 1

        print(tooString)


mostrarTabela()
