# 1-masala
# a = {1,2,3,4,5,6,7}
# b = {1,2,3,54,64,5,6,7}
# print (b | a)

#######################################################
# 2-masala
# a = 'salom'
# b = 'dunyo'
# c =  a.capitalize()
# print(c)

#######################################################
# 3-masala
# a = 'Salom' 
# b = 'dunyo'
# c = a.center(45)
# print(c)

#######################################################
# 4-masala
# a = 'Salomlar455' 
# b = 'dunyo'
# c = a.encode()
# print(c)

#######################################################
# 5-masala
# a = 'Salomlar455' 
# b = 'dunyo'
# c = a.endswith('455')
# print(c)

#######################################################
# 6-masala
# a = 'Salomlar455' 
# b = 'dunyo'
# c = a.startswith('Sal')
# print(c)

#######################################################
# 7-masala
# a = "Salomlar455" 
# b = "Dunyo"
# c = a.find('Salomla')
# print(c)

#######################################################
# 8-masala
# a = "{} {} sen 150000000 yoshdasan"
# b = "Dunyo"
# c = a.format('Salom', 'Dunyo')
# print(c)


#######################################################
# 9-masala
# a = 'sen 1500 yoshdasan'
# b = 'dunyo'
# c =  a.index('0')
# print(c)

#######################################################
# 10-masala
# a = 'sen 1500 yoshdasan'
# b = 'dunyo'
# c =  a.index('0')
# print(c)

#######################################################
# 11-masala
# a = 'yoshdasan'
# b = 'dunyo'
# c =  a.isalpha()
# print(c)

#######################################################
# 12-masala
# a = 'yoshdasan'
# b = 'dunyo'
# c =  a.isascii()
# f = "1"
# print(ord(c))

#######################################################
# 13-masala
# a = '13123'
# b = 'dunyo'
# c =  a.isdecimal()
# print(c)

#######################################################
# 14-masala
# a = '123.5'
# b = 'dunyo'
# c =  a.isdigit()
# print(c)

#######################################################
# 15-masala
# a = "asd4"
# b = 'dunyo'
# c =  a.isidentifier()
# print(c)

#######################################################
# 16-masala
# a = 'yoshdasan' #katta xarf false buladi
# b = 'dunyo'
# c =  a.islower()
# print(c)

#######################################################
# 17-masala
# a = '23457'
# b = 'dunyo'
# c =  a.isnumeric()
# print(c)

#######################################################
# 18-masala
# a = '234567'  #print chixaradimi yumi tikshiradi'
# b = 'dunyo'
# c =  a.isprintable("salom")
# print(c)
# a = input("son kiritin: ")
# b = input("son kiriting: ")
######################################################
# 19-masala
# a = "asd   dfsfvc                      fasft"
# b = 'dunyo'
# c =  a.split("d" 'f')
# print(c)

#######################################################
# 20--masala
# a = 'asd dfsf  c fasf'
# b = 'dunyo'
# c =  "  ".join(b) qushib biradi usha uzgaruvchiya
# print(c)

#######################################################
# 21-masala
# a = '    salo        m         '
# b = 'dunyo'
# c =  a.strip()
# print(c)

#######################################################
# 22 -masala
# a = 'sa  lo    m            '
# b = 'dunyo'
# c =  a.rstrip()
# print(c)

#######################################################
# 23-masala
# a = '     y     osh dasan         '
# b = 'dunyo'
# c =  a.lstrip()
# print(c,'demo')

#######################################################
# 24-masala
# a = 'yoshdasan' xammasi katta
# b = 'dunyo'
# c =  a.upper()
# print(c)

#######################################################
# 25-masala
# a = 'yoshdasan'
# b = 'dunyo'
# c =  a.title()
# print(c)

#######################################################
# 26-masala
# a = 'SALOM salom'
# b = 'dunyo'
# c =  a.swapcase()
# print(c)

#######################################################
# 27-masala
# a = 'abduvali'
# b = 'dunyo'
# c =  a.replace("a", "1",)
# print(c)

#######################################################
# 28-masala
# a = 'vali'
# b = 'dunyo'
# c =  a.replace('vali', 'ali')
# print(

#######################################################
               # tamom




# a  = "s"
# b = a.maketrans
# print(b)



# a = "hello" 
# b = a.translate
# print

# def son_list(n):
#     a = []
#     for i in range (1,n+1):
#         a.append(i)
#     return a

# print(son_list(90))



# def son_list(n,m):
#     a = []
#     for i in range (n,m+1):
#         a.append(i)
#     return a
#     # print("salom")

# b = (son_list(10,15))
# # print(b)

# # def min(a,b): 
# def min(a,b):
#     if a > b:
#         return a 
#     elif a < b:
#         return b
#     else:
#         return"teng"

# # print(min(a,b))



# # # def func(a, b, c=2): # c - необязательный аргумент
# # #      # return a + b + c
# def maxx(a,b):
#     if a > b:
#         return a 
#     elif a < b:
#         return b
    # else:
        # return"teng"
# print(maxx(124, 25))


# funksiya to murojat qimagancha ishlamidi


# def x(num):
#     a =  num - 1
#     print(a)
#     x(a)
# x(5)

# a = 25
# def sonlar():
#     a = 15
#     print(a)
    
   
# # sonlar()

# # print(a)
# # a = '['
# a = [1,2,3,4,5,6]
# b = [9,8,7,6,5,4]
# def add_list(n,m):
#     return n+m
#     # n.extend(m)
#     # print(n)

# print(add_list(a,b))


# a = 10 
# b = 5
# print(b+a)





a = [1,2,3,4,5,67,78,89]

def delete(x,y):
    x = x[:y]+x[y+1:]
    return x

print(delete(a, 2))







































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































