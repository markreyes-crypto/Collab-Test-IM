from Grover101 import run as grover
from Loevah_Paderog import run as loevah
from hey import run as hey
from jeanvhee_patch_1 import run as jeanvhee

def main():
    print("==============================")
    print("     COLLABORATIVE SYSTEM")
    print("==============================")

    grover()
    loevah()
    hey()
    jeanvhee()

    print("==============================")
    print("All branches connected!")
    print("==============================")

if __name__ == "__main__":
    main()