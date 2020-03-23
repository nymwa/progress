import sys
from tqdm import tqdm

def main():
    for line in tqdm(sys.stdin):
        print(line, end='')

if __name__ == '__main__':
    main()

