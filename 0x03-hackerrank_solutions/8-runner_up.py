#!/usr/bin/python3

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    max_score = max(scores)
    print(max([i for i in scores if i != max_score]))
