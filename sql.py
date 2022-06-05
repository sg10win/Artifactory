import sqlite3
import pandas as pd
import os
DB_NAME = 'DataBase.db'
QUERY = """
           SELECT *
           FROM Libs
        """
'''This code open and close a connection each time it execute something with we cursor'''


def test_connection(db_name):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(db_name)
        cursor = sqlite_connection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The SQLite connection is closed")


def create_table(table_name):
    query = f'''
                CREATE TABLE {table_name}(  
                    file_name varchar(255),
                    size int,
                    content BLOB
                )
                
            '''
    return sql_query(DB_NAME, query)


def drop_table(table_name):
    query = f'''
                DROP TABLE {table_name}
            '''
    return sql_query(DB_NAME, query)


def clear_table(table_name):
    query = f'''
                DELETE FROM {table_name}
            '''
    return sql_query(DB_NAME, query)


def reset():
    try:
        drop_table('Libs')
        create_table('Libs')
    except:
        create_table('Libs')


def sql_query(db_name, query):
    sqlite_connection = None
    cursor = None
    try:
        sqlite_connection = sqlite3.connect(db_name)
        cursor = sqlite_connection.cursor()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    '''Query Time...'''
    if cursor and sqlite_connection:
        cursor.execute(query)
        sqlite_connection.commit()
        record = cursor.fetchall()
        sqlite_connection.close()
        return record
    return


def res_to_frame(res):
    if res is []:
        '''res is empty list'''
        return None
    file_name, size, content = list(map(lambda x: list(x), list(zip(*res))))
    df_dict = {
        'file_name': file_name,
        'size': size,
        'content': content
    }
    return pd.DataFrame(df_dict)


def files_directory_to_bytes(directory):
    _dict = {}
    files_names = os.listdir(f'./{directory}')
    print(f'{len(files_names)} files in directory: "{directory}"')
    i = 0
    for file_name in files_names:

        file_size = os.path.getsize(f'./files/{file_name}')
        bytes_file = open(f'./files/{file_name}', 'rb').read()
        _dict[file_name] = {
                            'file_name': file_name,
                            'size': file_size,
                            'content': bytes_file
                           }
        i+=1
        if i % 5 == 0:
            print(f'{i}/{len(files_names)}')
    return _dict


def insert_row(file: dict):
    query = f'''
            INSERT into Libs
            (file_name, size, content)
            VALUES
            ("{file['file_name']}", {file['size']}, "{file['content']}")
        '''
    print(query)
    sql_query(DB_NAME, query)


def encode_file_row(file):
    file['file_name'] = file['file_name'].replace('\\', 'ggg/')
    file['content'] = file['content'].replace('\\', 'ggg/')
    return file


def decode_file_row(file):
    file['file_name'] = file['file_name'].replace('ggg', '\\')
    file['content'] = file['content'].replace('ggg', '\\')
    return file


def insert_with_values(params):
    sqlite_insert_with_param = """
                              INSERT INTO Libs
                              (file_name, size, content)
                              VALUES
                              (?, ?, ?)
                              """

    data_tuple = params
    sqlite_connection = sqlite3.connect(DB_NAME)
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_insert_with_param, data_tuple)
    sqlite_connection.commit()
    sqlite_connection.close()


def insert_all_files_to_database_table(directory_dict):
    for key in list(directory_dict.keys()):
        file = directory_dict[key]
        row_tuple = (file['file_name'], file['size'], file['content'])
        insert_with_values(row_tuple)


if __name__ == '__main__':
    '''Connection Test'''
    test_connection(DB_NAME)
    '''Push Test Row to Libs Table'''
    testing_insert_q = '''
            INSERT into Libs
            (file_name, size, content)
            VALUES
            ("testing_file", 0, "testing_content")
        '''
    sql_query(DB_NAME, testing_insert_q)
    '''Gets All The Table Back as Dict'''
    res = sql_query(DB_NAME, QUERY)
    '''Converts the Dict to DataFrame Type Object'''
    frame_res = res_to_frame(res)
    print(frame_res)
    '''Converts All the Files in "files" Directory to Dict as the Libs Table'''
    directory_as_bytes = files_directory_to_bytes('files')
    insert_all_files_to_database_table(directory_as_bytes)



