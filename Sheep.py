#If you can't sleep, just count sheep!!

def count_sheep(n):
    sheep = ""
    for i in range(n):
        sheep += f"{i+1} sheep..."
    return sheep