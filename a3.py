def find_lcm_loop(a,b):
    maximum=max(a,b)
    while True:
        if maximum % a==0 and maximum % b==0:
            return maximum
        maximum +=1

print(f"The LCM is: {find_lcm_loop(15,20)}")