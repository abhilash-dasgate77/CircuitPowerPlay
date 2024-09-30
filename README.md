# CircuitPowerPlay
The tool is a simple tool to calculate the delay and power consumption of a digital circuit having registers and logic gates. This tool works on practical grounds based on the datasheet specifications of 90nm CMOS technology.

## How to use the timing_calculator.py tool
Suppose you have a circuit Y = A.B + C. You can implement it using the NAND gates as shown below.

#write the timing circuit here
t1 = AD(0,0) # here 0 refers to the initial timing entry
t2 = OR(t1,0)

print("combinational circuit delay/ critical path delay =",t2/1000,"ns")

print("delay =",t2,"ps")
