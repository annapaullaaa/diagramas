class Artigo:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def getArtigo(self):
        return "Titulo:" + self.titulo + " | " + "Autor:" + self.autor
    
class Edicao:
    def __init__ (self, numero, volume, data):
        self.numero = numero
        self.volume = volume
        self.data = data
        self.artigos = []
        
    def addNovoArtigo(self, artigo):
        self.artigos.append(artigo)
        
    def getEdicao(self):
        return "Edição número: " + str(self.numero) + " | " + "Volume: " + str(self.volume) + " | " + "Data: " + str(self.data)
    
    def removerArtigo(self, titulo):
        indice = None
        for i, artigo in enumerate(self.artigos):
            if artigo.titulo == titulo:
                indice = i
                break
        if indice is not None:
            self.artigos.pop(indice)
            
    def showArtigos(self):
        for artigo in self.artigos:
            print(artigo.getArtigo())
    
    def getNumeroDeArtigo(self):
        return len(self.artigos)
    
class Revista:
    def __init__(self, titulo, issn, periodicidade):
        self.titulo = titulo
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = []

    def addNovaEdicao(self, edicao):
        num_artigos = edicao.getNumeroDeArtigo()
        if(num_artigos >= 10 and num_artigos <= 15):
            self.edicoes.append(edicao)
            return "Edição Lançada com Sucesso!"
        else:
            return "É necessário no mínimo 10 artigos e no máximo 15 artigos para lançar a ediçao"

    def showEdicoes(self):
        for edicao in self.edicoes:
            print(edicao.getEdicao())