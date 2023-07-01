import psycopg2

try: 
    conn = psycopg2.connect(user="odtblykm", password="a9HGD27vXsktr0CPK2EmhrXGQTWQlI0g",  host="mahmud.db.elephantsql.com", port="5432")
    print("Conectado a la base de agentes")
    cur = conn.cursor()
except:
    print("No es posible conectarse a la Base de datos de Agentes")

def ingresar_Agentes():
    print("Ingresar agentes")
    agent_name = input("Ingrese nombre del agente: ")
    agent_descp = input("Ingrese descripción del agente: ")
    agent_key = input("Ingrese key del agente: ")
    api_key = "ac3d74a1-3577-4552-96d1-60ee0c9196fc"
    cur.execute("insert into agentes(agent_key, api_key, nombre_agente, descripcion) values (%s, %s, %s, %s) RETURNING nombre_agente", [agent_key, api_key, agent_name, agent_descp,])
    conn.commit()
    if(cur.fetchall()!= None):
        print("Inserción de agente " + agent_name + " realizada con exito")
def verAgente_key(nombre_agente):
    try:
        cur.execute("select agent_key from agentes where nombre_agente = %s", [nombre_agente,])
        print(str(cur.fetchall()[0])[1:-1].replace(",", "").replace("'", ""))
    except:
        print("no encontrado")

if __name__ == '__main__' :
    ingresar_Agentes()


