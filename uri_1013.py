valores = raw_input()

a, b, c = valores.split(' ')

a = int(a)
b = int(b)
c = int(c)

maiorAB = ((a + b + abs(a - b)) / 2)
saida = (maiorAB + c + abs(maiorAB - c)) / 2

print("%d eh o maior" % saida)