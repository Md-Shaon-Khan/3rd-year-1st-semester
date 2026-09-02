n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter the arrival time of P{i+1}: "))
    bt = int(input(f"Enter the burst time of P{i+1}: "))
    processes.append([i+1, at, bt, bt, 0])

processes.sort(key=lambda x:x[1])

current_time = 0
completed = 0
ttat = 0
twt = 0

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
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

    current_time += 1
    process[3] -= 1

    uid, at, bt, rt, ct = process

    if process[3] == 0:
        ct = current_time
        process[4] = ct

        tat = ct - at
        wt = tat - bt

        twt = twt + wt
        ttat = ttat + tat

        print(f"{uid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

        completed += 1

awt = twt / n
atat = ttat / n

print(awt, atat)