import sys

if len(sys.argv) == 3:
    rows= int(sys.argv[1])
    colums= int(sys.argv[2])

    print (f"Values of arguments are rows {rows} and columns {colums} ")

    for r in range(rows):
        print("")
        for c in range(colums):
            print("*",end="")
        
else:
    print("No input values detected")