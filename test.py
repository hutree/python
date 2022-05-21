current_users = ["anny", "marry", "Sure", "dew", "lola", "lily"]
new_users = ["sure", "dew", "jon", "juli"]
for new_user in new_users:
    have = "False"
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            have = "True"
            break
        else:
            have = "False"

    if have == "False":
        print("you can use：" + new_user)
    else:
        print("choose another：" + new_user)
