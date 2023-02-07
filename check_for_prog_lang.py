# Usage:
#   python check_for_prog_lang.py file_with_all_trees.txt

import gitlab
import os
import json
import sys

if len(sys.argv) < 2:
    print("Path to input file expected")
    exit(1)

if not os.path.isfile('Programming_Languages_Extensions.py'):
    with open('Programming_Languages_Extensions.py', 'w') as fi:
        print('import NameChecker', file=fi)
        print('checker = NameChecker.Checker()', file=fi)
        ignore = ['Smalltalk', 'C', 'C++', 'Objective-C', 'PLpgSQL', 'SQLPL']
        with open('prog_langs/Programming_Languages_Extensions.json', "r") as f:
            PLE = json.load(f)
            PLE = [i for i in PLE if not i['name'] in ignore]
            for lang in PLE:
                if lang['type'] != "programming": continue
                if not 'extensions' in lang:
                    continue
                ext = '"'+'", "'.join(lang['extensions'])+'"'
                print(f'checker.Add("{lang["name"]}", {ext})', file=fi)

from Programming_Languages_Extensions import checker

checker.Add('Smalltalk', '.st')
checker.Add('C-C++', ".c", ".h", ".idc", ".cpp", ".c++", ".cc", ".cp", ".cxx", ".h++", ".hh", ".hpp", ".hxx", ".inc", ".inl", ".ipp", ".tcc", ".tpp")

checker.Add('Bin', '.jar', '.dll', '.exe', '.bin', '.so', '.so.1', '.so.2', '.so.3', '.so.4', '.so.5', '.so.6', '.so.7', '.so.8', '.so.9')
checker.Add('Obj', '.obj', '.o', '.a')

with open(sys.argv[1], 'r') as f:
    for line in f:
        checker.Check(line.split('\n')[0])
