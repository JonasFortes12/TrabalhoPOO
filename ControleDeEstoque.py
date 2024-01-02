from datetime import datetime

class ControleDeEstoque:
    def __init__(self, nome_produto, marca, validade, quantidade):
        self.nome_produto = nome_produto
        self.marca = marca
        self.validade = validade
        self.quantidade = int(quantidade)

    def get_nome_do_produto(self):
        return self.nome_produto

    def get_marca(self):
        return self.marca

    def set_marca(self, nova_marca):
        self.marca = nova_marca

    def data_valida(self):
        dia, mes, ano = self.validade.split("/")
        dia_data = '01/02/2024'
        dv_converter = datetime.strptime(self.validade, '%m/%d/%Y')
        dd_converter = datetime.strptime(dia_data, '%m/%d/%Y')
        
        if int(ano) >= 2024:
            qtd_dias = abs((dd_converter - dv_converter).days)
            return qtd_dias
        else:
            return False
        

    def controle_de_validade(self):
        controle = self.data_valida()
        
        if controle != False:
            if  controle == 1:
                print(f'Seu produto vence amanhã')
            elif controle < 5 and controle > 1:
                print(f'Seu produto vence em menos de {controle} dias')
            elif controle == 10:
                print(f'Seu produto vence em {controle} dias')
            elif controle == 30:
                print('Seu produto vence em 1 mês')
            elif controle > 30:
                print(f'Seu produto ira vencer em {controle} dias')
        else:
            print('Esse produto venceu')

    def get_quantidade(self):
        if self.quantidade == 0:
            print ('Esse produto esgotou')
        elif self.quantidade <= 5 and self.quantidade:
            print (f'Estoque baixo, temos apenas {self.quantidade}')
        elif self.quantidade >= 5 and self.quantidade <= 20:
            print (f'Reponha o estoque, temos apenas {self.quantidade}')
        else:
            print (f'{self.quantidade}')

    def set_quantidade(self, nova_quantidade):
        self.quantidade = self.quantidade - nova_quantidade


    def controle_de_compra(self, compra):
        if self.quantidade == 0:
            self.get_quantidade()
        elif compra == 0:
            print('Compra invalida')
        elif compra >= self.quantidade:
            print(f'Estoque baixo, temos apenas {self.quantidade}')
        else:
            print(f'compra realizada com sucesso')
    def __str__(self):
        return f'Produto {self.nome_produto} | marca: {self.marca} | validade: {self.validade} | quantidade {self.quantidade}'

sabonete = ControleDeEstoque('Sabonete', 'Lux', '02/02/2024', '0')
print(sabonete)
sabonete.controle_de_compra(3)
sabonete.controle_de_validade()

print('')
arroz  = ControleDeEstoque('Arroz', 'parborizado', '01/02/2023', '5')
print(arroz)
arroz.controle_de_compra(2)
arroz.get_quantidade()

arroz.controle_de_validade()


