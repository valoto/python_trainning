with open ('9.txt', 'r') as f:
    for i in f.readlines():
        i = i.strip('\n')
        octetos = i.split('.')        
        if len(octetos) == 4:
            for oc in octetos:
                if int(oc) <= 0 or int(oc) >=255:
                    break
            with open ('91.txt', 'a') as fi:
                fi.write(i + '\n')
