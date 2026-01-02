import copy

CORPO, CABECA, PERNA, OLHO, ANTENA, RABO = range(6)

LIMITES = [1, 1, 6, 2, 2, 1]
NOMES = ["Corpo", "Cabeça", "Perna", "Olho", "Antena", "Rabo"]

class GameState:
    def __init__(self):
        self.board = [[0]*6, [0]*6]
        self.destroys_left = [LIMITES.copy(), LIMITES.copy()]
        self.shields = [3, 3]
        self.shield_timer = [0, 0]
        self.turn = 0

    def clone(self):
        return copy.deepcopy(self)

    def is_terminal(self):
        for p in [0, 1]:
            if self.board[p] == LIMITES:
                return True, p
        return False, None

    def get_valid_moves(self):
        moves = []
        me = self.turn
        opp = 1 - me
        my_b = self.board[me]
        opp_b = self.board[opp]

        # ---------- CONSTRUÇÃO ----------
        if my_b[CORPO] < 1:
            moves.append(('add', CORPO, me))
        else:
            if my_b[CABECA] < 1: moves.append(('add', CABECA, me))
            if my_b[PERNA] < 6: moves.append(('add', PERNA, me))
            if my_b[RABO] < 1: moves.append(('add', RABO, me))
            if my_b[CABECA] > 0:
                if my_b[OLHO] < 2: moves.append(('add', OLHO, me))
                if my_b[ANTENA] < 2: moves.append(('add', ANTENA, me))

        # ---------- PROTEÇÃO ----------
        if self.shields[me] > 0 and self.shield_timer[me] == 0:
            moves.append(('shield', None, me))

        # ---------- SABOTAGEM ----------
        if self.shield_timer[opp] == 0:
            for i in range(6):
                if opp_b[i] > 0 and self.destroys_left[me][i] > 0:
                    if i in [OLHO, ANTENA]:
                        moves.append(('remove', i, opp))
                    elif i == CABECA and opp_b[OLHO] == 0 and opp_b[ANTENA] == 0:
                        moves.append(('remove', i, opp))
                    elif i == CORPO and sum(opp_b) == 1:
                        moves.append(('remove', i, opp))
                    elif i in [PERNA, RABO]:
                        moves.append(('remove', i, opp))
        return moves

    def apply_move(self, move):
        new = self.clone()
        tipo, idx, player = move
        me = self.turn
        opp = 1 - me

        # Atualiza escudos
        for p in [0, 1]:
            if new.shield_timer[p] > 0:
                new.shield_timer[p] -= 1

        if tipo == 'add':
            new.board[player][idx] += 1

        elif tipo == 'remove':
            new.board[player][idx] -= 1
            new.destroys_left[me][idx] -= 1

        elif tipo == 'shield':
            new.shields[player] -= 1
            new.shield_timer[player] = 2

        new.turn = opp
        return new
    
    def print_board(self):
        p1 = self.board[0]
        p2 = self.board[1]
        print(f"--- Placar ---")
        print(f"P1: {p1} (Total: {sum(p1)})")
        print(f"P2: {p2} (Total: {sum(p2)})")
        print("--------------")