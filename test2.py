import argparse
import requests

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Test 1",
                                     description="program testing")
    parser.add_argument("card_amount", help="insert amount of card you want to get")
    parser.add_argument("-p", "--print", help="Pass p if you want to print the card", action="store_true")
    args = parser.parse_args()
    create_deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    deck_id = create_deck.json()["deck_id"]
    card = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={args.card_amount}")
    card_list = card.json()["cards"]
    if args.print:
        for c in card_list:
            print(c["value"], c["suit"])
    else:
        print("bye bye")
