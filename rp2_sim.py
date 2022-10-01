def asm_pio(*args, **kwargs):
    #Función principal que toma los parametros
    def decorador(programa):
        #Decorador de asm_pio con parametro programa
        def compilador():
            #Muestra los parametros en el programa y lo ejecuta
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador

def decorador_instr(fun_inst):
    #Define decorador_instr con fun_inst
    def decoracion_instr(self,*args, **kwargs):
        #Asigna los atributos ya definidos a fun_inst 
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

pins='pins'

class PIO():
    OUT_LOW='PIO.OUT_LOW'
    

class StateMachine:
  def __init__(self, id_, program, freq=125000000, **kwargs):
      #Inicializa los atributos globales, crea una lista con las instrucciones, ejecuta el programa, muestra la cantidad de instrucciones leidas y asigna un id (maquina de estado) a fsms, con la frecuencia definida.
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass
      
        
  def active(self, x=None):
      #Detecta si se esta haciendo uso de la RP2 en el momento para realizar la simulación.
    '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    if x==1:
        print('Está pendiente de realizar la simulacón')

fsms=[None]*8

sm_iniciandose=None    


class nop:
    @decorador_instr
    def __init__(self,*args, **kwargs):
        #Inicia la clase sm_iniciandose, muestra el nombre de la clase en ejecución y lo agrega a una lista.
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
     
    def __getitem__(self,name):
        #Obtiene los parametros para la clase nop
        #print('nop.__getattr__',name)
        pass
        
class set(nop):
    def __init__(self,*args, **kwargs):
        #Inicializa los atributos para la clase nop
        super().__init__(*args, **kwargs)
        pass
   
class wrap_target(nop):
    def __init__(self,*args, **kwargs):
        #Inicializa los atributos para la clase wrap_target
         super().__init__(*args, **kwargs)
         pass 
  
class wrap(nop):
    def __init__(self,*args, **kwargs):
        #Inicializa los atributos para la clase wrap
         super().__init__(*args, **kwargs)
         pass 
         
         
