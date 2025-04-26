import math, os

mode = "gcd"

try:
    while True:
        # Example numbers
        ao = input("A/OP> ")
        

        try:
            a = int(ao)
        except:
            if ao == "exit" or ao == "quit":
                print("Bye.")
                break
            if ao.lower() == "gcd":
                mode = "gcd"
                print("Ok.")
                continue
            elif ao.lower() == "lcm":
                mode = "lcm"
                print("Ok.")
                continue
            elif ao.lower() == "all":
                mode = "all"
                print("Ok.")
                continue
            print("Invalid input.")
            continue

        b = int(input("B> "))

        gcd = math.gcd(a, b)
        if mode == "gcd" or mode == "all":
            print(f"{mode == "gcd" if "" else "GCD "}{gcd}")
        if mode == "lcm" or mode == "all":
            lcm = (a * b) // gcd
            print(f"{mode == "lcm" if "" else "LCM "}{lcm}")

except KeyboardInterrupt:
    print("Bye.")
    os._exit(0)
