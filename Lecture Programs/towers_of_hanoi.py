def TowerOfHanoi(n, fr, to, spare):
    def printMove(fr, to):
            print(f'Move from {fr} to {to}')

    def Towers(n, fr, to, spare):
        if n == 1:
            printMove(fr, to)
        else:
            TowerOfHanoi(n-1, fr, spare, to)
            TowerOfHanoi(1, fr, to, spare)
            TowerOfHanoi(n-1, spare, to, fr)

    Towers(n, fr, to, spare)

# Calling Tower of hanoi with no. of disks and poles with names
TowerOfHanoi(4, 'P1', 'P2', 'P3')
