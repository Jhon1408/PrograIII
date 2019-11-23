from processing import proccesInput

class pacienteInput():
    def __init__(self):
        #Personal
        self.sexo = ''
        self.edad = 0
        #Enfermedades previas
        self.CMama = False
        self.CRinon = False
        self.CPulmon = False
        self.CColon = False
        #Sintomas
        self.Memoria = ''
        self.Nauseas = ''
        self.Vision = ''
        self.Vomito = ''
        self.Comportamiento = ''
        self.Convulsiones = ''
        self.Debilidad = ''
        self.Dolor_cabeza = ''
        self.Movimiento = ''
        #Cancer en familiares
        self.Abuelos = False
        self.Tios = False
        self.Padres = False
        #Extras
        self.Radiacion = False
        self.Estres = False
        self.Golpes = False
        self.Medicacion = False
        #Contadores
        self.cantSintomas = 0
        self.probabilidad = 0
        
    def insertPersonal(self, sexoIn, edadIn):
        self.sexo = str(sexoIn)
        self.edad = int(edadIn)
        
    def insertCancer(self, mama, rinon, pulmon, colon):
        if(mama == True):
            self.CMama = True
        if(rinon == True):
            self.CRinon = True
        if(pulmon == True):
            self.CPulmon = True
        if(colon == True):
            self.CColon = True
            
    def insertSintomas(self, memoria, nauseas, vision, vomito, comportamiento, convulsiones, debilidad, dolor_cabeza, movimiento):
        if(memoria == True):
            self.Memoria = 'Perdida de la memoria'
            self.cantSintomas = self.cantSintomas + 1
        if(nauseas == True):
            self.Nauseas = 'Nauseas'
            self.cantSintomas = self.cantSintomas + 1
        if(vision == True):
            self.Vision = 'Problemas de vision'
            self.cantSintomas = self.cantSintomas + 1
        if(vomito == True):
            self.Vomito = 'Vomitos'
            self.cantSintomas = self.cantSintomas + 1
        if(comportamiento == True):
            self.Comportamiento = 'Cambios de comportamiento'
            self.cantSintomas = self.cantSintomas + 1
        if(convulsiones == True):
            self.Convulsiones = 'Convulsiones'
            self.cantSintomas = self.cantSintomas + 1
        if(debilidad == True):
            self.Debilidad = 'Debilidad'
            self.cantSintomas = self.cantSintomas + 1
        if(dolor_cabeza == True):
            self.Dolor_cabeza = 'Dolor de cabeza'
            self.cantSintomas = self.cantSintomas + 1
        if(movimiento == True):
            self.Movimiento = 'Dificultad de movimiento'
            self.cantSintomas = self.cantSintomas + 1
            
    def insertFamiliares(self, abuelos, tios, padres):
        if(abuelos == True):
            self.Abuelos = True
        if(tios == True):
            self.Tios = True
        if(padres == True):
            self.Padres = True
    
    def insertExtra(self, radiacion, estres, golpes, medicacion):
        if(radiacion == True):
            self.Abuelos = True
        if(estres == True):
            self.Tios = True
        if(golpes == True):
            self.Padres = True
        if(medicacion == True):
            self.Abuelos = True
    
    def mostrarResultado(self):
        dataSheet = ()
        value = 'improbable'
        if(self.cantSintomas > 3):
            if(self.CMama == True or self.CColon == True or self.CRinon == True or self.CPulmon == True):
                #Metastasico con sintomas severos y alta provabilidad de tener cancer cerebral
                value = 'preciso'
            elif(self.Abuelos == True or self.Padres == True):
                #Posible tumor con sintomas, debe de ser verificado
                value = 'preciso'
            elif(self.Radiacion == True or self.Estres == True or self.Golpes == True or self.Medicacion == True):
                #Posible tumor con sintomas, debe de ser verificado
                value = 'preciso'
            elif(self.edad < 9 and self.sexo == 'masculino'):
                #Posible tumor en niño menor, debe ser verificado
                value = 'preciso'
            elif(self.edad < 7 and self.sexo == 'femenino'):
                #Posible tumor en niña menor, debe de ser verificado
                value = 'preciso'
            else:
                value = 'probable'
        elif(self.cantSintomas == 3):
            if(self.Abuelos == True or self.Padres == True):
                if(self.Nauseas != '' and self.Vomito != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Nauseas,self.Vomito,self.Dolor_cabeza)
                    value = 'preciso'
                elif(self.Vision != '' and self.Dolor_cabeza != '' and self.Movimiento != ''):
                    dataSheet = (self.Vision,self.Dolor_cabeza,self.Movimiento)
                    value = 'preciso'
                elif(self.Nauseas != '' and self.Vision != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Nauseas,self.Vision,self.Dolor_cabeza)
                    value = 'preciso'
                elif(self.Comportamiento != '' and self.Convulsiones != '' and self.Debilidad != ''):
                    dataSheet = (self.Comportamiento,self.Convulsiones,self.Debilidad)
                    value = 'preciso'
                else:
                    value = 'probable'
            elif(self.Radiacion == True or self.Estres == True or self.Golpes == True or self.Medicacion == True):
                if(self.Nauseas != '' and self.Vomito != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Nauseas,self.Vomito,self.Dolor_cabeza)
                    value = 'preciso'
                elif(self.Vision != '' and self.Dolor_cabeza != '' and self.Movimiento != ''):
                    dataSheet = (self.Vision,self.Dolor_cabeza,self.Movimiento)
                    value = 'preciso'
                elif(self.Nauseas != '' and self.Vision != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Nauseas,self.Vision,self.Dolor_cabeza)
                    value = 'preciso'
                elif(self.Comportamiento != '' and self.Convulsiones != '' and self.Debilidad != ''):
                    dataSheet = (self.Comportamiento,self.Convulsiones,self.Debilidad)
                    value = 'preciso'
                else:
                    value = 'probable'
            elif(self.CMama == True or self.CColon == True or self.CRinon == True or self.CPulmon == True):
                if(self.Nauseas != '' and self.Vomito != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Nauseas,self.Vomito,self.Dolor_cabeza)
                    value = 'preciso'
                elif(self.Vision != '' and self.Dolor_cabeza != '' and self.Movimiento != ''):
                    dataSheet = (self.Vision,self.Dolor_cabeza,self.Movimiento)
                    value = 'preciso'
                elif(self.Nauseas != '' and self.Vision != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Nauseas,self.Vision,self.Dolor_cabeza)
                    value = 'preciso'
                elif(self.Comportamiento != '' and self.Convulsiones != '' and self.Debilidad != ''):
                    dataSheet = (self.Comportamiento,self.Convulsiones,self.Debilidad)
                    value = 'preciso'
                else:
                    value = 'probable'
            else:
                if(self.Nauseas != '' and self.Vomito != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Nauseas,self.Vomito,self.Dolor_cabeza)
                    value = 'probable'
                elif(self.Vision != '' and self.Dolor_cabeza != '' and self.Movimiento != ''):
                    dataSheet = (self.Vision,self.Dolor_cabeza,self.Movimiento)
                    value = 'probable'
                elif(self.Nauseas != '' and self.Vision != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Nauseas,self.Vision,self.Dolor_cabeza)
                    value = 'probable'
                elif(self.Comportamiento != '' and self.Convulsiones != '' and self.Debilidad != ''):
                    dataSheet = (self.Comportamiento,self.Convulsiones,self.Debilidad)
                    value = 'probable'
                else:
                    value = 'improbable'
        elif(self.cantSintomas == 2):
            if(self.CMama == True or self.CColon == True or self.CRinon == True or self.CPulmon == True):
                if(self.Memoria != '' and self.Convulsiones != ''):
                    dataSheet = (self.Memoria, self.Convulsiones)
                    value = 'preciso'
                elif(self.Nauseas != '' and self.Vision != ''):
                    dataSheet = (self.Nauseas, self.Vision)
                    value = 'preciso'
                elif(self.Memoria != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Memoria, self.Dolor_cabeza)
                    value = 'preciso'
                else:
                    value = 'probable'
            elif(self.Abuelos == True or self.Padres == True):
                if(self.Memoria != '' and self.Convulsiones != ''):
                    dataSheet = (self.Memoria, self.Convulsiones)
                    value = 'probable'
                elif(self.Nauseas != '' and self.Vision != ''):
                    dataSheet = (self.Nauseas, self.Vision)
                    value = 'probable'
                elif(self.Memoria != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Memoria, self.Dolor_cabeza)
                    value = 'probable'
                else:
                    value = 'improbable'
            elif(self.Radiacion == True or self.Estres == True or self.Golpes == True or self.Medicacion == True):
                if(self.Memoria != '' and self.Convulsiones != ''):
                    dataSheet = (self.Memoria, self.Convulsiones)
                    value = 'probable'
                elif(self.Nauseas != '' and self.Vision != ''):
                    dataSheet = (self.Nauseas, self.Vision)
                    value = 'probable'
                elif(self.Memoria != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Memoria, self.Dolor_cabeza)
                    value = 'probable'
                else:
                    value = 'improbable'
            elif((self.Radiacion == True or self.Estres == True or self.Golpes == True) or (self.Medicacion == True) and (self.Abuelos == True or self.Padres == True)):
                if(self.Memoria != '' and self.Convulsiones != ''):
                    dataSheet = (self.Memoria, self.Convulsiones)
                    value = 'preciso'
                elif(self.Nauseas != '' and self.Vision != ''):
                    dataSheet = (self.Nauseas, self.Vision)
                    value = 'preciso'
                elif(self.Memoria != '' and self.Dolor_cabeza != ''):
                    dataSheet = (self.Memoria, self.Dolor_cabeza)
                    value = 'preciso'
                else:
                    value = 'probable'
            else:
                value = 'improbable'
        else:
            value = 'improbable'
            
        return proccesInput.makeGuess(value,dataSheet)
        

