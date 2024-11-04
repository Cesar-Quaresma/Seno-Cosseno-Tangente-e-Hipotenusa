import math
print(" Nesse sistema operacional aritmético, terá a possibilidade em realizar operações diferentes das convencionais,\n(Adição, Subtração, etc.) como calcular: \033[1:35mHipotenusa, \033[1:32mSeno,\033[1:36m Cosseno, \033[1:33mTangente\033[0:39m, por meio dos dígitos iniciais \ndessas como: \033[1:35m'H \033[0:39mou \033[1:35mh' \033[0:39mpara \033[1:35mHipotenusa, \033[1:32m'S \033[0:39mou \033[1:32ms' \033[0:39mpara \033[1;32mSeno, \033[1:36m'C \033[0:39mou \033[1:36mc' \033[0:39mpara \033[1:36mCosseno, \033[0:39me \033[1:33m'T \033[0:39mou \033[1:33mt' \033[0:39mpara \033[1:33mTangente\033[0:39m.\n\n\033[4:33mVAMOS COMEÇAR?\033[0:39m")
opção = str(input("Qual a operação desejada? ")).lower()
if opção in 'Hh' or opção in 'Ss' or opção in 'Cc' or opção in 'Tt':
   if opção in 'Hh':
       catoposto = float(input("\033[1:33mCateto Oposto: "))
       catadjacente = float(input("\033[1:32mCateto Adjacente: "))
       hipotenusa = math.hypot(catoposto, catadjacente)
       print("\033[1:39mO resultado da \033[1:35mHipotenusa\033[1:39m, ora entre os catetos: \033[1:33mcateto oposto {}, \033[1:39me \033[1:32mcateto adjacente {}, \033[1:39mé de: \033[1:34m{}".format(catoposto, catadjacente, hipotenusa))
   elif opção in 'Ss':
       a = float(input("Número: "))
       seno = math.sin(math.radians(a))
       print("\033[1:39mO \033[1:32mSeno \033[1:39mdo número \033[1:37m{}, \033[1:39mé de: \033[1:34m{}".format(a, seno))
   elif opção in 'Cc':
       b = float(input("Número: "))
       cosseno = math.cos(math.radians(b))
       print("\033[1:39mO \033[1:36mCosseno \033[1:39mdo número \033[1:37m{}, \033[1:39mé de: \033[1:34m{}.".format(b, cosseno))
   elif opção in 'Tt':
       c = float(input("Número: "))
       tangente = math.tan(math.radians(c))
       print("\033[1:39mA \033[1:33mTangente \033[1:39mdo número \033[1:37m{},\033[1:39m é de: \033[1:34m{}.".format(c, tangente))
else:
     print("\033[1:31mErro na operação!! Tente novamente!")
print("\033[1:37m FIM.")

