# input: get 2 ints (length and width in m)
# output: 2 ints (area in sq m and sq ft)

units = input('f for feet and m for meters: ').lower()
if units == 'f':
    units = 'feet'
    conversion_units = 'meters'
else:
    units = 'meters'
    conversion_units = 'feet'

length = float(input('Length of room: '))
width = float(input('Width of room: '))

area = length * width

if units == 'feet':
    converted_area = area / 10.7639
else:
    converted_area = area * 10.7639

print(f'Area of room in square {units}: {area:.2f}')
print(f'Area of room in square {conversion_units}: {converted_area:.2f}')