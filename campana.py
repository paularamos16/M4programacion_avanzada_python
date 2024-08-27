from anuncio import Anuncio
from datetime import date
from error import LargoExcedidoException
import anuncio as a

class Campana:
    largo_nombre_campana = 20
    
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []
        self.__num_videos = 0
        self.__num_displays = 0
        self.__num_socials = 0

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor) > 250:
            raise LargoExcedidoException(f'Error: Superó los 250 carácteres permitidos')
        else:
            self.__nombre = valor

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def _fecha_inicio(self, valor):
        self.__fecha_inicio = valor

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def _fecha_termino(self, valor):
        self.__fecha_termino = valor

    @property
    def num_videos(self):
        return self.__num_videos

    @num_videos.setter
    def num_videos(self, valor):
        self.__num_videos = valor

    @property
    def num_displays(self):
        return self.__num_displays

    @num_displays.setter
    def num_displays(self, valor):
        self.__num_displays = valor

    @property
    def num_socials(self):
        return self.__num_socials

    @num_socials.setter
    def num_socials(self, valor):
        self.__num_socials = valor

    @property
    def anuncios(self):
        return self.__anuncios

    def crear_video(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        anuncio_video = a.Video(url_archivo, url_clic, sub_tipo, duracion)
        self.__anuncios.append(anuncio_video)
        self.num_videos += 1
    
    def crear_display(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        anuncio_display = a.Display(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.__anuncios.append(anuncio_display)
        self.num_displays += 1
        
    def crear_social(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        anuncio_social = a.Social(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.__anuncios.append(anuncio_social)
        self.__num_socials += 1

    def __str__(self):
        return f'Nombre de la campana: {self.nombre}\nAnuncios: {self.num_videos} Video, {self.num_displays} Display, {self.num_socials} Social'