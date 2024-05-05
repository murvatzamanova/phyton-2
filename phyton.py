# sortData = input("Data: ").lower()

# splitWords = sortData.split()

# for index in range(len(splitWords)):
#     newList = list(splitWords[index])
#     newList.sort()
#     splitWords[index] = "".join(newList)

# result = " ".join(splitWords)
# print(result)

# list = ["Salam", "necesen", "alma"]
# list.lower.sort()
# print(list)


# def hesabla(a, b):
#     print(a + b)
#     return a + b
    
# x = hesabla(5, 4)
# print(x + 10)

# def myFunction(num):
#     return num * 2

# lambdaFunction = lambda a,b : a + b
# print(lambdaFunction(5, 9))


# myString = ["Salam", "Mikhail", "Tal", "Fisher"]

# def checkData(data):
#     return data in myString

# # print(checkData("Tal"))
# print(list(map(checkData, ["Tal", "Salam"])))
# print(list(filter(checkData, ["Tal"])))


# Scope
# x = 20 # global
# def hesabla():
#     # Enclosing
#     x = 10
#     print(x)
#     def myFunction2():
#         x = 30
#         print(x)
#         # Local
#     myFunction2()
    
# hesabla()

# x = 20

# def hesabla():
#     global x
#     x = 5
#     return x * 10

# print(hesabla())
# print(x)

# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print(x)
# print("Python is " + x)

# LEGB > L local > E enclosing > G global > B Build in


# list comprehension function
# newList = []
# for i in range(1, 10):
#     if i % 2 == 0:
#         newList.append(i)
#         break
        
# print(newList)
# print(list(num for num in range(1, 10) if num % 2 == 0))



-----------------------------------------------------------------------------------


# ......NEW TASK.....
# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]


# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# def tap(mylist):
#     for num in mylist:
#         if num**0.5 == mylist[0]:
#             print(num)
# tap(mylist)

-----------------------------------------------------------------------------------


#  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
#  input:[-1,1,2,2,6,7,7,'say']

# input_list=(input("List daxil edin")) ??
# def tekrarlanmayan(liste):
#     return list(set([x for x in liste if liste.count(x) == 1]))

# input_list = [-1, 1, 2, 2, 6, 7, 7, 'say']
# print(tekrarlanmayan(input_list))


-----------------------------------------------------------------------------------


# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

# input = input("Hasilin tapmaq istediyiniz reqemleri yazin: ")
# def hesab(input):
#     hasil = 1
#     for eded in input:
#         if eded.isdigit():      ##isdigit() sətir metodudur və sətrin yalnız rəqəm simvollarından ibarət olub olmadığını yoxlayır. Bu üsul sətirdə dövr edir, hər simvolun rəqəm olub-olmadığını yoxlayır və True və ya False qaytarır.
#             reqem = int(eded)
#             hasil *= reqem
#     return hasil
# print(hesab(input))


-----------------------------------------------------------------------------------


# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın
# num = int(input("Bölənlərini tapmaq istədiyiniz ədədi daxil edin: "))
# bolenler = [x for x in range(1, num + 1) if num % x == 0]
# print(f"{num} ədədinin bölənləri: {bolenler}")


-----------------------------------------------------------------------------------


# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}



# mylist = ['yanvar', 'fevral', 'may', 'iyun', 'iyul', 'avqust', 'sentyabr', 'oktyabr', 'noyabr', 'dekabr']

# month_lengths = {month: len(month) for month in mylist}

# print(month_lengths)


-----------------------------------------------------------------------------------

# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']




# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# lowercase_names = [name.split()[0].lower() for name in names]

# print(lowercase_names)



-----------------------------------------------------------------------------------

# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# results=[ 2.5, 3.5, 4.5]

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# results = [(nums1[i] + nums2[i]) / 2 for i in range(len(nums1))]

# print(results)





















