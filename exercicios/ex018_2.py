class Carrinho:
    def __init__(self,):
        self._produtos = []
        
    def total(self):
        return sum(p.valor for p in self._produtos)
        
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
            
    def listar_produtos(self):
        for produto in self._produtos:
            print(f'{produto.nome}: {produto.valor}')
        
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
carrinho = Carrinho()
p1, p2 = Produto('Creme de cabelo', 14.0), Produto('Camisa', 10)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())