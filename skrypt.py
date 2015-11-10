
# coding: utf-8

# In[62]:

def numerologicznaSumaCyfr(liczba):
    #tak dlugo jak suma cyfr wieksza od 9 i nie jest liczbą mistrzowską (podzielną przez 11)
    while (liczba%11 !=0 and liczba > 9 ):
        liczba = sum(int(digit) for digit in str(liczba))
    return liczba
        

def liczPortretNumerologiczny(data_urodzenia):
    # format daty typu dzien.miesiac.rok
    suma = sum(int(x) for x in data_urodzenia if x.isdigit())
    # print("Suma przed pętlą %d" %suma)
    return numerologicznaSumaCyfr(suma)



def liczNumerologieSlowa(slowo):
    slownik = {'a':1,
               'b':2,
               'c':3,
               'd':4,
               'e':5,
               'f':6,
               'g':7,
               'h':8,
               'i':9,
               'j':1,
               'k':2,
               'l':3,
               'm':4,
               'n':5,
               'o':6,
               'p':7,
               'q':8,
               'r':9,
               's':1,
               't':2,
               'u':3,
               'v':4,
               'w':5,
               'x':6,
               'y':7,
               'z':8 }
    
    suma=0
    for litera in slowo.lower():
        for key in slownik:
            if litera == key:
                suma+=slownik[key]
    return numerologicznaSumaCyfr(suma)


# In[61]:

print(liczNumerologieSlowa("Aleksander"))

print("Twoja droga życia to: %d " % (liczPortretNumerologiczny("02.06.1184")))


# In[64]:

print(liczNumerologieSlowa("Pawel"))
print(liczNumerologieSlowa("Woloch"))

print("Twoja droga życia to: %d " % (liczPortretNumerologiczny("01.04.1977")))
        
        
    


# In[69]:

print(liczNumerologieSlowa("Jan"))
print(liczNumerologieSlowa("Niemiec"))
print("Twoja droga życia to: %d " % (liczPortretNumerologiczny("12.10.1985")))


# In[68]:

print(liczNumerologieSlowa("Alan"))
print(liczNumerologieSlowa("Zakrzewski"))


print("Twoja droga życia to: %d " % (liczPortretNumerologiczny("02.09.1987")))


# In[70]:

print(liczNumerologieSlowa("Dawid"))
print(liczNumerologieSlowa("Wozniak"))

print("Twoja droga życia to: %d " % (liczPortretNumerologiczny("10.09.1985")))
        
        


# In[71]:

print(liczNumerologieSlowa("Janusz"))
print(liczNumerologieSlowa("Cieszynski"))

print("Twoja droga życia to: %d " % (liczPortretNumerologiczny("25.08.1988")))
        
        


# In[ ]:



