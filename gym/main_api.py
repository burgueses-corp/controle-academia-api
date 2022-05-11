from pydoc import cli
from gym import gym_list

def main():

    for gym in gym_list:
        print(gym.nome,gym.cnpj,gym.email,gym.telefone)

if __name__=='__main__':
    main()