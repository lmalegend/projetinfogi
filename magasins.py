



class Magasin:
    '''
    Classe modelisant un magasin par ses differentes variables:
    - Sa capacite de stockage (produits)
    - Son cout de stockage (€/jour/produit)
    - Son stock initial (produits)
    - Son stock cible final (produits)
    - Son historique de demande (Liste de [produits/jour])
    '''
    def __init__(self, capa: int, cout: float, init: int, final: int) -> None:
        self._capa: int = capa
        self._cout: float = cout
        self._init: int = init
        self._final: int = final
    
    @property
    def capacite (self) -> int:
        return self._capa

    @property
    def cout (self) -> float:
        return self.cout

    @property
    def initialise (self) -> int:
        return self._init

    @property
    def final (self) -> int:
        return self._final