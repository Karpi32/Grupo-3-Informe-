class Cliente:
    
    def __init__(self,_nombre,_CUI) -> None:
        self.nombre = _nombre
        self.CUI = _CUI
        pass
    def Obtener_clientes(self):
        return [self.nombre,self.CUI]
    def Update_cliente(self,nombre,CUI):
        self.nombre = nombre
        self.CUI = CUI 