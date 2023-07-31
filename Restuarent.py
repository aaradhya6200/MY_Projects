def sorting(qp,y):
    list_left=[]
    list_right=[]
    list1=[]
    for i in range(len(y)):
            if y[i][0]<qp[0]:
                list_left.append(y[i])
            else:
                list_right.append(y[i])
    list1.append(list_left)
    list1.append(list_right)
    return list1
    
def bst(root,list,list1):
    if root is None:
        return
    if (root.val[1]>=list1[1][0]) and (root.val[1]<=list1[1][1]):
        temp=root.val
        list.append(temp)
        bst(root.left,list,list1)
        bst(root.right,list,list1)
    elif(root.val[1]<=list1[1][0]):
        if(root.val[1]==list1[1][0]):
            temp=root.val
            list.append(temp)
        bst(root.right,list,list1)
    elif(root.val[1]>=list1[1][1]):
        if(root.val[1]==list1[1][1]):
            temp=root.val
            list.append(temp)
        bst(root.left,list,list1)
                
class node:
    def __init__(self,key):
        #created  a node
        self.val=key
        self.left=None
        self.right=None
def RangeTree(list,l,r):
    if(l>r ):
        return None
    if(r-l)%2==0:
        mid=(r+l)//2
    else:
        mid=(r+l)//2 +1
    root=node(list[mid])
    root.left=RangeTree(list,l,mid-1)
    root.right=RangeTree(list,mid+1,r)
    return root     
class  PointDatabase1:
    def __init__(self,sorted_x,sorted_y,l):
            n=len(sorted_x)
            m=len(sorted_x)//2
            self.val=sorted_x[m]
            self.left=None
            self.right=None
            self.root1=sorted_y
            list=sorting(self.val,sorted_y)
            if m>0:
                self.left=PointDatabase1(sorted_x[:m],list[0],0)
            if (n-m)>0 and n!=1:
                if len(sorted_x)!=1:
                    self.right=PointDatabase1(sorted_x[m:],list[1],0)
                else:
                    if l==0:
                        l=l+1
                        self.right=PointDatabase1(sorted_x[m:],list[1],l)
def bst1(list,pts,q):
    for i in list:
        if(i[1]>=q[1][0] and i[1]<=q[1][1]):
            pts.append(i)

class  PointDatabase:
    def __init__(self, pointlist):
        if len(pointlist)==0:
            self.val=None
        else:
            #I have sorted x and y and stored in sorted_x and sorted_y respectively
            pointlist.sort(key=lambda x:x[0])
            sorted_x=[]
            for i in range(len(pointlist)):
                sorted_x.append(pointlist[i])
            pointlist.sort(key=lambda x:x[1])
            sorted_y=[]
            for i in range(len(pointlist)):
                sorted_y.append(pointlist[i])
            root=PointDatabase1(sorted_x,sorted_y,0)
            #I have send the the sorted_x and sorted_y to create a range tree.
            self.val=root.val
            self.root1=root.root1
            self.left=root.left
            self.right=root.right        
    def searchNearby(self, q, d):
        x1=q[0]-d
        x2=q[0]+d
        y1=q[1]-d
        y2=q[1]+d
        list1=[(x1,x2),(y1,y2)]
        list2=[]
        #x1,x2,y1,y2 are the boundary points
        def newfunction(root,list1,dirc,div):
            if root==None:
                return 
            if(root.left==None and root.right ==None):
                if(root.val[0]>=list1[0][0] and root.val[0]<=list1[0][1]):
                    if(root.val[1]>=list1[1][0] and root.val[1]<=list1[1][1]):
                        list2.append(root.val)
                return
            m=root.val
            if m[0]<=list1[0][0]:
                newfunction(root.right,list1,dirc,div)
            elif m[0]>list1[0][1]:
                newfunction(root.left,list1,dirc,div)
            elif (list1[0][0] < m[0] <= list1[0][1]):
                
                if(div==0):
                    div=div+1
                    newfunction(root.left,list1,0,div)
                    newfunction(root.right,list1,1,div)
                else:
                    if(dirc==0):
                        newfunction(root.left,list1,dirc,div)
                        bst1(root.right.root1,list2,list1)
                    else:
                        newfunction(root.right,list1,dirc,div)
                        bst1(root.left.root1,list2,list1)
        if self.val==None:
            return list2
        else:
            newfunction(self,list1,-1,0)
            return list2

        
        
        
        

        
