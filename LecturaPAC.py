from libreriaPAC import *
import time
import serial.tools.list_ports


puertos_pac=list(serial.tools.list_ports.comports())
if len(puertos_pac)==0:
	print("NO se encontró ningun puerto serial")
	exit()



FUNCTION_CODE_READ     =   4
# se le asiganan los id del esclavos en la posicion del equipo a leer
SLAVE_ADDRESS_PAC =  [1,2,3] 
print(puertos_pac[0].device)
# se le asiganan los puerto a posicion del equipo a leer
PORT                   =   [puertos_pac[0].device, puertos_pac[0].device, puertos_pac[0].device]  #'/dev/ttyAMA0'
MODE                   =   'rtu'
VELOCITY               =   9600
BYTE_SIZE              =   8
STOP_BIT               =   1
TIMEOUT                =   0.5

#REGISTROS LibreriaPAC3120
TENSION_L1             =  1
TENSION_L2		  	   =  3
TENSION_L3             =  5
CORRIENTE_L1           =  13
CORRIENTE_L2           =  15
CORRIENTE_L3           =  17
POTENCIA_APARENTE_L1   =  19
POTENCIA_APARENTE_L2   =  21
POTENCIA_APARENTE_L3   =  23
POTENCIA_ACTIVA_L1     =  25
POTENCIA_ACTIVA_L2     =  27
POTENCIA_ACTIVA_L3     =  29
POTENCIA_REACTIVA_L1   =  31
POTENCIA_REACTIVA_L2   =  33
POTENCIA_REACTIVA_L3   =  35
FACTOR_DE_POTENCIA_L1  =  37
FACTOR_DE_POTENCIA_L2  =  39
FACTOR_DE_POTENCIA_L3  =  41


POTENCIA_ACTIVA_L1_L2_L3 = (25, 27, 29)
POTENCIA_APARENTE_L1_L2_L3 = (19, 21, 23)
POTENCIA_REACTIVA_L1_L2_L3 = (31, 33, 35)
FACTOR_DE_POTENCIA_L1_L2_L3 = (37, 39, 41)

ALL_REGISTER_PAC3120 = (63, 65, 67, 19, 25, 31, 37, 1, 13, 55, 21, 27, 33, 29, 35, 41, 5, 17, 55)

#REGISTROS HUAWEI
POTENCIA_ACTIVA_HUAWEI = 32080
leer_pac = []
tiempo_inicio = time.time()
for i in range(3):
    leer_pac.append(PAC3120(SLAVE_ADDRESS_PAC[i], FUNCTION_CODE_READ, PORT[i], MODE, VELOCITY, BYTE_SIZE, STOP_BIT, TIMEOUT))

#leer.port_on()

# inicio la conecion con el PAC3120
for i in range(3):
    leer_pac[i].init_pac()


while True:  
    for j, obj_pac in enumerate(leer_pac):   
        print(f'Registros de potencia activa, reactiva y factor de potencia del PAC3120 {j+1}:')
        print('Potencia Activa de L1, L2 y L3')
        leer_pac[j].read_list(POTENCIA_ACTIVA_L1_L2_L3)        
        for i , PA in enumerate(Registros_pac3120[:len(POTENCIA_ACTIVA_L1_L2_L3)]):                   
           print(f"Potencia Activa de  L{i+1}: {PA/1000} kW")
        
        print('Potencia Reactiva de L1, L2 y L3')
        leer_pac[j].read_list(POTENCIA_REACTIVA_L1_L2_L3)        
        for i, PR in enumerate(Registros_pac3120[:len(POTENCIA_REACTIVA_L1_L2_L3)]):                   
            print(f"Potencia Activa de  L{i+1}: {PR/1000} kvar")
            
        print('Factores de Potencia de L1, L2 y L3')
        leer_pac[j].read_list(FACTOR_DE_POTENCIA_L1_L2_L3)        
        for i, FP in enumerate(Registros_pac3120[:len(FACTOR_DE_POTENCIA_L1_L2_L3)]):                   
           print(f"Factores de Potencia de L{i+1}: {FP}") 
           
        print('Potencia Aparente de L1, L2, L3')
        leer_pac[j].read_list(POTENCIA_APARENTE_L1_L2_L3)
        for i, FP in enumerate(results_pac[:len(POTENCIA_APARENTE_L1_L2_L3)]):
            print(f'Potencia Aparente de L{i+1}')
        
        tiempo_final = time.time()
        Tiempo_Codigo = tiempo_final-tiempo_inicio
        print(Tiempo_Codigo)                 
        time.sleep(1)

# leer.find_pac(TENSION_L1)
# leer.find_pac(TENSION_L2)
# leer.find_pac(TENSION_L3)
# leer.find_pac(CORRIENTE_L1)
# leer.find_pac(CORRIENTE_L2)
# leer.find_pac(CORRIENTE_L3)
# leer.find_pac(POTENCIA_APARENTE_L1)
# leer.find_pac(POTENCIA_APARENTE_L2)
# leer.find_pac(POTENCIA_APARENTE_L3)
# leer.find_pac(POTENCIA_ACTIVA_L1)
# leer.find_pac(POTENCIA_ACTIVA_L2)
# leer.find_pac(POTENCIA_ACTIVA_L3)
# leer.find_pac(FACTOR_DE_POTENCIA_L1)
# leer.find_pac(FACTOR_DE_POTENCIA_L2)
#leer.find_pac(FACTOR_DE_POTENCIA_L3)
# print(results)  


 


