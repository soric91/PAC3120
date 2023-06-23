import minimalmodbus
import numpy as npp
import serial
import io

results_pac = []
Registros_pac3120 = npp.zeros(24)

class PAC3120():
    
    # Ingresos de parametros al metedos de las variables 
    def __init__(self, s_address, f_read, port, mode, vel, b_size, s_bit, timeout):
        self.slave_address = s_address
        self.function_read = f_read
        self.port = port
        self.mode = mode
        self.velocity = vel
        self.bsize = b_size
        self.sbit = s_bit
        self.timeout = timeout
        
    # lectura de parametros con la conexion del equipo PAC3120
    def init_pac(self):
        try:
            self.instrument_pac = minimalmodbus.Instrument(self.port, self.slave_address, mode= self.mode)
            self.instrument_pac.serial.baudrate = self.velocity
            self.instrument_pac.serial.bytesize = self.bsize
            self.instrument_pac.serial.parity = minimalmodbus.serial.PARITY_NONE
            self.instrument_pac.serial.stopbits = self.sbit
            self.instrument_pac.serial.timeout = self.timeout             
        except (minimalmodbus.ModbusException, AttributeError, serial.SerialException) as e:
            print("Error al conectarse con el PAC3120", str(e))     

    # lectura de un regustro en una posicion de memeoria especifica devuelve un solo valor 
    def finc_pac(self, registeraddress):
        try:            
            Registro_pac = self.instrument_pac.read_float(registeraddress, functioncode = self.function_read)
            results_pac.append(Registro_pac)
            return Registro_pac
        except (minimalmodbus.ModbusException, AttributeError, serial.SerialException) as e:
            print("Error al leer los registros Modbus:", str(e))
        
    # lectura de todos los registros en un vector asiganos previamente y devuelve un vector con los valores resultante
    def read_list(self, registerall):        
        try:
           for i, addrs in enumerate(registerall):
              Registros_pac3120[i] = self.instrument_pac.read_float(addrs, functioncode = self.function_read)
        except (minimalmodbus.ModbusException, AttributeError, serial.SerialException) as e:
            print("Error al leer los registros Modbus:", str(e))
            
       
    
            
    
        

         