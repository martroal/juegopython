#imports de distintas librerias principalmente para el efecto de type writer
import sys
from time import sleep

dic={"reputacion": "",}


#FUNCION DE EFECTO TYPE WRITER MACHINE, no se si es necesaria la funcion, o si le agrego el loop for a cada print o input... veremos

words = ("estas serian las palabras que se imprimen en una linea con efecto de maquina de escribir")
for char in words:
        sleep(0.001)
        print(char, end='', flush=True)

#imprime la bienvenida
def bienvenida():
        print("")
        print("    ###################################")
        print("    #                                 #")
        print("    # Hola. Bienvenido a Vikingos.TXT #")
        print("    #      por Marcel Troconis        #")
        print("    #                                 #")
        print("    ###################################")

bienvenida()

#UPSALA1
def primer_pregunta():
        print(" ")
        respuesta = input("    Estás en Upsala, eliges (Noruega / Suecia)  ").lower().strip()
        for char in respuesta:
                sleep(0.001)
                print(char, end="", flush=True)
        if respuesta == "noruega":
                noruega()
        elif respuesta == "suecia":
                suecia()
        else:
                error()
                
#upsala - noruega
def noruega():
        dic["reputacion"] =+ 100
        print(" ")
        respuesta = input("    El Rey de noruega, 100 barcos, eliges: (Mon1 / Mon2)").lower().strip()
        if respuesta == "mon1":
                dic["reputacion"] =+ 1000
                print("    Te ha ido muy bien tienes 1000kg de oro")
                francia_inglaterra()
        elif respuesta == "mon2":
                dic["reputacion"] =+ 500
                print("    Te ha ido regular tienes 500kg de oro")
                francia_inglaterra()
        else: 
                error()

#upsala suecia 
def suecia():
        dic["reputacion"] =+ 100
        print(" ")
        respuesta = input("    El Rey de Suecia, solo te da 500 barcos, eliges: (Mon1 / Mon2)").lower().strip()
        if respuesta == "mon1":
                dic["reputacion"] =+ 400
                print("    Te ha ido regular tienes 500kg de oro")
                francia_inglaterra()
        elif respuesta == "mon2":
                dic["reputacion"] =-50
                print("    Ha sido un desastre, regresaste con las manos vacias")
                pelea_o_regresa()

        else:
                error()

#upsala suecia mon2
def pelea_o_regresa():
        print(" ")
        print("      Tienes dos opciones pelear contra el Rey de Suecia o Regresar a casita " )
        respuesta = input("Eliges (Pelea / Regresa)").lower().strip()
        if respuesta == "pelea":
                dic["reputacion"] =+ 300
                print("    Le ganaste a ese viejo demente, tu repu ha subido")
                francia_inglaterra()
        elif respuesta == "regresa":
                dic["reputacion"] =- 49
                print("    El que no arriesga no gana.")
                primer_pregunta() 
        else: 
                error()

#upsala noruega mon1 mon2 / suecia mon1
def francia_inglaterra():
        print(" ")
        print("    Se dice que hay mas tierras al este bla bla  ")
        respuesta = input("    Eliges ( Francia / Inglaterra) ").lower().strip()
        if respuesta == "francia":
                print("    Eres un guerrero formidable asediaste Paris con exito")     
                en_francia()
        elif respuesta == "inglaterra":
                print("    Eres un guerrero formidable asediaste Wessex con exito")
                en_inglaterra()
        else:
                error()

#upsala nor/sue MON francia
def en_francia():
        dic["reputacion"] =+ 2000
        print(" ")
        print("    Historia, aqui van los pros y contras de regresar o asentamiento")
        print("    aqui sigue los pros y contras en otra lineaa")
        respuesta = input("    Eliges (Escandinavia / Asentamiento) ")
        if respuesta == "escandinavia":
                print("")
                print("    En el largo camino a casa piensas bla bla bla")
                escandinavia()
        elif respuesta == "asentamiento":
                print("    Estas nuevas tierras necesitan trabajo y sangre bla bla    ")
                asentamiento()
        else:
                error()

#upsala nor/sue MON inglaterra
def en_inglaterra():
        dic["reputacion"] =+ 2000
        print(" ")
        print("    Historia, aqui van los pros y contras de aliados o asesinar")
        print("    aqui sigue los pros y contras en otra lineaa")
        respuesta = input("    Eliges (Aliados / Asesinar) ")
        if respuesta == "aliados":
                print("    Te has aliado con el Rey Egbertp de Wessex bla bla")
                aliado_egberto()
        elif respuesta == "asesinar":
                print("    Eres un despiadado vikingo, Odin lo aprueba bla bla")
                asesinar_egberto()
        else:
                error()

#upsala nor/sue MON inglaterra aliarseEg --- esto lleva a escandinavia o asentamiento en francia
def aliado_egberto():
        dic["reputacion"] =+ 900
        print(" ")
        print("    hisotoria de lo sucedido mientras aliado de egberto")
        print("    tienes que elegir si seguir a Egberto a asentamiento en francia o ir a Escandinavia")
        respuesta = input("    Eliges (Asentamiento / Escandinavia) ")
        if respuesta == "asentamiento":
                print("    has sacrificado tu ego por el bien de tu pueblo")
                asentamiento()
        elif respuesta == "escandinavia":
                print("    Tienes mas fuerza para lograr tu objetivo")
                escandinavia()
        else:
                error()

#upsala nor/sue MON inglaterra asesinarEg
def asesinar_egberto():
        dic["reputacion"] =+ 1600
        print(" ")
        print("    Has matado al Rey Egberto, esta tierra Wessex que sin monarca")
        print("    tienes dos opciones intentas ser rey de wessex o avanzas con tus tropas hacia northubria")
        respuesta = input("    Eliges (Wessex / Nort) ")
        if respuesta == "wessex":
                print("    Esta gente no quiere un rey extranjero...")
                wessex()
        elif respuesta == "nort":
                print("    Las tierras del norte te esperan...")
                northumbria()
        else:
                error()

#upsala nor/sue MON inglaterra asesinarEg intentarreydewessex
def wessex():
        dic["reputacion"] =+ 1000
        print(" ")
        print("    No sabias lo que el odio por un extranjero puede llegar a hacer")
        print("    Debes aceptar tu destino, te han derrotado, tus ambiciones te han llevado a la muerte ")
        #muerte_digna()

#upsala nor/sue MON inglaterra asesinarEg iraNortumbria ---- esto lleva a reyInglaterra o reyVikingo
def northumbria():
        dic["reputacion"] =+ 1800
        print(" ")
        print("    conquistaste tambien northumbria ")
        print("    la cuestion es si acabar tus dias gobernando a otros o a tu pueblo")
        respuesta = input("    Eliges (ReyInglaterra / ReyVikingo) ")
        if respuesta == "reyInglaterra":
                print("    Eres el primer rey de toda inglaterra ")
                #rey_inglaterra()
        elif respuesta == "reyVikingo":
                print("    Eres un despiadado vikingo, Odin lo aprueba bla bla")
                #rey_vikingo()
        else:
                error()

#upsala nor/sue MON francia escandinavia
def escandinavia():
        dic["reputacion"] =+ 3100
        print(" ")
        print("    Historia, aqui van los pros y contras de pelear por kategat o ser rey")
        print("    intentar ser rey de todo escandinavia, como el verdadero hijo de odin")
        respuesta = input("    Eliges (Kategat / Rey) ")
        if respuesta == "kategat":
                print("    Siempre has querido gobernar Kategat bla bla bla")
                kategat()
        elif respuesta == "rey":
                print("    Estas nuevas tierras necesitan trabajo y sangre bla bla    ")
                #rey_vikingo()
        else:
                error()

#upsala nor/sue MON francia asentamiento
def asentamiento():
        dic["reputacion"] =+ 2900
        print(" ")
        print("    Historia, aqui van los pros y contras de asesinar a todos o negociar")
        print("    aqui sigue los pros y contras en otra lineaa")
        respuesta = input("    Eliges (Asesinar / Negociar) ")
        if respuesta == "asesinar":
                print("    Tu pueblo te aclama por tu sed de sangre sobre los Francos")
                asesinar()
        elif respuesta == "negociar":
                print("    Estos Francos pueden ser traicioneros...")
                negociar()
        else:
                error()

#upsala nor/sue MON francia asentamiento negociar
def negociar():
        dic["reputacion"] =+ 900
        print(" ")
        print("    los francos son unos personajes traicioneros")
        print("    aqui sigue los pros y contras en otra lineaa")
        respuesta = input("    Eliges (gobernar / regresar) ")
        if respuesta == "gobernar":
                print("    quizas no fue la mejor desicion ")                
                gobernar()
        elif respuesta == "regresar":
                print("    vuelves al norte ")
                escandinavia()
        else:
                error()

#upsala nor/sue MON francia asentamiento negociar/asesinar gobernar
def gobernar():
        dic["reputacion"] =- 500
        print(" ")
        print("    intentas pero los francos te asesinan por la espalda")
        print("    nunca debiste haber confiado en ellos, debiste assinarlos a todos")
        #muerte_indigna()

#upsala nor/sue MON francia asentamiento asesinar
def asesinar():
        dic["reputacion"] =+ 3100
        print(" ")
        print("   Matas a cualquier frances que se cruce por tu camino")
        print("   los dioses conspiran a tu favor, la sangre les llama prefieres gobernar estas tierras o regresar a la tuya").lower().strip()
        respuesta = input("    Eliges (Gobernar / Escandinavia ) ")
        if respuesta == "gobernar":
                print(" ")
                gobernar()
        elif respuesta == "negociar":
                escandinavia()
        else:
                error()  

##upsala nor/sue MON francia escandinavia kategat
def kategat():
        dic["reputacion"] =+ 2600
        print(" ")
        print("    estas en kategat y su lider te insulta y te reta a un duelo...")
        print("    ...ves fragil a su lider pero te informan que ha muerto el rey de Wessex en Inglaterra")
        respuesta = input("    Eliges (Pelear / Inglaterra ) ")
        if respuesta == "pelear":
                print("    no fue suficiente," + nombre)
                #muerte_digna
        elif respuesta == "inglaterra":
                print("  ")
                northumbria()
        else:
                error()

















#ERROR todos los elssssseeeeeee
def error():
        print(" ")
        print("   ####################################################################")
        print(" ")
        print("    Desicion invalida, cobarde. Vuelve a ejecutar el juego y esribe/elige bien.")
        print(" ")
        print("   #########################################################################")


def pregunta_4A():
        print ("sig preg")


#recibe el apellido y lo imprime con mayuscula
print(" ")
print("--------------------------------------------------")  
print(" ") 
nombre = input("    Cual es tu apellido? " ).capitalize()
print(" ")
print("    Mucho gusto, Ragnar ", nombre )
print(" ")

#inicializa el juego (entra en el loop if/else)
respuesta = input("    Quieres jugar? (si/no) " )
if respuesta == "si":
        primer_pregunta()
else: 
        error()


print(dic)