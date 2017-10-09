BUFF_MAG = 7
HIST_MAG = 9

BUFF = 2**BUFF_MAG
HIST = 2**HIST_MAG
UNIT = 1

orders = []
mid = 0
encode = ""
binary = ""
binfin = ""
final = ""

def char(ltr, num):
    return bind(ord(ltr),num)

def bind(num,limit):
    return (limit-len(bin(num)[2:]))*'0'+bin(num)[2:]

def tochr(text):
    num = text
    order = 0
    for i in range(len(num)):
        order += int(num[0])
        order *= 2
        num = num[1:]
    order /= 2
    return chr(order)

text = open("alice29.txt")
for line in text:
    for letter in line:
        encode += letter

for i in range(len(encode)):
    binary+=char(encode[i],8)

while(len(binary)>mid):
    read = binary[mid:mid + BUFF * UNIT]
    refr = binary[max(0, mid - HIST * UNIT - 1):mid]
    done = False
    for i in range(min(BUFF * UNIT, mid), 1, -1):
        check = read[0:i]
        for j in range(HIST * UNIT - i):
            if check == refr[j:j + i]:
                orders += [[j,i,check[-1]]]
                mid += i
                done = True
                break
        if done:
            break
    if done:
        continue
    orders += [[0,0,read[0]]]
    mid += 1

for i in orders:
    binfin += bind(i[0],HIST_MAG)+bind(i[1],BUFF_MAG)+bind(ord(i[2]),8)

for i in range(len(binfin),len(binfin)%8+8,-8):
    final = tochr(binfin[i-8:i])+final
final = tochr(binfin[0:len(binfin)%8]) + final

print str(len(encode)) + "B from " + str(len(final)) + "B: " + str(float(len(final))/len(encode)) +"%"
