# x=int(input("teref daxil ed"))
# if x==4:
#     print("4bucaqlidir")
#     teref1=int(input("teref1"))
#     teref2=int(input("teref2"))
#     teref3=int(input("teref3"))
#     teref4=int(input("teref4"))
#     if teref1==teref2==teref3==teref4:
#         print("kvadratdir")
#     elif teref1==teref2 or teref3==teref4 or teref1==teref3 or teref2==teref4:
#         print("beraberyanlidir")
#     else:
#         print("sade dortbucaqlidir")
# elif x==3:
#     print("3bucaqlidir")
#     a=int(input("teref1"))
#     b=int(input("teref2"))
#     c=int(input("teref3"))
#     if a==b==c:
#         print("berabertereflidir")
#     elif a==b or b==c or a==c:
#         print("beraberyanlidir")
#     else:
#         print("sade ucbucaqlidir")
# else:
#     print("duzgun teref daxil ed")



# _____NEW_TASK_____
# 1). Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# [4,1,78,99,45] >> [1,4,45,78,99]
list = [4, 1, 78, 99, 45]
new_listed = sorted(list)
print(new_listed)



# 2). Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir". 
#  Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü. 
soz = input("Sozu yazin: ")
sozler = soz.split()
duzeltilmis_sozler = []

for list in sozler:
    siralanmis_list = ''.join(sorted(list))
    duzeltilmis_sozler.append(siralanmis_list)

duzeltilmis_cumle = ' '.join(duzeltilmis_sozler)
print(duzeltilmis_cumle)



# 3.)Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
# tapdığını print etsin. while istifade edin . Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
# ilk input== 4   
# ikinci input == 7
# ucuncu input == 2
# dorduncu input == 13

# tebrikler . 4 cehdde 13 reqemeni tapdiz
n = 13
sayi = 0

while True:
    input = int(input("Eded daxil edin: "))
    sayi += 1
    
    if input == n:
        print(f"Təbriklər! {sayi} cəhdə 13 nömrəsini tapdınız.")
        break

# 4). 1 ile 100 arasinda sade ededleri print edin. (for loops)
for sade in range(2, 101):
    reqem = True
    for i in range(2, sade):
        if (sade % i) == 0:
            reqem = False
            break
    if reqem:
        print(sade)













