from . import repo

tareas = repo.get_task_list()

tareas_html = """<tr>
    <th>ID</th>
    <th>Titulo</th>
    <th>Prioridad</th>
    <th>Fecha</th>
    <th>Descripción</th>
    <th>Tags</th>
    <th>Completada</th>
  </tr>"""


for tarea in tareas:
    
    tareas_html += f'<tr class="{"completada" if tarea.completada else ""}">\
    <td>{tarea.id}</td>\
    <td>{tarea.titulo}</td>\
    <td>{tarea.prioridad}</td>\
    <td>{tarea.fecha}</td>\
    <td>{tarea.descripcion}</td>\
    <td>{", ".join(tarea.tags) if tarea.tags != None else ""}</td>\
    <td>{"X" if tarea.completada else ""}</td>\
    </tr>\n'



html_completo = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Agenda TikiTiki</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>La Agenda TikiTiki</h1>
    <table>
        {tareas_html}
    </table>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_completo)