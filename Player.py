class Player():
    def __init__(self, hand = [], status = True):
        self._hand = hand
        self._status = status
    
    def hit(self, deck = []):
        card = deck.pop(0)
        self._hand.append(card)
        if Player.getHandValue(self) > 21:
            self._status = False
        return card
    
    def stand(self):
        self._status = False
    
    def getHandValue(self):
        total = 0
        aces = 0
        for card in self._hand:
            total += card.getValue()
            if card.getValue() == 1:
                aces += 1
        
        while aces > 0 and total <= 11:
            total += 10
            aces -= 1
            
        return total
    
    def getHand(self):
        return self._hand.copy()
    
    def getStatus(self):
        return self._status

class House(Player):    
    def getHandValue(self):
        total = 0
        aces = 0
        hasEleven = False
        
        for card in self._hand:
            total += card.getValue()
            if card.getValue() == 1:
                aces += 1
        
        while aces > 0 and total <= 11:
            total += 10
            aces -= 1
            hasEleven = True

        return total, hasEleven
                    
                    
            
