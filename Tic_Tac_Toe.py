# Tic Tac Toe Game

def board_print(board):
    for x in board:
        print(' ---' * 3)
        print(f'| {x[0]} | {x[1]} | {x[2]} |')
    print(' ---' * 3)

def player_input(numb):
    global ttt_list
    player = input('Player %d input: ' %numb).split(',')
    row = int(player[0].strip()) - 1
    col = int(player[1].strip()) - 1
    if row not in [0,1,2] or col not in [0,1,2]:
        print('Invalid input! Try again!!')
        return player_input(numb)
    if ttt_list[row][col] == 'X' or ttt_list[row][col] == 'O':
        print('This slot is already occupied! Try again!!')
        return player_input(numb)
    return [row, col]

def checker():
    global check, p1_win_count, p2_win_count
    # rows check
    if first_row == ['X', 'X', 'X'] or second_row == ['X', 'X', 'X'] or third_row == ['X', 'X', 'X']:
        print('\nPlayer 1 wins!!')
        check = 1; p1_win_count += 1
        return 1
    elif first_row == ['O', 'O', 'O'] or second_row == ['O', 'O', 'O'] or third_row == ['O', 'O', 'O']:
        print('\nPlayer 2 wins!!')
        check = 1; p2_win_count += 1
        return 1

    # columns check
    for y in range(3):
        if first_row[y] == second_row[y] == third_row[y] == 'X':
            print('\nPlayer 1 wins!!')
            check = 1; p1_win_count += 1
            return 1
        elif first_row[y] == second_row[y] == third_row[y] == 'O':
            print('\nPlayer 2 wins!!')
            check = 1; p2_win_count += 1
            return 1

    # diagonal check
    if first_row[0] == second_row[1] == third_row[2] == 'X' or first_row[2] == second_row[1] == third_row[0] == 'X':
        print('\nPlayer 1 wins!!')
        check = 1; p1_win_count += 1
        return 1
    elif first_row[0] == second_row[1] == third_row[2] == 'O' or first_row[2] == second_row[1] == third_row[0] == 'O':
        print('\nPlayer 2 wins!!')
        check = 1; p2_win_count += 1
        return 1

if __name__ == "__main__":
    p1_win_count = p2_win_count = 0
    repeat = 'y'
    while repeat == 'Y' or repeat == 'y':
        count = check = temp = 0
        first_row = [' ', ' ', ' ']
        second_row = [' ', ' ', ' ']
        third_row = [' ', ' ', ' ']
        ttt_list = [first_row, second_row, third_row]

        print('~~*~~' * 17)
        print('TIC TAC TOE GAME')
        print("Players should mention their preferred position on the board in the 'row,column' format.")
        print("Player 1 is 'X' and Player 2 is 'O'\n")

        print('Empty board: ')
        board_print(ttt_list)

        while count < 9:
            p1_input = player_input(1)
            ttt_list[p1_input[0]][p1_input[1]] = 'X'
            count += 1
            board_print(ttt_list)
            temp = checker()
            if temp == 1:
                break

            if count == 9:
                break
            else:
                p2_input = player_input(2)
                ttt_list[p2_input[0]][p2_input[1]] = 'O'
                count += 1
                board_print(ttt_list)
                temp = checker()
                if temp == 1:
                    break

        if check == 0:
            print('\nAll slots filled, no result!')

        repeat = input('\nDo you want to continue? Type (Y/N): ')
        if repeat == 'N' or repeat == 'n':
            print(f'Player 1 total wins: {p1_win_count}')
            print(f'Player 2 total wins: {p2_win_count}')