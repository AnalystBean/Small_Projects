import random

class Blackjack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(self.deck)
        self.dealer = []
        self.player = []

    def start_game(self):
        self.player.append(self.deck.pop())
        self.dealer.append(self.deck.pop())
        self.player.append(self.deck.pop())
        self.dealer.append(self.deck.pop())
        print("Your cards:", self.player)
        print("Dealer's cards: [{}, X]".format(self.dealer[0]))

    def hit(self):
        self.player.append(self.deck.pop())
        print("Your cards:", self.player)
        print("Your total:", sum(self.player))
        if sum(self.player) > 21:
            print("You busted.")
            self.play_dealer()

    def stand(self):
        self.play_dealer()

    def play_dealer(self):
        while sum(self.dealer) < 17:
            self.dealer.append(self.deck.pop())
        print("Dealer's cards:", self.dealer)
        print("Dealer's total:", sum(self.dealer))
        if sum(self.dealer) > 21:
            print("Dealer busted. You win!")
        elif sum(self.dealer) > sum(self.player):
            print("Dealer wins.")
        elif sum(self.dealer) < sum(self.player):
            print("You win!")
        else:
            print("Push.")

if __name__ == '__main__':
    game = Blackjack()
    game.start_game()
    while True:
        choice = input("Do you want to hit or stand? ")
        if choice == 'hit':
            game.hit()
        elif choice == 'stand':
            game.stand()
            break