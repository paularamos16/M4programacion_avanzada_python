from abc import ABC, abstractmethod
from error import SubTipoInvalidoException

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        if ancho < 0:
            self.__ancho = ancho
        else:
            self.__ancho = 1
        self.__alto = alto if alto < 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def _ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if isinstance(self, Video):
            if sub_tipo in Video.SUB_TIPOS:
                self.__sub_tipo = sub_tipo
            else:
                raise SubTipoInvalidoException(f'Formato "{sub_tipo}", no está permitido para video.')
        elif isinstance(self, Display):
            if sub_tipo is not Display.SUB_TIPOS:
                raise SubTipoInvalidoException(f'Formato "{sub_tipo}", no está permitido para Display.')
            else:
                self.__sub_tipo = sub_tipo
        elif isinstance(self, Social):
            if sub_tipo is not Social.SUB_TIPOS:
                raise SubTipoInvalidoException(f'Formato "{sub_tipo}", no está permitido para Social.')
            else:
                self.__sub_tipo = sub_tipo
        else:
            raise SubTipoInvalidoException(f'campana no tiene anuncios.')

    @staticmethod
    def mostrar_formatos():
        clases_existentes = [Video, Social, Display] # Clases actuales
        for clase in clases_existentes:
            print(f'''
{clase.formato.upper()} {clases_existentes.index(clase) + 1}
==========''')
            for tipo in clase.SUB_TIPOS:
                print(f'- {tipo}')

    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self):
        pass




class Video(Anuncio):
    formato = 'Video'
    SUB_TIPOS = ('instream', 'outstream')
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        ancho_fijo = 1
        alto_fijo = 1
        super().__init__(ancho_fijo, alto_fijo, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5

    def comprimir_anuncio(self):
        return print('COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN')
    
    def redimensionar_anuncio(self):
        return print('RECORTE DE VIDEO NO IMPLEMENTADO AÚN')





class Display(Anuncio):
    formato = 'Display'
    SUB_TIPOS = ('tradicional', 'native')
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        return print ('COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN')

    def redimensionar_anuncio(self):
        return print ('REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN')





class Social(Anuncio):
    formato = 'Social'
    SUB_TIPOS = ('facebook', 'linkedin')
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio(self):
        return print('COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN')
    
    def redimensionar_anuncio(self):
        return print('REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN')



if __name__ == '__main__':
    # Método estático para mostrar formatos:
    Anuncio.mostrar_formatos() # ok, mostrando
    
    # Prueba instancia video:
    video = Video('www.arhivo', 'www.click', 'vhs', 120) # ok
    
    # Prueba si es instancia de video
    print(isinstance(video, Video)) # ok, True
    
    # Prueba setter de formato correcto
    print(video.sub_tipo) # vhs
    video.sub_tipo = 'outstream' # Uso setter con sub_tipo correcto
    print(video.sub_tipo) # oustream
    
    # Prueba setter de formato erroneo
    video.sub_tipo = 'ligero' # ok : error.SubTipoInvalidoException: Formato "ligero", no está permitido para video.