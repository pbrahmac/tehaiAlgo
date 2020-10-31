def damdaar_tehai(beats, name="this taal"):
    leg = (beats + 1)
    counter = 0
    def recurse(leg, counter):
        if leg % 3 == 0:
            leg, gap = leg // 3, counter / 2
            return f"{leg} + {gap} + {leg} + {gap} + {leg}"
        else:
            return recurse(leg - 1, counter + 1)
            
    tehai = recurse(leg, counter)
    print(f"Tehai for {name}: {tehai}")
    return


def main():
    while True:
        beats = input("Enter the # of beats: ")
        
        if beats == "q":
            break

        damdaar_tehai(beats=int(beats))

        print("\n")
    
    damdaar_tehai(12, "Ektaal")
    
if __name__ == "__main__":
    main()