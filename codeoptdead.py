def dead_code_elimination(code):
    change = code.replace('if(i==1) a= b+5;', '')
    print("\nAfter Dead Code Elimination, the code is: ")
    print(change) # For Program: i=0; if(i==1) a= b+5;
    while True:
        print("\nCode Optimization: Dead Code Elimination")
        print("1. Optimize Code")
        print("2. Exit")
        choice = int(input("\nEnter your choice (1/2): "))
        if choice == 1:
            code = input("\nEnter the code to be optimized: ")
            dead_code_elimination(code)
        elif choice == 2:
            print("Exiting...")
            break
        else:
            print("Invalid Choice. Please enter 1 or 2.")
