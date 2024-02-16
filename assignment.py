currrent_users = ['kofi', 'Ama', 'Kwame', 'Kwabena', 'Esi', 'Joe']
new_users = ['kofi', 'George', 'esi', 'Ekua']

current_users_lower = [user.lower() for user in currrent_users]


for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} already exists")
    else :
        print(f"{new_user} is available")