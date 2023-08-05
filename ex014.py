temperatura = float(input('Informe a temperatura em °C: '))

fahrenheit = temperatura * 9 / 5 + 32
kelvin = temperatura + 273.15

print('Temperatura em Celsius é: {:.1f}°C \nTemperatura em Fahrenheit é: {:.1f}°F \nTemperatura em Kelvin é: {:.2f}K'.format(temperatura, fahrenheit, kelvin))
