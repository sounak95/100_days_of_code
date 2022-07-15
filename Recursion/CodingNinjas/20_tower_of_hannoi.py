

def toh(n,source, destination, auxillary):
    if n==1:
        print(f"move disk 1 from {source} to {destination}")
        return
    toh(n-1,source,auxillary,destination)
    print(f"mode disk {n} from {source} to {destination}")
    toh(n-1, auxillary,destination,source)



n = 4
toh(n,'A','B','C')