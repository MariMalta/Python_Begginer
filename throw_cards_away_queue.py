def make_deck(n):
    """ Makes a deck from 1 to n """
    return list(range(1, n+1))

def throw_away(deck):
    """ Discard first from pile, move the second to final until there is at least two elements """
    discard_pile = []

    while len(deck) > 1:
        discard_pile.append(deck[0])
        del deck[0]
        deck.append(deck[0])
        del deck[0]

    return (discard_pile, deck)

def prepare_output(deck):
     Builds a comma separated string from a list of numbers 
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
