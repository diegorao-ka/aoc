import re

MUL_RE = re.compile(r'mul\((\d+),\s*(\d+)\)')
FILTER_RE = re.compile(r'don\'t\(\)[\d\D]*?(do\(\)|$)')


def main():
    with open("03/input.txt") as f:
        s = f.read()
        s = re.sub(r'\n', '', s)

    print(s)
    s = re.sub(FILTER_RE, '', s)
    print()
    print(s)

    match_iter = re.finditer(MUL_RE, s)
    
    sum = 0
    for m in match_iter:
        tokens = m.group(1, 2)
        sum += int(tokens[0]) * int(tokens[1])
    
    print(sum)

if __name__ == '__main__':
    main()