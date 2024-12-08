import sys
import hashlib
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
)

# Clase para gestionar contactos
class Contacto:
    def __init__(self, nombre, apellidos, telefonos, emails, lugar_trabajo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefonos = telefonos if isinstance(telefonos, list) else [telefonos]
        self.emails = emails if isinstance(emails, list) else [emails]
        self.lugar_trabajo = lugar_trabajo

    def to_dict(self):
        return {
            "Nombre": self.nombre,
            "Apellidos": self.apellidos,
            "Teléfonos": ", ".join(self.telefonos),
            "Emails": ", ".join(self.emails),
            "Lugar de Trabajo": self.lugar_trabajo
        }

# Clase para manejar la agenda
class Agenda:
    def __init__(self):
        self.contactos = {}

    def _hash_contacto(self, contacto):
        """Crea un hash único basado en los atributos del contacto."""
        key = f"{contacto.nombre}{contacto.apellidos}"
        return hashlib.sha256(key.encode()).hexdigest()

    def agregar_contacto(self, contacto):
        hash_key = self._hash_contacto(contacto)
        if hash_key in self.contactos:
            return False  # Contacto duplicado
        self.contactos[hash_key] = contacto
        return True

    def actualizar_contacto(self, nombre, apellidos, nuevos_telefonos, nuevos_emails):
        """Actualiza los datos de un contacto existente."""
        hash_key = hashlib.sha256(f"{nombre}{apellidos}".encode()).hexdigest()
        if hash_key in self.contactos:
            contacto = self.contactos[hash_key]
            contacto.telefonos.extend(nuevos_telefonos)
            contacto.emails.extend(nuevos_emails)
            # Eliminar duplicados
            contacto.telefonos = list(set(contacto.telefonos))
            contacto.emails = list(set(contacto.emails))
            return True
        return False

    def buscar_contactos(self, criterio):
        """Busca contactos que coincidan con el criterio en cualquier campo."""
        resultados = []
        for contacto in self.contactos.values():
            if any(criterio.lower() in str(value).lower() for value in contacto.to_dict().values()):
                resultados.append(contacto)
        return resultados

# Interfaz gráfica principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agenda Electrónica")
        self.agenda = Agenda()
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Inputs
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre")
        self.apellidos_input = QLineEdit()
        self.apellidos_input.setPlaceholderText("Apellidos")
        self.telefono_input = QLineEdit()
        self.telefono_input.setPlaceholderText("Teléfono (separar múltiples con coma)")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email (separar múltiples con coma)")
        self.lugar_trabajo_input = QLineEdit()
        self.lugar_trabajo_input.setPlaceholderText("Lugar de Trabajo")

        # Botones
        self.agregar_button = QPushButton("Agregar Contacto")
        self.agregar_button.clicked.connect(self.agregar_contacto)

        self.actualizar_button = QPushButton("Actualizar Contacto")
        self.actualizar_button.clicked.connect(self.actualizar_contacto)

        self.buscar_input = QLineEdit()
        self.buscar_input.setPlaceholderText("Buscar contacto por cualquier campo")
        self.buscar_button = QPushButton("Buscar")
        self.buscar_button.clicked.connect(self.buscar_contacto)
        self.mostrar_todos_button = QPushButton("Mostrar Todos")
        self.mostrar_todos_button.clicked.connect(self.mostrar_todos_contactos)

        # Tabla de resultados
        self.resultados_table = QTableWidget()
        self.resultados_table.setColumnCount(5)
        self.resultados_table.setHorizontalHeaderLabels([
            "Nombre", "Apellidos", "Teléfonos", "Emails", "Lugar de Trabajo"
        ])

        # Agregar widgets al layout
        layout.addWidget(QLabel("Agregar o actualizar contacto:"))
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.apellidos_input)
        layout.addWidget(self.telefono_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.lugar_trabajo_input)
        layout.addWidget(self.agregar_button)
        layout.addWidget(self.actualizar_button)

        layout.addWidget(QLabel("Buscar contactos:"))
        layout.addWidget(self.buscar_input)
        layout.addWidget(self.buscar_button)
        layout.addWidget(self.mostrar_todos_button)
        layout.addWidget(self.resultados_table)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.actualizar_tabla_contactos()

    def agregar_contacto(self):
        nombre = self.nombre_input.text()
        apellidos = self.apellidos_input.text()
        telefonos = self.telefono_input.text().split(",")
        emails = self.email_input.text().split(",")
        lugar_trabajo = self.lugar_trabajo_input.text()

        if not (nombre and apellidos and telefonos and emails and lugar_trabajo):
            QMessageBox.warning(self, "Error", "Por favor, completa todos los campos.")
            return

        contacto = Contacto(nombre, apellidos, telefonos, emails, lugar_trabajo)
        if self.agenda.agregar_contacto(contacto):
            QMessageBox.information(self, "Éxito", "Contacto agregado correctamente.")
            self.limpiar_formulario()
            self.actualizar_tabla_contactos()
        else:
            QMessageBox.warning(self, "Error", "El contacto ya existe.")

    def actualizar_contacto(self):
        nombre = self.nombre_input.text()
        apellidos = self.apellidos_input.text()
        nuevos_telefonos = self.telefono_input.text().split(",")
        nuevos_emails = self.email_input.text().split(",")

        if not (nombre and apellidos):
            QMessageBox.warning(self, "Error", "Por favor, completa los campos de nombre y apellidos.")
            return

        if self.agenda.actualizar_contacto(nombre, apellidos, nuevos_telefonos, nuevos_emails):
            QMessageBox.information(self, "Éxito", "Contacto actualizado correctamente.")
            self.limpiar_formulario()
            self.actualizar_tabla_contactos()
        else:
            QMessageBox.warning(self, "Error", "No se encontró el contacto para actualizar.")

    def buscar_contacto(self):
        criterio = self.buscar_input.text()
        if not criterio:
            QMessageBox.warning(self, "Error", "Por favor, ingresa un criterio de búsqueda.")
            return

        resultados = self.agenda.buscar_contactos(criterio)
        self.resultados_table.setRowCount(0)

        for contacto in resultados:
            fila = self.resultados_table.rowCount()
            self.resultados_table.insertRow(fila)
            for col, value in enumerate(contacto.to_dict().values()):
                self.resultados_table.setItem(fila, col, QTableWidgetItem(value))

    def limpiar_formulario(self):
        self.nombre_input.clear()
        self.apellidos_input.clear()
        self.telefono_input.clear()
        self.email_input.clear()
        self.lugar_trabajo_input.clear()
    
    def actualizar_tabla_contactos(self):
        self.resultados_table.setRowCount(0)
        for contacto in self.agenda.contactos.values():
            fila = self.resultados_table.rowCount()
            self.resultados_table.insertRow(fila)
            for col, value in enumerate(contacto.to_dict().values()):
                self.resultados_table.setItem(fila, col, QTableWidgetItem(value))
    
    def mostrar_todos_contactos(self):
        self.buscar_input.clear()
        self.actualizar_tabla_contactos() 

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
