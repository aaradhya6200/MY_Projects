import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

# return appropriate N that satisfies the error bounds
def findN(eps,m):
    return int(2*(m/eps)*(math.log(26,2))*(math.log((2*(m/eps))*(math.log(26,2)),2)))
    #let's denote the pattern by P and substring diff than P by Q such that,
    #Lets denote (Σ(26**m-i-1)(Pi-Qi))by Y
    #Here we can see that Q is a prime factor of |Y|,it will give the false positive.
    #let denote the prime number upper bound by N
    #probablity of Q when it is false positive= (no. of prime factors of |Y|)/(total no. of prime <=N
    # Return sorted list of starting indices where p matches x
    # so as per the formula given in assignment ,(1)the no. of prime factor of any no. a is equal or less than to log|a|,(2)the no. of primes less than or equal to π(N) ≥ N / (2 log2 N)
	# let us assume N be the upper bound prime no. 
	# so the probability of l being false +ve is no. , e =< (2m(logN)log26)/N......(lets take e=eps)
	#so, N/logN => log(2mlog26/e).......1
	# taking log on both side in 1 we get, logN-log(logN) => log(2mlog26/e)..........2
	# by multiplying 1 and 2 we get ; N-(Nlog(logN)/logN) => (2mlog26/e)(log(2mlog26/e))
	# so as we know, 0<=log(logN)/logN<=1/2 
    # 4(log(2mlog26/e))<= N, Therefore any N greater than or equal to (2mlog26/e)log(2mlog26/e)


def modPatternMatch(q,p,x):
    m = len(p)
    n = len(x)
    p_hashcode=0
    finallist=[]
    #finallist is the list where index will be stored
    for i in range(0,m):
        p_hashcode=(p_hashcode * 26 + (ord(p[i])-ord('A')))%q
    #p_hashcode is the value of function %q calculated with the help of pattern
    x_hashcode=0
    p=1
    for i in range(1,m):
        p=(p*26)%q
    #this loop calculate the value of 26 to the power (m-1) mod q

    for i in range(0,m):
        x_hashcode=(x_hashcode * 26 + (ord(x[i])-ord('A')))%q
    #x_hashcode is the value of function %q calculated with the help of x(calculated the hashcode of first m values of x string)

    if(x_hashcode==p_hashcode):
        finallist.append(0)
    #If x_hashcode and p_hashcode is equal then I apended 0 because first m terms of string will be same as pattern.
    for j in range(n-m):
        x_hashcode=((x_hashcode-p*(ord(x[j])-ord('A')))*26 +(ord(x[j+m])-ord('A')))%q
        if(x_hashcode==p_hashcode):
            finallist.append(j+1)
        #traverse the string and calculated the value of each m charector and compare it with pattern vale.If it will be equal then I append the index in finallist.
    return finallist
    #return the finallist containing index.

def modPatternMatchWildcard(q,p,x):
    m=len(p)
    n=len(x)
    p_hashcode=0
    finallist=[]
    #finallist is the list where I stored index
    for i in range(m):
        if(p[i]=='?'):
            l=i
            p_hashcode = (p_hashcode*26)%q 
        else:
            # p_hashcode=p_hashcode + (pow(26,m-i-1)*(ord(p[i])-ord("A")))
            p_hashcode=(p_hashcode * 26 + (ord(p[i])-ord('A')))%q
    #from this loop I calculated the value of function mod%q of the pattern
    #p_mod=p_hashcode%q
    x_hashcode=0
    for i in range(0,m):
        if(i==l):
            x_hashcode = (x_hashcode*26)%q
        else:
            x_hashcode=(x_hashcode*26+(ord(x[i])-ord("A")))%q
     #from this loop I calculated the value of function mod%q of the first m term of the string
    if(x_hashcode==p_hashcode):
        finallist.append(0)
    # if the value of first m terms of string matches with pattern value then I appended 0 as a index in my finallist.
    p=1
    for i in range(1,m):
        p=(p*26)%q
    #from  this for loop I calculated the value of 26 to the power (m-1) mod q.

    r=1
    for i in range(1,m-l):
        r=(r*26)%q
    #from  this for loop I calculated the value of 26 to the power (m-l-1)mod q.

    o=1
    for i in range(0,m-l):
        o=(o*26)%q
    #from  this for loop I calculated the value of 26 to the power (m-l-1)mod q.


    for j in range(n-m):
        x_hashcode=((x_hashcode-p*(ord(x[j])-ord('A')))*26 +(ord(x[j+m])-ord('A')) - r*(ord(x[l+j+1])-ord('A')) + o*(ord(x[l+j])-ord('A')))%q
        if(x_hashcode==p_hashcode):
            finallist.append(j+1)
        #traverse the string and calculated the value of each m charector and compare it with pattern vale.If it will be equal then I append the index in finallist.
    return finallist
    #return the finallist containing index.
