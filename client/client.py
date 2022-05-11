class Client:

    def __init__(self,nome,cpf,email,telefone,data_de_nascimento):
        self.nome=nome
        self.cpf=cpf
        self.email=email
        self.telefone=telefone
        self.data_de_nascimento=data_de_nascimento


client_list=[
    Client("Paulo","455.494.730-03","paulo@gmail.com","98152020","01/01/1990"),
    Client("Tulio","451.711.040-00","tulio@gmail.com","98001231","16/06/1995"),
    Client("Fernanda","691.280.600-75","fernanda@gmail.com","91102345","04/01/1999"),
]
