#imports de distintas librerias principalmente para el efecto de type writer
import sys
from time import sleep

#diccionario para poder llevar cuenta de reputacion, que se suma mediante cada eleccion
dic={"reputacion": "",}


#FUNCION DE EFECTO TYPE WRITER MACHINE... veremos 
#de prueba esto ira comentado en la version final
# for char in words:
#         sleep(0.01)
#         print(char, end='', flush=True)

#imprime la bienvenida
def bienvenida():
        print("")
        print("    ###################################")
        print("    #                                 #")
        print("    # Hola. Bienvenido a Vikingos.TXT #")
        print("    #      por Marcel Troconis        #")
        print("    #                                 #")
        print("    ###################################")

#llamando la funcion
bienvenida()

#UPSALA1
def primer_pregunta():
        print(" ")
        descrip = ("Estas en Upsala, un pueblo agricola en el corazon de Escandinavia, ano 750. Eres un guerrero con ansias de sangre, llevas sonando expediciones por todo el mundo por muchos anos, tienes ideas pero no tienes los medios, si quieres cumplir con tus metas debes ir a un reino mas poderoso y pedir apoyo, en Noruega se sabe que les gusta las aventuras, en Suecia se inclinan mas por el dinero.")
        for char in descrip:
                sleep(0.01)
                print(char, end='', flush=True)
        print("")
        respuesta = input("    Eliges (Noruega / Suecia)  ").lower().strip()
        if respuesta == "noruega":
                noruega()
        elif respuesta == "suecia":
                suecia()
        else:
                error()
                
#upsala - noruega
def noruega():
        dic["reputacion"] =+ 1
        descrip = ("Has elegido ir a Noruega, el Rey de Noruega comparte tus ideas, le emociona tu discurso y te otorga 100 barcos para que te acompanen. Durante el viaje, estan perdidos en el mar, debes elegir entre ir al norte o al sur")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True)    
        print(" ")
        respuesta = input("    Eleccion: (Norte / Sur)").lower().strip()
        if respuesta == "norte":
                dic["reputacion"] =+ 4
                print("    Te ha ido muy bien conseguiste 1000kg de oro y tu reputacion va creciendo")
                francia_inglaterra()
        elif respuesta == "sur":
                dic["reputacion"] =+ 2
                print("    Te ha ido regular tienes 500kg de oro, bueh, todo suma, no?")
                francia_inglaterra()
        else: 
                error()

#upsala suecia 
def suecia():
        dic["reputacion"] =+ 1
        print(" ")
        descrip=("Has elegido ir a Suecia, el Rey de Suecia es medio ortiva, pero quiere ganar dinero asi que te da 50 barcos para que te acompanen. Durante el viaje, estan perdidos en el mar, debes elegir entre ir al norte o al sur")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True)    
        print(" ")
        respuesta = input("    Eliges: (norte / sur)").lower().strip()
        if respuesta == "norte":
                dic["reputacion"] =+ 2
                print("    Te ha ido regular tienes 500kg de oro")
                francia_inglaterra()
        elif respuesta == "sur":
                dic["reputacion"] =-10
                print("    Ha sido un desastre, regresaste con las manos vacias")
                pelea_o_regresa()

        else:
                error()

#upsala suecia-sur
def pelea_o_regresa():
        print(" ")
        descrip =("Ya nadie te cree, perdiste muchos hombres y no ganaste nada. Tienes dos opciones pelear contra el Rey de Suecia y recuperar algo de tu reputacion o regresar a casa a llevar una vida de granjero..." )
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
        respuesta = input("Eliges (Pelear / Regresar)").lower().strip()
        if respuesta == "pelear":
                dic["reputacion"] =+ 4
                print("    Le ganaste a ese viejo demente, tu reputacion ha subido")
                francia_inglaterra()
        elif respuesta == "regresar":
                dic["reputacion"] =- 3
                print("    Esta vez no pudo ser. Odin confia en que lo intentes de nuevo")
                primer_pregunta() 
        else: 
                error()

#upsala noruega-norte-sur / suecia-norte
def francia_inglaterra():
        print(" ")
        descrip=("    Se dice que hay mas tierras al del mundo es imperativo ir a explorar y saquear  ")
        for char in descrip:
                sleep(0.01)
                print(char, end='', flush=True)
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
        dic["reputacion"] =+ 3
        print(" ")
        descrip=("    Historia, aqui van los pros y contras de regresar o asentamiento")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
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
        dic["reputacion"] =+ 3
        print(" ")
        descrip=("    Historia, aqui van los pros y contras de aliados o asesinar")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
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
        dic["reputacion"] =+ 1
        print(" ")
        descrip=("    hisotoria de lo sucedido mientras aliado de egberto")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
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
        dic["reputacion"] =+ 2
        print(" ")
        descrip=("    Has matado al Rey Egberto, esta tierra Wessex que sin monarca")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
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
        dic["reputacion"] =+ 3
        print(" ")
        print("    No sabias lo que el odio por un extranjero puede llegar a hacer")
        print("    Debes aceptar tu destino, te han derrotado, tus ambiciones te han llevado a la muerte ")
        #muerte_digna()

#upsala nor/sue MON inglaterra asesinarEg iraNortumbria ---- esto lleva a reyInglaterra o reyVikingo
def northumbria():
        dic["reputacion"] =+ 2
        print(" ")
        descrip=("    conquistaste tambien northumbria ")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
        respuesta = input("    Eliges (ReyInglaterra / ReyVikingo) ")
        if respuesta == "reyInglaterra":
                print("    Eres el primer rey de toda inglaterra ")
                rey_inglaterra()
        elif respuesta == "reyVikingo":
                print("    Eres un despiadado vikingo, Odin lo aprueba")
                rey_vikingo()
        else:
                error()

#upsala nor/sue MON francia escandinavia
def escandinavia():
        dic["reputacion"] =+ 3
        print(" ")
        descrip=("    Historia, aqui van los pros y contras de pelear por kategat o ser rey")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
        respuesta = input("    Eliges (Kategat / Rey) ")
        if respuesta == "kategat":
                print("    Siempre has querido gobernar Kategat bla bla bla")
                kategat()
        elif respuesta == "rey":
                print("    Estas nuevas tierras necesitan trabajo y sangre bla bla    ")
                rey_vikingo()
        else:
                error()

#upsala nor/sue MON francia asentamiento
def asentamiento():
        dic["reputacion"] =+ 2
        print(" ")
        descrip=("    Historia, aqui van los pros y contras de asesinar a todos o negociar")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
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
        dic["reputacion"] =+ 1
        print(" ")
        descrip=("    los francos son unos personajes traicioneros")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
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
        dic["reputacion"] =- 10
        print(" ")
        print("    intentas pero los francos te asesinan por la espalda")
        print("    nunca debiste haber confiado en ellos, debiste assinarlos a todos")
        #muerte_indigna()

#upsala nor/sue MON francia asentamiento asesinar
def asesinar():
        dic["reputacion"] =+ 3
        print(" ")
        descrip=("   Matas a cualquier frances que se cruce por tu camino los dioses conspiran a tu favor, la sangre les llama prefieres gobernar estas tierras o regresar a la tuya").lower().strip()
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True) 
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
        dic["reputacion"] =+ 3
        print(" ")
        descrip=("    Estas en kategat y su lider te insulta y te reta a un duelo... ves fragil a su lider pero te informan que ha muerto el rey de Wessex en Inglaterra")
        for char in descrip: 
                sleep(0.01)
                print(char, end='', flush=True)     
        respuesta = input("    Eliges (Pelear / Inglaterra ) ")
        if respuesta == "pelear":
                print("    no fue suficiente," + nombre)
                muerte_digna()
        elif respuesta == "inglaterra":
                print("  ")
                northumbria()
        else:
                error()


def muerte_digna(): 
        dic["reputacion"] =+ 3
        print(" ")
        descrip = ("    has muerto dignamente, Odin y todos los dioses te reciben el Valhala y bla bla bla bla bla bla ")
        for char in descrip:
                sleep(0.001)
                print(char, end='', flush=True)
        endgame()

def rey_inglaterra(): 
        dic["reputacion"] =+ 5
        print(" ")
        descrip = ("Has elegido gobernar un pueblo que no era el tuyo pasaras tus ultimos dias odiandote por no haber regresado a casa... igualmente... enhorabuena, por lo menos eres rey de algun lado")
        for char in descrip:
                sleep(0.001)
                print(char, end='', flush=True)
        endgame()

def rey_vikingo():
        dic["reputacion"] =+ 10
        print(" ")
        descrip = ("    Vas por la gloria, te quieres saltar varios pasos... y eso esta bien, en tu ADN vikingo esta programado para que seas asi,")
        for char in descrip:
                sleep(0.001)
                print(char, end='', flush=True)
        respuesta= input("prefieres atacar primero a (Dinamarca/Noruega")
        if respuesta == "dinamarca" or "suecia":
                leyenda_vikinga()
        else:
                error()

def leyenda_vikinga(): 
        dic["reputacion"] =+ 5
        print(" ")
        descrip = ("    Te convertiste en rey de toda escandinavia. Y atacaste lejanas tierras eres y seras el Vikingo mas grandes que ha existido.")
        for char in descrip:
                sleep(0.001)
                print(char, end='', flush=True)
        endgame()

def muerte_indigna():
        dic["reputacion"] =+ 0
        print(" ")
        descrip = ("  Eres una desgracias para tu pueblo, iras al cielo cristiano a sufir por toda la eternidad")
        for char in descrip:
                sleep(0.001)
                print(char, end='', flush=True)
        endgame()       

def endgame():
        print("#################################################################")
        print("#                                                               #")
        print("#                            FIN                                #")
        print("#                                                               #")
        print("#################################################################")

#ERROR va en todos los else, aparece cuando se elige una opcion distinta de las ofrecidas
def error():
        print(" ")
        print("###############################################################################")
        print("#                                                                             #")
        print("#  Desicion invalida, cobarde. Vuelve a ejecutar el juego y esribe/elige bien #")
        print("#                                                                             #")
        print("###############################################################################")

#recibe el apellido y lo imprime con mayuscula
print(" ")
print("--------------------------------------------")  
print(" ") 
apellido = input("    Cual es tu apellido? " ).capitalize()
print(" ")
nombre=("Ragnar "+ apellido)
print("Bienvennido "+nombre)
print(" ")

#inicializa el juego (entra en el loop if/else)
respuesta = input("    Quieres jugar? (si/no) " )
if respuesta == "si":
        primer_pregunta()
else: 
        error()

#imprime reputacion/puntuacion
print(dic)
