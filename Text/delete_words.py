infile = "C:\\Users\\Admin\\source\\repos\\hello_world\\hello_world\\Text\\t.txt"
outfile = "C:\\Users\\Admin\\source\\repos\\hello_world\\hello_world\\Text\\t_new.txt"

delete_list = ["się", " i ", "dlaczego", "oraz", "nigdy", " i"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
       line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()