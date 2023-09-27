import time
from queue import Queue

class MusicPlaylist:
    def __init__(self):
        self.queue = Queue()

    def agregar_cancion(self, cancion, duracion):
        self.queue.put((cancion, duracion))
        print(f'Se ha agregado la canción: {cancion}')

    def reproducir_siguiente(self):
        if not self.queue.empty():
            cancion, duracion = self.queue.get()
            print(f'Reproduciendo: {cancion} por {duracion} minutos')
            time.sleep(duracion * 60)  # Duración en minutos convertida a segundos
        else:
            print('La playlist está vacía. Agrega canciones primero.')

    def mostrar_playlist(self):
        if not self.queue.empty():
            print('Playlist actual:')
            for i, (cancion, duracion) in enumerate(list(self.queue.queue), start=1):
                print(f'Canción {i}: {cancion}, Duración: {duracion} minutos')
        else:
            print('La playlist está vacía.')

if __name__ == '__main__':
    mi_playlist = MusicPlaylist()

    mi_playlist.agregar_cancion('Bohemian Rhapsody', 6.07)
    mi_playlist.agregar_cancion('Hotel California', 6.30)
    mi_playlist.agregar_cancion('Stairway to Heaven', 8.02)
    mi_playlist.agregar_cancion('Sweet Child o\' Mine', 5.55)

    mi_playlist.mostrar_playlist()
    print()

    mi_playlist.reproducir_siguiente()
    mi_playlist.reproducir_siguiente()
    mi_playlist.reproducir_siguiente()
    mi_playlist.reproducir_siguiente()
