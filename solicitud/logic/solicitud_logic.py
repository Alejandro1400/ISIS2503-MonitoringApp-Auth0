from ..models import Solicitud

def get_archivos():
    archivos = Solicitud.objects.all()
    return archivos

def get_archivo(archivo_pk):
    archivo = Solicitud.objects.get(nombre=archivo_pk)
    return archivo

def create_archivo(pArchivo):
    archivo = Solicitud(
        nombre = pArchivo["nombre"],
    )
    archivo.save()
    return archivo

def update_archivo(archivo_pk, new_archivo):
    archivo = get_archivo(archivo_pk)
    archivo.nombre = new_archivo["nombre"]
    archivo.save()
    return archivo

def delete_archivo(archivo_pk):
    archivo = get_archivo(archivo_pk)
    archivo.delete()
    return archivo