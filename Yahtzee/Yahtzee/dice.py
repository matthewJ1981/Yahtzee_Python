from die import Die

class Dice:
    def __init__(self):
        self._dice = []
    
    def AddDice(self, d):
        self._dice.append(d)
    
    def RemoveDice(self, index):
        del self._dice[index]

    def Roll(self):
        for d in self._dice:
            d.Roll()
    
    def Size(self):
        return len(self._dice)

    def Empty(self):
        return self.Size() == 0
    
    def __getitem(self, index):
       return self._dice[index]

    def YahtzeeDice():
        dice = Dice()
        for i in range(5):
            dice._dice.append(Die())

        return dice;
    

    def __add__ (self, other):
        dice = Dice()

        for i in range(self.Size()):
            dice.AddDice(self[i])

        for i in range(other.Size()):
            dice.AddDice(other[i]);

        return dice;
    

    def Clear(self):
        self._dice.empty()
    

    def __str__(self):
        result = ""
        for i in range(len(self._dice)):
            result += self._dice[i].__str__()
            if (i < len(self._dice) - 1):
                result += ", ";

        return result
    

    # public IEnumerator<Die> GetEnumerator()
    
    #     for (int i = 0; i < _dice.Count; ++i)
    #         yield return _dice[i];

    

    # IEnumerator IEnumerable.GetEnumerator()
    
    #     return ((IEnumerable)_dice).GetEnumerator();
    


