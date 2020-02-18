import sys
from tqdm import tqdm

if __name__ == '__main__':
    for line in tqdm(sys.stdin):
        print(line, end='')

