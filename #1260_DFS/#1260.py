
n,l,s = map(int, input().split())
line = []
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(l):
    a,b = map(int, input().split())
    line.append([a,b])
    arr[a][b] = 1
    arr[b][a] = 1

def dfs(current_node, row, foot_print):
    foot_print += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_print:
            foot_print = dfs(search_node, row, foot_print)
    return foot_print
    
def bfs(start):
    queue = [start]
    footprint = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(arr[current_node])):
            if arr[current_node][search_node] and search_node not in footprint:
                footprint += [search_node]
                queue += [search_node]
    return footprint
    

print(dfs(s,arr,[]))
# print(bfs(s))
