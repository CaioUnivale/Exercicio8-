class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        desconto_valor = self.preco * percentual / 100
        preco_com_desconto = self.preco - desconto_valor
        return preco_com_desconto

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor
    
    def desconto(self, percentual):
        desconto_geral = super().desconto(percentual)
        desconto_adicional = desconto_geral * 0.10
        preco_com_desconto = desconto_geral - desconto_adicional
        return preco_com_desconto

class Jogo(Produto):
    def __init__(self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma


produto_generico = Produto("Produto Genérico", 100)
preco_com_desconto = produto_generico.desconto(20)
print(f"Preço com desconto: {preco_com_desconto}")

livro = Livro("O Senhor dos Anéis", 50, "J.R.R. Tolkien")
preco_livro_com_desconto = livro.desconto(15)
print(f"Preço do livro com desconto: {preco_livro_com_desconto}")

jogo = Jogo("The Witcher 3", 60, "PC")
preco_jogo_com_desconto = jogo.desconto(10)
print(f"Preço do jogo com desconto: {preco_jogo_com_desconto}")