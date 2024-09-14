import sys
from os.path import isfile, exists
from collections import deque


def read_file_n_last_lines(file: str, N: int=10)-> list[str]:
    lines = deque() # faster than regular list
    with open(file) as f:
        while(l := f.readline()):
            lines.append(l.rstrip())
            if len(lines) > N:
                lines.popleft()
    
    return lines


def main(args):
    if len(args) < 2:
        print("Not all arguments provided. Expected input: t2.py <file_path>")
        return -1
    
    file_path = args[1]
    
    if not exists(file_path) or not isfile(file_path):
        print(f"File {file_path} can't be found")
        return -1

    n = 10
    lines = read_file_n_last_lines(file_path, n)
    print(f"Last {n} lines:")
    for l in lines:
        print(l)


    return lines

    
main(sys.argv)