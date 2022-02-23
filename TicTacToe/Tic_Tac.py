import random

board = {}
for i in range(1, 10):
    board.__setitem__(i," ")

win_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

print("Hello")


def comp_turn():
    comp_option = random.randint(1, 9)
    if board[comp_option] == ' ':
        board[comp_option] = '0'
        return
    comp_turn()


def user_option():
    option = int(input("Enter Position:"))
    if board[option] == ' ':
        board[option] = 'X'
        return
    user_option()



def display():
    print(f"{board[1]} {board[2]} {board[3]}\n{board[4]} {board[5]} {board[6]}\n{board[7]} {board[8]} {board[9]}")


def main():
    while True:
        display()
        user_option()
        comp_turn()
        for i in win_list:
            if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
                print("You Win!!!")
                display()
                return
            if board[i[0]] == '0' and board[i[1]] == '0' and board[i[2]] == '0':
                print("Comp Win!!!")
                display()
                return

if __name__ == "__main__":
    main()

