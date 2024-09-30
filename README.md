# CircuitPowerPlay
The tool is a simple tool to calculate the delay and power consumption of a digital circuit having registers and logic gates. This tool works on practical grounds based on the datasheet specifications of 90nm CMOS technology.

## How to use the timing_calculator.py tool
Suppose you have a circuit Y = A.B + C with A, B, and C as input and Y as output. You can implement it using the NAND gates as shown below.

You can change the data specification as per your requirement. But don't modify the basic functions in the code.

#write the timing circuit here

t1 = AD(0,0) # here 0 is the entry time in picoseconds.

t2 = OR(t1,0)

t3 = reg1(5,0,0)[0] + t2 

print("combinational circuit delay/ critical path delay =",t3/1000,"ns")

print("delay =",t3,"ps")

# reading arguments for timing_calculator.py
All the arguments are entry time in picoseconds.

The integer returned by the function is the maximum delay in picoseconds.

For a 1-bit register reg1(en_t,d,c) #d - data bit, c - clk (negative 0/ positive 1), en_t - register enable time in clocks.

reg1(en_t,d,c)[0] is the output time by next state $Q$ and reg1(en_t,d,c)[1] is the output time by next state $\overline{Q}$.

## How to use the future_powerplay.py tool

To see the output just type "python3 future_powerplay.py".

Don't modify the second last argument of any calling function.
