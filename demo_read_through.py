import time

# Simulación de la base de datos
class Database:

    def __init__(self):
        self.users = {
            1: {"nombre": "Juan", "edad": 20},
            2: {"nombre": "Carlos", "edad": 25},
            3: {"nombre": "Maria", "edad": 22}
        }

    def get_user(self, user_id):
        print(f"   [BASE DE DATOS] Consultando usuario {user_id}...")

        time.sleep(2)  # Simula el tiempo de consulta

        return self.users.get(user_id)


# Caché con patrón Read-Through
class ReadThroughCache:

    def __init__(self, database):
        self.database = database
        self.cache = {}

    def get(self, user_id):

        # Verificar si el dato está en caché
        if user_id in self.cache:
            print("[CACHE HIT] Dato encontrado en caché")
            return self.cache[user_id]

        # Si no existe, la caché consulta la BD
        print("[CACHE MISS] Dato no encontrado")

        data = self.database.get_user(user_id)

        if data is not None:
            # Guardar automáticamente en caché
            self.cache[user_id] = data
            print("[CACHE] Dato almacenado correctamente")

        return data


# Aplicación
class Application:

    def __init__(self, cache):
        self.cache = cache

    def show_user(self, user_id):
        print(f"\nSolicitando usuario {user_id}...")

        user = self.cache.get(user_id)

        if user:
            print(f"Usuario recibido: {user}")
        else:
            print("Usuario no encontrado")


# Ejecución de la demostración
database = Database()
cache = ReadThroughCache(database)
app = Application(cache)

# Primera consulta: Cache Miss
app.show_user(1)

# Segunda consulta: Cache Hit
app.show_user(1)

# Tercera consulta: Cache Miss
app.show_user(2)

# Cuarta consulta: Cache Hit
app.show_user(2)
