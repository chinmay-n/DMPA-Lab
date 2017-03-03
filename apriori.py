#k-means
import math

def median(q,k):
        p=len(q)
        med=list()
        w=list()
        w.append("")
        for i in range(k):
                med.append(0)
        for i in range(p):
                w=q[i]
                for j in range(k):
                        med[j]=med[j]+w[j]
        for i in range(k):
                med[i]/=p
        return med

x=int(input("Enter number of transactions N : "))
k=int(input("\nEnter the number of clusters : "))
y=int(input("\nEnter the number of attributes : "))
tr=list()
if(x<k):
        print("Clusters should be less than number of tuples")
        exit(0)
for i in range(x):
        tr.append(input("Enter comma separated values for transaction T"+str(i)))
        q=(tr[i].split(",",3))
        d=[]
        for item in q:
                item=float(item)
                d.append(item)
        tr[i]=(d[:y])
        print("\n"+str(tr))
clusters={}
leaders=list()
c=list()
l=list()
tmp=0
print(tr)
for i in range(k):
        l.append(tr[i])
        leaders.append([])
        c.append(0)
iter=0
while(leaders!=l):
        leaders=l[:]
        clusters.clear()
        print("Iteration : "+str(iter))
        iter+=1
        for i in range(k):
                clusters[i]=[]
        for i in range(x):
                temp=list()
                temp=tr[i]
                #print(str(i)+"temp:"+str(temp))
                for j in range(k):
                        d=list()
                        d=leaders[j]
                        tmp=0
                        #print("d:"+str(d))
                        for p in range(y):
                                alp=float(temp[p]-d[p])
                                tmp+=math.pow(alp,2)
                        c[j]=tmp
                        #print("c="+str(c))
                mi=min(c)
                ind=c.index(mi)
                s=clusters[ind]
                s.append(temp)
                clusters[ind]=s
        print("Clusters:"+str(clusters))
        for i in range(k):
                temp=clusters.get(i)
                #print("Temporary="+str(temp))
                l[i]=median(temp,k)
                #print(l)

print(str(leaders))
print(str(clusters))
