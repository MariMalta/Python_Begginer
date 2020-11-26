""" URI Exercise #1110 - https://www.urionlinejudge.com.br/judge/pt/problems/view/1110 """

def make_deck(n) -> list:
    """ Makes a deck from n to 1 """
    return list(range(n, 0, -1))

def throw_away(deck) -> tuple:
    """ Discard first from pile, move the second to final until there is at least two elements """
    discard_pile = []

    while len(deck) > 1:
        top = deck.pop()
        discard_pile.append(top)

        sub_top = deck.pop()
        deck.insert(0, sub_top)

    return (discard_pile, deck)

def prepare_output(deck) -> str:
    """ Builds a comma separated string from a list of numbers """
    return ', '.join(map(str, deck))

if __name__ == "__main__":
    while True:
        val = int(input())
        if (val != 0):
            deck = make_deck(val)
            discard, final_deck = throw_away(deck)

            print(f"Discarded cards: {prepare_output(discard)}")
            print(f"Remaining card: {prepare_output(final_deck)}")
        else:
            break
