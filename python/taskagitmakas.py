def main():
    firstplayer = input("")
    secondplayer = input("")

    if(firstplayer == secondplayer):
        print("berabere")
    elif(firstplayer == "taş"):
        if(secondplayer == "kağıt"):
            print("ikinci oyuncu kazandı")
        else:
            print("birinci oyuncu kazandı")
    elif(firstplayer == "kağıt"):
        if(secondplayer == "makas"):
            print("ikinci oyuncu kazandı")
        else:
            print("birinci oyuncu kazandı")
    elif(firstplayer == "makas"):
        if(secondplayer == "taş"):
            print("ikinci oyuncu kazandı")
        else:
            print("birinci oyuncu kazandı")


if __name__ == "__main__":
    main()
