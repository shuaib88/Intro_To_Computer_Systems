//Main.vm
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
(Main.fibonacci)
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
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// ARITHMETIC
@SP
AM=M-1
D=M
A=A-1
D=M-D
@FALSE1
D;JGE
@SP
A=M-1
M=-1
@CONTINUE1
0;JMP
(FALSE1)
@SP
A=M-1
M=0
(CONTINUE1)
//IfGoto
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE
//GoTo
@IF_FALSE
D;JMP
// LABEL
(IF_TRUE)
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
// LABEL
(IF_FALSE)
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
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// ARITHMETIC
@SP
AM=M-1
D=M
A=A-1
M=M-D
// writeCall
@Main.fibonacci2
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
@Main.fibonacci
0;JMP
(Main.fibonacci2)
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
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// ARITHMETIC
@SP
AM=M-1
D=M
A=A-1
M=M-D
// writeCall
@Main.fibonacci3
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
@Main.fibonacci
0;JMP
(Main.fibonacci3)
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
//Sys.vm
// writeFunction
(Sys.init)
//PUSH_POP
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// writeCall
@Main.fibonacci4
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
@Main.fibonacci
0;JMP
(Main.fibonacci4)
// LABEL
(WHILE)
//GoTo
@WHILE
D;JMP
