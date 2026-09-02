n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

allocation = []
maximum = []

# Input Allocation
print("\nEnter Allocation Matrix:")
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input(f"P{i+1} R{j+1}: ")))
    allocation.append(row)

# Input Maximum
print("\nEnter Maximum Matrix:")
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input(f"P{i+1} R{j+1}: ")))
    maximum.append(row)

# Input Available
print("\nEnter Available Resources:")
available = []

for j in range(m):
    available.append(int(input(f"R{j+1}: ")))


# Calculate Need
need = []

for i in range(n):
    row = []

    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])

    need.append(row)


# Banker's Algorithm
completed = []

while len(completed) < n:

    found = False

    for i in range(n):

        if i not in completed:

            possible = True

            for j in range(m):
                if need[i][j] > available[j]:
                    possible = False

            if possible:

                # Process finishes
                for j in range(m):
                    available[j] += allocation[i][j]

                completed.append(i)
                found = True

    if found == False:
        break


# Result
if len(completed) == n:

    print("\nSystem is SAFE")
    print("Safe Sequence: ", end="")

    for i in completed:
        print(f"P{i+1}", end=" ")

else:

    print("\nSystem is UNSAFE")