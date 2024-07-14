# (0°C × 9/5) + 32 c to f
# 0°C + 273.15  c to k
# (0°F − 32) × 5/9 f to c
# (0°F − 32) × 5/9 + 273.15  f to k
# 0K − 273.15  k to c
# (0K − 273.15) × 9/5 + 32  k to f


def celcius_conversion(celcius):
    far=((celcius * 9/5) + 32)
    kelvin=celcius + 273.15
    return far,kelvin

def far_conversion(far):
    cel=((far - 32) * 5/9)
    kelvin=((far - 32) * 5/9 + 273.15 )
    return cel,kelvin

def kelvin_conversion(kelvin):
    cel=kelvin - 273.15 
    far=((kelvin - 273.15) * 9/5 + 32 )
    return cel,far


print("------------Temperature Convertor------------")
temp=int(input("Enter The temperature:"))
unit=input("Enter the original unit (celcius,farenhiet,kelvin):")
if unit=="celcius":
    print("---------Celcius Conversion---------")
    far,kel=celcius_conversion(temp)
    print(temp,"°C")
    print(far,"°F")
    print(kel,"K")
elif unit=="farenhiet":
    print("---------farenhiet Conversion---------")
    cel,kel=far_conversion(temp)
    print(cel,"°C")
    print(temp,"°F")
    print(kel,"K")
else:
    print("---------Kelvin Conversion---------")
    cel,far=kelvin_conversion(temp)
    print(cel,"°C")
    print(far,"°F")
    print(temp,"K")


