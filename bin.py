#ikilik sistemi onluk sisteme çevirme
x = input("2' lik Sistemde Sayı :")
 
try:
    y = int(x,2)  
    print("Girilen Sayı 10' luk Sistemde :", y)    
    
except ValueError:
    print("Geçersiz Giriş")