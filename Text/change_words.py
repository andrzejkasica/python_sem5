infile = "C:\\Users\\Admin\\source\\repos\\hello_world\\hello_world\\Text\\t.txt"
outfile = "C:\\Users\\Admin\\source\\repos\\hello_world\\hello_world\\Text\\t_new_change.txt"

change_list = {" i": " oraz", " oraz": " i", " nigdy": " prawie nigdy", " dlaczego": " czemu"}
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in change_list:
       line = line.replace(word,change_list[word])
    fout.write(line)
fin.close()
fout.close()
