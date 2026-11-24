# Herbo Natura

Sitio web de una tienda de hierbas y productos naturales, desarrollado con Django como proyecto de la asignatura **Programación Back-End**.

---

## El sitio

**Herbo Natura** es una tienda en línea orientada a personas interesadas en el bienestar natural, que buscan hierbas medicinales, aromáticas y productos naturales de calidad.

El sitio presenta el catálogo de la tienda con información de cada producto, permite buscar productos por nombre y muestra indicadores de disponibilidad en tiempo real según el stock.

### Páginas disponibles

| Ruta | Página | Descripción |
|---|---|---|
| `/` | Inicio | Presentación de la tienda con imagen y llamado a la acción |
| `/catalogo/` | Catálogo | Listado de productos con buscador por nombre |
| `/nosotros/` | Nosotros | Misión y visión de la tienda |
| `/contacto/` | Contacto | Correo de contacto de la tienda |

---

## Cómo ejecutarlo

### Requisitos previos

- Python 3.11 o superior
- PowerShell (Windows)

### Pasos

**1. Crear y activar el entorno virtual:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, habilitar scripts para la sesión:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

**2. Instalar las dependencias:**

```powershell
pip install -r requirements.txt
```

**3. Aplicar las migraciones:**

```powershell
py manage.py migrate
```

**4. Levantar el servidor de desarrollo:**

```powershell
py manage.py runserver
```

**5. Abrir en el navegador:**

- Sitio: http://127.0.0.1:8000/
- Catálogo: http://127.0.0.1:8000/catalogo/
- Nosotros: http://127.0.0.1:8000/nosotros/
- Contacto: http://127.0.0.1:8000/contacto/

---

## Uso de IA

### Agente utilizado

**ChatGPT (GPT-4o)** — usado como asistente durante el desarrollo del front end y para resolver dudas puntuales del código.

### Prompts principales

1. *"Necesito una navbar de Bootstrap 5 con 4 enlaces: Inicio, Catálogo, Nosotros y Contacto. Que el enlace activo se resalte automáticamente según la página donde estoy. Estoy usando Django Templates."*

2. *"Tengo un archivo JSON con productos. Quiero mostrarlos en tarjetas Bootstrap. Cada tarjeta debe mostrar nombre, categoría, descripción, precio y stock. Si el stock es 0, que aparezca un badge que diga 'Producto agotado' en vez del número."*

3. *"¿Cómo hago una búsqueda por nombre en Django que no distinga mayúsculas, minúsculas ni acentos? Los datos vienen de un JSON, no de una base de datos."*

4. *"Genera el HTML de una página de inicio con imagen a la izquierda y texto a la derecha usando Bootstrap 5. Que sea responsive."*

5. *"Quiero un footer que siempre quede pegado al fondo de la página, aunque el contenido sea corto. Uso Bootstrap 5 y un div con clase `min-vh-100`."*

### Qué se aceptó

- El diseño general de las tarjetas del catálogo (`card`, `card-body`, `card-footer`) fue aceptado casi sin cambios.
- La estructura de la navbar con collapse para móviles se aceptó tal como la propuso la IA.
- La sugerencia de usar `flex-column min-vh-100` en el `body` para mantener el footer abajo fue adoptada directamente.
- El esquema de colores verde (`bg-success`, `text-success`) lo propuso la IA como paleta coherente con el tema natural de la tienda.

### Qué se corrigió

- La IA propuso detectar la página activa con una variable de contexto pasada desde la vista. Se corrigió para usar `request.resolver_match.url_name` directamente en el template, que es más limpio y no requiere modificar cada vista.
- El código de búsqueda inicial no ignoraba los acentos. Se ajustó para instalar y usar `unidecode` tanto en el texto del producto como en la búsqueda del usuario, de forma que buscar "manzanilla" encuentre "Manzanilla" aunque el dato tenga tilde.
- La IA sugirió `STATIC_ROOT` y `collectstatic` para los archivos estáticos. Se descartó porque es configuración de producción; en desarrollo basta con `STATIC_URL` y `APP_DIRS: True`.

### Qué se descartó

- La IA propuso un carrusel de Bootstrap en la página de inicio. Se descartó por preferir un diseño más simple y directo.
- Se descartó un formulario de contacto con lógica de envío de correo porque la evaluación no requiere base de datos ni procesamiento de formularios.
- Se descartó el uso de `django-crispy-forms` porque agrega complejidad innecesaria para un formulario tan simple.

---

## Estructura del proyecto

```text
Herbo_natural/
├── manage.py
├── requirements.txt
├── README.md
├── mysite/
│   ├── settings.py
│   └── urls.py
└── HerboNatura/
    ├── views.py
    ├── urls.py
    ├── data/
    │   └── productos.json
    ├── templates/
    │   ├── base.html
    │   ├── inicio.html
    │   ├── catalogo.html
    │   ├── nosotros.html
    │   └── contacto.html
    └── static/
        ├── css/
        │   └── estilos.css
        └── img/
            ├── Inicio.png
            └── Narvar.png
```

---

## Tecnologías usadas

- **Python 3** — lenguaje base
- **Django 6.1** — framework web
- **Unidecode** — normalización de texto para búsqueda sin acentos
- **Bootstrap 5.3** — framework CSS para el diseño responsive
- **Bootstrap Icons 1.11** — íconos del menú y la interfaz
- **JSON** — almacenamiento de datos de productos (sin base de datos)
