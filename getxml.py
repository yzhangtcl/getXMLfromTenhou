import os
import sys
import requests as req
inputfile=sys.argv[1]
fd=open(inputfile, "r")
text=fd.read()
# print(text)
for line in text.split('\n') :
    f=0
    for sent in line.split(' ') :
        # print(sent) 
        # print(f)
        if f==1 or f==2 :
            f=f+1
        elif f==3 :
            link='http://tenhou.net/0/log/?'
            tmp=''
            for i in range(31,62) :
                tmp += sent[i]
            link += tmp
            print(tmp)
            # lcfile = tmp + '.xml'
            # response = req.get(link)
            # if response.status_code == 200 :
            #     with open(lcfile , 'wb') as file :
            #         file.write(response.content)
            f=4
        elif f!=4:
            if len(sent)>2 and sent[0]=='四' :
                f=1
            

