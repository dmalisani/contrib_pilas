import pilas
from pilas.actores.ventilador  import Ventilador
pilas.iniciar()

v=Ventilador()
v.apagar()
p=pilas.actores.Pelota()
ps = p * 3
ps.aprender(pilas.habilidades.Arrastrable)
v.encender()
v.afectar_a(ps,pilas.escena_actual())
v.velocidad_viento=50
v.aprender(pilas.habilidades.Arrastrable)
#v.rotar=150
pilas.ejecutar()



