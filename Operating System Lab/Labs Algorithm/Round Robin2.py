n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input("Enter the arrival time: "))
    bt = int(input("Enter the burst time: "))
    processes.append([i+1, at, bt, bt, 0])

time_quantum = int(input("Enter the time quantum: "))

current_time = 0
completed = 0
ttat = 0
twt = 0

queue = []
index = 0

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

while completed < n:
    while index < n and processes[index][1] <= current_time:
        queue.append(processes[index])
        index += 1

    if len(queue) == 0:
        current_time = processes[index][1]
        continue

    process = queue.pop(0)

    uid, at, bt, rt, ct = process

    if process[3] > time_quantum:
        current_time += time_quantum
        process[3] -= time_quantum
    else:
        current_time += rt
        process[3] = 0

        ct = current_time
        tat = ct - at
        wt = tat - bt

        twt += wt
        ttat += tat

        print(f"{uid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
        completed += 1 

    while index < n and processes[index][1] <= current_time:
        queue.append(processes[index])
        index += 1

    if process[3] > 0:
        queue.append(process)


awt = twt / n
atat = ttat / n

print(awt, atat)