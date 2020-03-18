class Progression:
    '''Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2, ...
    '''

    def __init__(self, start=0):
        '''Initialize current to the first value of the progression.'''
        self._current = start
        
    def _advance(self):
        '''Update self. current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        '''
        self._current += 1

    def __next__(self):
        '''Return the next element, or else raise StopIteration error.'''
        if self._current is None: # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current # record current value to return
            self._advance( ) # advance to prepare for next time
            return answer # return the answer
    
    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator.'''
        return self

    def print_progression(self, n):
        '''Print next n values of the progression.'''
        print(' '.join(str(next(self)) for j in range(n)))

class GeometricProgression(Progression): # inherit from Progression
    '''Iterator producing a geometric progression.'''
    
    def __init__(self, base=0.5, start=65536):
        '''Create a new geometric progression.

        base the fixed constant multiplied to each term (default 2)
        start the first term of the progression (default 1)
        '''
        super().__init__(start)
        self._base = base
        self._start = start
    
    def _advance(self): # override inherited version
        '''Update current value by multiplying it by the base value.'''
        self._current **= self._base
        self._current = int(self._current)

obj = GeometricProgression()
obj.print_progression(3)