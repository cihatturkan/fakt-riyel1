sayigir=int(input("faktöriyel işlemi için sayı giriniz: "))

# 1*2*3*4*5*6 faktöriyel
faktöriyel=1

if sayigir<0:
    print("negatif sayının faktöriyeli olmaz")
    
elif sayigir==0:
    print("sonuç: ( 0 ) ")

else:
    for i in range(1,sayigir+1):
        faktöriyel=faktöriyel* i
    print("sonuç:",faktöriyel)
    
