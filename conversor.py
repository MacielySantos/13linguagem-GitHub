def conversor():
  vlr_cm = float(input('Digite o valor em centímetros:'))
  vlr_pole= vlr_cm/2.54

  conversao = open('conversao.txt','w+')
  conversao.write(f'O valor {vlr_cm} em centímetros corresponde a {vlr_pole} em polegadas')
