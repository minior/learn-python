# messing around with global / nonlocal / local scopes, something I previously struggled with
eggs = 43
def spam():
    global eggs
    eggs = 99
    print(eggs)

eggs = 42
spam()  # ➜ 0
print(eggs)
