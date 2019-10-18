##################### 
#####Description#####
#ieeeei#

#####################

def makeBoard() :
    theBoard = {};
    rows = ['top','mid','low']
    cols = ['L','M','R']
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            theBoard.setdefault(key,False)
    print('DEBUG: '+str(theBoard))
    return theBoard

def printCell(cell) :
    if cell : 
        return ' '+str(cell)+' '
    else :
        return '   '

def showBoard(board) : 
    print(printCell(board['top-L'])+'|'+printCell(board['top-M'])+'|'+printCell(board['top-R']))
    print('-----------')
    print(printCell(board['mid-L'])+'|'+printCell(board['mid-M'])+'|'+printCell(board['mid-R']))
    print('-----------')
    print(printCell(board['low-L'])+'|'+printCell(board['low-M'])+'|'+printCell(board['low-R']))

def determineVictory(board):
    rows = ['top','mid','low']
    cols = ['L','M','R']
    # se uma linha tiver todas as colunas iguais é vitoria
    for r in rows :
        col1 = str(r)+'-L'
        col2 = str(r)+'-M'
        col3 = str(r)+'-R'
        if board[col1] == board[col2] == board[col3] and bool(board[col1]) :
            return board[col3]
    # se uma coluna tiver todas as linhas iguais é vitoria
    for c in cols :
        row1 = 'top-'+str(c)
        row2 = 'mid-'+str(c)
        row3 = 'low-'+str(c)
        if board[row1] == board[row2] == board[row3] and bool(board[row1]) :
            return board[row3]
    # se houver uma diagonal com todas iguais então é vitoria
    middle = 'mid-M';
    sel1, sel2 = str(rows[0]+'-'+cols[2]), str(rows[2]+'-'+cols[0])
    if board[middle] == board[sel1] == board[sel2] :
       return board[middle]
    sel1, sel2 = str(rows[0]+'-'+cols[0]), str(rows[2]+'-'+cols[2])
    if board[middle] == board[sel1] == board[sel2] :
       return board[middle]
    return False

def determineAvailableMoves(board) :
    rows = ['top','mid','low']
    cols = ['L','M','R']
    hasMoves = False
    # verifica se posicão escolhida é válida
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            if not bool(board[key]) :
                return True
    return hasMoves

def readInputAndTryToPutOnBoard(board, player) :
    rows = ['top','mid','low']
    cols = ['L','M','R']
    print('To make a move type an row (top, mid, low), followed by a dash (-), and an column (L, M, R), like top-M')
    move = input()
    valida = False
    # verifica se posicão escolhida é válida
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            if key == move :
                valida = True

    if valida & bool(board[move]):
        print('Position already taken!');
        return False
    elif valida : 
        board[move] = player
        return True
    else : 
        print('Invalid position!');
        return False

def changePlayer(player) :
    if player == 'X':
        print('Player O turn!')
        return 'O'
    else :
        print('Player X turn!')
        return 'X'
    
def game():
    print('Lets play a game, X goes first, O goes after!')
    player = 'X'
    board = makeBoard();
    while True :
        showBoard(board);
        # Obtem movimento
        while True : 
            move = readInputAndTryToPutOnBoard(board, player)
            if move :
                break
        # Verifica se movimento concedeu vitoria
        if determineVictory(board) :
            showBoard(board);
            print('Player '+player+' wins!!!')
            return True
        # verifica se ainda há movimentos possíveis
        if not determineAvailableMoves(board) :
            print('Draw, or like we say in Brazil, deu velha...')
            return True
        # caso não tenha vencido então muda jogador e tenta denovo
        player = changePlayer(player)
        
game();
