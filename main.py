import random
import time



BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
puntaje = random.randint(0,10)

def bonus():
  puntos = 0
  print("Como ultima oportunidad, responde de manera correcta una ultima pregunta y te sumara un bonus random")
  time.sleep(2)
  print(BLUE + "BONUS Cual de los siguientes es un Hobbie de Alfred Pennyworth?" + RESET)
  time.sleep(4)
  print("1) Bowling")
  print("2) Cultivar rosas")
  print("3) Observar mariposas")
  print("4) Coleccionar estampas")
  rbonus = input("Tu respuesta es: ")
  if rbonus == "2":
    puntos = random.randint(8, 13)
    puntaje =+ puntos
    print(GREEN +"Gracias", nombre,"por jugar mi trivia. Alcanzaste ", puntaje, "puntos " + RESET)
  else:
    print(GREEN +"Incorrecto\n Gracias", nombre,"por jugar mi trivia. Alcanzaste ", puntaje, "puntos" + RESET)

  
#Encabezado y Bienbenida a la Trivia 

for numero_carga  in range (5, 0, -1):
  print(numero_carga)
  time.sleep(1)

print("                    ***********************")   
print("              *********************************")
print("           *******   *     *       *    *    *******")
print("        *******   ***      **     **     ***   *******")
print("      ******   *****       *********      *****    *****")
print("    ******  ********       *********       ******    *****")
print("   ****   **********       *********       *********   *****")
print("  ****  **************    ***********     ************   ****")
print(" ****  *************************************************  ****")
print("****  ***************************************************  ****")
print("****  ****************************************************  ****")
print("****  ****************************************************  ****")
print(" ****  ***************************************************  ****")
print("  ****  *******     ****  ***********  ****     *********  ****")
print("   ****   *****      *      *******      *      ********  ****")
print("    *****   ****             *****             ******   *****")
print("      *****   **              ***              **    ******")
print("       ******   *              *              *   *******")
print("         *******                                *******")
print("            ********                         *******")
print("               *********************************")
print("                    ***********************\n")

print(YELLOW + "Bienvenidos a la Trivia de quien sabe mas de BATMAN"+ RESET)
nombre = str( input("\nIndicame cual es tu nombre: "))


print(GREEN + "\nHola " + nombre +  " Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n" + RESET )

time.sleep(5)

print(YELLOW + "Bien " + nombre + " comencemos y veamos cuanto sabes de BATMAN. Empiezas con", puntaje,"puntos" + RESET)

time.sleep(3)

  #Pregunta 1 
print(BLUE +"A) Cual es el origen de Batman?\n" + RESET)
print ("1) Bruce Wayne vino de un planeta extinto como unico sobreviviente del mismo ")
print("2) Alfred es quien induce a que el joven Bruce Wayne luche contra el crimen en Ghotam")
print("3) Los padres de Bruce Wayne son asesinados por un ladron en Gotham frente a el")
print("4) Clark Kent anima a Bruce a que se vuelva un justiciero nocturno de Ghotam")
#Almacenamos la respuesta del usuario enla variable Y colocamos un While para validar la respuesta
respuesta_1 = input ("Tu respuesta: ")
while respuesta_1 not in ('1', '2', '3', '4'):
  print(GREEN +'Hmmm...')
  time.sleep(2)
  print("Creo que algo anda mal"+ RESET)
  time.sleep(2)
  respuesta_1 = input(CYAN +"\nDebes responder 1, 2, 3, o 4 ingresa nuevamente tu respuesta: " + RESET)

if respuesta_1 == '3':
  puntaje += 5
  print(GREEN +'\nMuy bien, aunque esa es muy facil. Vamos por otra mas difici!\n' + RESET)
  time.sleep(2)
else:
  puntaje -= 2
  print(RED +'\nNo es correcto, Sigamos\n' + RESET)
time.sleep(2)
print(GREEN + 'Tienes', puntaje, "puntos hasta el momento\n"+ RESET)
time.sleep(3)
print(GREEN + "Cierto no te conte,  restaras puntos por las fallas, asi que presta mucha  atencion\n" + RESET)
time.sleep(5)

print(BLUE + 'B) Cual ha sido su primer robin?\n' + RESET)
print('1) Damian Wayne')
print('2) Dick Grayson')
print('3) Jason Todd')
print('4) Stepphanie Brown ')
respuesta_2 = input('Tu respuesta es: ')
while respuesta_2 not in ('1', '2', '3', '4', '5'):
  respuesta_2 = input(CYAN + "\nDebes responder 1, 2, 3, o 4 ingresa nuevamente tu respuesta: " + RESET) 

if respuesta_2 == "1":
  puntaje -= 2
  print(RED + "\nIncorrecto!", nombre, "El es el ultimo robin\n" +RESET )
elif respuesta_2 == "3":
  puntaje -= 2
  print(RED + "\nIncorrecto!", nombre, "El es el segundo robin\n" + RESET)
elif respuesta_2 == "4":
  puntaje -= 2
  print(RED + "\nIncorrecto!", nombre, "Ella es la version femenina de robin que aparecio en 1992\n"+ RESET)
  puntaje -= 2
else:
  puntaje += 5
  print(GREEN + "Muy bien", nombre, "! Dick Grayson es el primer robin quien en su infancia pertenecia a una familia de acrobatas\n" + RESET)
time.sleep(2)
print(GREEN + 'Tienes', puntaje, "puntos hasta el momento\n"+ RESET)
time.sleep(1)
if respuesta_2 == '12':
  time.sleep(3)
  print(MAGENTA + 'Enhorabuena eres mas fan de lo que yo pensaba En realidad contando todos los Elseworlds serian 12 robins\n' + RESET)
  
print(BLUE + 'C) Quien de estos ha llevado el manto de Batman?' + RESET)
print('1) Thomas Wayne')
print('2) Jean Paul Valley')
print('3) Hugo Strange')
print('4) Todas la anterioes')

respuesta_3 = input('Tu respuesta es: ')
while respuesta_3 not in ('1', '2', '3', '4', ):
  respuesta_3 = str(input(CYAN +"\nDebes responder 1, 2, 3, o 4 ingresa nuevamente tu respuesta: " + RESET))
if respuesta_3 == "4":
  puntaje += 5
  print(GREEN +'Es correcta\n')
else:
  puntaje -= 2
  print(RED + 'Es incorrecto\n ' + RESET)
time.sleep (2)
print(GREEN + 'Tienes', puntaje, "puntos hasta el momento\n"+ RESET)
time.sleep (2)
print(BLUE +"D) De dónde obtuvo la idea del nombre de la ciudad Gotham Bill Finger?" + RESET)
print("1) De un periodico")
print("2) De una valla publicitaria")
print("3) De una guia de telefonica")
print("4) De un anuncio de joyeria")
respuesta_4 = str(input('Tu respuesta es: '))
while respuesta_4 not in ('1', '2', '3', '4', '5'):
  respuesta_4 = input(CYAN +"\nDebes responder 1, 2, 3, o 4 ingresa nuevamente tu respuesta: " + RESET)


if respuesta_4 == "4":
    puntaje += 5
    time.sleep(3)
    print(GREEN + "Y la respuesta es....")
    time.sleep(4)
    print(GREEN + "Correcta\n" + RESET)
else:
  print(RED + "INCORRECTO" +RESET)

time.sleep(1)
if puntaje <= 10:
  bonus()
else:
  print (GREEN +"Gracias", nombre,"por jugar mi trivia. Alcanzaste ", puntaje, "puntos " + RESET)
