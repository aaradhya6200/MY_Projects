def insert(H,k):
        j=len(H)
        H.append(k)
        while(j!=0 and H[(j-1)//2][0]<H[j][0]):
            temp=H[j]
            H[j]=H[(j-1)//2]
            H[(j-1)//2]=temp
            j=(j-1)//2
def swap(H,i,j):
        H[i],H[j] = H[j], H[i]
def heapUp(H,L,i) :
    while (i > 0 and H[(i - 1) // 2][1] < H[i][1]) :
        swap(H,(i - 1) // 2, i)
        swap(L,(i - 1) // 2, i)
        i =(i - 1) // 2

def heapDown(H,i) :
 
    maxIndex = i
    size=len(H)-1
    l =(2 * i) + 1
       
    if (l <= size and H[l][0] > H[maxIndex][0]) :
     
        maxIndex = l
    r = (2 * i) + 2
       
    if (r <= size and H[r][0] > H[maxIndex][0]) :
     
        maxIndex = r
    if (i != maxIndex) :
     
        swap(H,i, maxIndex)
        heapDown(H,maxIndex)
def extractmax(H):
        if(len(H)!=0):
            H[0], H[len(H)-1] = H[len(H)-1], H[0]
            maxlement=H.pop()
            heapDown(H,0) 
            return maxlement
        else:
            print("error")

def findMaxCapacity(n,links,s,t):
    m=len(links)
    adj_list=[]
    heap=[]
    for i in range(n):
        adj_list.append([i])
    for i in range (m):
        x=links[i][0]
        y=links[i][1]
        z=links[i][2]
        adj_list[x].append([y,z])
        adj_list[y].append([x,z])
    visited_list=[]
    for i in range(n):
        visited_list.append(float('-inf'))
    visited_list[s]=1
    x=adj_list[s][0]
    for j in range (1,len(adj_list[s])):
        u=adj_list[s][j][1]
        v=adj_list[s][j][0]
        list=[]
        list.append(u)
        list.append([s,v])
        insert(heap,list)
    m=extractmax(heap)
    capacity=m[0]
    path=m[1]
    while path[len(path)-1]!=t:
        p=path[len(path)-1]
        for j in range (1,len(adj_list[p])):
            path2=[]
            for i in range (len(path)):
                path2.append(path[i])
            list=[]
            u=adj_list[p][j][1]
            v=adj_list[p][j][0]
            path2.append(v)
            if visited_list[v]!=1:
                c=min(u,capacity)
                list.append(c)
                list.append(path2)
                insert(heap,list)
        m=extractmax(heap)
        capacity=m[0]
        path=m[1]
        visited_list[path[len(path)-1]]=1
    return (capacity,path)
        