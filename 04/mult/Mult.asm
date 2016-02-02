// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

//My strategy is to read x + y as x added y times. X being the addend and y being a counter. 

@R2 	//Location of product
0 		//Zeroes the destination for the product


@R1 	//Jump to END if counter is <=0
D=M 	//storing counter for comparison
@END 	//queing if condition not met
D;JLE 	//Jump if counter is 0 or less than

(LOOP) 	//I think this identifies start of loop
@R0 	//Accessing the addend
D=M 	//Store D in memory
@R2 	//Access destination for final product
M=D+M 	//Add the addend to running total
@R1 	//Access counter
M=M-1 	//Decrement counter
D=M 	//Store counter in D for comparison
@LOOP
D;JGT 	//Jump if counter is >0

(END)
@END
0;JMP 	//Infinite Loop


