
def create_user(login,password,connection):
    query = "insert into users (login, password) values (%s, %s)"
    value = (login, password)
    connection.commit()
    cursor = connection.cursor()
    cursor.execute(query, value)
    
    

def read_users():
    return True


def update_user():
    return True


def delete_user():
    return True