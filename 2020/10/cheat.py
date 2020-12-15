import math
from collections import defaultdict, deque
import os
import copy

dp = [0 for i in range(100001)]
a = [i.split('\n') for i in open("input.txt","r")]
for idx in range(len(a)):
    a[idx] = int(a[idx][0])
a = sorted(a)
a.append(a[len(a)-1]+3)
print(a)

deg = [0 for i in range(100001)]
def bsearch(vl):
    l = 0
    r = len(a)-1

    while(l <= r):
        md = int( l + round(r-l)/2.0 )
        if(a[md] < vl):
            l = md+1
        elif(a[md] >vl):
            r=md-1
        else:
            return md
    if(vl==3):
        return l
    return r

adj = defaultdict(list)
im = bsearch(3)
if(a[im]==3):#some weird occurrences when binary searching with parameter = 0
    im += 1
adj[0].append(a[0:im])
for j in a[0:im]:
    deg[j] += 1
for idx in range(len(a)):
    idx2 = bsearch(a[idx]+3)
    #print(a[idx])
    adj[a[idx]].append(a[idx+1:idx2+1])
    ls = a[idx+1:idx2+1]
    for j in ls:
        #print("DEGREE: " + str(j) )
        deg[j] += 1

print(adj)
vis = {}
def topological_sort(node):
    q = deque()
    q.append(node)
    order = []
    while(len(q) > 0):
        tmp = q.popleft()
        order.append(tmp)
        lst = adj[tmp][0]
        #print(lst)
        for elem in lst:
            #print(deg[elem])
            if(deg[elem]==1):
                q.appendleft(elem)
            deg[elem]-=1
    return order

topo_order = (topological_sort(0))
print(topo_order)
dp[topo_order[len(topo_order)-1]] = 1
for j in range(len(topo_order)-1,-1,-1):
    print(topo_order[j])
    adj_lst = adj[topo_order[j]][0]
    print(adj_lst)
    for k in adj_lst:
        dp[topo_order[j]] += dp[k]
print(dp[0])
