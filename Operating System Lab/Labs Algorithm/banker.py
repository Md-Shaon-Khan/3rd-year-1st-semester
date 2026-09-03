n = int(input("Enter the number of processes: "))
m = int(input("Enter the number of resources: "))

allocation = []
maximum = []
need = []
available = []

completed = []

print("Enter allocation matrix: ")
for i in range(n):
    row = []
    for j in range(m):
        value = int(input(f"Enter P{i+1} R{j+1}"))
        row.append(value)
    allocation.append(row)

print("Enter maximum matrix: ")
for i in range(n):
    row = []
    for j in range(m):
        value = int(input(f"Enter P{i+1} R{j+1}"))
        row.append(value)
    maximum.append(row)

print("Available matrix: ")
for j in range(m):
    available.append(int(input(f"Available matrix R{i+1}: ")))

for i in range(n):
    row = []
    for j in range(m):
        value = maximum[i][j] - allocation[i][j]
        row.append(value)
    need.append(row)

while len(completed) < n:
    found = False

    for i in range(n):
        if i not in completed:
            possible = True

            for j in range(m):
                if need[i][j] > available[j]:
                    possible = False

            if possible:
                for j in range(m):
                    available[j] += allocation[i][j]

                completed.append(i)
                found = True

    if found == False:
        break

if len(completed) == n:
    print("Safe")
    for i in range(n):
        print(completed[i],end = " ")
else:
    print("Unsafe")