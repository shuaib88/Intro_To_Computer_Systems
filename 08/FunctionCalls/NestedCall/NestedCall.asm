//Sys.vm
// INIT
@256
D=A
@SP
M=D
// writeCall
@Sys.init0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init0)
// writeFunction
(Sys.init)
// writeCall
@Sys.main1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
(Sys.main1)
//PUSH_POP
@SP
AM=M-1
D=M
@6
M=D
// LABEL
(LOOP)
//GoTo
@LOOP
D;JMP
// writeFunction
(Sys.main)
//PUSH_POP
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// writeCall
@Sys.add122
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
0;JMP
(Sys.add122)
//PUSH_POP
@SP
AM=M-1
D=M
@5
M=D
//PUSH_POP
@246
D=A
@SP
A=M
M=D
@SP
M=M+1
// RETURN
@LCL
D=M
@FRAME
M=D
@FRAME
D=M
@5
A=D-A
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@FRAME
A=M-1
D=M
@THAT
M=D
@FRAME
D=M
@2
A=D-A
D=M
@THIS
M=D
@FRAME
D=M
@3
A=D-A
D=M
@ARG
M=D
@FRAME
D=M
@4
A=D-A
D=M
@LCL
M=D
@RET
A=M
0;JMP
// writeFunction
(Sys.add12)
//PUSH_POP
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH_POP
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH_POP
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//PUSH_POP
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//PUSH_POP
@12
D=A
@SP
A=M
M=D
@SP
M=M+1
// ARITHMETIC
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// RETURN
@LCL
D=M
@FRAME
M=D
@FRAME
D=M
@5
A=D-A
D=M
@RET
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@FRAME
A=M-1
D=M
@THAT
M=D
@FRAME
D=M
@2
A=D-A
D=M
@THIS
M=D
@FRAME
D=M
@3
A=D-A
D=M
@ARG
M=D
@FRAME
D=M
@4
A=D-A
D=M
@LCL
M=D
@RET
A=M
0;JMP
