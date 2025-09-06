import numpy as np
import matplotlib.pyplot as plt
class FourVector:
    """
    This is the class of Four Vectors as defined in STR and GR.
    The Attributes of this class are :
    1) ct:time like component(initialised to 0)
    2) r:space like componenet(initialised to null vector)
    """
    def __init__(self , ct = 0 , r = [0,0,0]):
        self._r = np.array(r , dtype=float)
        self._ct = ct
        if len(self._r)!=3:
            raise Exception("FourVector parameter r has incorrect size")
        #print(f"Four Vector has been initialised with time and space components as : {self.ct , self.r}")
    def __repr__(self):
        return f"FourVector(ct = {self._ct} , r = ({self._r}))"
    def __str__(self):
        return f"({self._ct} , {self._r[0]} ,{self._r[1]} , {self._r[2]})"
    def ct(self):
        return self._ct
    def r(self):
        return self._r
    def setr(self , new_r = None):
        if new_r is not None:
            self._r = new_r
    def setct(self , new_ct = None):
        if new_ct is not None:
            self._ct = new_ct
    def copy(self):
        return FourVector(ct=self._ct , r = self._r)
    def __add__(self ,other):
        return FourVector(ct=self._ct+other._ct , r = self._r+other._r)
    def __iadd__(self , other):
        self._ct+=other._ct
        self._r+=other._r
        return self
    def __sub__(self,other):
        return FourVector(ct=self._ct-other._ct , r = self._r-other._r)
    def __isub__(self , other):
        self._ct-=other._ct
        self._r-=other._r
        return self
    def inner(self ,other):
        return self._ct*other._ct - np.dot(self._r , other._r)
    def magsquare(self):
        return self.inner(other=self)
    def boost(self , beta):
        gamma = 1/np.sqrt(1-beta**2)
        z_new = gamma*(self._r[2]-beta*self._ct)
        ct_new = gamma*(self._ct - beta*self._r[2])
        return FourVector(ct=ct_new , r =[self._r[0] , self._r[1] , z_new])
    
    


#  ct' = gamma(ct-beta*x)
    

    




    
        