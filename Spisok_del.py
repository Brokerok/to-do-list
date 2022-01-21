import sys
import json


with open("db.json", 'r') as data:
    db = json.load(data)

print("HELLO")
while True:
    login = input('Enter your Email:')
    if login == 'exit':
        break
    elif login not in db.keys():
        print('wrong email')
        continue
    else:
        current_user = db[login]
    i = 5
    while i > 0:
        passs = input('Enter your password:')
        if passs == current_user['pass']:
            print('Access!!!')
            break
        else :
            i -= 1
            print('Wrong pass')
            print('Attempts left: {}'.format(i))
            if i < 1:
                sys.exit()
    while True:
        print("""\n
add
delete
done
exit
        """)
        choose = input('Choose options:')
        x = current_user['todo']
        y = current_user['done']
        if choose == 'exit':
            break
        else:
            while True:
                if choose == 'add':
                    point = input('Enter your to do element:')
                    if point == 'back':
                        break
                    else:
                        x.append(point)
                        print('Your to do list: {}'.format(x))
                elif choose == 'delete':
                    choose2 = input('Index or value? ')
                    if choose2 == 'back':
                        break
                    elif choose2 == 'index':
                        index_element = int(input('Index: '))
                        if len(x) < index_element or index_element < 0:
                            print('Wrong index')
                        else:
                            delete_element = x.pop(index_element)
                            print('You deleted "{}" element'.format(delete_element))
                            print('Your to do list {}'.format(x))
                    elif choose2 == 'value':
                        element_value = input('Value: ')
                        if element_value in x:
                            x.remove(element_value)
                            print('You deleted "{}" element'.format(element_value))
                            print('Your to do list {}'.format(x))
                        else:
                            print('Value not in list!')
                    else:
                        print('Wrong!!!')
                elif choose == 'done':
                    choose2 = input('Index or value? ')
                    if choose2 == 'back':
                        break
                    elif choose2 == 'index':
                        index_element = int(input('Index: '))
                        if len(x) < index_element or index_element < 0:
                            print('Wrong index!!!')
                        else:
                            z = x[index_element]
                            done_element = y.append(z)
                            print('You have already "{}" element done'.format(done_element))
                    elif choose2 == 'value':
                        element_value = input('Value: ')
                        if element_value in x:
                            y.append(element_value)
                            print('You have already "{}" element done'.format(element_value))
                    else:
                            print('Wrong!')
                    print('Your done list {}'.format(y))
                    print('Your to do list {}'.format(x))
                else:
                    print('Wrong options!')
                    break
        with open("db.json", 'w') as write:
            json.dump(db, write)
print('Bye')
