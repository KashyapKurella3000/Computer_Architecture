 
print ('DOT PRODUCT Simulation without forwarding in Python ')
print ('STUDENT ID - 016018925 ')
 
# string
ST_ID1 = "016018925"
ST_ID2 = "561563470"

dot_product = 0 + 3 + 48 + 0 + 3 + 0 + 9 + 8 + 35

print('Vector1 = { 0, 1, 6, 0, 1, 8, 9, 2, 5 }')
print('Vector2 = { 5, 6, 1, 5, 6, 3, 4, 7, 0 }')

# Register 0 initialized to 0
REG0 = 0

# Store values of vector in list
# VALUES in memory

# Pointer to Vector 2 ST_ID1
REG3 = 0
# Pointer to Vector 2 ST_ID2
REG5 = 0

REG2 = 0

# Store the values in REG2_49
ST_ID1 = [int(i) for i in ST_ID1]

# Store the values in REG4_49
ST_ID2 = [int(i) for i in ST_ID2]


NUM_OF_STALLS = 0
NUM_OF_CPU_CYCLES = 0

# addu $r1 $r0 $r0
REG1 = REG0
NUM_OF_CPU_CYCLES += 1

REG7 = len(ST_ID1)
NUM_OF_CPU_CYCLES += 1

def done():
    global NUM_OF_STALLS
    NUM_OF_STALLS = NUM_OF_STALLS + 3
    print("Dot product result sotred in R1: ", REG1)
    print("Number of stalls: " + str(NUM_OF_STALLS))
    exit()

while True:
    # Breaking logic, The REG7 is decremented after every iteration
    # beq $r7 $r0 done
    if REG0 == REG7:
        done()
    else:
        # Cycle 3
        if ST_ID1: # Fetch lw $r2 0($r3)
            NUM_OF_CPU_CYCLES += 1
            pass

        # cycle 4
        if ST_ID1[REG3] != '': # Decode lw $r2 0($r3)
            if ST_ID2: # Fetch lw $r4 0($r5)
                NUM_OF_CPU_CYCLES += 1
                pass

        # cycle 5
        if len(ST_ID1) >= 0: # Execute lw $r2 0($r3)
            if ST_ID2[REG5] != '':  # Decode lw $r4 0($r5)
                if REG2 != None: # Fetch mul $R2 $R2 $R4
                    NUM_OF_CPU_CYCLES += 1
                    pass

        # cycle 6
        if ST_ID1[REG3] >= 0 : # Memory lw $R2 0($R3)
            if len(ST_ID2) >= 0:  # Execute lw $r4 0($r5)
                # Stall mul $r2 $r2 $r4
                NUM_OF_STALLS += 1
                NUM_OF_CPU_CYCLES += 1
                pass

        # cycle 7
        if ST_ID1[REG3] >= 0:
            REG2 = ST_ID1[REG3] # Write lw $R2 0($R3)
            if ST_ID2[REG5] >= 0:  # Memory lw $R4 0($R5)
                # Stall mul $r2 $r2 $r4
                NUM_OF_STALLS += 1
                NUM_OF_CPU_CYCLES += 1
                pass

        # cycle 8
        if ST_ID2[REG5] >= 0:
            REG4 = ST_ID2[REG5] # Write lw $R4 0($R5)
            NUM_OF_STALLS += 1
            NUM_OF_CPU_CYCLES += 1
            pass


        # cycle 9
        if REG2 != '': # Decode mul $R2 $R2 $R4
            # Fetch addu $R1 $R1 $R2
            if REG1 >= 0:
                NUM_OF_CPU_CYCLES += 1
                pass

        # cycle 10
        if len(ST_ID1) >= 0: # Execute mul $R2 $R2 $R4
            # Stall addu $R1 $R1 $R2
            NUM_OF_CPU_CYCLES += 1
            NUM_OF_STALLS += 1

        # cycle 11
        if REG2 >= 0:  # Memory mul $R2 $R2 $R4
            # Stall addu $R1 $R1 $R2
            NUM_OF_STALLS += 1
            NUM_OF_CPU_CYCLES += 1

        # cycle 12
        if REG2 >= 0:  # Write mul $R2 $R2 $R4
            REG2 = REG2 * REG4
            # Stall addu $R1 $R1 $R2
            NUM_OF_STALLS += 1
            NUM_OF_CPU_CYCLES += 1


        # Cycle 13
        # Decode addu $R1 $R1 $R2
        if REG1 != '':
            if REG3 >= 0: # Fetch addu $R3 $R3 $R4
                NUM_OF_CPU_CYCLES += 1
                pass

        # Cycle 14
        if REG1 >= 0: # Execute addu $R1 $R1 $R2
            if REG3 != '': # Decode addiu $R3 $R3 #4
                if REG5 >= 0:  # Fetch addiu $R5 $R5 #4
                    NUM_OF_CPU_CYCLES += 1
                    pass

        # Cycle 15
        if REG1 >= 0:  # Memory addu $R1 $R1 $R2
            if REG3 >= 0:  # Execute addiu $R3 $R3 #4
                if REG5 != '':  # Decode addiu $R5 $R5 #4
                    if REG7 >= 0:  # Fetch addiu $R7 $R7 #-1
                        NUM_OF_CPU_CYCLES += 1
                        pass

        # Cycle 16
        if REG1 >= 0:  # Write addu $R1 $R1 $R2
            REG1 = REG1 + REG2
            if REG3 >= 0:  # Memory addiu $R3 $R3 #4
                if REG5 >= 0:  # Execute addiu $R5 $R5 #4
                    if REG7 != '':  # Decode addiu $R7 $R7 #-1
                        NUM_OF_CPU_CYCLES += 1
                        pass

        # Cycle 17
        if REG3 >= 0:  # Write addiu $R3 $R3 #4
            REG3 = REG3 + 1
            if REG5 >= 0:  # Memory addiu $R5 $R5 #4
                if REG7 >= 0:  # Execute addiu $R7 $R7 #-1
                    NUM_OF_CPU_CYCLES += 1
                    pass # Fetch beq $R7 $R0 done

        # Cycle 18
        if REG5 >= 0 : # Write addiu $R5 $R5 #4
            REG5 = REG5 + 1
            if REG7 >= 0:  # Memory addiu $R7 $R7 #-1
                # Stall beq $R7 $R0 done
                NUM_OF_CPU_CYCLES += 1
                NUM_OF_STALLS += 1

        # Cycle 19
        if REG7 >= 0:  # Write addiu $R7 $R7 #-1
            REG7 = REG7 - 1
            # Stall beq $R7 $R0 done
            NUM_OF_CPU_CYCLES += 1
            NUM_OF_STALLS += 1

        # Cycle 20
        if REG7 != '':  # Decode beq Rr7 R0 done ; done looping?
            NUM_OF_CPU_CYCLES += 1
            pass  # NOP due to STALL

        # Cycle 21
        if REG7 >= 0:  # Execute BEQ $R7 $R0 done ; done looping?
            NUM_OF_CPU_CYCLES += 1
            pass

        # Cycle 22
        if REG7: # Memory BEQ $R7 $R0 done ; done looping?
            NUM_OF_CPU_CYCLES += 1
            pass

        # Cycle 23
        NUM_OF_CPU_CYCLES += 1
        if REG7 == REG0: # Write BEQ $R7 $R0 done ; done looping?
            pass

        print("---------Iteration------ " + str(REG3))
        print("Register Values :" + "\tR0 - " + str(REG0) + "\tR1 - " + str(REG1) + "\tR2 - " + str(REG2)
               + "\tR3 - " + str(REG3)+ "\tR4 - " + str(REG4)+ "\tR5 - " + str(REG5)
               + "\tR7 - " + str(REG7))
        # print("Number of stalls: " + str(NUM_OF_STALLS))
        print("Number of Clock cycles: " + str(NUM_OF_CPU_CYCLES))






