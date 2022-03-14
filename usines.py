



class Usine:
    '''
    Classe modelisant une usine par ses variables:
    - Sa capacite de stockage (produits)
    - Son cout de stockage (€/produit/jour)
    - Son stock initial (produits)
    - Son stock cible final (produits)
    - Sa capacite de production (produits/jour)
    - Son cout de production (€/produit)
    '''
    def __init__(self, capa: int, cout: float, init: int, final, capa_prod: int, cout_prod: int) -> None:
        self._capa_stock: int = capa
        self._cout_stock: float = cout
        self._stock_init: int = init
        self._stock_fin: int = final
        self._capa_prod: int = capa_prod
        self._cout_prod: float = cout_prod