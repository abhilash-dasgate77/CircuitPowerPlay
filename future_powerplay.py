std_cell_delay = 23 #ps
std_cell_pwr = 0.88 #nW static // no frequency involved.
std_load_cap = 17.6 #fF
Vdd = 1.2 #V
f = 10 #MHz




def ND(a,b,stage_t,stage_p): #building block
	c = a * b
	c_ = 1 - c
	if stage_t == -1:
		y = global_time[len(global_time) - 1]
		global_time.append(round(y + std_cell_delay,2))


	else:
		y = global_time[len(global_time) + stage_t]
		global_time[len(global_time) + stage_t] = max(global_time[len(global_time) + stage_t ],round(y + std_cell_delay,2))


	if stage_p == -1:
		y = global_pwr[len(global_pwr) - 1]
		global_pwr.append(round(y + std_cell_pwr,2))
	else:
		y = global_pwr[len(global_pwr) + stage_p]
		global_pwr[len(global_pwr) + stage_p + 1] = round(y + std_cell_pwr,2)
	return c_


def NT(a,stage_t,stage_p):
	t1 = ND(a,a,-1 + (1 + stage_t),-1 + (1 + stage_p))
	return t1


def OR(a,b,stage_t,stage_p):
	t1 = ND(a,a,-1 + (1 + stage_t),-1 + (1 + stage_p))
	t2 = ND(b,b,-2 + (1 + stage_t),-1 + (1 + stage_p))


	t3 = ND(t1,t2,-1 + (1 + stage_t),-1 + (1 + stage_p))
	return t3


def XR(a,b,stage_t,stage_p):
	t1 = ND(a,b,-1 + (1 + stage_t),-1 + (1 + stage_p))


	t2 = ND(a,t1,-1 + (1 + stage_t),-1 + (1 + stage_p))
	t3 = ND(t1,b,-2 + (1 + stage_t),-1 + (1 + stage_p))


	t4 = ND(t2,t3,-1 + (1 + stage_t),-1 + (1 + stage_p))
	return t4






def AD(a,b,stage_t,stage_p):
	t1 = ND(a,b,-1 + (1 + stage_t),-1 + (1 + stage_p));


	t2 = NT(t1,-1 + (1 + stage_t),-1 + (1 + stage_p));
	return t2


def NR(a,b,stage_t,stage_p):
	t1 = OR(a,b,-1 + (1 + stage_t),-1 + (1 + stage_p))


	t2 = NT(t1,-1 + (1 + stage_t),-1 + (1 + stage_p))
	return t2


def reg1(en_t,d,c,stage_t,stage_p):#d - data, c - clk, en_t - enable time in clocks
	t1 = ND(d,c,-1 + (1 + stage_t),-1 + (1 + stage_p))
	t2 = NT(d,-2 + (1 + stage_t),-1 + (1 + stage_p))


	t3 = ND(c,t2,-1 + (1 + stage_t),-1 + (1 + stage_p))


	t4 = ND(t1,0,-1 + (1 + stage_t),-1 + (1 + stage_p))
	t5 = ND(1,t3,-2 + (1 + stage_t),-1 + (1 + stage_p))


	while(en_t):
		t4 = ND(t1,t5,-1 + (1 + stage_t),-1 + (1 + stage_p))
		t5 = ND(t4,t3,-2 + (1 + stage_t),-1 + (1 + stage_p))
		en_t -= 1
	return (t4,t5)


def sb4(x0,x1,x2,x3,stage_t,stage_p):
	y3 = x3
	y2 = XR(AD(x1,x3,-1 + (1 + stage_t),-1 + (1 + stage_p)),x2,-1 + (1 + stage_t),-1 + (1 + stage_p))
	y1 = x1
	y0 = x0
	return (y0,y1,y2,y3)


def sb3(x0,x1,x2,x3,stage_t,stage_p):
	y3 = XR(AD(x0,x2,-1 + (1 + stage_t),-1 + (1 + stage_p)),x3,-1 + (1 + stage_t),-1 + (1 + stage_p))
	y2 = x2
	y1 = x1
	y0 = x0
	return (y0,y1,y2,y3)


def sb2(x0,x1,x2,x3,stage_t,stage_p):
	y3 = x3
	y2 = x2
	y1 = x1
	y0 = XR(XR(AD(x0,x3,-1 + (1 + stage_t),-1 + (1 + stage_p)),x1,-1 + (1 + stage_t),-1 + (1 + stage_p)),1,-1 + (1 + stage_t),-1 + (1 + stage_p))
	return (y0,y1,y2,y3)


def sb1(x0,x1,x2,x3,stage_t,stage_p):
	y3 = x3
	y2 = x2
	y1 = XR(AD(x0,x2,-1 + (1 + stage_t),-1 + (1 + stage_p)),x1,-1 + (1 + stage_t),-1 + (1 + stage_p))
	y0 = x0
	return (y0,y1,y2,y3)


def sb(x0,x1,x2,x3,stage_t,stage_p):
	t1 = sb4(x0,x1,x2,x3,stage_t,stage_p)
	t2 = sb3(t1[0],t1[1],t1[2],t1[3],stage_t,stage_p)
	t3 = sb2(t2[0],t2[1],t2[2],t2[3],stage_t,stage_p)
	t4 = sb1(t3[0],t3[1],t3[2],t3[3],stage_t,stage_p)
	return t4


def mx4(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,stage_t,stage_p):
	c0 = XR(b12,b8,-1 + (1 + stage_t),-1 + (1 + stage_p))
	c1 = XR(b13,b9,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c2 = XR(b14,b10,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c3 = XR(b11,b15,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c4 = b0
	c5 = b1
	c6 = b2
	c7 = b3
	c8 = XR(b0,b4,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c9 = XR(b1,b5,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c10 = XR(b2,b6,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c11 = XR(b3,b7,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c12 = b8
	c13 = b9
	c14 = b10
	c15 = b11
	return (c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)


def mx3(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,stage_t,stage_p):
	c0 = XR(b12,b8,-1 + (1 + stage_t),-1 + (1 + stage_p))
	c1 = XR(b13,b9,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c2 = XR(b10,b14,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c3 = XR(b11,b15,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c4 = b0
	c5 = b1
	c6 = b2
	c7 = b3
	c8 = XR(b3,b4,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c9 = XR(b0,b5,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c10 = XR(b1,b6,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c11 = XR(XR(b3,b7,-2 + (1 + stage_t),-1 + (1 + stage_p)),b2,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c12 = b8
	c13 = b9
	c14 = b10
	c15 = b11
	return (c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)


def mx2(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,stage_t,stage_p):
	c0 = XR(b13,b8,-1 + (1 + stage_t),-1 + (1 + stage_p))
	c1 = XR(b14,b9,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c2 = XR(XR(b10,b12,-2 + (1 + stage_t),-1 + (1 + stage_p)),b15,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c3 = XR(b11,b12,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c4 = b0
	c5 = b1
	c6 = b2
	c7 = b3
	c8 = XR(b3,b4,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c9 = XR(b0,b5,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c10 = XR(b1,b6,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c11 = XR(XR(b3,b7,-2 + (1 + stage_t),-1 + (1 + stage_p)),b2,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c12 = b8
	c13 = b9
	c14 = b10
	c15 = b11
	return (c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)


def mx1(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,stage_t,stage_p):
	c0 = XR(b12,b8,-1 + (1 + stage_t),-1 + (1 + stage_p))
	c1 = XR(b13,b9,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c2 = XR(b14,b10,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c3 = XR(b11,b15,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c4 = b0
	c5 = b1
	c6 = b2
	c7 = b3
	c8 = XR(b0,b4,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c9 = XR(b1,b5,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c10 = XR(b2,b6,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c11 = XR(b3,b7,-2 + (1 + stage_t),-1 + (1 + stage_p))
	c12 = b8
	c13 = b9
	c14 = b10
	c15 = b11
	return (c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)


def mx(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,stage_t,stage_p):
	t0 = mx4(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,stage_t,stage_p)
	t1 = mx3(t0[0],t0[1],t0[2],t0[3],t0[4],t0[5],t0[6],t0[7],t0[8],t0[9],t0[10],t0[11],t0[12],t0[13],t0[14],t0[15],stage_t,stage_p)
	t2 = mx2(t1[0],t1[1],t1[2],t1[3],t1[4],t1[5],t1[6],t1[7],t1[8],t1[9],t1[10],t1[11],t1[12],t1[13],t1[14],t1[15],stage_t,stage_p)
	t3 = mx1(t2[0],t2[1],t2[2],t2[3],t2[4],t2[5],t2[6],t2[7],t2[8],t2[9],t2[10],t2[11],t2[12],t2[13],t2[14],t2[15],stage_t,stage_p)
	return (t3[0],t3[1],t3[2],t3[3],t3[4],t3[5],t3[6],t3[7],t3[8],t3[9],t3[10],t3[11],t3[12],t3[13],t3[14],t3[15])


def mux2x1_16bit(a,b,s,stage_t,stage_p):#a[0-15], b[0-15]
	t0 = AD(a[0],NT(s,-1 + (1 + stage_t),-1 + (1 + stage_p)),-1 + (1 + stage_t),-1 + (1 + stage_p))
	t1 = AD(b[0],s,-2 + (1 + stage_t),-1 + (1 + stage_p))
	t2 = OR(t0,t1,-1 + (1 + stage_t),-1 + (1 + stage_p))
	t = [t2]
	for i in range(1,16):
		t0 = AD(a[i],NT(s,-3 + (1 + stage_t),-1 + (1 + stage_p)),-2 + (1 + stage_t),-1 + (1 + stage_p))
		t1 = AD(b[i],s,-2 + (1 + stage_t),-1 + (1 + stage_p))
		t2 = OR(t0,t1,-2 + (1 + stage_t),-1 + (1 + stage_p))
		t.append(t2)
	return t


def XR_16bit(a,b,stage_t,stage_p):#a[0-15], b[0-15]
	t2 = XR(a[0],b[0],-1 + (1 + stage_t),-1 + (1 + stage_p))
	t = [t2]
	for i in range(1,16):
		t2 = XR(a[i],b[i],-2 + (1 + stage_t),-1 + (1 + stage_p))
		t.append(t2)
	return t


global_time = [0] #ps
global_pwr = [0]  #nW at given time instance
#write circuit code here


b0 = 0 #1-bit
b1 = 0 #1-bit
b2 = 0 #1-bit
b3 = 0 #1-bit
Ksh16 = 0 #1-bit
Ksh5 = 0#1-bit
sm = 1 #1-bit
X = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #16-bit
K0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #16-bit
K1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #16-bit
RC0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #16-bit
RC1 = [0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0] #16-bit


t1 = ND(b0,b2,-1,-1)                   #23
t2 = XR(b1,b3,-2,-1)                   #69
t3 = XR(b0,b2,-2,-1)                    #69
t4 = sb(X[0],X[1],X[2],X[3],-2,-1)     #529
t5 = sb(X[4],X[5],X[6],X[7],-2,-1)
t12 = sb(X[8],X[9],X[10],X[11],-2,-1)
t6 = sb(X[12],X[13],X[14],X[15],-2,-1)
t7 = mux2x1_16bit(K0,K1,b3,-2,-1)       #115


t13 = mx(t4[0],t4[1],t4[2],t4[3],t5[0],t5[1],t5[2],t5[3],t12[0],t12[1],t12[2],t12[3],t6[0],t6[1],t6[2],t6[3],-1,-1)
t9 = OR(t2,t3,-2,-1)
t10 = XR_16bit(X,t7,-2,-1)


t8 = mux2x1_16bit(RC0,RC1,t9,-1,-1)
t14 = mux2x1_16bit([t4[0],t4[1],t4[2],t4[3],t5[0],t5[1],t5[2],t5[3],t12[0],t12[1],t12[2],t12[3],t6[0],t6[1],t6[2],t6[3]],t13,t1,-2,-1)


t11 = XR_16bit(t10,t8,-1,-1)


t15 = mux2x1_16bit(t11,t14,sm,-1,-1)


tmp0 = global_pwr[len(global_pwr)-1]/1000
print("static power (non-reg)=",tmp0,"uW")
# static power for logic gates ends here


global_time = [0] #ps
global_pwr = [0]  #nW at given time instance
#write circuit code here
clockCycles = 144 #total clock cycles
reg1(clockCycles,1,1,-1,-1)
numberRegs = 3
reg_bit = 64
for i in range(reg_bit*numberRegs):
	reg1(clockCycles,1,1,-2,-1)


tmp1 = global_pwr[len(global_pwr)-1]/1000
print("dynamic power (reg)=",tmp1,"uW")
# static power for registers ends here


alpha = 0.8
Dy_power = alpha * std_load_cap*10**(-15) * Vdd * Vdd * f*10**(6)
print("dynamic power =",Dy_power*10**6,"uW")


print("total power dissipated =",tmp0 + tmp1 + Dy_power,"uW")
'''


##########	TEST	#################
#print(ND(0,0,-1,-1))
#print(XR_16bit([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1],-1,-1))
#print(AD(0,0,-1,-1))
#print(sb(0,0,0,0,-1,-1))
#print(mux2x1_16bit([0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1],0,-1,-1))
#print(mx(0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,-1,-1))
print(reg1(144,1,1),reg1(144,1,1))
######### SAMPLE CIRCUIT , not A and B xor C ##################
t1 = NT(0,-1,-1)
t2 = OR(1,1,-2,-1)
t3 = XR(1,1,-2,-1)
t4 = AD(1,1,-2,-1)
print(global_time[len(global_time)-1],"ps, ",global_pwr[len(global_pwr)-1],"nW")
'''

