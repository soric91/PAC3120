from libreriaPAC import *
import time
import serial.tools.list_ports
import math


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

# asiganacion de direcion de memoria segun los datos a pedir del PAC3120
POTENCIA_ACTIVA_L1_L2_L3 = (25, 27, 29)
POTENCIA_APARENTE_L1_L2_L3 = (19, 21, 23)
POTENCIA_REACTIVA_L1_L2_L3 = (31, 33, 35)
FACTOR_DE_POTENCIA_L1_L2_L3 = (37, 39, 41)
POTENCIA_TRIFACICA_V = (1, 3, 5) # L1, L2, L3
POTENCIA_TRIFACICA_I = (13, 15, 17) # A1, A2, A3

ALL_REGISTER_PAC3120 = (63, 65, 67, 19, 25, 31, 37, 1, 13, 55, 21, 27, 33, 29, 35, 41, 5, 17, 55)

#REGISTROS HUAWEI
POTENCIA_ACTIVA_HUAWEI = 32080
leer_pac = []
# tiempo_inicio = time.time()
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
        
        leer_pac[j].read_list(POTENCIA_TRIFACICA_V)
        for i, PTT in enumerate(results_pac[:(len(POTENCIA_TRIFACICA_V))]):
            voltaje =+ results_pac[i]
        
        leer_pac[j].read_list(POTENCIA_TRIFACICA_I)
        for i, PTT in enumerate(results_pac[:(len(POTENCIA_TRIFACICA_I))]):
            amperios =+ results_pac[i]        
        
        PotenciaTT = math.sqrt(3) * voltaje/3 * amperios/3
        print(f'Potencia Trifacica total: {PotenciaTT} W')
    time.sleep(1)
 


