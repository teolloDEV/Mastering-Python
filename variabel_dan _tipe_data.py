# Membuat variabel
# python tidak memiliki perintah untuk deklarasi variabel

x = 7 #Variabel dibuat saat pertama memberikan nilai pada variabel
y = "Arif "
print(x)
print(y)

"""
Variabel tidak perlu dideklarasikan dengan tipe tertentu, dan bahkan bisa berubah tipe
setelah diberikan nilai

"""

x = 4
x = "Arif"
print(x)


# menggabungkan teks dan variabel, Python menggunakan karakter " + "

x = "python is "
y = "Awesome"

print(x + y)

# Variabel Global

x = "Awesome"
def my_func():
    x = "fantastic"
    print("python is " + x)
my_func()
print("Python is " + x)