n = int(input("Enter the number of processes: "))
processes = []

for i in range (n):
    at = int(input(f"Enter the arrival of P{i+1}: "))
    bt = int(input(f"Enter the burst of P{i+1}: "))
    processes.append([i+1, at, bt, bt, 0])

time_quantum = int(input("Enter the time quantum: "))

queue = []

completed = 0
current_time = 0
index = 0
twt = 0
ttat = 0

processes.sort(key=lambda x:x[1])

while completed < n:
    while index < n and  processes[index][1] <= current_time:
        queue.append(processes[index])
        index += 1

    if len(queue) == 0:
        current_time += processes[index][1]
        continue


    process = queue.pop(0)

    uid, at, bt, rt, ct = process

    if rt > time_quantum:
        current_time += time_quantum
        process[3] -= time_quantum
    else:
        current_time += rt
        process[3] = 0
        ct = current_time

        tat = ct - at
        wt = tat - bt

        twt = twt + wt
        ttat = ttat + tat

        completed += 1

    while index < n and  processes[index][1] <= current_time:
            queue.append(processes[index])
            index += 1

    if process[3] > 0:
         queue.append(process)

avg_wt = twt / n
avg_tat = ttat / n

print(avg_wt, avg_tat)