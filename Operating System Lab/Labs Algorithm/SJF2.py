n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter the arrival time of P{i+1}: "))
    bt = int(input(f"Enter the burst time of P{i+1}: "))
    processes.append([i+1, at, bt])

processes.sort(key=lambda x:x[1])

current_time = 0
ttat = 0
twt = 0

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
while len(processes) > 0:
    available = []

    if current_time < processes[0][1]:
        current_time = processes[0][1]

    for process in processes:
        if process[1] <= current_time:
            available.append(process)

    available.sort(key=lambda x:x[2])

    process = available[0]

    uid, at, bt = process

    ct = current_time + bt
    current_time = ct

    tat = ct - at
    wt = tat - bt

    twt += wt
    ttat += tat

    print(f"{uid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    processes.remove(process)

awt = twt / n
atat = ttat / n

print(awt, atat)