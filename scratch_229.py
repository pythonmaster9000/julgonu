boarD = [['o', 'o', 'o', 'o'],
         ['o', 'o', 'o', 'o'],
         ['o', 'o', 'o', 'o'],
         ['o', 'o', 'o', 'o'], ]

pieces = {
    'piecesBlack': {
        'b1': [0, 0],
        'b2': [0, 1],
        'b3': [0, 2],
        'b4': [0, 3]
    },
    'piecesWhite': {
        'w1': [3, 0],
        'w2': [3, 1],
        'w3': [3, 2],
        'w4': [3, 3]
    }
}


def colliding(x, y):
    for piece in pieces['piecesBlack'].values():
        if [x, y] == piece:
            return False
    for piece in pieces['piecesWhite'].values():
        if [x, y] == piece:
            return False
    return True


def bounds(x, y):
    return x in range(0, 4) and y in range(0, 4)


# check all cords where pieces are and prevent moving into a piece
def move(x, y, direction):
    if direction == 'd':
        return (x, y + 1) if bounds(x, y + 1) and colliding(x, y + 1) else False
    if direction == 'u':
        return (x, y - 1) if bounds(x, y - 1) and colliding(x, y - 1) else False
    if direction == 'l':
        return (x - 1, y) if bounds(x - 1, y) and colliding(x - 1, y) else False
    if direction == 'r':
        return (x + 1, y) if bounds(x + 1, y) and colliding(x + 1, y) else False


# check around moved piece to see if it is touching an enemy piece and then if there is a friendly piece in the same
# direction
def killed_a_piece(x, y, color):
    ecolor = 'piecesWhite' if color == 'piecesBlack' else 'piecesBlack'
    if bounds(x, y + 1) and any([c == [x, y + 1] for c in pieces[color].values()]):
        # piece moved touches an enemy piece now check if one of our pieces is behind it
        print('touched this piece DOWN')
        if bounds(x, y + 2) and any([c == [x, y + 2] for c in pieces[ecolor].values()]):
            print('captured touched piece DOWN')
            for piece in pieces[color]:
                if pieces[color][piece] == [x, y + 1]:
                    del pieces[color][piece]
                    break
            boarD[y + 1][x] = 'o'
    if bounds(x, y - 1) and any([c == [x, y - 1] for c in pieces[color].values()]):
        print('touched this piece UP')
        if bounds(x, y - 2) and any([c == [x, y - 2] for c in pieces[ecolor].values()]):
            print('captured touched piece UPN')
            for piece in pieces[color]:
                if pieces[color][piece] == [x, y - 1]:
                    del pieces[color][piece]
                    break
            boarD[y - 1][x] = 'o'
    if bounds(x + 1, y) and any([c == [x + 1, y] for c in pieces[color].values()]):
        print('touched this piece RIGHT')
        if bounds(x + 2, y) and any([c == [x + 2, y] for c in pieces[ecolor].values()]):
            print('captured touched piece RIGHT')
            for piece in pieces[color]:
                if pieces[color][piece] == [x + 1, y]:
                    del pieces[color][piece]
                    break
            boarD[y][x + 1] = 'o'
    if bounds(x - 1, y) and any([c == [x - 1, y] for c in pieces[color].values()]):
        print('touched this piece LEFT')
        if bounds(x - 2, y) and any([c == [x - 2, y] for c in pieces[ecolor].values()]):
            print('captured touched piece LEFT')
            for piece in pieces[color]:
                if pieces[color][piece] == [x - 1, y]:
                    del pieces[color][piece]
                    break
            boarD[y][x - 1] = 'o'


while True:
    for piece in pieces['piecesBlack'].values():
        boarD[piece[1]][piece[0]] = 'b'
    for piece in pieces['piecesWhite'].values():
        boarD[piece[1]][piece[0]] = 'w'
    for k in range(len(boarD)):
        print(boarD[k])
    playerMove = input('choose direction and piece ')
    direction = playerMove.split()[0]
    piece = playerMove.split()[1]
    if piece[0] == 'b':
        theMove = move(pieces['piecesBlack'][piece][0], pieces['piecesBlack'][piece][1], direction)
        if not theMove:
            print('invalid as fuck')
            continue
        boarD[pieces['piecesBlack'][piece][1]][pieces['piecesBlack'][piece][0]] = 'o'
        pieces['piecesBlack'][piece][0] = theMove[0]
        pieces['piecesBlack'][piece][1] = theMove[1]
        print(killed_a_piece(theMove[0], theMove[1], 'piecesWhite'))
        continue
    if piece[0] == 'w':
        theMove = move(pieces['piecesWhite'][piece][0], pieces['piecesWhite'][piece][1], direction)
        if not theMove:
            print('invalid as fuck')
            continue
        boarD[pieces['piecesWhite'][piece][1]][pieces['piecesWhite'][piece][0]] = 'o'
        pieces['piecesWhite'][piece][0] = theMove[0]
        pieces['piecesWhite'][piece][1] = theMove[1]
        print(killed_a_piece(theMove[0], theMove[1], 'piecesBlack'))
        continue
    break
