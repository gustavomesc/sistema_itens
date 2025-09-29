class item:
    def __init__(self,id,descricao,quantidade):
        self.set_descricao(descricao)
        self.set_quantidade(quantidade)
        self.set_id(id)
    def set_descricao(self,valor):
        self.__descricao = valor
    def set_quantidade(self,valor):
        self.__quantidade = valor
    def get_descricao(self):
        return self.__descricao
    def get_quantidade(self):
        return self.__quantidade
    def set_id(self,valor):
        self.__id = valor
    def get_id(self):
        return self.__id