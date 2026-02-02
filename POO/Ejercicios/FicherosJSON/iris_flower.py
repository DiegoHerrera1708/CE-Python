class iris_flower:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, variety):
        self.__sepal_length = None
        self.__sepal_width = None
        self.__petal_length = None
        self.__petal_width = None
        self.__variety = None

        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.variety = variety

    @property
    def sepal_length(self):
        return self.__sepal_length
    
    @sepal_length.setter
    def sepal_length(self, sepal_length):
        if not isinstance(sepal_length, float) or sepal_length < 0:
            raise ValueError("El número debe ser flotante y positivo")
        self.__sepal_length = sepal_length

    @property
    def sepal_width(self):
        return self.__sepal_width
    
    @sepal_width.setter
    def sepal_width(self, sepal_width):
        if not isinstance(sepal_width, float) or sepal_width < 0:
            raise ValueError("El número debe ser flotante y positivo")
        self.__sepal_width = sepal_width

    @property
    def petal_length(self):
        return self.__petal_length
    
    @petal_length.setter
    def petal_length(self, petal_length):
        if not isinstance(petal_length, float) or petal_length < 0:
            raise ValueError("El número debe ser flotante y positivo")
        self.__petal_length = petal_length

    @property
    def petal_width(self):
        return self.__petal_width
    
    @petal_width.setter
    def petal_width(self, petal_width):
        if not isinstance(petal_width, float) or petal_width < 0:
            raise ValueError("El número debe ser flotante y positivo")
        self.__petal_width = petal_width

    @property
    def variety(self):
        return self.__variety
    
    @variety.setter
    def variety(self, variety):
        if not isinstance(variety, str) or not variety:
            raise ValueError("La variedad debe ser una cadena no vacía")
        self.__variety = variety

    def from_dict(self, data):
        self.sepal_length = data['sepal.length']
        self.sepal_width = data['sepal.width']
        self.petal_length = data['petal.length']
        self.petal_width = data['petal.width']
        self.variety = data['variety']
    
    def to_dict(self):
        return {
            'sepal.length': self.sepal_length,
            'sepal.width': self.sepal_width,
            'petal.length': self.petal_length,
            'petal.width': self.petal_width,
            'variety': self.variety
        }