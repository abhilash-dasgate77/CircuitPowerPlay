std_cell_delay = 23 #ps
# all values are time in pico second

def ND(a,b):
	return max(a,b) + std_cell_delay

def NT(a):
	t1 = ND(a,a)
	return t1

def AD(a,b):
	t0 = ND(a,b)
	return ND(t0,t0)

def OR(a,b):
	t0 = ND(a,a)
	t1 = ND(b,b)
	return ND(t0,t1)

def NR(a,b):
	t0 = OR(a,b)
	return NT(t0)

def XR(a,b):
	t1 = ND(a,b)
	t2 = ND(a,t1)
	t3 = ND(t1,b)
	t4 = ND(t2,t3)
	return t4

def sb4(x0,x1,x2,x3):
	y3 = x3
	y2 = XR(AD(x1,x3),x2)
	y1 = x1
	y0 = x0
	return (y0,y1,y2,y3)

def sb3(x0,x1,x2,x3):
	y3 = XR(AD(x0,x2),x3)
	y2 = x2
	y1 = x1
	y0 = x0
	return (y0,y1,y2,y3)

def sb2(x0,x1,x2,x3):
	y3 = x3
	y2 = x2
	y1 = x1
	y0 = XR(XR(AD(x0,x3),x1),0)
	return (y0,y1,y2,y3)

def sb1(x0,x1,x2,x3):
	y3 = x3
	y2 = x2
	y1 = XR(AD(x0,x2),x1)
	y0 = x0
	return (y0,y1,y2,y3)

def sb(x0,x1,x2,x3):
	t1 = sb4(x0,x1,x2,x3)
	t2 = sb3(t1[0],t1[1],t1[2],t1[3])
	t3 = sb2(t2[0],t2[1],t2[2],t2[3])
	t4 = sb1(t3[0],t3[1],t3[2],t3[3])
	return t4

def mx4(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15):
	c0 = XR(b12,b8)
	c1 = XR(b13,b9)
	c2 = XR(b14,b10)
	c3 = XR(b11,b15)
	c4 = b0
	c5 = b1
	c6 = b2
	c7 = b3
	c8 = XR(b0,b4)
	c9 = XR(b1,b5)
	c10 = XR(b2,b6)
	c11 = XR(b3,b7)
	c12 = b8
	c13 = b9
	c14 = b10
	c15 = b11
	return (c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)

def mx3(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15):
	c0 = XR(b12,b8)
	c1 = XR(b13,b9)
	c2 = XR(b10,b14)
	c3 = XR(b11,b15)
	c4 = b0
	c5 = b1
	c6 = b2
	c7 = b3
	c8 = XR(b3,b4)
	c9 = XR(b0,b5)
	c10 = XR(b1,b6)
	c11 = XR(XR(b3,b7),b2)
	c12 = b8
	c13 = b9
	c14 = b10
	c15 = b11
	return (c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)

def mx2(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15):
	c0 = XR(b13,b8)
	c1 = XR(b14,b9)
	c2 = XR(XR(b10,b12),b15)
	c3 = XR(b11,b12)
	c4 = b0
	c5 = b1
	c6 = b2
	c7 = b3
	c8 = XR(b3,b4)
	c9 = XR(b0,b5)
	c10 = XR(b1,b6)
	c11 = XR(XR(b3,b7),b2)
	c12 = b8
	c13 = b9
	c14 = b10
	c15 = b11
	return (c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)

def mx1(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15):
	c0 = XR(b12,b8)
	c1 = XR(b13,b9)
	c2 = XR(b14,b10)
	c3 = XR(b11,b15)
	c4 = b0
	c5 = b1
	c6 = b2
	c7 = b3
	c8 = XR(b0,b4)
	c9 = XR(b1,b5)
	c10 = XR(b2,b6)
	c11 = XR(b3,b7)
	c12 = b8
	c13 = b9
	c14 = b10
	c15 = b11
	return (c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)

def mx(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15):
	t0 = mx4(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15)
	t1 = mx3(t0[0],t0[1],t0[2],t0[3],t0[4],t0[5],t0[6],t0[7],t0[8],t0[9],t0[10],t0[11],t0[12],t0[13],t0[14],t0[15])
	t2 = mx2(t1[0],t1[1],t1[2],t1[3],t1[4],t1[5],t1[6],t1[7],t1[8],t1[9],t1[10],t1[11],t1[12],t1[13],t1[14],t1[15])
	t3 = mx1(t2[0],t2[1],t2[2],t2[3],t2[4],t2[5],t2[6],t2[7],t2[8],t2[9],t2[10],t2[11],t2[12],t2[13],t2[14],t2[15])
	return (t3[0],t3[1],t3[2],t3[3],t3[4],t3[5],t3[6],t3[7],t3[8],t3[9],t3[10],t3[11],t3[12],t3[13],t3[14],t3[15])

def mux2x1_16bit(a,b,s):#a[0-15], b[0-15]
	t0 = AD(a[0],NT(s))
	t1 = AD(b[0],s)
	t2 = OR(t0,t1)
	t = [t2]
	for i in range(1,16):
		t0 = AD(a[i],NT(s))
		t1 = AD(b[i],s)
		t2 = OR(t0,t1)
		t.append(t2)
	return t

def XR_16bit(a,b):#a[0-15], b[0-15]
	t2 = XR(a[0],b[0])
	t = [t2]
	for i in range(1,16):
		t2 = XR(a[i],b[i])
		t.append(t2)
	return t

def reg1(en_t,d,c):#d - data, c - clk, en_t - enable time in clocks
	t1 = ND(d,c)
	t2 = NT(d)

	t3 = ND(c,t2)

	t4 = ND(t1,0)
	t5 = ND(0,t3)

	while(en_t):
		t4 = ND(t1,t5)
		t5 = ND(t4,t3)
		en_t -= 1
	return (t4,t5)

def AD_16bit(a,b):#a[0-15], b[0-15]
	t2 = AD(a[0],b[0])
	t = [t2]
	for i in range(1,16):
		t2 = AD(a[i],b[i])
		t.append(t2)
	return t

b0 = 0 #1-bit
b1 = 0 #1-bit
b2 = 0 #1-bit
b3 = 0 #1-bit
Ksh16 = 0 #1-bit
Ksh5 = 0#1-bit
sm = 0 #1-bit

l = reg1(1+8*3,0,0)[0]  # 1 clock cycle to load + 8-bit register loads in parallel for X, K0 and K1.
X = [l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l]  #16-bit
K0 = [l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l] #16-bit
K1 = [l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l] #16-bit
RC0 = [l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l] #16-bit
RC1 = [l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l] #16-bit

# write the timing circuit here
clocks = 1

while(clocks):
	t1 = ND(b0,b2)                   #23
	t2 = XR(b1,b3)                   #69
	t3 = XR(b0,b2)                    #69
	t4 = sb(X[0],X[1],X[2],X[3])     #529
	t5 = sb(X[4],X[5],X[6],X[7])
	t12 = sb(X[8],X[9],X[10],X[11])
	t6 = sb(X[12],X[13],X[14],X[15])
	t7 = mux2x1_16bit(K0,K1,b3)       #115

	t13 = mx(t4[0],t4[1],t4[2],t4[3],t5[0],t5[1],t5[2],t5[3],t12[0],t12[1],t12[2],t12[3],t6[0],t6[1],t6[2],t6[3])
	t9 = OR(t2,t3)
	t10 = XR_16bit(X,t7)

	t8 = AD_16bit(RC1,[t9 for j in range(16)])
	t14 = mux2x1_16bit([t4[0],t4[1],t4[2],t4[3],t5[0],t5[1],t5[2],t5[3],t12[0],t12[1],t12[2],t12[3],t6[0],t6[1],t6[2],t6[3]],t13,t1)

	t11 = XR_16bit(t10,t8)

	t15 = mux2x1_16bit(t11,t14,sm)

	clocks -= 1

	X = t15

print("combinational circuit delay =",max(t15)/1000,"ns")

print("delay =",max(t15),"ps")

##############	TESTING ###################
#print(XR_16bit(K0,K1))
#print(mx(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
#print(sb(0,0,0,0))
#print(reg1(1,0,0))
