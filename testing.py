import sql


# try:
#     sql.create_table('Libs')z``
# except:
#     '''means the table already exists'''
#
# sql.clear_table('Libs')
sql.drop_table('Libs')
sql.create_table('Libs')
print('Clean Table')

# directory_as_bytes = sql.files_directory_to_bytes('files')
# sql.insert_row(directory_as_bytes[list(directory_as_bytes.keys())[0]])
# row = directory_as_bytes[list(directory_as_bytes.keys())[0]]
# row_tuple = (row['file_name'], row['size'], row['content'])
# sql.insert_with_values(row_tuple)




