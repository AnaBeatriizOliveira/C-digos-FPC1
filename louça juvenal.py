class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

def simulate_game(deck_mesa, decks_convidados):
    mesa = LinkedList()
    for card in reversed(deck_mesa):
        mesa.append(card)
    
    num_convidados = len(decks_convidados)
    current_player = 0

    for _ in range(1000):
        current_card = mesa.pop()

        if current_card is None:
            return 0

        if current_card == decks_convidados[current_player][0]:
            decks_convidados[current_player].pop(0)
            if not decks_convidados[current_player]:
                return current_player + 1
            mesa.append(current_card)  # Move the card to the end of the table
        else:
            decks_convidados[current_player].append(current_card)

        current_player = (current_player + 1) % num_convidados

    return 0  # Juvenal

# Test Case 1
deck_mesa_1 = [1, 7, 3, 2, 4]
decks_convidados_1 = [[2, 3, 1], [1, 7, 4], [1, 2, 1, 3]]
result_1 = simulate_game(deck_mesa_1, decks_convidados_1)
print(result_1)  # Output should be 2

# Test Case 2
deck_mesa_2 = [1, 2, 3, 4]
decks_convidados_2 = [[2, 1], [4, 3]]
result_2 = simulate_game(deck_mesa_2, decks_convidados_2)
print(result_2)  # Output should be 0
