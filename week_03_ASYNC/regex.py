import re


def find_name(line):
    pattern = r"((?:(?:Mr\.|Ms\.|Mrs\.|Mx\.|Dr\.)|(?:[A-Z])(?:(?:(?:'|-)(?:[A-Z])?)*(?:[a-z]))+)(?: (?:[A-Z])(?:(?:(?:'|-)(?:[A-Z])?)*(?:[a-z]))+){1,3})"
    #pattern = r"([A-Z])((('|-)([A-Z])?)*([a-z]))+( ([A-Z])((('|-)([A-Z])?)*([a-z]))+){1,3}"
    result = re.findall(pattern,line)

    return result


f = open("datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)