import os, sys, json

with open(os.path.abspath(sys.argv[2])) as json_file: dictionar = json.load(json_file) # aici am incarcat json-ul in variabila "dictionar"

def create_project(d,path):
    os.chdir(path)                                      # schimbam folderul de fiecare data cand se apeleaza functia
    for key in d.keys():                                # parcurgem fiecare cheie in parte
        if isinstance(d[key],dict):                     # verificam daca valoarea cheii este un dictionar
            new_path = os.path.join(path,key)           # cream un nou path
            os.mkdir(new_path)                          # creeaza folderul
            create_project(d[key],new_path)             # parcurgem recursiv dictionarul gasit
            os.chdir(path)                              # iesim din new_path schimband cu path-ul anterior
        else:                                           # creeaza si scrie fisierul
            if (d[key][:2] == "\\x"): 
                with open(key,"wb") as f: 
                    f.write(bytes(d[key].encode()))
            else: 
                with open(key,'w') as f: f.write(d[key]) 
 
create_project(dictionar,os.path.abspath(sys.argv[1]))