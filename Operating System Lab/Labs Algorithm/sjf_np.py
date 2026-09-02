n = int(input("Enter the number of resources: "))
processes = []

for i in range (n):
    at = int(input(f"Enter the arrival of P{i+1}: "))
    bt = int(input(f"Enter the burst of P{i+1}: "))
    processes.append([i+1, at, bt])

current_time = 0
twt = 0
ttat = 0

processes.sort(key=lambda x:x[1])

while len(processes) > 0:
    available = []

    if current_time < processes[0][1]:
        current_time = processes[0][1]

    for process in processes:
        if process[1] <= current_time:
            available.append(process)

    available.sort(key=lambda x:x[2])

    uid, at, bt = available[0]

    ct = current_time + bt
    tat = ct - at
    wt = tat - bt

    twt = twt + wt
    ttat = ttat + tat

    processes.remove(available[0])

    current_time = ct

avg_wt = twt / n
avg_tat = ttat / n

print(avg_wt, avg_tat)