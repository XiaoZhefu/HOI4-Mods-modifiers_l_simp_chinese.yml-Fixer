import re
from shutil import copyfile


def cn_extract_pound_identifiers(cntext):
    pattern = r'£\w+\s'
    identifiers = re.findall(pattern, cntext)
    return identifiers


def en_extract_pound_identifiers(entext):
    pattern = r'£\w+\s'
    identifiers = re.findall(pattern, entext)
    return identifiers


copyfile('modifiers_l_simp_chinese.yml', 'modifiers_l_simp_chinese_new.yml')

with open('modifiers_l_simp_chinese.yml', 'r', encoding='UTF-8-SIG') as file:
    listCN = []
    for i in file:
        try:
            k, v = i.split(': ')
        except ValueError:
            listCN.append(i)
        else:
            listCN.append({k: v})

with open('modifiers_l_english.yml', 'r', encoding='UTF-8-SIG') as file:
    listEN = []
    for i in file:
        try:
            k, v = i.split(':')
        except ValueError:
            listEN.append(i)
        else:
            listEN.append({k: v})

for i in listCN:
    if type(i) == dict:
        for ik in i.keys():
            for j in listEN:
                if type(j) == dict:
                    for jk in j.keys():
                        if ik == jk:
                            iv = i[ik]
                            jv = j[jk]
                            ic = iv.count('£')
                            jc = jv.count('£')
                            if ic == 0 and jc == 1:
                                need_to_delete = cn_extract_pound_identifiers(iv)
                                need_to_add = en_extract_pound_identifiers(jv)
                                iv = iv.replace('\"', '')
                                iv = iv.replace(str(need_to_delete), '')
                                ccb = []
                                iv = '\"'+str(need_to_add[0])+' '+str(iv)+'\"'
                                i.update({ik: iv})

listCN_new = []
for i in listCN:
    if type(i) == dict:
        ik = list(i.keys())
        iv = list(i.values())
        i = str(ik[0])+': '+str(iv[0])
        i = i.replace('\n', '')
    listCN_new.append(i)

with open('modifiers_l_simp_chinese_new.yml', 'w', encoding='UTF-8-SIG') as file:
    for i in listCN_new:
        file.write(f"{i}\n")
