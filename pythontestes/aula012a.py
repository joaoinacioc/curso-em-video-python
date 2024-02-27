nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'João':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino!')
print(f'Tenha um bom dia, {nome}!')
