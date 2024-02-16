currrent_users = ['kofi', 'Ama', 'Kwame', 'Kwabena', 'Esi', 'Joe']
new_users = ['kofi', 'George', 'Esi', 'Ekua']


for new_user in new_users:
    if new_user in currrent_users:
        print(f"{new_user} already exists")
    else :
        print(f"{new_user} is available")