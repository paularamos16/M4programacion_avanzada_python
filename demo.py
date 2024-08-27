from anuncio import Anuncio, Video, Display, Social
from campana import Campana
from error import LargoExcedidoException, SubTipoInvalidoException
# se agrega fecha y hora para el error.log
import time
fecha_actual = time.strftime('%d-%m-%Y') 
hora_actual = time.strftime('%H:%M:%S')

# Creación de campana 
c1 = Campana('Campaña Seguidores', 2024-4-28, 2024-5-28)

# Creando un video para la campana
c1.crear_video('www.arch', 'www.click', 'outstream', 160)

print(c1) # Probando sobrescritura __str__


# Modficicación de la campana
print('\nModificando campaña:')

try:
    nuevo_nombre = input('Ingrese nuevo nombre de la campana:\n(Para test, se modificó máximo a 20 carácteres)\n> ')
    c1.nombre = nuevo_nombre
    
    nuevo_sub_tipo = input('Ingrese nuevo subtipo para video:\n> ')
    c1.anuncios[0].sub_tipo = nuevo_sub_tipo # El aunicion en la posicicón 1
    
except LargoExcedidoException as e:
    print(e.mensaje)
    with open('error.log', 'a') as log:
        log.write(f'ERROR: {e.mensaje} - Fecha: {fecha_actual} - Hora: {hora_actual}\n')

except SubTipoInvalidoException as e:
    print(e.mensaje)
    with open('error.log', 'a') as log:
        log.write(f'ERROR: {e.mensaje} - Fecha: {fecha_actual} - Hora: {hora_actual}\n')

print('\nConfirmación:')
print(f'Nombre campana: {c1.nombre}')
print(f'Subtipo: {c1.anuncios[0].sub_tipo}')