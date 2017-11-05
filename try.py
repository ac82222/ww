import json
import re

lecdata =[

    {"type" : 1 , "regex" : "\(\w+\)" , "kpiname" : "ERROR_COUNT"},
    {"type": 2, "regex": "\w+\W(\d\d)", "kpiname": "TOOL_VER"}
]

lectest ="For someone who has (lived) through the .com bubble the madness " \
         "currently unfolding in the crypto space is just plain breathtaking. " \
         "It is quite awe inspiring to see people make the exact same mistakes " \
         "they made 17 years ago. Of course, today’s investors are likely different " \
         "people who, for the most part, have not lived through the .com bubble."

class REMatcher(object):

    def __init__(self , regexp , matchstring):
        self.regexp = regexp
        self.matchstring = matchstring
    def Search(self):
        self.pattern = re.search(self.regexp , self.matchstring)
        if self.pattern != None:
            return self.pattern.group(0)
        else:
            None
    def Group(self,i):
        self.pattern = re.search(self.regexp , self.matchstring)
        return self.pattern.group(i)

with open('data.text' , 'w') as file:
    a = json.dumps(lecdata) #string
    file.write(a)
    file.close()

with open('data.text','r') as readfile:
    line=readfile.read()
    b=json.loads(line)
    # for i in range(len(b)):
    #     TypeName = b[i]['type']
    #     RegexName =b[i]['regex']
    #     KpiName = b[i]['kpiname']

with open('lec.text','w') as f:
    f.write(lectest)
    f.close()
    with open('lec.text','r') as F:
        for eachline in F:
            for i in range(len(b)):
                TypeName = b[i]['type']
                RegexName = b[i]['regex']
                KpiName = b[i]['kpiname']
                if TypeName == 1:
                    Regex=REMatcher(RegexName, eachline).Search()
                    if Regex != None:
                        Name=KpiName+':'+Regex+'1'
                        print(Name)
                    else:
                        None
                elif TypeName == 2:
                    Regex=REMatcher(RegexName, eachline).Group(1)
                    if Regex != None:
                        print(Regex)
                    else:
                        print('None')











#
#
# for i in range(len(lecdata)):
#     typename=lecdata[i]['type']
#     regexname=lecdata[i]['regex']
#     targetname=lecdata[i]['kpiname']
#     print(typename)
#     print(regexname)
#     print(targetname)


#
# with open('lecdata.text' , 'r') as readfile:
#     b=readfile.read()
#     list1 = b.split()
#     print(type(list1))
#     for i in list1:
#         print(i[0])