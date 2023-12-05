__author__ = "Fernando Nathaniel Sutanto"
import random
import time


def set_cover(universe, subsets,costs):
    cost=0
    elements = set(e for s in subsets for e in s)  
    if elements != universe:   #Cek semua
        return None
    covered = set()
    cover = []
    while covered != elements:
        # subset = max(subsets, key=lambda s: len(s - covered) / costs[subsets.index(s)])
        subset = min(subsets, key=lambda s: (costs[subsets.index(s)] / len(s - covered)) if len(s - covered) != 0 else float('inf'))
        cover.append(subset)
        cost+=costs[subsets.index(subset)]
        covered |= subset
 
    return cover, cost

from memory_profiler import memory_usage

def profile_memory(func):
    def wrapper(*args, **kwargs):

        def target():
            return func(*args, **kwargs)
        
        mem_usage, retval = memory_usage(target, interval=.1, timeout=1, retval=True, max_usage=True)
        print(f">{func.__name__}'s memory usage: {mem_usage} MiB.")
        return retval
    return wrapper

@profile_memory
def main(a,b,c,x=time.time()):
    m= a
    universe = set(range(1, m+1))
    sub = b  
    
    subsets = [set(x) for x in sub]
    costs =  c 
    cover = set_cover(universe, subsets,costs)
    print('cost= ',cover[1],'$')
    print('time in ms: ',(time.time()-x)*1000)

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

