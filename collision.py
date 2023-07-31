
class HeapPriorityQueue:
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j+1
    def _right(self, j):
        return 2*j+2

    def _has_left(self, j):
        return self._left(j) < len(self._data)
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._data[i][2],self._data[j][2]=self._data[j][2],self._data[i][2]
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j][0] < self._data[parent][0]:
            self._swap(j, parent)
            self._upheap(parent)
        elif j > 0 and self._data[j][0]== self._data[parent][0] and self._data[j][1]<self._data[parent][1]:
            self._swap(j, parent)
            self._upheap(parent)
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right][0] < self._data[left][0]:
                    small_child = right
                if self._data[right][0] == self._data[left][0] and self._data[right][1] < self._data[left][1]:
                    small_child = right
            if self._data[small_child][0] < self._data[j][0]:
                self._swap(j, small_child)
                self._downheap(small_child)
            if self._data[small_child][0] ==self._data[j][0] and self._data[small_child][1] <self._data[j][1]:
                self._swap(j, small_child)
                self._downheap(small_child)
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def _heapify(self):
        new=[None]*len(self._data)
        for i in range (len(self._data)-1,-1,-1):
            new[i]=self._data[i]
            self._data[i]=0
        for i in range (len(self._data)-1,-1,-1):
            self._data[i]=new[i]
            self._downheap(i)
    def _create(self,data):
        self._data.append([data[0],data[1],data[1]])
    def min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty" )
        item = self._data[0]
        return [item[0], item[1],item[2]]
        return [item[0], item[1],item[2]]
    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[-1]
    def replace_root(self,j):
        self._data[0][0]=j
        self._downheap(0)
    def _update(self,j):
        parent=self._parent(j)
        
        if self._data[parent][0]>self._data[j][0]:
            self._upheap(j)
        if self._data[parent][0]==self._data[j][0] and self._data[parent][1]>self._data[j][1]:
            self._upheap(j)
        if self._has_right(j):
            left=self._left(j)
            right=self._right(j)
            if (self._data[left][0]<self._data[j][0]) or (self._data[right][0]<self._data[j][0]):
                self._downheap(j)
            if (self._data[left][0]==self._data[j][0]) and (self._data[right][0]==self._data[j][0]) or (self._data[left][1]==self._data[j][1]) and (self._data[right][1]<self._data[j][1]):
                self._downheap(j)
        if self._has_right(j)==False and self._has_left(j):
            left=self._left(j)
            if (self._data[left][0]<self._data[j][0]):
                self._downheap(j)
            if (self._data[left][0]==self._data[j][0]) and (self._data[left][1]<self._data[j][1]):
                self._downheap(j)
    def print(self):
        return self._data

def velocities(m1,m2,v1,v2):
    v1f=((m1-m2)*v1/(m1+m2))+((2*m2*v2)/(m1+m2))
    v2f=((2*m1)*v1/(m1+m2))+((m2-m1)*v2/(m1+m2))
    return (v1f,v2f)

def listCollisions(M,x,v,m,T):
    U=[] #This is my final reuired list
    r=[]
    t=0
    h=0
    N=[[0,0]] #N is a list which will be storing previous collison time
    Y=[] #it will be my pointer list
    D=HeapPriorityQueue()  #Define a class of heap priority queue
    for i in range (0,len(M)-1):

        N.append([0,0])  
        if v[i+1]>=v[i]:
            D._create([10**16,i])
            Y.append(D.last())
            i+=1
        else:
            D._create([((x[i+1]-x[i])/(abs(v[i+1]-v[i]))),i])
            Y.append(D.last())
            i+=1
    D._heapify()
    while h<m and t<=T:
        l=D.min()
        r.append(l[0])
        if t<T:


            #update x of colliding particles after collision
            if l[0]!=N[l[1]][0]:
                x[l[1]]=x[l[1]]+(v[l[1]]*(l[0]-N[l[1]][0]))
                if (l[1]+2)<len(M):
                    e1=x[l[1]+2]+(v[l[1]+2]*(l[0]-N[l[1]+2][0]))
                if (l[1]-1)>=0:
                    
                    e2=x[l[1]-1]+(v[l[1]-1]*(l[0]-N[l[1]-1][0]))
                x[l[1]+1]=x[l[1]]
            elif l[0]==N[l[1]][0]:
                x[l[1]]=x[l[1]]+(v[l[1]]*(l[0]-N[l[1]][1]))
                if (l[1]+2)<len(M):
                    e1=x[l[1]+2]+(v[l[1]+2]*(l[0]-N[l[1]][1]))
                if (l[1]-1)>=0:
                    e2=x[l[1]-1]+(v[l[1]-1]*(l[0]-N[l[1]][1]))
                x[l[1]+1]=x[l[1]]
            [a,b]=velocities(M[l[1]],M[l[1]+1],v[l[1]],v[l[1]+1])
            if N[l[1]][0]==l[0]:
                N[l[1]][0]=l[0]
            elif N[l[1]][0]!=l[0]:
                N[l[1]][1]=N[l[1]][0]
                N[l[1]][0]=l[0]
            if N[l[1]+1][0]==l[0]:
                N[l[1]+1][0]=l[0]
            
            else:
                N[l[1]+1][1]=N[l[1]+1][0]
                N[l[1]+1][0]=l[0]

            #update velocities after collision
            v[l[1]]=a
            v[l[1]+1]=b
            t=l[0]
            if t!=10**16 and t<=T:
                U.append((round(l[0],4),l[1],round(x[l[1]],4)))

            #update time of precessor and successor of the two colliding particles and the new time of particles those collided just now
            if (l[1]-1)>=0:
                if v[l[1]]-v[l[1]-1]<0:
                    Y[l[1]-1][0]=r[-1]+abs((x[l[1]]-e2)/abs(v[l[1]]-v[l[1]-1]))
                    D._update(Y[l[1]-1][2])
                elif v[l[1]]-v[l[1]-1]>=0:
                    Y[l[1]-1][0]=10**16
                    D._update(Y[l[1]-1][2])
            if (l[1]+2)<len(M):
                if v[l[1]+2]-v[l[1]+1]<0:
                    Y[l[1]+1][0]=r[-1]+abs(e1-x[l[1]+1])/abs(v[l[1]+2]-v[l[1]+1])
                    D._update(Y[l[1]+1][2])
                if v[l[1]+2]-v[l[1]+1]>=0:
                    Y[l[1]+1][0]=10**16 
                    D._update(Y[l[1]+1][2])
            D.replace_root(10**16)

            h+=1
    return U
