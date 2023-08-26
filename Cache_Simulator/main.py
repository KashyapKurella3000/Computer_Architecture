import math
file1_20 = open('addr_trace.txt', 'r') #reads the file
Lines_20 = file1_20.read()
Line_20 = Lines_20.splitlines() #used to seperate \n from the file
count_20 = 0
a_20 = []
# Strips the newline character
k_20 = len(Line_20) #actual length 1500000
i_20 = 0
while i_20<k_20:
    if count_20 == 1048576: # limited to make it 2^N format, 2^20
        break
    if i_20==0:
        a_20.append(int(Line_20[i_20]))
        count_20+=1
    else:
        ab_20 = int(Line_20[i_20])+a_20[-1] #will add the previous address
        a_20.append(ab_20)
        count_20+=1
    i_20+=1
#print(a_20) # MEMORY, elements from adder trace file
Memory_size_20 = len(a_20)
#######################------CHANGE VALUES HERE BELOW-----------
##################
##number of words for the cache
block_size_20 = int(input("enter block_size")) #1 #can be changed, user input
byte_ref_20= 1024
cache_sz_20 = int(input('enter_cache_size'))
CACHE_SIZE_20 =cache_sz_20 * byte_ref_20 #8*1024 #can be chaged, user input
set_associativity = int(input('enter set_ass'))#2
###############################################################################
n_blocks_memory_20 = int(Memory_size_20/block_size_20) #number of blocks in memory
line_size_20 = block_size_20 #LINE IN CACHE MEMORY
#print(a_20)
def MEMORY_20(a_20,Memory_size_20,block_size_20,n_blocks_memory_20):
    i_20 = 0
    c_20 = 0
    d_20 = {}
    while i_20<n_blocks_memory_20:
        aa_20 = []
        k_20 = c_20
        while c_20<k_20+block_size_20:
            aa_20.append(a_20[c_20])
            c_20+=1

        d_20[i_20] = aa_20
        i_20+=1
    return d_20

MEM_ORG_20 = MEMORY_20(a_20,Memory_size_20,block_size_20,n_blocks_memory_20) #memory organized in blocks
# print("------------Memory------------------")
# print(MEM_ORG_20)
# print("Number of blocks in memory:", len(MEM_ORG_20))
# print("------------------x-------------------")


#K = BLOCK_NUMBER, N = number of lines, K mod n
def CACHE(CACHE_SIZE_20,line_size_20): #empty cache
    num_lines_20 = CACHE_SIZE_20//line_size_20
    print(num_lines_20)
    i = 0
    cache = {}
    while i<num_lines_20:
        cache[i] = 0
        i+=1
    return cache
empty_cache_20 = CACHE(CACHE_SIZE_20,line_size_20)
# print("-------------EMPTY CACHE---------")
# print(CACHE_SIZE_20, line_size_20)
# print("len(empty_cache_20: " + str(len(empty_cache_20)))
# print(empty_cache_20)
# print("---------------------------------")
def DIRECT_CACHE(MEM_ORG_20,empty_cache_20,k,line_size_20): #k represents which block will be accessed
    m = k%line_size_20
    #B0, B4,B8,B12.....----L0 #B0, B1 MEANS BLOCK0 BLOCK 1 ETC
    #B1, B5,B9,B13...-----L1
    #B2,B6,B10......-----L2
    empty_cache_20[m] = MEM_ORG_20[k]
    return empty_cache_20
CC = DIRECT_CACHE(MEM_ORG_20,empty_cache_20,9,line_size_20)
print("# direct cache -----")
# print("MEM_ORG_20")
# print(MEM_ORG_20)
# print("empty_cache_20")
# print(empty_cache_20)
# print(line_size_20)
# print(CC)


def PHYSICAL_ADDRESS(MEM_len,block_size,cache_size,associative):
    MEM_size_bit = int(math.log(MEM_len,2))
    print(MEM_size_bit)
    NUM_BLOCKS = MEM_len//block_size
    address_len = int(math.log(MEM_len,2))
    block_offset = int(math.log(block_size,2))
    block_no_ = int(math.log(NUM_BLOCKS,2))
    #cache_size = 16
    NUM_LINES = cache_size//block_size
    if associative == 1:
        line_offset = int(math.log(NUM_LINES,2)) #line offst if associativity = 1
    else:
        line_offset_1 = int(math.log(NUM_LINES,2))
        associativity = int(math.log(associative,2))
        line_offset = line_offset_1 - associativity # set offset if associativity!= 1
    TAG = address_len - line_offset - block_offset
    return MEM_size_bit,TAG,line_offset,block_offset
    #MEM_size_bit -------> length of address
    #TAG = TAG , line_offset = line offset , block_offset = block offset


p = PHYSICAL_ADDRESS(Memory_size_20,block_size_20,CACHE_SIZE_20,1)
print(p)

def SET_ASSOCIATIVE_CACHE(block_size,cache_size,set_associativity,c): #empty cache split in n-ways
    Num_lines = cache_size//block_size
    Num_sets = Num_lines//set_associativity
    s = {}
    i = 0
    j = 0
    while i<Num_sets:
        d = {}
        k = 0
        count = 0
        while j<len(empty_cache_20):
            if count == set_associativity:
                break
            d[j] = empty_cache_20[j]
            count+=1
            j+=1
        s[i] = d
        i+=1
    return s
s = SET_ASSOCIATIVE_CACHE(block_size_20,CACHE_SIZE_20,set_associativity,empty_cache_20)
#print(s)

def FLAG(s):
    index = 0
    flag = {}
    while index < len(s):
        flag[index] = min(s[index].keys())
        index += 1
    return flag


flag = FLAG(s)

def check_hit_(s,cache_line_num,flag,a,index):
    x = max(s[cache_line_num].keys())
    i = min(s[cache_line_num].keys())
    hit = 0
    while i<x+1:
        if s[cache_line_num][i] != 0:
            if a[index] in s[cache_line_num][i]:
                hit+=1
                break
        i+=1
    return hit

num_of_cache_line = CACHE_SIZE_20//block_size_20

def LRU (a,s,MEM,flag,set_, num_of_cache_line): #a = a_20, s = set_associative_empty_cache, MEM = MEM_ORG_20 #set_ = set_associativity
    index = 0
    hit = 0
    hitcount = 0
    miss = 0
    while index<len(a):
        block_num = index//block_size_20 #index//block_size
        cache_line_num = block_num % num_of_cache_line #block_num% number of cache line
        if set_ > 1:
            cache_line_num = cache_line_num//set_
            hit = check_hit_(s,cache_line_num,flag,a,index)
        else:
            if s[cache_line_num] != 0:
                if a[index] in s[cache_line_num]:
                    hit+=1
        if hit != 0:
            hitcount += block_size_20
            index += block_size_20
        if hit == 0:
            miss += 1
            k = flag[cache_line_num]
            s[cache_line_num][k] = MEM[block_num]
            f = k + 1
            if f > max(s[cache_line_num].keys()):
                f = min(s[cache_line_num].keys())
                flag[cache_line_num] = f
            else:
                flag[cache_line_num] = f
            index += 1
            # print(flag)
            # print (s)
        hit = 0
    return hitcount, miss

hit,miss = LRU(a_20,s,MEM_ORG_20,flag,set_associativity,num_of_cache_line)
hit1,miss1 = LRU(a_20[::-1],s,MEM_ORG_20,flag,set_associativity,num_of_cache_line)
#miss = Memory_size_20 - hit
print('')
print('SJSU-id:016018925')
print('')
print("Block size: ", block_size_20)
print("cache size: ", CACHE_SIZE_20)
print("set associativity: ", set_associativity)

print ("HIT: ", hit+hit1, "MISS: ", miss+miss1)
print("Hit Ratio: " , (hit+miss1)/(hit+hit1+miss+miss1))
print("Miss Ratio: " , (miss+miss1)/(hit+hit1+miss+miss1))