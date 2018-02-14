class Calculations:
    def __init__(self,indx):
        self.name = indx
        self.mc = []

    def findMnC(self,x1,y1,x2,y2):
        if (x1-x2)!=0:
            m = (y1-y2)/(x1-x2)
            c = y1-(m*x1)
            if abs(m)==0:
                self.mc.insert(0,abs(m))
            else:
                self.mc.insert(0,m)
            self.mc.insert(1,c)
        else:
            self.mc.insert[0,None]
            self.mc.insert[1,0]
            self.mc.insert[2,x1]

    def returnIndex(self):
        return self.name

class Positions:
    def __init__(self,default_m,default_c):
        self.position = None
        self.default_m = default_m
        self.default_c = default_c

    def mEqual(self,m):
        if self.default_m==m:
            return True
        else:
            return False

    def cEqual(self,c):
        if self.default_c==c:
            return True
        else:
            return False
        
    def leftOright(self,tmpc):
        if self.default_m>0:
            if self.default_c>tmpc:
                return 1  #right/front
            else:
                return 0  #left/back
        elif self.default_m<0:
            if self.default_c>tmpc:
                return 0  #left/back
            else:
                return 1  #right/front
        else:
            return

    def isIntersec(self,m,c,dArray,tArray):
        tt1 = float(tArray[1])
        tt2 = float(tArray[3])
        ttm1 = max(tt1,tt2)
        ttm2 = min(tt1,tt2)
        if self.default_m!=None and m!=None:
            if self.default_m*m<0:                  #when intersec would happen if m1 x m2 <0
                if self.default_c<c:
                    dt = max(float(dArray[1]),float(dArray[3]))
                    if ttm1>dt and ttm2<dt:
                        return True
                    else:
                        return False
                elif self.default_c>c:
                    dt = min(float(dArray[1]),float(dArray[3]))
                    if ttm1>dt and ttm2<dt:
                        return True
                    else:
                        return False
                else:
                    return True           #if both c's are equal
            elif self.default_m!=m and self.default_m*m>0:
                x = (c - self.default_c)/(self.default_m-m)
                y = m*x+c
                if y>ttm2 and y<ttm1:
                    return True
                else:
                    return False
            else:
                return False
        elif self.default_m==None:
            x = float(dArray[0])
            tx1 = float(tArray[0])
            tx2 = float(tArray[2])
            txm1 = max(tx1,tx2)
            txm2 = min(tx1,tx2)
            
            if x>txm2 and x<txm1:
                return True
            else:
                return False
        elif m==None:
            x = float(tArray[0])
            dx1 = float(dArray[0])
            dx2 = float(dArray[2])
            dxm1 = max(dx1,dx2)
            dxm2 = min(dx1,dx2)
            
            if x>dxm2 and x<dxm1:
                return True
            else:
                return False
        else:
            return False     
