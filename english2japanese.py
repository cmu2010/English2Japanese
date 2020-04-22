def conversion(dcharSet,iword): 
    s2="" 
    for i in iword:
        #print("hello " + i)
        ipos = dcharSet.find(i)
        #print(ipos)
        #print(char for char in iword)
        #print(s2)
        s2 += jalphabets[ipos]
        print(s2)
if "" == "":
    jalphabets = ' ' , '.' , 'ka' ,'tu' ,'mi' , 'te' , 'ku' , 'lu' , 'ji' , 'ri' , 'ki' , 'zu' , 'me' , 'ta' , 'rin' , 'to' , 'mo' , 'no' , 'ke' , 'shi' , 'ari' , 'chi' , 'do' , 'ru' , 'mei' , 'na' , 'fu' , 'zi'
    dcharSet = " .abcdefghijklmnopqrstuvwxyz"
    iword = input("Enter your name to have it in Japanese! :")

   # print('japanese of c is '+ jalphabets[x])
   # print('japanese of'+ jalphabets[x + 1], ' is '+ jalphabets[x + 1])

    #print(split(iword))
    print(conversion(dcharSet,iword))
    #print(jalphabets[3])
    
