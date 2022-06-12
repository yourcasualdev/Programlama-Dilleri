xbaslayan = []
xbaslamayan = []

girdi = input("")
while(girdi != ""):
    if(girdi[0] == "x"):
        xbaslayan.append(girdi)
    else:
        xbaslamayan.append(girdi)
    girdi = input("")
xbaslayan.sort()
xbaslamayan.sort()
for eleman in xbaslayan+xbaslamayan:
    print(eleman)
