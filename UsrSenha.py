while True:
    
    usr = str(input(Usuario: ))
    senha = str(input(Senha: ))
    
    if( usr == senha):
        print('Erro! Usuario nao pode ser igual a senha, tente novamente.')
    else:
        break
