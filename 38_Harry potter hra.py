print ('''
 _                                       _   _            
| |                                     | | | |           
| |__   __ _ _ __ _ __ _   _ _ __   ___ | |_| |_ ___ _ __ 
| '_ \ / _` | '__| '__| | | | '_ \ / _ \| __| __/ _ \ '__|
| | | | (_| | |  | |  | |_| | |_) | (_) | |_| ||  __/ |   
|_| |_|\__,_|_|  |_|   \__, | .__/ \___/ \__|\__\___|_|   
                        __/ | |                           
                       |___/|_|                           
''')

print("Vitejte")
print("Nyni se vypravte do svych koleji")
follow = input("Nasledovat spoluzaky ano nebo ne?? : ").lower()
if follow == "ano":
    stay = input("jdete po schodech... Napiste zustat nebo loznice. ").lower()
    if stay == "loznice":
        print("Krasnou noc")
    else:
        ("Zustavate a sladkosti")
else:
    print("Konec")
    