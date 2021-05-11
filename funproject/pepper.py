#!/usr/bin/env python3


output = "Based on your SHU value, "

SHU_VALUE = int(input("What is is your SHU Value?\n") )

if SHU_VALUE >= 2200000:
    output = output + 'you are Carolina Reaper'

elif SHU_VALUE >= 2000000:
    output = output + 'you are Trinidad Scorpion Moruga'
elif SHU_VALUE >= 1800000:
    output = output + 'you are 7 Pot Douglah'
elif SHU_VALUE >= 1400000:
    output = output + ['you are 7 Pot Primo', 'you are 7 Pot Douglah']
elif SHU_VALUE >= 1300000:
    output = output + 'you are Naga Viper'
elif SHU_VALUE >= 5000:
    output = output + ' You do not belong in this group. You are Paprika'

else:
    print('What do you call a nosey pepper?')
    print('jalapeno business')
    output = output + ' you need to stop it before I am Jalapeno face. '
print(output)

