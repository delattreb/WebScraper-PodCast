"""
com_sqlite.py v1.0.0
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import sqlite3

from lib import com_config


def connect():
    conf = com_config.Config()
    config = conf.getconfig()
    con = sqlite3.connect(config['SQLITE']['database'])
    cursor = con.cursor()
    return con, cursor


def select(val):
    con, cursor = connect()
    rows = cursor.execute("SELECT id FROM data WHERE id='" + str(val) + "'")
    index = 0
    for row in rows:
        index = row[0]
    con.close()
    return index


def insert(val):
    con, cursor = connect()
    try:
        cursor.execute("INSERT INTO data(id) VALUES('" + str(val) + "')")
        con.commit()
    except:
        con.rollback()
    con.close()


def delete(val):
    con, cursor = connect()
    try:
        cursor.execute("DELETE FROM data WHERE id ='" + str(val) + "'")
        con.commit()
    except:
        con.rollback()
    con.close()
