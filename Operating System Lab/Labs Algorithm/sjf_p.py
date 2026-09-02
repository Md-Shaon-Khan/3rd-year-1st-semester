n = int(input("Enter the number of resources: "))
processes = []

for i in range (n):
    at = int(input(f"Enter the arrival of P{i+1}: "))
    bt = int(input(f"Enter the burst of P{i+1}: "))
    processes.append([i+1, at, bt, bt, 0])

current_time = 0
twt = 0
ttat = 0
completed = 0

processes.sort(key=lambda x:x[1])

while completed < n:
    available = []

    for process in processes:
        if process[1] <= current_time and process[3] > 0:
            available.append(process)

    if len(available) == 0:
        current_time += 1
        continue

    available.sort(key=lambda x:x[3])

    process = available[0]

    uid, at, bt, rt, ct = process

    current_time += 1
    process[3] -= 1

    if process[3] == 0:
        ct = current_time
        process[4] = ct
        process[3] = 0

        rt = 0
        tat = ct - at
        wt = tat - bt

        twt += wt
        ttat = ttat + tat
        completed += 1

avg_wt = twt / n
avg_tat = ttat / n
