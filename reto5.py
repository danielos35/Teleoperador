import os
import math


opcion_usuario = '0'
punto_usuario ='0'

print('Bienvenido al sistema de ubicación para zonas públicas WIFI')

coordenadas = [
    [0,0], # Trabajo
    [0,0], # Casa
    [0,0], # Parque
]

#Ingresar Cordenada

latitud_maxima = float(6.690)
latitud_minima = float(6.532)
longitud_maxima = float(-72.872)
longitud_minima = float(-73.120)

#RETO 4
daniel = 0

#Predefinidas 

predefinidas = [
    [6.632,-72.984,285],
    [6.564,-73.061,127],
    [6.532,-73.002,15],
    [6.623,-72.978,56],
]

R =6372.795477598
latitud_inicial, longitud_inicial = [0,0],[0,0]
#Opciones 
var2={'1','2','3'}
zonas_cercanas = [{},{}]

#RETO4


#CALCULAR DISTANCIA
def calcular_distancia (lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon2)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    
    sin2_lat = math.sin(delta_lat / 2) ** 2
    sin2_lon = math.sin(delta_lon / 2) ** 2
    
    raiz_cuadrada = math.sqrt(sin2_lat + math.cos(lat1)*math.cos(lat2)*sin2_lon)
    distancia = 2 * R * math.asin(raiz_cuadrada)    
    return round(distancia)      

#UBICAR ZONA WIFI
prom_moto = 19.24
prom_pie=0.483


longitud_inicial = 1
latitud_inicial = 1
tiempo_promedio_moto = 0
tiempo_promedio_pie = 0



def ubicar_zona_wifi():
    global longitud_inicial, latitud_inicial, tiempo_promedio_moto
    global tiempo_promedio_pie
    global all
    if str(coordenadas[0][0]) == '0':
        print('Error sin registro de coordenadas')
        exit()
    else: 
        print(f"Coordenada [latitud, longitud] 1: ['{coordenadas[0][0]}','{coordenadas[0][1]}']")
        print(f"Coordenada [latitud, longitud] 2: ['{coordenadas[1][0]}','{coordenadas[1][1]}']")    
        print(f"Coordenada [latitud, longitud] 3: ['{coordenadas[2][0]}','{coordenadas[2][1]}']")
        ubicacion_actual = input('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión ')
        
        if ubicacion_actual not in var2:
            print('Error ubicación')
            exit()
        elif ubicacion_actual == '1':
            latitud_inicial, longitud_inicial = coordenadas[0][0],coordenadas[0][1]
        elif ubicacion_actual == '2':
             latitud_inicial, longitud_inicial = coordenadas[1][0],coordenadas[1][1]
        elif ubicacion_actual == '3':
            latitud_inicial, longitud_inicial = coordenadas[2][0],coordenadas[2][1]
        
        for zona in predefinidas:
            latitud_final, longitud_final = zona[0],zona[1]
            distancia= calcular_distancia(latitud_inicial,longitud_inicial,latitud_final,longitud_final)
            diccionario_distancia = {'distancia':distancia,'usuarios':zona[2],'coordenadas':(zona[0],zona[1])}
            if not zonas_cercanas[0]:
                zonas_cercanas[0] = diccionario_distancia
            else:
                if distancia < zonas_cercanas[0]['distancia']:
                    zonas_cercanas[1] = zonas_cercanas [0]
                    zonas_cercanas[0] = diccionario_distancia
                elif not zonas_cercanas[1] or distancia < zonas_cercanas[1]['distancia']:
                    zonas_cercanas[1] = diccionario_distancia
        if zonas_cercanas [1]['usuarios'] < zonas_cercanas[0]['usuarios']:
            zonas_cercanas[0], zonas_cercanas[1] = zonas_cercanas[1], zonas_cercanas[0]    

        print('Zonas wifi cercanas con menos usuarios')
        print(f"La zona wifi 1: ubicada en ['{zonas_cercanas[0]['coordenadas'][0]}','{zonas_cercanas[0]['coordenadas'][1]}'] a {zonas_cercanas[0]['distancia']} metros, tiene en promedio {zonas_cercanas[0]['usuarios']} usuarios")
        print(f"La zona wifi 2: ubicada en ['{zonas_cercanas[1]['coordenadas'][0]}','{zonas_cercanas[1]['coordenadas'][1]}'] a {zonas_cercanas[1]['distancia']} metros, tiene en promedio {zonas_cercanas[1]['usuarios']} usuarios")
        
        punto_usuario = input('Elija 1 o 2 para recibir indicaciones de llegada ')
        
        
        if punto_usuario not in ('1','2'):
            print('Error zona wifi')
            exit()
        else:
            
            
            
            if punto_usuario == '1':
                if abs(zonas_cercanas[0]['coordenadas'][0]-latitud_inicial) < abs(zonas_cercanas[0]['coordenadas'][1] -longitud_inicial):
                    if latitud_inicial < zonas_cercanas[0]['coordenadas'][0] and longitud_inicial < zonas_cercanas[0]['coordenadas'][1]:
                        print("Para llegar a la zona wifi dirigirse primero al norte y luego hacia el oriente")
                    elif latitud_inicial < zonas_cercanas[0]['coordenadas'][0] and longitud_inicial > zonas_cercanas[0]['coordenadas'][1]:
                        print ('Para llegar a la zona wifi dirigirse primero al norte y luego hacia el occidente')
                    elif latitud_inicial > zonas_cercanas[0]['coordenadas'][0] and longitud_inicial < zonas_cercanas[0]['coordenadas'][1]:
                        print ('Para llegar a la zona wifi dirigirse primero al sur y luego hacia el oriente')
                    elif latitud_inicial > zonas_cercanas[0]['coordenadas'][0] and longitud_inicial > zonas_cercanas[0]['coordenadas'][1]:
                        print ('Para llegar a la zona wifi dirigirse primero al sur y luego hacia el occidente')
                        
                elif abs(zonas_cercanas[0]['coordenadas'][0]-latitud_inicial) > abs(zonas_cercanas[0]['coordenadas'][1] -longitud_inicial):
                    
                    if longitud_inicial < zonas_cercanas[0]['coordenadas'][1] and latitud_inicial < zonas_cercanas[0]['coordenadas'][0]:
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                    elif longitud_inicial < zonas_cercanas[0]['coordenadas'][1] and latitud_inicial > zonas_cercanas[0]['coordenadas'][0]:
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el sur")
                    elif longitud_inicial > zonas_cercanas[0]['coordenadas'][1] and latitud_inicial < zonas_cercanas[0]['coordenadas'][0]:
                        print("Para llegar a la zona wifi dirigirse primero al occidene y luego hacia el norte") 
                    elif longitud_inicial > zonas_cercanas[0]['coordenadas'][1] and latitud_inicial > zonas_cercanas[0]['coordenadas'][0]:
                        print("Para llegar a la zona wifi dirigirse primero al occidene y luego hacia el sur")
                        
                tiempo_promedio_moto =  (zonas_cercanas[0]['distancia'])/ prom_moto
                tiempo_promedio_pie = (zonas_cercanas[0]['distancia'])/ prom_pie  
                print(f'Tiempo promedio en moto: {tiempo_promedio_moto} minutos')
                print(f'Tiempo promedio a pie: {tiempo_promedio_pie} minutos')
                input('Presiones 0 para salir: ')                   
            
            elif punto_usuario == '2':
                
                if abs(zonas_cercanas[1]['coordenadas'][0]-latitud_inicial) < abs(zonas_cercanas[1]['coordenadas'][1] -longitud_inicial):
                    if latitud_inicial < zonas_cercanas[1]['coordenadas'][0] and longitud_inicial < zonas_cercanas[1]['coordenadas'][1]:
                        print("Para llegar a la zona wifi dirigirse primero al norte y luego hacia el oriente")
                    elif latitud_inicial < zonas_cercanas[1]['coordenadas'][0] and longitud_inicial > zonas_cercanas[1]['coordenadas'][1]:
                        print ('Para llegar a la zona wifi dirigirse primero al norte y luego hacia el occidente')
                    elif latitud_inicial > zonas_cercanas[1]['coordenadas'][0] and longitud_inicial < zonas_cercanas[1]['coordenadas'][1]:
                        print ('Para llegar a la zona wifi dirigirse primero al sur y luego hacia el oriente')
                    elif latitud_inicial > zonas_cercanas[1]['coordenadas'][0] and longitud_inicial > zonas_cercanas[1]['coordenadas'][1]:
                        print ('Para llegar a la zona wifi dirigirse primero al sur y luego hacia el occidente')
                        
                elif abs(zonas_cercanas[1]['coordenadas'][0]-latitud_inicial) > abs(zonas_cercanas[1]['coordenadas'][1] -longitud_inicial):
                    print(abs(zonas_cercanas[1]['coordenadas'][0]-latitud_inicial), abs(zonas_cercanas[1]['coordenadas'][1] -longitud_inicial))
                    
                    if longitud_inicial < zonas_cercanas[1]['coordenadas'][1] and latitud_inicial < zonas_cercanas[1]['coordenadas'][0]:
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                    elif longitud_inicial < zonas_cercanas[1]['coordenadas'][1] and latitud_inicial > zonas_cercanas[1]['coordenadas'][0]:
                        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el sur")
                    elif longitud_inicial > zonas_cercanas[1]['coordenadas'][1] and latitud_inicial < zonas_cercanas[1]['coordenadas'][0]:
                        print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte") 
                    elif longitud_inicial > zonas_cercanas[1]['coordenadas'][1] and latitud_inicial > zonas_cercanas[1]['coordenadas'][0]:
                        print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el sur")       
                
                # print(zonas_cercanas[1]['distancia'])
                # print(type(zonas_cercanas[1]['distancia']))
                # print(prom_moto)
                # print(type(prom_moto))
                tiempo_promedio_moto =  (zonas_cercanas[1]['distancia'])/prom_moto
                tiempo_promedio_pie = (zonas_cercanas[1]['distancia'])/prom_pie
                print(f'Tiempo promedio en moto: {tiempo_promedio_moto} minutos')
                print(f'Tiempo promedio a pie: {tiempo_promedio_pie} minutos')
                input('Presione 0 para salir: ')  
    
def cambiar_contraseña():
    global contraseña
    contraseña_entrada = input('Ingrese contraseña actual: ')
    if contraseña_entrada != contraseña:
        print('Error')
        exit()
    elif contraseña_entrada == contraseña:
       newpassword = input('Nueva contraseñá: ')
       
    if newpassword == contraseña:
        print('Error')
    else:
        contraseña = newpassword
        print(contraseña)
        return contraseña
    
def ingresar_coordenadas():
    global coordenadas
    
    try:
        
        #Trabajo
        coordenadas[0][0] = float(input('Ingrese latitud para trabajo: '))
        if coordenadas[0][0] > latitud_maxima or coordenadas[0][0]<latitud_minima:
            print('Error coordenada')
            exit()
        else:
            pass
        
        coordenadas[0][1] = float(input('Ingrese longitud para Trabajo: '))
        if coordenadas[0][1] < longitud_minima or coordenadas[0][1] > longitud_maxima:
            print('Error coordenada')
            exit()
        else:
            
        #Casa
        
         coordenadas[1][0] = float(input('Ingrese latitud para Casa: '))
        if coordenadas[1][0] > latitud_maxima or coordenadas[1][0]<latitud_minima:
            print('Error coordenada')
            exit()
        else:
            pass
        
        coordenadas[1][1] = float(input('Ingrese longitud para Casa: '))
        if coordenadas[1][1] < longitud_minima or coordenadas[1][1] > longitud_maxima:
            print('Error coordenada')
            exit()
        else:
        
        #Parque
         coordenadas[2][0] = float(input('Ingrese latitud para Parque: '))
        if coordenadas[2][0] > latitud_maxima or coordenadas[2][0]<latitud_minima:
            print('Error coordenada')
            exit()
        else:
            pass
        
        coordenadas[2][1] = float(input('Ingrese longitud para Parque: '))
        if coordenadas[2][1] < longitud_minima or coordenadas[2][1] > longitud_maxima:
            print('Error coordenada')
            exit()
        else:
                
            pass
        
        
    except ValueError:
        print('Error')
        exit()


def actualizar_coordenadas():
    
    global coordenadas
    
    
    
    latitud_mas_al_sur =  coordenadas[0][0]
    posicion_mas_al_sur =  0
    longitud_mas_al_oriente = coordenadas[0][1]
    posicion_mas_al_oriente = 0 
    
    try:
    
        for posicion, latlong in enumerate(coordenadas):
            if latitud_mas_al_sur > latlong[0]:
                posicion_mas_al_sur = posicion
                latitud_mas_al_sur = latlong[0]
            else:
                pass
            
            if longitud_mas_al_oriente < latlong[1]:
                posicion_mas_al_oriente = posicion
                longitud_mas_al_oriente = latlong[1]
            else: 
                pass
            
            
        print(f"Coordenada [latitud, longitud] 1: ['{coordenadas[0][0]}','{coordenadas[0][1]}']")
        print(f"Coordenada [latitud, longitud] 1: ['{coordenadas[1][0]}','{coordenadas[1][1]}']")    
        print(f"Coordenada [latitud, longitud] 1: ['{coordenadas[2][0]}','{coordenadas[2][1]}']")
        print(f'La coordenada {posicion_mas_al_sur + 1} es la que está más al sur')
        print(f'La coordenada {posicion_mas_al_oriente+1} es la que está más al oriente')
        posicion_a_cambiar = int(input('Presione 1,2 o 3 para actualizar la respectiva coordenadas\npresione 0 para regresar al menu\n'))
        if posicion_a_cambiar not in [0,1,2,3]:
            print('Error actualización')
            exit()
        elif posicion_a_cambiar != 0:
            posicion_final = int(posicion_a_cambiar-1)
            latitud = float(input('ingrese latitud: '))
            if latitud > latitud_maxima or latitud<latitud_minima:
                print('Error coordenada')
                exit()
            else:
                coordenadas[posicion_final][0] = latitud
                
            longitud = float(input('Ingrese longitud: '))
            if longitud < longitud_minima or longitud > longitud_maxima:
                print('Error coordenada')
                exit()
            else:
                coordenadas[posicion_final][1] = longitud
                
                
    except ValueError:
        print('Error')
        exit()

def guardar_archivo():
    global zonas_cercanas
    try:
        if zonas_cercanas[0]['distancia'] < zonas_cercanas[1] ['distancia']:
            mas_cerca = zonas_cercanas[0]['distancia']
        elif zonas_cercanas[0]['distancia'] > zonas_cercanas[1] ['distancia']:
            mas_cerca = zonas_cercanas[1]['distancia']
    except KeyError:
            pass
    #wifi 1 
    try:
        tiempo_promedio_moto1 =  (zonas_cercanas[0]['distancia'])/ prom_moto
        tiempo_promedio_pie1 = (zonas_cercanas[0]['distancia'])/ prom_pie  
        if tiempo_promedio_moto1 < tiempo_promedio_pie1:
            mas_rapido1 = 'moto'
        elif tiempo_promedio_moto1 > tiempo_promedio_pie1:
            mas_rapido1 ='pie'
            
            
        #Wifi2
        tiempo_promedio_moto2 =  (zonas_cercanas[1]['distancia'])/ prom_moto
        tiempo_promedio_pie2 = (zonas_cercanas[1]['distancia'])/ prom_pie  
        if tiempo_promedio_moto2 < tiempo_promedio_pie1:
            mas_rapido2 = 'moto'
        elif tiempo_promedio_moto2 > tiempo_promedio_pie1:
            mas_rapido2 ='pie'
    
    except KeyError:
        pass
    
    if coordenadas[0][0] == 0 or latitud_inicial  == [0.00000,0.00000] or longitud_inicial == [0.000,0.00000]:
        print('Error de alistamiento')
        exit()
    else:
        try:
            
            if zonas_cercanas[0]['distancia'] < zonas_cercanas[1] ['distancia']:
                informacion ={
                    'actal':[latitud_inicial,longitud_inicial],
                    'zonawifi1':[(zonas_cercanas[0]['coordenadas'][0]),(zonas_cercanas[0]['coordenadas'][1]),(zonas_cercanas[0]['usuarios'])],
                    'recorrido':[mas_cerca,mas_rapido1,tiempo_promedio_moto1],
                    }
            elif zonas_cercanas[0]['distancia'] > zonas_cercanas[1] ['distancia']:
                 informacion ={
                    'actal':[latitud_inicial,longitud_inicial],
                    'zonawifi1':[(zonas_cercanas[1]['coordenadas'][0]),(zonas_cercanas[1]['coordenadas'][1]),(zonas_cercanas[1]['usuarios'])],
                    'recorrido':[mas_cerca,mas_rapido2,tiempo_promedio_moto2],
                    }
                
        except KeyError:
            print('Error de alistamiento')
            exit()
        
        print(informacion)
        exportar = input('¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal ')
        if exportar == '1':
            print('Exportando archivo')
            nuevo = open("archivo.txt","w")
            nuevo.write(f"{informacion}")
            nuevo.close
            exit()
        elif exportar =='2':
            pass
   
def actualizar():
    ncordenadas = open('ncordenadas.txt')
    leer = ncordenadas.readline()
    
    n2cordenadas = eval(leer)
    
    final = input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal')
    if final == '0':
        pass
#Credenciales

nombre_de_usuario = str (51595)
contraseña = str (59515)

ingresoNombre = input ('')
bandera = False

if  nombre_de_usuario  == ingresoNombre:
    pass
else:
    print ('Error')
    exit() 
    
ingresoContraseña = input ('')

if  contraseña == ingresoContraseña:
    pass
else:
    print ('Error')
    exit()

sum1 = int(595)
sum2 =int ( 5*1+5+5-5-1)

print(sum1,'+', sum2)

resultado_suma = int(input())

if resultado_suma == sum1 + sum2:
    print ('Sesión iniciada')
else:
    print ('Error')
    
menu = ['Cambiar contraseña',
        'Ingresar coordenadas actuales',
        'Ubicar zona wifi más cercana',
        'Guardar archivo con ubicación cercana',
        'Actualizar registros de zonas wifi desde archivo',
        'Elegir opción de menú favorita',
        'Cerrar sesión']

opciones_validas = ['1','2','3','4','5','6','7']
acciones = ['']
salida = 1
while True:
    for i, opcion in enumerate(menu):
            print(f'{i+1} {opcion}')
    
    while True:
        
        salida+=1
        opcion_usuario=input('Elija una opción: ')
        
        if opcion_usuario not in opciones_validas:
            if salida < 3:
                if salida == 2:
                    print('Error')
                elif salida < 4:
                    pass
            elif salida == 5:
                exit()
        else:
            break
        
        if opcion_usuario > '0' and opcion_usuario < '8':
            break
      
    if opcion_usuario > '0' and opcion_usuario < '6':
        if opcion_usuario == '1':
            cambiar_contraseña()
        elif opcion_usuario == '2':
            if coordenadas[0][0] == 0:
                ingresar_coordenadas()
            else: 
                actualizar_coordenadas()
        elif opcion_usuario == '3':
            ubicar_zona_wifi()
        elif opcion_usuario =='4':
            guardar_archivo()
        elif opcion_usuario =='5':
            actualizar()
        elif opcion_usuario in acciones:
            print(f'Usted ha elegido la opción {opcion_usuario}')
            exit()
    elif opcion_usuario == '7':
        print ('Hasta pronto')
        exit()
    elif opcion_usuario == '6':
        comfirmacion =input('Selecciona la opción favorita: ')
        if comfirmacion < '6' and comfirmacion > '0':
            adivina1 = input('Para confirmar por favor responda: ¿Si tienes 10 manzanas y te comes una cuantas te quedan?: ')
            if adivina1 == '9':
                adivina2 =input('Para confirmar por favor responda:¿Cuantos dedos tienes en tu mano?: ')
                bandera = True
                if adivina2 == '5':
                    pass
                    bandera = True
                else:
                   pass
                   print('Error')
                   salida = 1
                   bandera = False
                   
                   
    
            else:
                print('Error')
                pass
                salida = 1
                bandera = False
                
                
        else:
            print('Error')
            exit()

    if bandera == True:
        eliminado = menu.pop(int(comfirmacion) - 1)
        menu.insert(0, eliminado)
        salida = 1
        os.system("cls")
    else:
        pass
            

        
        



5
