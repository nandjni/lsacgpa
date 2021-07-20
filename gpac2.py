# code to convert UBC percentage GPA to LSAC GPA (out of 4.33)

lof = []
lol = []
count = 0

while True:
    x = (input('enter percentage '))
    if x == 'done':
        break
    try:
        floatify = float(x)
        lof.append(floatify)
    except:
        print('say done when done')
        continue

#print("UBC percentages summary:", *lof)

for f in lof:
    count = count + 1
    if f in range(90,101):
        lol.append(4.33)
    elif f in range(85, 90):
        lol.append(4.0)
    elif f in range(80, 85):
        lol.append(3.67)
    elif f in range(76, 80):
        lol.append(3.33)
    elif f in range(72, 76):
        lol.append(3.0)
    elif f in range(68, 72):
        lol.append(2.67)
    elif f in range(64, 68):
        lol.append(2.33)
    elif f in range(60, 64):
        lol.append(2.0)
    elif f in range(55, 60):
        lol.append(1.5)
    elif f in range(50, 55):
        lol.append(1.0)
    else:
        lol.append(0.0)

#print("LSAC GPA summary:", *lol)
#print("number of courses:", count)

finallsacgpa = sum(lol) / count

print("your GPA:", finallsacgpa)
