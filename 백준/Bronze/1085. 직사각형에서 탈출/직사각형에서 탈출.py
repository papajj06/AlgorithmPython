import sys

read = sys.stdin.readline

x, y, w, h = list(map(int, read().split()))

print(min([x, y, w - x, h - y]))