def strays():
    #ask how mnay tins there are
    ST = int(input("How many small tins are there?: "))
    nstins = ST / 6
    print("You need",nstins, "trays")
    return(nstins)


def btrays():
    #ask how mnay tins there are
    BT = int(input("How many big tins are there?: "))
    nbtins = BT / 4
    print("You need",nbtins, "trays")
    return(nbtins)


s_or_b = input("Are there any big or small tins? (small/big/both): ")
if s_or_b == "small":
    strays()
elif s_or_b == "big":
    btrays()
else:
    strays()
    btrays()
