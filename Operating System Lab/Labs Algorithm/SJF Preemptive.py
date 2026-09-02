n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Arrival time (AT) for P{i+1}: "))
    bt = int(input(f"Enter Burst time (BT) for P{i+1}: "))
    processes.append([i+1, at, bt, bt, 0])

processes.sort(key=lambda x: x[1])

current_time = 0
completed = 0
twt = 0
ttat = 0

print(f"\nProcess\tAT\tBT\tCT\tTAT\tWT")

while completed < n:

    available = []

    for process in processes:
        if process[1] <= current_time and process[3] > 0:
            available.append(process)

    if len(available) == 0:
        current_time += 1
        continue

    available.sort(key=lambda x: x[3])

    process = available[0]

    pid, at, bt, remaining_bt, ct = process

    process[3] -= 1
    current_time += 1

    if process[3] == 0:

        process[4] = current_time

        ct = process[4]
        tat = ct - at
        wt = tat - bt

        twt += wt
        ttat += tat

        completed += 1

        print(f"P{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")


avg_wt = twt / n
avg_tat = ttat / n

print(f"\nAverage waiting time = {avg_wt:.2f}")
print(f"Average turnaround time = {avg_tat:.2f}")