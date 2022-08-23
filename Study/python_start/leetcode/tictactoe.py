import random
class Tictactoe:
    def __init__(self) -> None:
        self.board=[]
    def create_board(self):
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append('-')
            
            self.board.append(row)
    def play(self, row, col, player):
        self.board[row-1][col-1] = player
    def display(self):
        for row in self.board:
            print(*row)
    def start(self):
        self.create_board()
        player = ['X','O']
        idx = random.randint(0,1)
        moves = []
        while True:
            idx = (idx+1 ) % 2
            row, col = map(int, input().split())
            self.play(row,col, player[idx])
            moves.append([row-1,col-1])
            self.display()
            if self.tictactoe(moves) != "Pending":
                break 
    def tictactoe(self, moves) -> str:
            flag = len(moves) % 2
            A_Info = [0] * 8
            B_Info = [0] * 8
            for i in range(0,len(moves),2):
                A_Info[moves[i][0]] +=1
                A_Info[moves[i][1]+3] +=1
                flag = 1 if moves[i][0] == moves[i][1] else 2 if abs(moves[i][1] - moves[i][0]) == 2 else None
                if flag: 
                    A_Info[6+flag-1] +=1 
                    if moves[i][0] == 1:
                        A_Info[7] +=1
                # print(A_Info)
                if any(3 == i for i in A_Info):
                    print("A is winner")
                    return 
                if i+1 < len(moves):
                    B_Info[moves[i+1][0]] +=1
                    B_Info[moves[i+1][1]+3] +=1 
                    flag = 1 if moves[i+1][0] == moves[i+1][1] else 2 if abs(moves[i+1][1] - moves[i+1][0]) == 2 else None
                    if flag:
                        B_Info[6+flag-1] +=1 
                        if moves[i+1][0] == 1:
                            B_Info[7] +=1
                    # print(B_Info)
                    if any(3 == i for i in B_Info):
                        print("B is winner")
                        return 
            return "Draw" if len(moves) == 9 else "Pending"
play_game = Tictactoe()
play_game.start()