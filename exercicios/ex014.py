class Camera:
    def __init__(self, nome, filmando=False,):
        self.nome = nome
        self.filmando= filmando
        
    def filmar(self):
        if self.filmando:  #se filmando == true, aparece isso
            print(f'{self.nome} JÁ esta filmando...') 
            return
        print(f'{self.nome} está filmando...') 
        self.filmando = True #filmando se torna True
        
        
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não esta filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando=False
        
    def fotografar(self):
         if not self.filmando:
             print(f'{self.nome} está fotografando')
             return
         print(f'{self.nome} ja esta filmando, nao pode fotografar...')
         
        
# filmar, para de filmar, fotografar
c1 = Camera('Canon')
c2 = Camera('Sony')

c1.parar_filmar()
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
print()

c2.parar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()