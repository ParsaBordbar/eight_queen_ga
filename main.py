import random

from utils import select_a_random, swap

def generate_board():
    board = []
    valid_bord_values = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(8):
        index = select_a_random()
        board.append(valid_bord_values[index])
    return board

def fitness_evaluation(queens): 
    fitness = 28
    conflicts = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i] == queens[j]:
                conflicts += 1
            elif abs(queens[i] - queens[j]) == abs(i - j):
                conflicts += 1
    fitness -= conflicts
    return fitness

def mution(queens):
    mut_index_1 = select_a_random()
    mut_index_2 = select_a_random()

    mut_el1, mut_el2 = swap(queens[mut_index_1], queens[mut_index_2])

    queens[mut_index_1] = mut_el1
    queens[mut_index_2] = mut_el2
    return queens

def main():
    for i in range(100):
        board = generate_board()
        print(f"chromozuoms: {board}")
        print(f"Fitness Eavaluation: {fitness_evaluation(board)}")
        print(f"Mutation: {mution(board)}")
        print("--------------------------------------------------")


if __name__ == "__main__":
    main()
