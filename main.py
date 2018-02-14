import re
from calc import *
from Tree import *

def function(flst,head,s):
    selected = flst[s-1]
    slcArray = selected.split(" ")
    sc = Calculations(flst.index(selected)+1)
    sc.findMnC(float(slcArray[0]),float(slcArray[1]),float(slcArray[2]),float(slcArray[3]))
    sp = Positions(sc.mc[0],sc.mc[1])

    head.insertHead(sc.mc[0],s)
    for i in flst:
        tmpi = i.split(" ")
        indx = flst.index(i)+1
        tmpc = Calculations(indx)
        tmpc.findMnC(float(tmpi[0]),float(tmpi[1]),float(tmpi[2]),float(tmpi[3]))
      
        if sp.mEqual(tmpc.mc[0]):             #if m is equal
            if tmpc.mc[0]!=None:              #if m != infinity
                if sp.cEqual(tmpc.mc[1]):     #if c is also equal,then both lines are same  
                    
                    continue
                else:
                    if sp.leftOright(tmpc.mc[1])==1:
                        head.insertRight(tmpc.mc[0],indx)
                                                    #right/front
                    else:
                        head.insertLeft(tmpc.mc[0],indx)
                                                   #left/back
            else:                             #if m is infinity
                if sc.mc[2]>tmpc.mc[2]:
                    head.insertLeft(tmpc.mc[0],indx)        #check right or left by x coardinates
                  
                else:
                    head.insertRight(tmpc.mc[0],indx)
                   
        else:                               #if m is not equal
            if sp.isIntersec(tmpc.mc[0],tmpc.mc[1],slcArray,tmpi)!=True:         #check intersection of 2 lines
                if tmpc.mc[0]!=None and sc.mc[0]!=None:     #if both m's are not infinity
                    if tmpc.mc[0]*sc.mc[0]>0:               #if m1 x m2 > 0 
                        if sp.leftOright(tmpc.mc[1])==1:
                            head.insertRight(tmpc.mc[0],indx)
                        
                        else:
                            head.insertLeft(tmpc.mc[0],indx)
                            
                    elif sc.mc[0]==0:
                        k = max(float(tmpi[1]),float(tmpi[3]))
                        t = min(float(tmpi[1]),float(tmpi[3]))
                        
                        if k<float(slcArray[1]) and t<float(slcArray[1]):
                            head.insertLeft(tmpc.mc[0],indx)
                        else:
                            head.insertRight(tmpc.mc[0],indx)
                    elif tmpc.mc[0]==0:
                        k = max(float(slcArray[0]),float(slcArray[2]))
                        t = min(float(slcArray[0]),float(slcArray[2]))
                        kk = max(float(tmpi[0]),float(tmpi[2]))
                        tt = min(float(tmpi[0]),float(tmpi[2]))

                        if k<tt:
                            head.insertRight(tmpc.mc[0],indx)
                        else:
                            head.insertLeft(tmpc.mc[0],indx)
                    else:                                   #if m1 x m2 < 0
                        k = max(float(slcArray[0]),float(slcArray[2]))
                        t = min(float(slcArray[0]),float(slcArray[2]))
                        if k>float(tmpi[0]) and k>float(tmpi[2]):
                            head.insertRight(tmpc.mc[0],indx)
                            
                        elif t<float(tmpi[0]) and t<float(tmpi[2]):
                            head.insertLeft(tmpc.mc[0],indx)
                          

                elif sc.mc[0]==None:                        #if given line's m is infinity

                    k = float(slcArray[0])
                    if k>float(tmpi[0]) and k>float(tmpi[2]):
                        head.insertLeftt(tmpc.mc[0],indx)
                      
                    elif k<float(tmpi[0]) and k<float(tmpi[2]):
                        head.insertRight(tmpc.mc[0],indx)
                    

                elif tmpc.mc[0]==None:                     #if other lines' m's are infinity
                    
                    k = max(float(slcArray[0]),float(slcArray[2]))
                    t = min(float(slcArray[0]),float(slcArray[2]))
                    if k<float(tmpi[0]):
                        head.insertRight(tmpc.mc[0],indx)
                   
                    elif t>float(tmpi[0]):
                        head.insertLeft(tmpc.mc[0],indx)
                        
                else:
                    continue
            else:
                head.insertLeft(tmpc.mc[0],indx)
                head.insertRight(tmpc.mc[0],indx)
            
                #if intersect happense insert both lines into left and right

def main():
    n = int(input().strip())
    s = int(input().strip())
    lst = []
    flst = []
    front = []
    frontlst = []
    back = []
    backlst = []
    for i in range(n):
        lst.append(input())
    for i in range(n):
        k = " ".join(re.findall("[-\d]+",lst[i]))
        flst.append(k)

    head1 = BinaryS()
    function(flst,head1,s)
    r = head1.node
    l = head1.node
    k = None

    while r.right.node!=None:
        k = r.right.node.index
        front.append(k)
        r = r.right.node

    while l.left.node!=None:
        k = l.left.node.index
        back.append(k)
        l = l.left.node

    for i in front:
        frontlst.append(flst[i-1])

    for i in back:
        backlst.append(flst[i-1])

    if len(frontlst)>0:
        print("The line infront of all lines is : "+str(front[len(front)-1]))
    else:
        print("No lines infront of "+str(s)+" line and the line infront of whole lines : "+str(s))
    if len(frontlst)!=0:
        print("Front lines for line "+str(s)+" are : ")
        print(front)
    if len(backlst)!=0:
        print("Back lines for line "+str(s)+" are : ")
        print(back)
main()
