class Node:
      
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self,data):
        self.data = data
        self.next = None
      
class Stack:
      
    # head is default NULL
    def __init__(self):
        self.head = None
      
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
      
    # Method to add data to the stack
    # adds to the start of the stack
    def push(self,data):
          
        if self.head == None:
            self.head=Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    # Remove element that is the current head (start of the stack)
    def pop(self):
          
        if self.isempty():
            return None
              
        else:
            # Removes the head node and makes 
            #the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
      
    # Returns the head node data
    def top(self):
          
        if self.isempty():
            return None
              
        else:
            return self.head.data
st=Stack()
# I have created a stack named st.
def findPositionandDistance(P):
    list=[]
    # I have created  a list in which I append the value of x,y,z,d.
    s=len(P)
    x=0
    y=0
    z=0
    d=0
    st.push(1)
    #initally I push a element in stack that is 1
    i=0
    while i<s:
        if(P[i].isdigit()):
            num=""
            #num is a string in which i put the continuous digit
            while(P[i]!='('):
                num=num+P[i]
                i=i+1
            st.push(st.top()*int(num))
        #now we puch another element in st which is the multiplication of num and the top element of st
        elif(P[i]=='('):
            k=True
            i=i+1
            while(k and P[i]!=')'):
                if(P[i].isdigit()):
                    k=False
                    #here x is the x coordinate
                    #y is the y coordinate
                    #z is the  z coordinate
                else:
                    if(P[i]=='+' and P[i+1]=='X'):
                        x=st.top()+x
                        d=d+st.top()
                    elif(P[i]=='+' and P[i+1]=='Y'):
                        y=st.top()+y
                        d=d+st.top()
                    elif(P[i]=='+' and P[i+1]=='Z'):
                        z=st.top()+z
                        d=d+st.top()
                    elif(P[i]=='-' and P[i+1]=='X'):
                        x=x-st.top()
                        d=d+st.top()
                    elif(P[i]=='-' and P[i+1]=='Y'):
                        y=y-st.top()
                        d=d+st.top()
                    elif(P[i]=='-' and P[i+1]=='Z'):
                        z=z-st.top()
                        d=d+st.top()
                    i=i+2
        elif(P[i]==")"):
            st.pop()
            # if ")" came then we pop the element in st because that number will not multipled by string after this as closed bracket came.
            i=i+1
        else:
            if(P[i]=='+' or P[i]=='-'):
                if(P[i]=='+'and P[i+1]=='X'):
                    x=x+1
                    d=d+1
                elif(P[i]=='+'and P[i+1]=='Y'):
                    y=y+1
                    d=d+1
                elif(P[i]=='+'and P[i+1]=='Z'):
                    z=z+1
                    d=d+1
                elif(P[i]=='-'and P[i+1]=='X'):
                    x=x-1
                    d=d+1
                elif(P[i]=='-'and P[i+1]=='Y'):
                    y=y-1
                    d=d+1
                elif(P[i]=='-'and P[i+1]=='Z'):
                    z=z-1
                    d=d+1
                i=i+2
    list.append(x)
    list.append(y)
    list.append(z)
    list.append(d)
    return list

