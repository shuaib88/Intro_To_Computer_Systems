

//initialize a counter

//if keyboard is pressed, advance the counter

//if keyboard is released, check the counter is greater than 16384 and then unwind the counter






(LOOP0)		//clears the starting visual memory location
@16384		//set R0 to our starting visual memory location
D=A 		//store desired start memory location
@counter	//access counter
M=D 		//start counter from base


@24576		//keyboard memory location
D=M			//store keyboard value
@LOOP2		//getting ready to jump if condition not met
D;JEQ		//jump to clearing if keyboard is not pressed

@24576		//keyboard memory location
D=M			//store keyboard value
@LOOP1		//getting ready to jump if condition not met
D;JNE		//jump to fill if keyboard is pressed



(LOOP1)		//check if key is pressed then fill 
@24576		//keyboard memory location
D=M			//store keyboard value
@LOOP0		//getting ready to jump if keyboard not pressed
D;JEQ		//jump to clearing if value is zero

			//code to fills 16384 to 24575

@counter 	//access counter
A=M 		//go to location of current count
M=-1		//set value of current visual to -1
@counter 	//access counter
M=M+1 		//increment counter location
@LOOP1		//setting up for jump
0;JMP


(LOOP2) 	//check if key is not pressed then clear
@24576		//keyboard memory location
D=M			//store keyboard value
@LOOP0
D;JNE		//jump to filling if there IS a value

			//code to clear 16384 to 24575

@counter 	//access counter
A=M 		//go to location of current count
M=0			//set counter value to zero
@counter 	//access counter
M=M+1 		//increment counter location
@LOOP2		//setting up for jump
0;JMP