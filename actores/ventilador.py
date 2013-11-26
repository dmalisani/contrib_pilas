# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilas.actores import Animacion
import pilas
import math
import Box2D

class Ventilador(Animacion):

    def __init__(self, x=0, y=0):

        self.img_encendido = pilas.imagenes.cargar_grilla("ventilador_enc.png", 2)
        self.img_apagado  = pilas.imagenes.cargar_imagen("ventilador.png")
        self.encendido = True

        Animacion.__init__(self, self.img_encendido, ciclica=True, x=x, y=y)
        self.radio_de_colision = 100
        self.velocidad_viento = 50
        self.centro_x=140
        self.centro_y=70
        self.default_centro = (140,70)
        self._imagenespejada=False



    def encender(self):
        self.definir_imagen(self.img_encendido)
        self.definir_centro(self.default_centro)
        self.encendido = True

    def apagar(self):
        self.definir_imagen(self.img_apagado)
        self.definir_centro(self.default_centro)
        self.encendido = False

    def actualizar(self):
        Animacion.actualizar(self)

    def zona_viento(self,vent,objetivo):
        incidencia_viento = Box2D.b2Vec2(math.cos(math.radians(self.rotacion))  , -math.sin(math.radians(self.rotacion) ))
        opuesto = incidencia_viento * -1 * self.radio_de_colision + Box2D.b2Vec2(self.x,self.y)
        pto_contacto = Box2D.b2Vec2(objetivo.x,objetivo.y)
        dist= (opuesto -  pto_contacto).length
        vel=objetivo.figura._cuerpo.linearVelocity
        porc_dis =  100 - 100  * dist / (self.radio_de_colision *  4)
        fx=abs(dist *  self.velocidad_viento/500000  * porc_dis)
        objetivo.figura._cuerpo.linearVelocity=vel+incidencia_viento*fx

    def get_rotar(self):
        return self.rotacion
    def set_rotar(self,rotacion):
        self.rotacion=rotacion
        if rotacion>180:

            if not self._imagenespejada:
                self._imagenespejada=True
                #espejar la imagen
        else:
            if self._imagenespejada:
                #quitar espejado
                self._imagenespejada=False


    def afectar_a(self, actores, escena):
       escena.colisiones.agregar(self,actores,self.zona_viento)


    rotar= property(get_rotar,set_rotar,doc="Rota el ventilador espejando la imagen")

