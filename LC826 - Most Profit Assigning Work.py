def maxprofit(difficulty, profit,worker):
    tasks = sorted(list(zip(profit, difficulty)), reverse=True)
    worker.sort(reverse=True)
    numworkers = len(worker)
    workerid, maxprofit = 0,0
    
    for taskprofit, taskdiff in tasks:
        
        while workerid<numworkers and worker[workerid]>=taskdiff:
            maxprofit += taskprofit
            workerid += 1

    return maxprofit
 
difficulty =[66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63]
profit = [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77]
worker = [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]

print(maxprofit(difficulty, profit, worker))

