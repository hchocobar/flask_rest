from flask import Flask
from flask import jsonify
from flask import request
from data import table  # importamos nuestros datos de prueba

app = Flask(__name__)


@app.route('/rest')  # GET - mostramos la tabla completa
def get_table():
    return jsonify({'table': table,
                    'message': 'Tabla completa que devuelve la App'})


@app.route('/rest/<int:column_id>')  # GET - búsqueda por el campo 'id'
def get_column_id(column_id):
    column_found = [column for column in table if column['id'] == column_id]
    if column_found:  # True si la lista contiene algo; False si la lista está vacía
        return jsonify({'column': column_found[0],
                        'message': 'Columna encontrada'})
    return jsonify({'message': 'Columna no encontrada'})


@app.route('/rest/<string:column_name>')  # GET - búsqueda por el campo 'name'
def get_column_name(column_name):
    column_found = [column for column in table if column['name'] == column_name]
    if column_found:
        return jsonify({'column': column_found[0],
                        'message': 'Columna encontrada'})
    return jsonify({'message': 'Columna no encontrada'})


@app.route('/rest', methods=['POST'])
def add_column():
    new_column = {'id': request.json['id'],
                  'name': request.json['name'],
                  'price': request.json['price'],
                  'quantity': request.json['quantity']}
    table.append(new_column)
    return jsonify({'column': new_column,
                    'message': 'Columna agregada exitosamente'})


@app.route('/rest/<int:column_id>', methods=['PUT'])
def edit_column(column_id):
    column_found = [column for column in table if column['id'] == column_id]
    if column_found:
        column_found[0]['id'] = request.json['id']
        column_found[0]['name'] = request.json['name']
        column_found[0]['price'] = request.json['price']
        column_found[0]['quantity'] = request.json['quantity']
        return jsonify({'column': column_found[0],
                        'message': 'Columna actualizada exitosamente'})
    return jsonify({'message': 'Columna no encontrada'})


@app.route('/rest/<int:column_id>', methods=['DELETE'])
def delete_column(column_id):
    column_found = [column for column in table if column['id'] == column_id]
    if column_found:
        table.remove(column_found[0])
        return jsonify({'table': table,
                        'message': 'Columna eliminada exitosamente'})
    return jsonify({'message': 'Columna no encontrada'})


if __name__ == '__main__':
    app.run(debug=True)
