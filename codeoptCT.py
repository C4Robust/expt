def compile_time_evaluation(code):
    change = code.replace('22/7', '3.14')
    print("\nAfter Compile Time Evaluation, the code is: ")
    print(change) # For Program: Area of circle = 22/7*R*R
while True:
    print("\nCode Optimization: Compile Time Evaluation")
    print("1. Optimize Code")
    print("2. Exit")
    choice = int(input("\nEnter your choice (1/2): "))
    if choice == 1:
        code = input("\nEnter the code to be optimized: ")
        compile_time_evaluation(code)
    elif choice == 2:
        print("Exiting...")
        break
    else:
        print("Invalid Choice. Please enter 1 or 2.")