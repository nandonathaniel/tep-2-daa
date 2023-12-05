__author__ = "Fernando Nathaniel Sutanto"
import time

def bypassbranch(subset, i):#bypass a branch 
    for j in range(i-1, -1, -1):
        if subset[j] == 0:
            subset[j] = 1
            return subset, j+1

    return subset, 0

def nextvertex(subset, i, m):
    if i < m:
        subset[i] = 0
        return subset, i+1
    else:
        for j in range(m-1, -1, -1):
            if subset[j] == 0:
                subset[j] = 1
                return subset, j+1
                
    return subset, 0

def BB(universe,sets,costs):
    subset = [1 for x in range(len(sets))]#all sets in
    subset[0] = 0
    bestCost = sum(costs) #actually the worst cost 
    i = 1

    while i > 0:

        if i < len(sets):
            cost, tSet = 0, set()# t for temporary
            # print(i, end=' ')
            # print(subset)
            for k in range(i):
           
                cost += subset[k]*costs[k]#if 1 adds the cost to total
                if subset[k] == 1:
                    # print(k, end=" ")
                    tSet.update(set(sets[k]))#if 1 add the set to the cover
            # print()

            if cost > bestCost:#if the cost is larger than the currently best one, no need of further investigation
                subset, i = bypassbranch(subset, i)
                continue
            for k in range(i, len(sets)):
                tSet.update(set(sets[k]))
            if tSet != universe:#that means that the set was essential at this point to complete the uni.
                subset, i = bypassbranch(subset, i)
            else:
                subset, i = nextvertex(subset, i, len(sets))
                
        else:
            cost, fSet = 0, set()
            # print(i, end=' ')
            # print(subset)
            for k in range(i):
                cost += subset[k]*costs[k]
                if subset[k] == 1:
                    # print(k, end=" ")
                    fSet.update(set(sets[k]))
            # print()

            if cost < bestCost and fSet == universe:
                bestCost = cost
                bestSubset = subset[:]
            subset, i = nextvertex(subset, i, len(sets))

    return bestCost, bestSubset

# from memory_profiler import memory_usage

# def profile_memory(func):
#     def wrapper(*args, **kwargs):
#         def target():
#             return func(*args, **kwargs)
        
#         mem_usage, retval = memory_usage(target, interval=.1, timeout=1, retval=True, max_usage=True)
#         print(f">{func.__name__}'s memory usage: {mem_usage} MiB.")
#         return retval
#     return wrapper

# @profile_memory
def main(a,b,c,z=time.time()):
    m = a
    S = b 
    C = c
    F = set([x for x in range(1,m+1)])
    X=(BB(F,S,C))
    cost= X[0]
    # sets= X[1]
    # cover= []
    # for x in range(len(sets)):
    #     if sets[x]==1:
    #         cover.append(S[x])
    print('cost= ',cost,'$')
    # print('covering sets: ',cover,'\n','total cost: ',cost,'$')
    print('time in (ms):',(time.time()-z)*1000)

if __name__=='__main__':
    for sz in [20, 200, 2000]:
        sets_filename = f'sets/set_{sz}.txt'
        costs_filename = f'costs/cost_{sz}.txt'

        # Read sets from file
        with open(sets_filename, 'r') as file:
            sets = [list(map(int, line.strip().split())) for line in file]

        # Read costs from file
        with open(costs_filename, 'r') as file:
            costs = [int(line.strip()) for line in file]
        
        main(sz, sets, costs)
