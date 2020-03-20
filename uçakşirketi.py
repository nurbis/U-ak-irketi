#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 00:18:25 2020

@author: nurbanuozkan
"""


from datetime import datetime
from random import randint
"CLASSES"
class Şehir():
    def __init__(self,isim):
        self.__isim = isim
        self.__sıcaklık = randint(18,25)
        self.__hava_durumu = ["Açık","Kapalı","Yağmurlu","Sağanak Yağışlı"][randint(0,len(["Açık","Kapalı","Yağmurlu","Sağanak Yağışlı"])-1)]
    
    def get_isim(self):
        return self.__isim
    
    def get_sıcaklık(self):
        return self.__hava_durumu
    
    def set_sıcaklık(self,sıcaklık):
        if 18<=sıcaklık and sıcaklık<=25:
            self.__sıcaklık=sıcaklık
        else:
            pass
    
    def set_hava_durumu(self,durum):
        if not durum in ["Açık","Kapalı","Yağmurlu","Sağanak Yağışlı"]:
            pass
        else:
            self.__hava_durumu = durum
    def __str__():
        return self.__isim
    
class Uçuş:
    def __init__(self,nereden:Şehir,nereye:Şehir,tarih:datetime):
        self.__nereden = nereden
        self.__nereye = nereye
        self.__tarih = tarih
        
    def get_tarih(self):
        return self.__tarih
    
    def getnereden(self):
        return self.__nereden
    
    def getnereye(self):
        return self.__nereye
 
    def rötar(self,nekadar:int):
        day = self.__tarih.day
        hour = self.__tarih.hour
        minute = self.__tarih.minute
        
        if (nekadar+minute >= 60):
            hour+=(nekadar+minute)//60
            #hour += int((minute+nekadar)/60)
            minute=(nekadar+minute)%60
            
            if (hour >=24):
                day+= int(hour/24)
                hour = hour%24
        else:
            minute+=nekadar
        new_Date = datetime(self.__tarih.year,self.__tarih.month,day,hour,minute)
        self.__tarih=new_Date
    
   
 
class Yolcu():
    def __init__(self,isim:str,soyisim:str,tcno:int):
        self.isim = isim
        self.soyisim = soyisim
        self.tcno = tcno
    
    def getisim(self):
        return self.isim
    
    def getsoyisim(self):
        return self.soyisim
    
    def gettc(self):
        return self.tcno
    
class Bilet():
    def __init__(self,yolcu:Yolcu,uçuş:Uçuş,koltuk_numarası:str):
        self.__yolcu = yolcu
        self.__uçuş = uçuş
        self.__koltuk_numarası = koltuk_numarası
    
    def getuçuş(self):
        return self.__uçuş
    
    def __str__(self):
        return """İsim: {}
        Soyisim: {}
        Nereden: {}
        Nereye: {}
        TC: {}
        Uçuş Tarihi: {}
        Uçuşun Saati: {}
        Koltuk NO: {}""".format(self.__yolcu.getisim(),self.__yolcu.getsoyisim(),self.__uçuş.getnereden().get_isim(),self.__uçuş.getnereye().get_isim(),self.__yolcu.gettc(),self.__uçuş.get_tarih().date(),self.__uçuş.get_tarih().time(),self.__koltuk_numarası)

class Pegasus():
    def __init__(self):
        self.__aktifbiletler = list()
        self.__geçmişbiletler = list()
        self.__aktifuçuşlar = list()
        self.__geçmişuçuşlar = list()
    
    def bilet_al(self,yolcu:Yolcu,uçuş:Uçuş,koltuk_numarası:str):
        if uçuş in self.__aktifuçuşlar:
            bilet = Bilet(yolcu,uçuş,koltuk_numarası)
            self.__aktifbiletler.append(Bilet(yolcu,uçuş,koltuk_numarası))
            return bilet
    
    def uçuş_oluştur(self,nereden:Şehir,nereye:Şehir,tarih:datetime):
        x = Uçuş(nereden,nereye,tarih)
        self.__aktifuçuşlar.append(x)
        return x
    
    def biletiptal(self,bilet:Bilet):
        if bilet in self.__aktifbiletler:
            self.__aktifbiletler.remove(bilet)
    
    def uçuş_gerçekleşti(self,uçuş:Uçuş):
        for bilet in self.__aktifbiletler:
            if (bilet == bilet.getuçuş()):
                self.__aktifbiletler.remove(bilet)
                self.__geçmişbiletler.append(bilet)
        self.__aktifuçuşlar.remove(uçuş)
        self.__geçmişuçuşlar.append(uçuş)
    
    def rötar(self,uçuş:Uçuş,nekadar:int):
        Uçuş.rötar(nekadar)
def Main():
    s="""İstanbul,Ankara,İzmir,Adana,Adıyaman,Afyonkarahisar,Ağrı,Aksaray,Amasya,Antalya,Ardahan,Artvin,Aydın,Balıkesir,Bartın,Batman,Bayburt,Bilecik,Bingöl,Bitlis,Bolu,Burdur,Bursa,Çanakkale,Çankırı,Çorum,Denizli,Diyarbakır,Düzce,Edirne,Elazığ,Erzincan,Erzurum,Eskişehir,Gaziantep,Giresun,Gümüşhane,Hakkari,Hatay,Iğdır,Isparta,Kahramanmaraş,Karabük,Karaman,Kars,Kastamonu,Kayseri,Kırıkkale,Kırklareli,Kırşehir,Kilis,Kocaeli,Konya,Kütahya,Malatya,Manisa,Mardin,Mersin,Muğla,Muş,Nevşehir,Niğde,Ordu,Osmaniye,Rize,Sakarya,Samsun,Siirt,Sinop,Sivas,Şırnak,Tekirdağ,Tokat,Trabzon,Tunceli,Şanlıurfa,Uşak,Van,Yalova,Yozgat,Zonguldak"""

    şehirler = list() #sehir objelerini tutan
    for i in s.split(","):
        şehirler.append(Şehir(i)) #sehir objelerini olusturduk.
    yolcu1 = Yolcu("Furkan","Kızıloğlu",12345678901)
    pegasus = Pegasus()
    uçuş1 = pegasus.uçuş_oluştur(şehirler[5],şehirler[12],datetime(2018,4,9,7,40))
    bilet1 = pegasus.bilet_al(yolcu1,uçuş1,"A3")
    print(bilet1)
if __name__ == "__main__":
    Main()