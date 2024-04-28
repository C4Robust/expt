import re

f = open("macro.txt")
sent_tokens = f.readlines()

for i, line in enumerate(sent_tokens):
    tokens = line.split(' ')
    print(f"LINE {i+1}:{tokens}")
    




def pass1():
    macro_name_table = []
    mnt_index = 0
    flag = 0

    for sent in sent_tokens:
        sent = sent.strip()
        sent = sent.replace(", ", ",")
        
       

        if ';' in sent:
            sent = re.sub(';.*', '', sent)
        
        word_tokens = re.findall("[\S]+", sent)
        
        
        if "MACRO" in sent:
            flag = 1
            
        
        if flag == 1:
            macro_name = word_tokens[1]
            mnt_index += 1
            mnt_entry = {'Index': mnt_index, 'Macro Name': macro_name}
            macro_name_table.append(mnt_entry)
            flag = 0
        
        if "MEND" in sent:
            flag = 0
    
    print("\n\nMacro Name Table :- \n")
    print('{:10}'.format("Index"), '{:20}'.format("Macro Name"))
    for x in macro_name_table:
        print('{:10}'.format(str(x["Index"])), '{:20}'.format(x["Macro Name"]))

pass1()