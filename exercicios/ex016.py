class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self, user):
        self.user = user
        
    def set_password(self, password):
        self.password = password
        
    @classmethod
    def creat_with_auth(cls, user, password):
        conection = cls()
        conection.user = user
        conection.password = password
        return conection
    
    @staticmethod
    def somar(x, y):    
        return x+y
        
            
# c1 = Connection()
c1= Connection.creat_with_auth('luiz', '123')
print(c1.user)
print(c1.password)
print(Connection.somar(1, 4))