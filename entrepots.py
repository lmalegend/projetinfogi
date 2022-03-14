


class Entrepot:
    '''
    Classe modelisant un entrepot par ses varialbes:
    - Sa capacite de stockage (produits)
    - Son cout de stockage (€/produit/jour)
    - Son stock initial (produits)
    - Son stock final cible (produits)
    '''
    def __init__(self, capa_stock: int, cout_stock: float, stock_init: int, stock_final: int) -> None:
        self._capa: int = capa_stock
        self._cout: float = cout_stock
        self._init: int = stock_init
        self._final: int = stock_final

    
    @property
    def capacite(self)-> int:
        return self._capa

    @property 
    def cout(self)-> float:
        return self._cout
    
    @property
    def init(self)-> int:
        return self._init

    @property
    def final(self)-> int:
        return self._final

    
    




    
    