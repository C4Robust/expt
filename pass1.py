# Function to generate symbol table in Pass-I
def generate_symbol_table(source_code):
    symbol_table = {} # Dictionary to store symbols and their addresses
    for line in source_code:
        if line.strip(): # Ignore empty lines
            parts = line.split() # Split line into parts based on whitespace
        # Check if the line contains a label (symbol)
            if len(parts) >= 2 and parts[0][-1] == ':':
                label = parts[0][:-1] # Extract label without the ':'
                address = parts[1] # Address or location follows the label
                # Add label and its address to the symbol table
                symbol_table[label] = address
        return symbol_table
# Sample source code for demonstration
source_code = [
"START: 100",
"LOOP: 200",
" LDA X",
" STA Y",
" JUMP LOOP",
" HLT",
"X: DATA 5",
"Y: RES 1",
]
# Generate symbol table for the sample source code
symbol_table = generate_symbol_table(source_code)
# Display the symbol table
print("{:<10} {:<10}".format("Label", "Address"))
for label, address in symbol_table.items():
    print("{:<10} {:<10}".format(label, address))