# CircuitPowerPlay
The tool is a simple tool to calculate the delay and power consumption of a digital circuit having registers and logic gates. This tool works on practical grounds based on the datasheet specifications of 90nm CMOS technology.

## How to use the timing_calculator.py tool
Suppose you have a circuit Y = A.B + C with A, B, and C as input and Y as output. You can implement it using the NAND gates as shown below.

You can change the data specification as per your requirement. But don't modify the basic functions in the code.

#write the timing circuit here

t1 = AD(0,0)

t2 = OR(t1,0)

t3 = reg1(5,0,0)[0] + t2

print("combinational circuit delay/ critical path delay =",t3/1000,"ns")

print("delay =",t3,"ps")
