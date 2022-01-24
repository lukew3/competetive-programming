def printout(el, cl):
    elout = "Errors: "
    for i in range(len(el)-1):
        elout += el[i] + ', '
    elout += "and "
    elout += el[-1]
    print(elout)
    clout = "Correct: "
    for i in range(len(cl)-1):
        clout += cl[i] + ', '
    clout += "and "
    clout += cl[-1]
    print(clout)

def main():
    c, n = map(int, input().split())
    lines = input().split()
    el = []
    cl = []
    start_err = 0
    in_err = False
    if lines[0] != '1':
        if lines[0] == '2':
            cl.append('1')
        else:
            cl.append(f'1-{lines[0]-1}')
    start_err = int(lines[0])

    for i in range(1, len(lines)):
        if int(lines[i]) == int(lines[i-1])+1:
            in_err = True
        else:
            if int(lines[i-1]) == int(lines[i])-2:
                cl.append(str(int(lines[i])-1))
            elif int(lines[i-1])+1 < int(lines[i])-1:
                cl.append(f"{int(lines[i-1])+1}-{int(lines[i])-1}")

            if in_err:
                el.append(f"{start_err}-{int(lines[i-1])}")
            else:
                el.append(str(start_err))

            start_err = int(lines[i])
            in_err = False

    if in_err:
        el.append(f"{start_err}-{int(lines[-1])}")
    if int(lines[-1]) != c:
        if int(lines[i-1])+1 == c:
            cl.append(int(lines[i])-1)
        elif int(lines[i-1])+1 < c:
            # why +2
            cl.append(f"{int(lines[i-1])+2}-{c}")
    else:
        el.append(lines[-1])

    printout(el, cl)

main()
