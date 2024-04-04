from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connection():
   conn = None
   try:
      conn = sqlite3.connect("supermarket.sqlite")
   except sqlite3.Error as e:
      print(e)

   return conn

@app.route("/usuarios", methods=["GET", "POST"])
def users():
   conn = db_connection()
   cur = conn.cursor()

   if(request.method == "GET"):
      cur = conn.execute("SELECT * from users")
      users = [
         dict(id=row[0], name=row[1]) for row in cur.fetchall()
      ]
      conn.close()

      if(users is not None):
         return { "message": "Success", "status": 200, "data": users }, 200
      else:
         return { "message": "Something Wrong", "status": 404, "data": users }, 404

   elif(request.method == "POST"):
      new_user = request.get_json()

      sql_request = """ INSERT INTO users (name) VALUES (?) """
      cur = cur.execute(sql_request, [new_user["name"]])

      new_user = dict(id=cur.lastrowid, name=new_user["name"])
      conn.commit()
      conn.close()

      if(new_user is not None):
         return { "message": "Success", "status": 200, "data": new_user }, 200
      else:
         return { "message": "Something Wrong", "status": 404, "data": new_user }, 404

@app.route("/usuarios/find/<id>/usuarios", methods=["GET", "PUT", "DELETE"])
def findUsers(id: int):
   conn = db_connection()
   cur = conn.cursor()

   if(request.method == "GET"):
      user = None
      cur.execute("SELECT * FROM users WHERE id=(?);", [id])
      response_rows = cur.fetchall()
      for i in response_rows:
         user = i
      conn.close()

      if(user is not None):
         return { "message": "Success", "status": 200, "data": user }
      else:
         return { "message": "Something Wrong", "status": 404, "data": user }, 404

   if(request.method == "PUT"):
      updated_user = request.get_json()
      sql = """ UPDATE users set name=? WHERE id=(?) """
      cur.execute(sql, [updated_user["name"], id])

      updated_user = {
         "id": id,
         "name": updated_user["name"]
      }

      conn.commit()
      conn.close()

      return { "message": "Success", "status": 200, "data": updated_user }, 200

   if(request.method == "DELETE"):
      cur.execute(" DELETE FROM users WHERE id=(?) ", [id])
      conn.commit()
      conn.close()

      return { "message": "Success", "status": 200, "data": f"Usuário de id: {id} foi deletado!" }, 200

@app.route("/produtos", methods=["GET", "POST"])
def products():
   conn = db_connection()
   cur = conn.cursor()

   if(request.method == "GET"):
      cur = cur.execute(' SELECT * FROM products ')
      products = [
         dict(id=row[0], name=row[1]) for row in cur.fetchall()
      ]
      conn.close()

      if(products is not None):
         return { "message": "Success", "status": 200, "data": products }, 200
      else:
         return { "message": "Something Wrong", "status": 404, "data": products }, 404

   elif(request.method == "POST"):
      new_product = request.get_json()

      sql_request = """ INSERT INTO products (name) VALUES (?) """
      cur = cur.execute(sql_request, [new_product["name"]])

      new_product = dict(id=cur.lastrowid, name=new_product["name"])

      conn.commit()
      conn.close()

      if(new_product is not None):
         return { "message": "Success", "status": 200, "data": new_product }, 200
      else:
         return { "message": "Something Wrong", "status": 404, "data": new_product }, 404

@app.route("/produtos/find/<id>/produtos", methods=["GET", "PUT", "DELETE"])
def findProducts(id: int):
   conn = db_connection()
   cur = conn.cursor()

   if(request.method == "GET"):
      product = None
      cur.execute("SELECT * FROM products WHERE id=(?);", [id])
      response_rows = cur.fetchall()
      for i in response_rows:
         product = i
      conn.close()

      if(product is not None):
         return { "message": "Success", "status": 200, "data": product }
      else:
         return { "message": "Something Wrong", "status": 404, "data": product }, 404

   if(request.method == "PUT"):
      updated_product = request.get_json()
      sql = """ UPDATE products set name=? WHERE id=(?) """
      cur.execute(sql, [updated_product["name"], id])

      updated_product = {
         "id": id,
         "name": updated_product["name"]
      }

      conn.commit()
      conn.close()

      return { "message": "Success", "status": 200, "data": updated_product }, 200

   if(request.method == "DELETE"):
      cur.execute(" DELETE FROM products WHERE id=(?) ", [id])
      conn.commit()
      conn.close()

      return { "message": "Success", "status": 200, "data": f"Produto de id: {id} foi deletado!" }, 200

@app.route("/setores", methods=["GET", "POST"])
def sectors():
   conn = db_connection()
   cur = conn.cursor()

   if(request.method == "GET"):
      cur = cur.execute(' SELECT * FROM sectors ')

      sectors = [
         dict(id=row[0], name=row[1]) for row in cur.fetchall()
      ]
      conn.close()

      if(sectors is not None):
         return { "message": "Success", "status": 200, "data": sectors }, 200
      else:
         return { "message": "Something Wrong", "status": 404, "data": sectors }, 404

   elif(request.method == "POST"):
      new_section = request.get_json()

      sql_request = """ INSERT INTO sectors (name) VALUES (?) """
      cur = cur.execute(sql_request, [new_section["name"]])
      new_section = dict(id=cur.lastrowid, name=new_section["name"])

      conn.commit()
      conn.close()

      if(new_section is not None):
         return { "message": "Success", "status": 200, "data": new_section }, 200
      else:
         return { "message": "Something Wrong", "status": 404, "data": new_section }, 404

@app.route("/setores/find/<id>/setores", methods=["GET", "PUT", "DELETE"])
def findSectors(id: int):
   conn = db_connection()
   cur = conn.cursor()

   if(request.method == "GET"):
      sector = None
      cur.execute("SELECT * FROM sectors WHERE id=(?);", [id])
      response_rows = cur.fetchall()
      for i in response_rows:
         sector = i
      conn.close()

      if(sector is not None):
         return { "message": "Success", "status": 200, "data": sector }
      else:
         return { "message": "Something Wrong", "status": 404, "data": sector }, 404

   if(request.method == "PUT"):
      updated_sector = request.get_json()
      sql = """ UPDATE sectors set name=? WHERE id=(?) """
      cur.execute(sql, [updated_sector["name"], id])

      updated_sector = {
         "id": id,
         "name": updated_sector["name"]
      }

      conn.commit()
      conn.close()

      return { "message": "Success", "status": 200, "data": updated_sector }, 200

   if(request.method == "DELETE"):
      cur.execute(" DELETE FROM sectors WHERE id=(?) ", [id])
      conn.commit()
      conn.close()

      return { "message": "Success", "status": 200, "data": f"Setor de id: {id} foi deletado!" }, 200

@app.route("/categorias", methods=["GET", "POST"])
def categories():
   conn = db_connection()
   cur = conn.cursor()

   if(request.method == "GET"):
      cur = cur.execute(' SELECT * FROM categories ')

      categories = [
         dict(id=row[0], name=row[1]) for row in cur.fetchall()
      ]
      conn.close()

      if(categories is not None):
         return { "message": "Success", "status": 200, "data": categories }, 200
      else:
         return { "message": "Something Wrong", "status": 404, "data": categories }, 404

   elif(request.method == "POST"):
      new_category = request.get_json()

      sql_request = """ INSERT INTO categories (name) VALUES (?) """
      cur = cur.execute(sql_request, [new_category["name"]])
      new_category = dict(id=cur.lastrowid, name=new_category["name"])

      conn.commit()
      conn.close()

      if(new_category is not None):
         return { "message": "Success", "status": 200, "data": new_category }, 200
      else:
         return { "message": "Something Wrong", "status": 404, "data": new_category }, 404

@app.route("/categorias/find/<id>/categorias", methods=["GET", "PUT", "DELETE"])
def findCategories(id: int):
   conn = db_connection()
   cur = conn.cursor()

   if(request.method == "GET"):
      category = None
      cur.execute("SELECT * FROM categories WHERE id=(?);", [id])
      response_rows = cur.fetchall()
      for i in response_rows:
         category = i
      conn.close()

      if(category is not None):
         return { "message": "Success", "status": 200, "data": category }
      else:
         return { "message": "Something Wrong", "status": 404, "data": category }, 404

   if(request.method == "PUT"):
      updated_category = request.get_json()
      sql = """ UPDATE categories set name=? WHERE id=(?) """
      cur.execute(sql, [updated_category["name"], id])

      updated_category = {
         "id": id,
         "name": updated_category["name"]
      }

      conn.commit()
      conn.close()

      return { "message": "Success", "status": 200, "data": updated_category }, 200

   if(request.method == "DELETE"):
      cur.execute(" DELETE FROM categories WHERE id=(?) ", [id])
      conn.commit()
      conn.close()

      return { "message": "Success", "status": 200, "data": f"Categoria de id: {id} foi deletado!" }, 200

if __name__ == "__main__":
    app.run(debug=True)