input_grammar = []
eliminated_grammar = []
# Taking User Input
n = int(input("Enter number of lines of rules in your grammar\n"))
for i in range(n):
    rule = input("Enter rule : " + str(i) + "\n")
    input_grammar.append(rule)
# Scanning each rule one by one
for rule in input_grammar:
    # Separating right and left parts of the rule
    rule_splitted_by_arrow = rule.split('->')
    # Separating the numerous right parts of the rule
    rule_splitted_by_slash = rule_splitted_by_arrow[-1].split('/')
    rule_parts_with_left_recursion = []
    rule_parts_without_left_recursion = []
    k, l = 0, 0
    not_left_recursive_rule = 0
    
for c in rule_splitted_by_slash:
    # Checking if the grammar is ambiguous or not
    if rule_splitted_by_arrow[0] == c[0]:
        print("Left recursion in rule : ", rule + "\n\n")
        rule_parts_with_left_recursion.append(k)
    else:
        rule_parts_without_left_recursion.append(l)
    k += 1
    l += 1
    if len(rule_parts_with_left_recursion) == 0:
        eliminated_grammar.append(rule)
        continue

    oldRule = rule_splitted_by_arrow[0] + '->'
    for i in rule_parts_without_left_recursion:
        oldRule += rule_splitted_by_slash[i] + rule_splitted_by_arrow[0] + '\'/' 
    eliminated_grammar.append(oldRule)
    newRule = rule_splitted_by_arrow[0] + '\'->'
    for i in rule_parts_with_left_recursion:
        newRule += rule_splitted_by_slash[i].lstrip(rule_splitted_by_arrow[0]) + rule_splitted_by_arrow[0] + '\'/'
        newRule += 'null'
        eliminated_grammar.append(newRule)
    print("\n\n\nGrammar after removal of left recursion is :\n\n")
    for rule in eliminated_grammar:
        print(rule, end='\n')  