import os
import datetime
import pymysql

#Get username from Cloud9 workspace
#(modify this variable if running on another environment)
username = os.getenv('C9_USER')

#Connect to the datatbase
connection = pymysql.connect(host='localhost',
user=username, password='',db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        format_strings = ",".join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connect, regardless of whether the above was successful
    connection.close()