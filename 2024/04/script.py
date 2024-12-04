from typing import Literal

DIRECTIONS = ['nw', 'n', 'ne',
              'w',  'o', 'e',
              'sw', 's', 'se'
]


class Item(object):
    def __init__(self, l: Literal['X', 'M', 'A', 'S'], x: int, y: int) -> None:
        self.l = l
        self.x = x
        self.y = y

        # The following may be set as pointers to other Items
        self.n: Item = None
        self.ne: Item = None
        self.e: Item = None
        self.se: Item = None
        self.s: Item = None
        self.sw: Item = None
        self.w: Item = None
        self.nw: Item = None


    def starts_str(self, s: str, d: str) -> bool:
        # If searching for the empty string, you found it!
        if s == '':
            return True
        # If the current letter doesn't match the start of the target string,
        # fail.
        if self.l != s[0]:
            return False
        # Otherwise check down the line.
        _item = getattr(self, d)
        if _item is not None:
            # If we find a neighbor in the current direction, check if it
            # continues the target string.
            return _item.starts_str(s[1:], d)
        else:
            # If we don't find a neighbor, this had better be the last
            # character in the target string (and thus equal to the whole
            # thing).
            return self.l == s

    
    def __str__(self) -> str:
        return self.l


class Grid(object):
    def __init__(self, txt: list[list[str]]) -> None:
        # Populate grid with Items
        self.rows = []
        for y in range(len(txt)):
            row = []
            for x in range(len(txt[y])):
                row.append(Item(txt[y][x], x, y))
            self.rows.append(row)
        
        # Link Items in all directions
        for row in self.rows:
            for item in row:
                for d in range(len(DIRECTIONS)):
                    if DIRECTIONS[d] == 'o':
                        # Nothing to be done for own location
                        continue
                    dx = (d % 3) - 1
                    dy = (d // 3) - 1
                    _x = item.x + dx
                    _y = item.y + dy
                    setattr(item, DIRECTIONS[d], self.get_item(_x, _y))
        

    def get_item(self, x: int, y: int, wrap: bool = False) -> Item | None:
        if y >= len(self.rows) or x >= len(self.rows[y]):
            return None
        if (y < 0 or x < 0) and not wrap:
            return None
        return self.rows[y][x]

    

    def __str__(self) -> str:
        return ''.join([str(i) for r in self.rows for i in r])


def _count_appearances(grid: Grid, s: str='XMAS') -> int:
    appearances = 0
    for row in grid.rows:
        for item in row:
            for d in DIRECTIONS:
                if d == 'o':
                    # Nothing to be done for own location
                    continue
                if item.starts_str(s, d):
                    appearances += 1
    return appearances


def _count_x_mas(grid: Grid) -> int:
    target_set = {'M', 'S'}
    appearances = 0
    for row in grid.rows:
        for item in row:
            if item.l != 'A':
                # Ignore items that can't be the center of an X-MAS
                continue

            x1 = set()
            for d in ['nw', 'se']:
                _item = getattr(item, d)
                if _item is not None:
                    x1.add(_item.l)

            x2 = set()
            for d in ['ne', 'sw']:
                _item = getattr(item, d)
                if _item is not None:
                    x2.add(_item.l)

            if (x1 == target_set
                and x2 == target_set
            ):
                appearances += 1
    return appearances


# d = DIRECTIONS[(3*(dy+1))  + (dx + 1)]
def main():
    with open('04/input.txt') as f:
        txt = [line.strip() for line in f]
    grid = Grid(txt)
    print(f'XMAS appearances: {_count_appearances(grid, 'XMAS')}')
    print(f'X-MAS appearances: {_count_x_mas(grid)}')


if __name__ == '__main__':
    main()
