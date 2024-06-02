from trace_monoid import TraceMonoid
from word import Word, Letter
import typing as tp
import math
class ElementOfMonoid(TraceMonoid):
    def reconstruction( self,projections: tp.List[Word]):
        word=""
        length = len(projections)
        alphabet=len(self.alphabet)
        if(length!=(math.factorial(alphabet+1)/(math.factorial(alphabet-1)*2))):
            return "Wrong input"
        while len(projections)!=0:
         hasse=[]
         for projection in projections:
            for letter in projection:
                if letter != projection[0]:
                     hasse.append((projection[0],letter))
         for el in (x[0] for x in hasse):
            if el not in (x[1] for x in hasse):
                letter=el
         word+=letter
         newprojections=projections[:]
         for projection in newprojections:
          if  letter == projection[0]:
            projections.remove(projection)
            if len(projection)!=1:
                projections.append(projection[1:])
        return Word(word)
    def reconstructionPartiallyCommutative( self,projections: tp.List[Word]):
        word=""
        while len(projections)!=0:
         hasse=[]
         for projection in projections:
            for letter in projection:
                if letter != projection[0]:
                     hasse.append((projection[0],letter))
         letter=[]
         for el in (x[0] for x in hasse):
            if el not in (x[1] for x in hasse) and el not in letter:
                letter+=el
                word+=el
         if len(hasse)==0:
             for el in projections:
                 if el not in letter:
                     letter+=el
                     word+=el
         newprojections=projections[:]
         for lett in letter:
          for projection in newprojections:
               if  lett == projection[0]:
                   projections.remove(projection)
                   if len(projection)!=1:
                     projections.append(projection[1:])
        return Word(word)

