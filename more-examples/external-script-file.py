# See ./with-external-script-file.html

from browser import document, html


board = html.DIV()
document <= board
board.classList.add('board')

for _ in range(9):
    cell = html.DIV()
    board <= cell
    cell.classList.add('cell')
    cell.addEventListener(
        'click',
        (lambda cell:
            lambda event: cell.classList.toggle('on')
        )(cell)
    )
