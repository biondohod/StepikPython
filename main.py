lines_count = int(input())
lines_array = []
for _ in range(lines_count):
    x, y = map(int, input().split())
    lines_array.append([x, y])
lines_array.sort(key=lambda x: x[1])

dots = []
right_border = lines_array[0][1]
dots.append(right_border)
for i in range(1, len(lines_array)):
    if lines_array[i][0] > right_border:
        right_border = lines_array[i][1]
        dots.append(right_border)
print(len(dots))
for dot in dots:
    print(dot, end=" ")
