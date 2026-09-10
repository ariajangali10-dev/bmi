import math
def bmi(weight, height):
    bmi = weight / (height**2)
    return bmi
w = float(input('enter your weight(kg): '))
h = float(input('enter your height(m): '))
bmi_result = math.trunc(bmi(w, h))
print(f'your bmi is:{bmi_result}')
if bmi_result < 18.5:
    print('you are skinny')
elif bmi_result >= 18.5 or bmi_result < 25:
    print('you are normal')
else:
    print('you are fat')

