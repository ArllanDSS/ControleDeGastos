from datetime import datetime

tabela = [
'----------------------------------------------------------------',
'                       RELATÓRIO DE DESPESAS                    ',
'----------------------------------------------------------------',
' ID       Data       Horário         Despesa           Valor    ',
'----  ------------  ----------  -----------------  -------------'
]
despesas = []


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
          print('Erro: Data ou Horário inválido. (Tente     dd/mm/aaaa hh/mm)')
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
        res = float(val)//1
        break
      except ValueError:
        print('Erro: Valor inválido! (Tente 0.0)')
        
    desc = input('Descrição: ')

    if len(despesas) == 0:
        id = 1
    else:
        id = len(despesas)+1

    despesas.append({"ID": id, "Data": dt, "Horario": time, "Despesa": desp, "Valor": f'{float(val):.2f}', "Descricao": desc })
