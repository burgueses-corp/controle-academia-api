from pydoc import cli
from client import client_list

def main():

    for client in client_list:
        print(client.nome,client.cpf,client.email,client.telefone,client.data_de_nascimento)

if __name__=='__main__':
    main()