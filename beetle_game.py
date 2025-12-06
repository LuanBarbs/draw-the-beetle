import copy

CORPO = 0
CABECA = 1
PERNA = 2
OLHO = 3
ANTENA = 4
RABO = 5

LIMITES = [1, 1, 6, 2, 2, 1]
NOMES = ["Corpo", "Cabeça", "Perna", "Olho", "Antena", "Rabo"]

class GameState:
    def __init__(self):
        self.board = [[0]*6, [0]*6]
        self.turn = 0 # 0 para Player 1, 1 para Player 2
    
    def is_terminal(self):
        for player_idx in [0, 1]:
            if self.board[player_idx] == LIMITES:
                return True, player_idx
        return False, None

    def get_valid_moves(self):
        """
        Retorna uma lista de ações possíveis.
        Ação: ('tipo', indice_peca, jogador_alvo)
        tipo: 'add' (construir no seu) ou 'remove' (atacar o outro)
        """
        moves = []
        me = self.turn
        opp = 1 - self.turn

        my_b = self.board[me]

        if my_b[CORPO] < LIMITES[CORPO]:
            moves.append(('add', CORPO, me))
        else:
            if my_b[CABECA] < LIMITES[CABECA]: moves.append(('add', CABECA, me))
            if my_b[PERNA] < LIMITES[PERNA]: moves.append(('add', PERNA, me))
            if my_b[RABO] < LIMITES[RABO]: moves.append(('add', RABO, me))

            if my_b[CABECA] > 0:
                if my_b[OLHO] < LIMITES[OLHO]: moves.append(('add', OLHO, me))
                if my_b[ANTENA] < LIMITES[ANTENA]: moves.append(('add', ANTENA, me))
        
        opp_b = self.board[opp]

        if opp_b[OLHO] > 0: moves.append(('remove', OLHO, opp))
        if opp_b[ANTENA] > 0: moves.append(('remove', ANTENA, opp))
        if opp_b[PERNA] > 0: moves.append(('remove', PERNA, opp))
        if opp_b[RABO] > 0: moves.append(('remove', RABO, opp))

        if opp_b[CABECA] > 0 and opp_b[OLHO] == 0 and opp_b[ANTENA] == 0:
            moves.append(('remove', CABECA, opp))

        pieces_count = sum(opp_b)
        if opp_b[CORPO] > 0 and pieces_count == 1:
            moves.append(('remove', CORPO, opp))

        return moves
    
    def apply_move(self, move):
        new_state = copy.deepcopy(self)
        tipo, idx, player = move
        
        if tipo == 'add':
            new_state.board[player][idx] += 1
        elif tipo == 'remove':
            new_state.board[player][idx] -= 1
            
        new_state.turn = 1 - self.turn
        return new_state
    
    def print_board(self):
        p1 = self.board[0]
        p2 = self.board[1]
        print(f"--- Placar ---")
        print(f"P1: {p1} (Total: {sum(p1)})")
        print(f"P2: {p2} (Total: {sum(p2)})")
        print("--------------")