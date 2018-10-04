# Authors: Henry Sampson, Karim, Eric
# SIC instruction encoding format:
# ~~: R0/R1
# --: R2/R3
# lw    p 000 xx yy
# sw    p 001 xx yy
# add   p 100 ~~ --
# addi  p 100 -- ~~
# sub   p 010 ~~ --
# subi  p 010 -- ~~
# sltR0 p 011 ~~ --
# seqR0 p 011 -- ~~
# xor   p 110 ~~ --
# and   p 110 -- ~~
# init  p 101 ~~ --
# sll   p 101 -- ~~
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
            line = line.replace('00', '$0')
        elif (line[7:9] == '01'):
            line = line.replace('01', '$1')
        elif (line[7:9] == '10'):
            line = line.replace('10', '$2')
        else:
            line = line.replace('11', '$3')


    elif (line[1:3] == '001'):  # sw
        line[1:3] = line[1:3].replace('001', 'sw ')
        if(line[4:5] == '00'):
            line[4:5] = line[4:5].replace('00', '$0, ')
        elif(line[4:5] == '01'):
            line[4:5] = line[4:5].replace('01', '$1, ')
        elif(line[4:5] == '10'):
            line[4:5] = line[4:5].replace('10', '$2, ')
        else:
            line[4:5] = line[4:5].replace('11', '$3, ')

        if (line[6:7] == '00'):
            line[6:7] = line[6:7].replace('00', '$0')
        elif (line[6:7] == '01'):
            line[6:7] = line[6:7].replace('01', '$1')
        elif (line[6:7] == '10'):
            line[6:7] = line[6:7].replace('10', '$2')
        else:
            line[6:7] = line[6:7].replace('11', '$3')

    elif (line[1:3] == '100'):  # add/addi
        if(line[4] == '0'):
            line[1:3] = line[1:3].replace('100', 'add ')
        if(line[4] == '1'):
            line[1:3] = line[1:3].replace('100', 'addi ')

        if(line[4:5] == '00'):
            line[4:5] = line[4:5].replace('00', '$0, ')
        elif(line[4:5] == '01'):
            line[4:5] = line[4:5].replace('01', '$1, ')
        elif(line[4:5] == '10'):
            line[4:5] = line[4:5].replace('10', '$2, ')
        else:
            line[4:5] = line[4:5].replace('11', '$3, ')

        if (line[6:7] == '00'):
            line[6:7] = line[6:7].replace('00', '$0')
        elif (line[6:7] == '01'):
            line[6:7] = line[6:7].replace('01', '$1')
        elif (line[6:7] == '10'):
            line[6:7] = line[6:7].replace('10', '$2')
        else:
            line[6:7] = line[6:7].replace('11', '$3')

    elif (line[1:3] == '010'):  # sub/subi
        if (line[4] == '0'):
            line[1:3] = line[1:3].replace('010', 'sub ')
        if (line[4] == '1'):
            line[1:3] = line[1:3].replace('010', 'subi ')

        if (line[4:5] == '00'):
            line[4:5] = line[4:5].replace('00', '$0, ')
        elif (line[4:5] == '01'):
            line[4:5] = line[4:5].replace('01', '$1, ')
        elif (line[4:5] == '10'):
            line[4:5] = line[4:5].replace('10', '$2, ')
        else:
            line[4:5] = line[4:5].replace('11', '$3, ')

        if (line[6:7] == '00'):
            line[6:7] = line[6:7].replace('00', '$0')
        elif (line[6:7] == '01'):
            line[6:7] = line[6:7].replace('01', '$1')
        elif (line[6:7] == '10'):
            line[6:7] = line[6:7].replace('10', '$2')
        else:
            line[6:7] = line[6:7].replace('11', '$3')

    elif (line[1:3] == '011'):  # sltR0/seqR0
        if (line[4] == '0'):
            line[1:3] = line[1:3].replace('011', 'sltR0 ')
        if (line[4] == '1'):
            line[1:3] = line[1:3].replace('011', 'seqR0 ')

        if (line[4:5] == '00'):
            line[4:5] = line[4:5].replace('00', '$0, ')
        elif (line[4:5] == '01'):
            line[4:5] = line[4:5].replace('01', '$1, ')
        elif (line[4:5] == '10'):
            line[4:5] = line[4:5].replace('10', '$2, ')
        else:
            line[4:5] = line[4:5].replace('11', '$3, ')

        if (line[6:7] == '00'):
            line[6:7] = line[6:7].replace('00', '$0')
        elif (line[6:7] == '01'):
            line[6:7] = line[6:7].replace('01', '$1')
        elif (line[6:7] == '10'):
            line[6:7] = line[6:7].replace('10', '$2')
        else:
            line[6:7] = line[6:7].replace('11', '$3')

    elif (line[1:3] == '110'):  # xor/and
        if (line[4] == '0'):
            line[1:3] = line[1:3].replace('110', 'xor ')
        if (line[4] == '1'):
            line[1:3] = line[1:3].replace('110', 'and ')

        if (line[4:5] == '00'):
            line[4:5] = line[4:5].replace('00', '$0, ')
        elif (line[4:5] == '01'):
            line[4:5] = line[4:5].replace('01', '$1, ')
        elif (line[4:5] == '10'):
            line[4:5] = line[4:5].replace('10', '$2, ')
        else:
            line[4:5] = line[4:5].replace('11', '$3, ')

        if (line[6:7] == '00'):
            line[6:7] = line[6:7].replace('00', '$0')
        elif (line[6:7] == '01'):
            line[6:7] = line[6:7].replace('01', '$1')
        elif (line[6:7] == '10'):
            line[6:7] = line[6:7].replace('10', '$2')
        else:
            line[6:7] = line[6:7].replace('11', '$3')

    elif (line[1:3] == '101'):  # init/sll
        if (line[4] == '0'):
            line[1:3] = line[1:3].replace('101', 'init ')
        if (line[4] == '1'):
            line[1:3] = line[1:3].replace('101', 'sll ')

        if (line[4:5] == '00'):
            line[4:5] = line[4:5].replace('00', '$0, ')
        elif (line[4:5] == '01'):
            line[4:5] = line[4:5].replace('01', '$1, ')
        elif (line[4:5] == '10'):
            line[4:5] = line[4:5].replace('10', '$2, ')
        else:
            line[4:5] = line[4:5].replace('11', '$3, ')

        if (line[6:7] == '00'):
            line[6:7] = line[6:7].replace('00', '$0')
        elif (line[6:7] == '01'):
            line[6:7] = line[6:7].replace('01', '$1')
        elif (line[6:7] == '10'):
            line[6:7] = line[6:7].replace('10', '$2')
        else:
            line[6:7] = line[6:7].replace('11', '$3')

    elif (line[1:3] == '111'):  # j/beqR0
        if (line[4] == '0'):
            line[1:3] = line[1:3].replace('111', 'j ')
        if (line[4] == '1'):
            line[1:3] = line[1:3].replace('111', 'beqR0 ')

        if (line[5:7] == '000'):
            line[4:7] = line[4:7].replace('000', '0')
        elif (line[5:7] == '001'):
            line[4:7] = line[4:7].replace('001', '1')
        elif (line[5:7] == '010'):
            line[4:7] = line[4:7].replace('010', '2')
        elif (line[5:7] == '011'):
            line[4:7] = line[4:7].replace('011', '3')
        elif (line[5:7] == '100'):
            line[4:7] = line[4:7].replace('100', '4')
        elif (line[5:7] == '101'):
            line[4:7] = line[4:7].replace('101', '5')
        elif (line[5:7] == '110'):
            line[4:7] = line[4:7].replace('110', '6')
        else:
            line[4:7] = line[4:7].replace('111', '7')

        line = line.replace("0", "")

    elif (line[1:7] == '1111111'):
        line[1:7] = line[1:7].replace('1111111', 'Halt')
    else:
        print("Unknown instruction:" + line)

    output_file.write(line)

input_file.close()
output_file.close()
