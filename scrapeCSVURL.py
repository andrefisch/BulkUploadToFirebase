def pull_CSV_URL(filename):
    fin = open(filename, encoding="utf8")
    fout = open('urls.txt', "w+")
    lines = fin.readlines()
    for num, line in enumerate(lines, 1):
        if ('a href' in line and 'csv' in line):
            start = line.find('a href')
            end = line[start + 8:].find('"')
            print(line)
            fout.write("'" + line[start + 8:end + start + 8].replace("amp;", "") + "'")
            break
    fin.close()
    fout.close()

pull_CSV_URL("members.txt")
