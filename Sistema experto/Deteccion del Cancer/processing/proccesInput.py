from pyDatalog import pyDatalog
from database import data_base_cancer as database

pyDatalog.create_terms('X,Y,Z,sintoma,cancer,tratamiento,revision,tipoCancer')

database.cancer(X,Y)
database.sintoma(X,Y)
database.tratamiento(X,Y)
database.revision(X,Y)

tipoCancer(X,Y) <= sintoma(Y,Z) & cancer(Z,X)

def dataToString(variable):
    return ''.join(ch for ch in str(variable.data) if ch.isalnum() or ch == ' ' or ch == '_')

def makeGuess(value,Y):
    if(value == 'preciso'):
        x = tipoCancer(X,Y)
        y = sintoma(Y,X)
        if(dataToString(x) != '' and dataToString(y) != ''):
            resultset = """
            <p style="text-align: center;"><span style="color: #000000;"><strong>Resultado del Analisis</strong></span></p>
            <p style="text-align: left;"><span style="color: #000000;">Usted tiene alta provabilidad de tener {0}, es un tipo de cancer {1} y se debe tratar con: </span></p>
            <table style="border-color: black; margin-left: auto; margin-right: auto;" border="black">
            <tbody>
            <tr>
            <td><span style="color: #000000;">&nbsp;{2}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{3}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{4}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{5}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{6}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{7}</span></td>
            </tr>
            </tbody>
            </table>
            """
            table = dataToString(tratamiento(dataToString(y),X)).split(" ")
            i = len(table)
            while(i < 6):
                table.insert(i,"")
                i = i + 1
            return resultset.format(dataToString(y), dataToString(x), table[0], table[1], table[2], table[3], table[4], table[5])
        else:
            resultset = """
            <p style="text-align: center;"><span style="color: #000000;"><strong>Resultado del Analisis</strong></span></p>
            <p style="text-align: left;"><span style="color: #000000;">Usted tiene alta provabilidad de tener cancer cerebral, no obstante sus sintomas no determinan un tumor en espesifico, por lo tanto se recomienda hacer los siguientes examenes:</span></p>
            <table style="border-color: black; margin-left: auto; margin-right: auto;" border="black">
            <tbody>
            <tr>
            <td><span style="color: #000000;">&nbsp;{0}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{1}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{2}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{3}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{4}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{5}</span></td>
            </tr>
            </tbody>
            </table>
            """
            table = dataToString(revision('Metastasico',X)).split(" ")
            i = len(table)
            while(i < 6):
                table.insert(i,"")
                i = i + 1
            return resultset.format(table[0], table[1], table[2], table[3], table[4], table[5])
    elif(value == 'probable'):
        x = tipoCancer(X,Y)
        y = sintoma(Y,X)
        if(dataToString(x) != '' and dataToString(y) != ''):
            resultset = """
            <p style="text-align: center;"><span style="color: #000000;"><strong>Resultado del Analisis</strong></span></p>
            <p style="text-align: left;"><span style="color: #000000;">Es probable que usted tenga {0}, es un tipo de cancer {1} y se debe tratar con: </span></p>
            <table style="border-color: black; margin-left: auto; margin-right: auto;" border="black">
            <tbody>
            <tr>
            <td><span style="color: #000000;">&nbsp;{2}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{3}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{4}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{5}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{6}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{7}</span></td>
            </tr>
            </tbody>
            </table>
            """
            table = dataToString(tratamiento(dataToString(y),X)).split(" ")
            i = len(table)
            while(i < 6):
                table.insert(i,"")
                i = i + 1
            return resultset.format(dataToString(y), dataToString(x), table[0], table[1], table[2], table[3], table[4], table[5])
        else:
            resultset = """
            <p style="text-align: center;"><span style="color: #000000;"><strong>Resultado del Analisis</strong></span></p>
            <p style="text-align: left;"><span style="color: #000000;">Es probable que usted tenga cancer cerebral, no obstante el diagnostico no puede concretar un tumor en especifico es por eso que se recomienda cualquiera de los siguientes examenes: </span></p>
            <table style="border-color: black; margin-left: auto; margin-right: auto;" border="black">
            <tbody>
            <tr>
            <td><span style="color: #000000;">&nbsp;{0}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{1}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{2}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{3}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{4}</span></td>
            </tr>
            <tr>
            <td><span style="color: #000000;">&nbsp;{5}</span></td>
            </tr>
            </tbody>
            </table>
            """
            table = dataToString(revision('Metastasico',X)).split(" ")
            i = len(table)
            while(i < 6):
                table.insert(i,"")
                i = i + 1
            return resultset.format(table[0], table[1], table[2], table[3], table[4], table[5])
    elif(value == 'improbable'):
        resultset = """
            <p style="text-align: center;"><span style="color: #000000;"><strong>Resultado del Analisis</strong></span></p>
            <p style="text-align: left;"><span style="color: #000000;">La probabilidad de tener cancer es bastante baja, pero se recomienda estar alerta.</span></p>
            """
        return resultset

            
            
            
            
            