
# coding: utf-8

# In[ ]:


import datetime
pc_list = []
def hardwaremenu():
    print('(A)dd a new record')
    print('(L)ist existing records')
    print('(C)hange owner')
    print('(D)elete a record')
    print('(E)xport to CSV')
    print('(Q)uit')
def pcinfo():
    pcinfo = {'computerModel':'','purchaseYear':'','bluePlate':'','owner0':'','creat':'','update':''}
    pcinfo['computerModel'] = input('please enter ur computer model:')
    pcinfo['purchaseYear'] = input('please enter years purchased:')
    pcinfo['bluePlate'] = input('please enter blue plate number')
    pcinfo['owner0'] = input('please enter owner')
    pcinfo['creat'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pcinfo['update'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pc_list.append(pcinfo)
def listinfo():
    print(pc_list)
def changeinfo():
    i = int(input('Enter record ID:'))-1
    if i<=len(pc_list):
        new_owner = input('Enter a new owner:')
        pc_list[i]['owner0']=new_owner
        pc_list[i]['update']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(' has been updated.')
    else:
        print('There are no records')
def deleteinfo():
    delete = int(input('Enter record ID:'))-1
    if delete<=len(pc_list):
        print(pc_list[delete])
        keep = input('Do you wish to delete this record (Y/N):')
        if keep=='Y':
            pc_list.remove(pc_list[delete])
def save():
    with open('hardware.csv','a') as file:
        for d in pc_list:
            file.write('"' + d['computerModel'] + '","' +  d['purchaseYear'] + '","'+ d['bluePlate']+'","'+ d['owner0']+'"\n')
        file.close()    
def quit():
    print('Thank you')
    
while True:
    hardwaremenu()
    choice = input('your choice:')
    if choice == 'A':
        pcinfo()
    elif choice == 'L':
        listinfo()
    elif choice == 'C':
        changeinfo()
    elif choice == 'D':
        deleteinfo()
    elif choice == 'E':
        save()
    elif choice == 'Q':
        quit()
        break
    else:
        print('error')
    

