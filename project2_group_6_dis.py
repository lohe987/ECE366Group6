# Authors: Henry Sampson, Karim, Eric
# SIC instruction encoding format:
# ~~: R0/R1
# --: R2/R3
# ii: immediate
# lw    p 000 xx yy
# sw    p 001 xx yy
# add   p 100 ~~ --
# addi  p 100 -- ii
# sub   p 010 ~~ --
# subi  p 010 -- ii
# sltR0 p 011 ~~ --
# seqR0 p 011 -- ~~
# xor   p 110 ~~ --
# and   p 110 -- ~~
# init  p 101 ~~ ii
# sll   p 101 -- ii
# j     p 111 0i ii
# beqR0 p 111 1i ii
# Halt  p 111 11 11
# -----------------------------------------------------------

print("ECE366 Fall 2018 mini SIC disassembler")
input_file = open("MIPS_machine_code", "r")
output_file = open("MIPS_asm.txt", "w")

for line in input_file:
    line = line.replace("\n", "")  # remove 'endline' character
    if(line[0:1] == '0'):
        line = line.replace("0", "", 1)  # remove parity bit
    else:
        line = line.replace("1", "", 1)  # remove parity bit
    line = line.replace(" ", "")  # remove spaces anywhere in line

    if (line[0:3] == '000'):  # lw
        line = line.replace("000", "lw ", 1)  # remove 000 and use lw
        if(line[3:5] == '00'):
            line = line.replace('00', '$0, ', 1)
        elif(line[3:5] == '01'):
            line = line.replace('01', '$1, ', 1)
        elif(line[3:5] == '10'):
            line = line.replace('10', '$2, ', 1)
        else:
            line = line.replace('11', '$3, ', 1)

        if (line[7:9] == '00'):
            line = line.replace('00', '($0)', 1)
        elif (line[7:9] == '01'):
            line = line.replace('01', '($1)', 1)
        elif (line[7:9] == '10'):
            line = line.replace('10', '($2)', 1)
        else:
            line = line.replace('11', '($3)', 1)

    elif (line[0:3] == '001'):  # sw
        line = line.replace("001", "sw ", 1)  # remove 000 and use sw
        if(line[3:5] == '00'):
            line = line.replace('00', '$0, ', 1)
        elif(line[3:5] == '01'):
            line = line.replace('01', '$1, ', 1)
        elif(line[3:5] == '10'):
            line = line.replace('10', '$2, ', 1)
        else:
            line = line.replace('11', '$3, ', 1)

        if (line[7:9] == '00'):
            line = line.replace('00', '($0)', 1)
        elif (line[7:9] == '01'):
            line = line.replace('01', '($1)', 1)
        elif (line[7:9] == '10'):
            line = line.replace('10', '($2)', 1)
        else:
            line = line.replace('11', '($3)', 1)



    elif (line[0:3] == '100'):  # add/addi
        if(line[3:4] == '0'):
            line = line.replace('100', 'add ', 1)
            if (line[4:6] == '00'):
                line = line.replace('00', '$0, ', 1)
            elif (line[4:6] == '01'):
                line = line.replace('01', '$1, ', 1)
            elif (line[4:6] == '10'):
                line = line.replace('10', '$2, ', 1)
            else:
                line = line.replace('11', '$3, ', 1)

            if (line[8:10] == '00'):
                line = line.replace('00', '$0', 1)
            elif (line[8:10] == '01'):
                line = line.replace('01', '$1', 1)
            elif (line[8:10] == '10'):
                line = line.replace('10', '$2', 1)
            else:
                line = line.replace('11', '$3', 1)
        else:
            line = line.replace('100', 'addi ', 1)
            if (line[5:7] == '00'):
                line = line.replace('00', '$0, ', 1)
            elif (line[5:7] == '01'):
                line = line.replace('01', '$1, ', 1)
            elif (line[5:7] == '10'):
                line = line.replace('10', '$2, ', 1)
            else:
                line = line.replace('11', '$3, ', 1)

            if (line[9:11] == '00'):
                line = line.replace('00', '0')
            elif (line[9:11] == '01'):
                line = line.replace('01', '1')
            elif (line[9:11] == '10'):
                line = line.replace('10', '2')
            elif (line[9:11] == '11'):
                line = line.replace('11', '3')



    elif (line[0:3] == '010'):  # sub/subi
        if(line[3:4] == '0'):
            line = line.replace('010', 'sub ', 1)
            if (line[4:6] == '00'):
                line = line.replace('00', '$0, ', 1)
            elif (line[4:6] == '01'):
                line = line.replace('01', '$1, ', 1)
            elif (line[4:6] == '10'):
                line = line.replace('10', '$2, ', 1)
            else:
                line = line.replace('11', '$3, ', 1)

            if (line[8:10] == '00'):
                line = line.replace('00', '$0', 1)
            elif (line[8:10] == '01'):
                line = line.replace('01', '$1', 1)
            elif (line[8:10] == '10'):
                line = line.replace('10', '$2', 1)
            else:
                line = line.replace('11', '$3', 1)
        else:
            line = line.replace('010', 'subi ', 1)
            if (line[5:7] == '00'):
                line = line.replace('00', '$0, ', 1)
            elif (line[5:7] == '01'):
                line = line.replace('01', '$1, ', 1)
            elif (line[5:7] == '10'):
                line = line.replace('10', '$2, ', 1)
            else:
                line = line.replace('11', '$3, ', 1)

            if (line[9:11] == '00'):
                line = line.replace('00', '0')
            elif (line[9:11] == '01'):
                line = line.replace('01', '1')
            elif (line[9:11] == '10'):
                line = line.replace('10', '2')
            elif (line[9:11] == '11'):
                line = line.replace('11', '3')

    elif (line[0:3] == '011'):  # sltR0/seqR0
        if(line[3:4] == '0'):
            line = line.replace('011', 'sltR0 ', 1)
            if (line[6:8] == '00'):
                line = line.replace('00', '$0, ', 1)
            elif (line[6:8] == '01'):
                line = line.replace('01', '$1, ', 1)
            elif (line[6:8] == '10'):
                line = line.replace('10', '$2, ', 1)
            else:
                line = line.replace('11', '$3, ', 1)

            if (line[10:12] == '00'):
                line = line.replace('00', '$0', 1)
            elif (line[10:12] == '01'):
                line = line.replace('01', '$1', 1)
            elif (line[10:12] == '10'):
                line = line.replace('10', '$2', 1)
            else:
                line = line.replace('11', '$3', 1)
        else:
            line = line.replace('011', 'seqR0 ', 1)
            if (line[6:8] == '00'):
                line = line.replace('00', '$0, ', 1)
            elif (line[6:8] == '01'):
                line = line.replace('01', '$1, ', 1)
            elif (line[6:8] == '10'):
                line = line.replace('10', '$2, ', 1)
            else:
                line = line.replace('11', '$3, ', 1)

            if (line[10:12] == '00'):
                line = line.replace('00', '$0', 1)
            elif (line[10:12] == '01'):
                line = line.replace('01', '$1', 1)
            elif (line[10:12] == '10'):
                line = line.replace('10', '$2', 1)
            else:
                line = line.replace('11', '$3', 1)

    elif (line[0:3] == '110'):  # xor/and
        if (line[3:4] == '0'):
            line = line.replace('110', 'xor ', 1)
        else:
            line = line.replace('110', 'and ', 1)

        if (line[4:6] == '00'):
            line = line.replace('00', '$0, ', 1)
        elif (line[4:6] == '01'):
            line = line.replace('01', '$1, ', 1)
        elif (line[4:6] == '10'):
            line = line.replace('10', '$2, ', 1)
        else:
            line = line.replace('11', '$3, ', 1)

        if (line[8:10] == '00'):
            line = line.replace('00', '$0', 1)
        elif (line[8:10] == '01'):
            line = line.replace('01', '$1', 1)
        elif (line[8:10] == '10'):
            line = line.replace('10', '$2', 1)
        else:
            line = line.replace('11', '$3', 1)

    elif (line[0:3] == '101'):  # init/sll
        if(line[3:4] == '1'):
            line = line.replace('101', 'sll ', 1)
            if (line[4:6] == '00'):
                line = line.replace('00', '$0, ', 1)
            elif (line[4:6] == '01'):
                line = line.replace('01', '$1, ', 1)
            elif (line[4:6] == '10'):
                line = line.replace('10', '$2, ', 1)
            else:
                line = line.replace('11', '$3, ', 1)

            if (line[8:10] == '00'):
                line = line.replace('00', '0')
            elif (line[8:10] == '01'):
                line = line.replace('01', '1')
            elif (line[8:10] == '10'):
                line = line.replace('10', '2')
            elif (line[8:10] == '11'):
                line = line.replace('11', '3')
        else:
            line = line.replace('101', 'init ', 1)
            if (line[5:7] == '00'):
                line = line.replace('00', '$0, ', 1)
            elif (line[5:7] == '01'):
                line = line.replace('01', '$1, ', 1)
            elif (line[5:7] == '10'):
                line = line.replace('10', '$2, ', 1)
            else:
                line = line.replace('11', '$3, ', 1)

            if (line[9:11] == '00'):
                line = line.replace('00', '0')
            elif (line[9:11] == '01'):
                line = line.replace('01', '1')
            elif (line[9:11] == '10'):
                line = line.replace('10', '-2')
            elif (line[9:11] == '11'):
                line = line.replace('11', '-1')

    elif (line[0:3] == '111'):  # j/beqR0
        if (line[3:4] == '0'):
            line = line.replace('1110', 'j ', 1)
            if (line[2:5] == '000'):
                line = line.replace('000', '0')
            elif (line[2:5] == '001'):
                line = line.replace('001', '1')
            elif (line[2:5] == '010'):
                line = line.replace('010', '2')
            elif (line[2:5] == '011'):
                line = line.replace('011', '3')
            elif (line[2:5] == '100'):
                line = line.replace('100', '4')
            elif (line[2:5] == '101'):
                line = line.replace('101', '5')
            elif (line[2:5] == '110'):
                line = line.replace('110', '6')
            else:
                line = line.replace('111', '7')
        else:
            line = line.replace('1111', 'beqR0 ', 1)
            if (line[6:9] == '000'):
                line = line.replace('000', '0')
            elif (line[6:9] == '001'):
                line = line.replace('001', '1')
            elif (line[6:9] == '010'):
                line = line.replace('010', '2')
            elif (line[6:9] == '011'):
                line = line.replace('011', '3')
            elif (line[6:9] == '100'):
                line = line.replace('100', '4')
            elif (line[6:9] == '101'):
                line = line.replace('101', '5')
            elif (line[6:9] == '110'):
                line = line.replace('110', '6')
            else:
                line = line.replace('beqR0 111', 'Halt')

    else:
        print("Unknown instruction:" + line)

    output_file.write(line + "\n")

input_file.close()
output_file.close()
