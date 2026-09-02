n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Arrival time (AT) for P{i+1}: "))
    bt = int(input(f"Enter Burst time (BT) for P{i+1}: "))
    processes.append([i+1, at, bt, bt, 0])

time_quantum = int(input("\nEnter Time Quantum: "))

processes.sort(key=lambda x: x[1])

current_time = 0
completed = 0
twt = 0
ttat = 0

queue = []
index = 0

print(f"\nProcess\tAT\tBT\tCT\tTAT\tWT")

while completed < n:

    # Add arrived processes to queue
    while index < n and processes[index][1] <= current_time:
        queue.append(processes[index])
        index += 1

    # If queue is empty, move time to next process
    if len(queue) == 0:
        current_time = processes[index][1]
        continue

    # Take first process from queue
    process = queue.pop(0)

    pid, at, bt, remaining_bt, ct = process

    # Run for Time Quantum or remaining time
    if remaining_bt > time_quantum:
        current_time += time_quantum
        process[3] -= time_quantum
    else:
        current_time += remaining_bt
        process[3] = 0

        process[4] = current_time

        ct = process[4]
        tat = ct - at
        wt = tat - bt

        twt += wt
        ttat += tat

        completed += 1

        print(f"P{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    # Add newly arrived processes
    while index < n and processes[index][1] <= current_time:
        queue.append(processes[index])
        index += 1

    # If process is not finished, put it back at the end
    if process[3] > 0:
        queue.append(process)


avg_wt = twt / n
avg_tat = ttat / n

print(f"\nAverage waiting time = {avg_wt:.2f}")
print(f"Average turnaround time = {avg_tat:.2f}")