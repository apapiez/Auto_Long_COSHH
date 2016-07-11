import argparse
import subprocess
import os
import re

print("Please enter the path of the txt file")
path = input("-->")
path = r''+path+''


def get_data():
    with open(path, 'r') as infile:
        text = infile.read()
        return text
def getFields(text):
    def getHStatments():
        regex = r'(H\d{3})+'
        p = re.compile(regex)
        H_stmts = p.findall(text)
        H_stmts = list(set(H_stmts))
        return H_stmts
    def getPStatements():
        regex = r'(P\d{3})+'
        p = re.compile(regex)
        P_stmts = p.findall(text)
        P_stmts = list(set(P_stmts))
        return P_stmts
    def getName():
        regex = r'(Product name)[\n: ]+([A-Za-z0-9-\(\) ]+)'
        p = re.compile(regex)
        Name = p.findall(text)
        return Name[0][1]
    def getSignalWord():
        regex = r'(Danger\b|Warning\b)'
        p = re.compile(regex)
        SignalWord = p.findall(text)
        return SignalWord[0]
    def getCASNumber():
        regex = r'(\b[1-9]{1}[0-9]{1,5}-\d{2}-\d\b)'
        p = re.compile(regex)
        CASNumber = p.findall(text)
        CASNumber = list(set(CASNumber))
        return CASNumber[0]
    HStatements = getHStatments()
    PStatements = getPStatements()
    SignalWord = getSignalWord()
    Name = getName()
    CASNumber = getCASNumber()
    return HStatements, PStatements, SignalWord, Name, CASNumber
def writeout():
    with open("test.tex", "w") as outfile:
        outfile.write(toptext)
        compstring1 = r'''F:/PortableApps/miktex/miktex/bin/pdflatex.exe -synctex=1 -interaction=nonstopmode ''' + "test.tex"
        os.system(compstring1)
                                
text = get_data()
HStatements, PStatements, SignalWord, Name, CASNumber = getFields(text)
project_title = input("Enter Project title -> ")
supervisor = input("Enter Supervisor Name -> ")
dtablestring = r"\detailtable{"+Name+"}{"+CASNumber,"}{",project_title,"}{"+supervisor+"}{School of Life Sciences}{EBA606}"
exptdescription = input("Please enter a brief description of your experiment")
seconestring = r"\Sectionone{"+exptdescription+"}"
sectwostring = r"\Sectiontwo{"+Name+"}{"+(', '.join(map(str, HStatements)))+"}{"+(', '.join(map(str, PStatements)))+"}{}"
secthreestring = r"\Sectionthree{some illnesses here...}"
secfourstring = r"\Sectionfour{}{}{}{}{}{}{}{}{"+supervisor+"}"
secfivestring = r"\Sectionfive{}{}{}{}{}{}{}{}{}"
secsixstring = r"\Sectionsix{Alexander Papiez}{"+supervisor+"}"

toptext = r'''\documentclass[8pt,a4paper,portrait]{article}

\usepackage[width=19.00cm, height=28.00cm]{geometry}
\usepackage{my_commands}
\pagenumbering{gobble}

\begin{document}

\COSHHEADER{}''' + r'''
'''+seconestring+r'''
'''+sectwostring+r'''
'''+secthreestring+r'''
'''+secfourstring+r'''
'''+secfivestring+r'''
'''+secsixstring+r'''
\end{document}'''

writeout()

    
