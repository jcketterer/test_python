#making a inverted triangle with "*"
def inverted_tri(n):
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("*", end="")
        print("\r")

inverted_tri(5)

