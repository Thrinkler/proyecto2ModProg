from . import repo

tareas = repo.get_task_list()

tareas_html = ""
for tarea in tareas:
    tareas_html += f'<li class="Tarea">{tarea.titulo}</li>\n'

html_completo = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Agenda</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Mi Lista de Tareas</h1>
    <ul>
        {tareas_html}
    </ul>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_completo)