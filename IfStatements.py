is_Female = True
is_Tall = False

if is_Female and is_Tall:
    print("You are a Tall female")
elif is_Female and not(is_Tall):
    print("You are a short Female")
elif not(is_Female) and is_Tall:
    print("You are Female but not Tall")
else:
    print("You are neither Female nor Tall")
