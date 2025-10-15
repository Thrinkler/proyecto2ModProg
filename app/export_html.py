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


# Create the HTML for the table body by iterating through tasks
tbody_html = "".join(
    [
        f"""<tr class="{'is-success' if tarea.completada else ''}">
        <td>{tarea.id}</td>
        <td>{tarea.titulo}</td>
        <td>{tarea.prioridad}</td>
        <td>{tarea.fecha}</td>
        <td>{tarea.descripcion}</td>
        <td>{", ".join(tarea.tags) if tarea.tags else "N/A"}</td>
        <td>{'Sí' if tarea.completada else 'No'}</td>
        </tr>"""
        for tarea in tareas
    ]
)

# Assemble the final HTML document using Bulma classes
html_completo = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Agenda TikiTiki</title>
    <!-- Link to the Bulma CSS framework via CDN -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.4/css/bulma.min.css">
</head>
<body>

    <section class="section">
        <div class="container">

        
            <h1 class="title">La Agenda TikiTiki</h1>

            <div class="table-container">
                <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Titulo</th>
                            <th>Prioridad</th>
                            <th>Fecha</th>
                            <th>Descripción</th>
                            <th>Tags</th>
                            <th>Completada</th>
                        </tr>
                    </thead>
                    <tbody>
                        {tbody_html}
                    </tbody>
                </table>
            </div>

        </div>
    </section>

</body>
</html>
"""

# Write the generated HTML to a file
output_filename = "index.html"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(html_completo)

print(f"'{output_filename}' ha sido generado con éxito")
