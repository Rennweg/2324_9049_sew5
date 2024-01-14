#LUCA SAUTTER 5AX
class BritishWeights:
    '''
        >>> st1 = BritishWeights(2,4)
        >>> st2 = BritishWeights(1,16)
        >>> st3 = BritishWeights(7,13)
        >>> print(st1)
        2 st 4 lb
        >>> print(st2)
        2 st 2 lb
        >>> print(st1 + st2)
        4 st 6 lb
        >>> print(st1 + st3)
        10 st 3 lb
        >>> st4 = BritishWeights(0, 27)
        >>> print(st4)
        1 st 13 lb


    '''
    stone = 0
    pounds = 0
    def __init__(self, stone, pounds):
        '''
        Konstruktor der Klasse BritishWeight
        :param stone:
        :param pounds:
        '''
        self.pounds = pounds % 14
        self.stone = stone + (pounds // 14)

    def __str__(self):
        '''
        String methode der Klasse BritishWeights
        :return:
        '''
        if self.stone > 0:
            return f"{self.stone} st {self.pounds} lb"
        else:
            return f"{self.pounds} lb"

    def __add__(self, other):
        '''
        Addiert zwei British Weights miteinander
        :param other:
        :return:
        '''
        if isinstance(other, BritishWeights):
            return BritishWeights((self.stone + other.stone),(self.pounds + other.pounds))
        else:
            raise TypeError('Please use only BritishWeights for addition!')


