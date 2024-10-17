import random

# Definición de la clase Personaje
class Personaje:
    def __init__(self):
        self.nombre = ""
        self.jugador = ""
        self.ocupacion = ""
        self.genero = ""
        self.edad = 0
        self.lugar_residencia = ""
        self.lugar_nacimiento = ""
        self.caracteristicas = {
            "FUE": 0,
            "DES": 0,
            "POD": 0,
            "TAM": 0,
            "INT": 0,
            "Mov": 0,
            "CON": 0,
            "APA": 0,
            "EDU": 0
        }
        self.habilidades = {}  # Se rellenará más adelante
        self.armas = []
        self.trasfondo = ""
        self.equipo_posesiones = ""
        self.dinero_bienes = ""
        self.companeros_investigadores = []
        self.notas = ""

    # Función para generar las características aleatoriamente
    def generar_caracteristicas(self):
        for key in self.caracteristicas:
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            dado3 = random.randint(1, 6)
            self.caracteristicas[key] = dado1 + dado2 + dado3 * 5

        # Calcula Mov según TAM y FUE
        if self.caracteristicas["TAM"] < 65:
            self.caracteristicas["Mov"] = 8
        elif self.caracteristicas["TAM"] < 85:
            self.caracteristicas["Mov"] = 7
        else:
            self.caracteristicas["Mov"] = 6
        if self.caracteristicas["FUE"] < self.caracteristicas["TAM"]:
            self.caracteristicas["Mov"] -= 1

    # Función para inicializar las habilidades con el porcentaje base
    def inicializar_habilidades(self):
        self.habilidades = {
            "Antropología": 1,
            "Arqueología": 1,
            "Arte/Artesanía": 5,
            "Buscar libros": 20,
            "Cerrajería": 1,
            "Charlatanería": 5,
            "Ciencia": 1,
            "Ciencias ocultas": 5,
            "Combatir (Pelea)": 25,
            "Conducir automóvil": 20,
            "Conducir maquinaria": 1,
            "Contabilidad": 5,
            "Crédito": 0,
            "Derecho": 5,
            "Descubrir": 25,
            "Disfrazarse": 5,
            "Electricidad": 10,
            "Encanto": 15,
            "Equitación": 5,
            "Escuchar": 20,
            "Esquivar": self.caracteristicas["DES"] // 2,
            "Historia": 5,
            "Intimidar": 15,
            "Juego de manos": 10,
            "Lanzar": 20,
            "Lengua propia": self.caracteristicas["EDU"],
            "Otras lenguas": 1,
            "Mecánica": 10,
            "Medicina": 1,
            "Mitos de Cthulhu": 0,
            "Nadar": 20,
            "Naturaleza": 10,
            "Orientarse": 10,
            "Persuasión": 10,
            "Pilotar": 1,
            "Primeros auxilios": 30,
            "Psicoanálisis": 1,
            "Psicología": 10,
            "Saltar": 20,
            "Seguir rastros": 10,
            "Sigilo": 20,
            "Supervivencia": 10,
            "Tasación": 5,
            "Trepar": 20,
            "Armas de fuego (Arma corta)": 20,
            "Armas de fuego (Fusil/Escopeta)": 25
        }

    # Función para generar la salida HTML
    def generar_html(self):
        html = f"""
         Hoja de Personaje - Años 20
          {self.nombre}
          Jugador: {self.jugador}
              Ocupación:
              {self.ocupacion}
              Género:
              {self.genero}
              Edad:
              {self.edad}
              Lugar de residencia:
              {self.lugar_residencia}
              Lugar de nacimiento:
              {self.lugar_nacimiento}
        
          Características
          """
          for key, value in self.caracteristicas.items():
            html += f"""
              {key}
              {value}
              """
              html += f"""
               
          Habilidades del Investigador
          """
            for key, value in self.habilidades.items():
            html += f"""
                   """
            html += f"""
             
                Habilidad %
              {key}
              {value}%
            
          Armas """
            for arma in self.armas:
            html += f"""
             """
            html += f"""
                Arma
                Normal
                Difícil
                Extremo
                Daño
                Alcance
                Ataques
                Munición
                Avería
                {arma["nombre"]}
                {arma["normal"]}
                {arma["dificil"]}
                {arma["extremo"]}
                {arma["dano"]}
                {arma["alcance"]}
                {arma["ataques"]}
                {arma["municion"]}
                {arma["averia"]}
          Trasfondo
          {self.trasfondo}
          Equipo y Posesiones
          {self.equipo_posesiones}
          Dinero y Bienes
          {self.dinero_bienes}
          Compañeros Investigadores
          """
        for companero in self.companeros_investigadores:
            html += f"""
            {companero}
            """
        html += f"""
          Notas
          {self.notas}
        """
        return html
# Ejemplo de uso
personaje = Personaje()
personaje.nombre = "John Smith"
personaje.jugador = "Jane Doe"
personaje.ocupacion = "Escritor"
personaje.genero = "Masculino"
personaje.edad = 30
personaje.lugar_residencia = "Arkham"
personaje.lugar_nacimiento = "Boston"
personaje.generar_caracteristicas()
personaje.inicializar_habilidades()

# Agregar un arma
personaje.armas.append({
    "nombre": "Revólver .38",
    "normal": 20,
    "dificil": 40,
    "extremo": 80,
    "dano": "1D6+2",
    "alcance": "20m",
    "ataques": 1,
    "municion": 6,
    "averia": 90
})

# Agregar información de trasfondo, equipo, etc.
personaje.trasfondo = "John Smith es un escritor en apuros que busca inspiración en los oscuros secretos de Arkham..."

# Generar HTML y guardarlo en un archivo
html = personaje.generar_html()
with open("hoja_personaje.html", "w", encoding="utf-8") as f:
    f.write(html)