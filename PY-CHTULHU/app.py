from flask import Flask, render_template, request

from df_npcs import df_npcs

app = Flask(__name__)

@app.route('/')
def index():
    # Mostrar lista de NPCs para elegir
    return render_template('lista_npcs.html', npcs=df_npcs.to_dict('records'))

@app.route('/personaje/<int:npc_id>')
def personaje(npc_id):
    # Mostrar información detallada del NPC seleccionado
    npc = df_npcs.loc[df_npcs['ID'] == npc_id].to_dict('records')[0]
    return render_template('personaje.html', npc=npc)

if __name__ == '__main__':
    app.run(debug=True)
