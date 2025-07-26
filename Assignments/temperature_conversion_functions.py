def celcius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def celcius_to_kelvin(celsius):
    return celsius + 273.15


# Sample outputs as shown in the image
c = 0
f = celcius_to_fahrenheit(c)
print(f"{c}°C = {f:>6.1f}°F")

f = 32
k = fahrenheit_to_celcius(f)
print(f"{f}°F = {k:>7.2f}K")

k = 300
c = kelvin_to_celcius(k)
print(f"{k}K = {c:>7.2f}°C")