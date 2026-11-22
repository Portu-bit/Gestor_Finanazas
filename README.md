# Gestor de Finanzas Personales

Aplicación de línea de comandos para registrar y consultar ingresos y gastos personales. Los datos se almacenan localmente en una base de datos SQLite.

## Funcionalidades

- Registrar ingresos.
- Registrar gastos con validación de saldo disponible.
- Consultar el balance actual.
- Consultar el historial de transacciones.
- Exportar transacciones a un archivo CSV.
- Persistir los datos entre ejecuciones mediante SQLite.

## Tecnologías

- Python 3
- SQLite
- pytest (pruebas automatizadas)

## Estructura del proyecto

```text
Gestor_Finanazas/
├── finanzas/
│   ├── src/
│   │   ├── database.py
│   │   ├── excepciones.py
│   │   ├── reportes.py
│   │   └── transacciones.py
│   └── tests/
│       └── test_transacciones.py
└── main.py
```

## Requisitos

Python 3.10 o superior y pip.

## Instalación y ejecución

Clona el repositorio:

```bash
git clone https://github.com/Portu-bit/Gestor_Finanazas.git
cd Gestor_Finanazas
```

Instala pytest para ejecutar las pruebas:

```bash
python -m pip install pytest
```

Inicia la aplicación desde la carpeta raíz del repositorio:

```bash
python main.py
```

## Ejecutar las pruebas

Desde la carpeta raíz del repositorio:

```bash
python -m pytest finanzas/tests -v
```

Las pruebas utilizan una base de datos temporal independiente para no modificar los datos reales de la aplicación.
