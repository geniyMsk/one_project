import psycopg2
import datetime
import random
#from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from psycopg2.extras import NamedTupleCursor

import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


try:
    connection = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port=config.DB_PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute("""CREATE DATABASE db_bot""")
    print('База данных "freelance_bot" создана')
    cursor.close()
    connection.close()
except:
    pass

def NOW():
    dt = datetime.datetime.now()
    return dt




def add_user(chat_id, name, username, args):
    connect = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port=config.DB_PORT,
                                  database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    if args == '':
        cursor.execute(f"""INSERT INTO users (chat_id, name, username, reg_dt) VALUES
                                             ({chat_id}, '{name}', '{username}', '{NOW()}')""")
    else:
        cursor.execute(f"""INSERT INTO users (chat_id, name, username, reg_dt, args) VALUES
                                                     ({chat_id}, '{name}', '{username}', '{NOW()}', '{args}')""")
    connect.commit()
    connect.close()


def get_all_chat_id():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute("""SELECT chat_id FROM users""")
    chat_ids = cursor.fetchall()
    connect.commit()
    connect.close()
    return chat_ids



def get_random_motivating_phrase():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute("""SELECT phrase FROM motivating_phrases""")
    phrases = cursor.fetchall()
    connect.commit()
    connect.close()
    return random.choice(phrases)[0]


def get_random_notify_phrase():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute("""SELECT phrase FROM notify_phrases""")
    phrases = cursor.fetchall()
    connect.commit()
    connect.close()
    return random.choice(phrases)[0]


def get_random_thank_phrase():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute("""SELECT phrase FROM thank_phrases""")
    phrases = cursor.fetchall()
    connect.commit()
    connect.close()
    return random.choice(phrases)[0]


def add_job(chat_id, time, job_id):
    connect = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port=config.DB_PORT,
                                  database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO jobs (chat_id, time, job_id) VALUES
                                        ({chat_id}, '{time}', '{job_id}')""")
    connect.commit()
    connect.close()


def get_all_job():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute("""SELECT * FROM jobs""")
    jobs = cursor.fetchall()
    connect.commit()
    connect.close()
    return jobs


def add_progress(chat_id, text):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO progress (chat_id, dt, text) VALUES ({chat_id}, '{NOW()}', '{text}')""")
    connect.commit()
    connect.close()


def count_progress(chat_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""SELECT dt FROM progress WHERE chat_id = {chat_id}""")
    dt = cursor.fetchall()
    connect.commit()
    connect.close()
    a = []
    for x in dt:
        if x[0].date() == datetime.date.today():
            a.append(x[0].date())
    return len(a)


def get_progress(chat_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""SELECT * FROM progress WHERE chat_id = {chat_id}""")
    result = cursor.fetchall()
    connect.commit()
    connect.close()
    return result


def get_all_users():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute("""SELECT * FROM users""")
    result = cursor.fetchall()
    connect.commit()
    connect.close()
    return result


def get_all_progress():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute("""SELECT * FROM progress""")
    result = cursor.fetchall()
    connect.commit()
    connect.close()
    return result


def count_args_users(arg):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""SELECT COUNT(*) FROM users WHERE args = '{arg}'""")
    result = cursor.fetchone()[0]
    connect.commit()
    connect.close()
    return result


def get_job(chat_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""SELECT * FROM jobs WHERE chat_id = '{chat_id}'""")
    result = cursor.fetchone()
    connect.commit()
    connect.close()
    return result


def set_job_id(id, job_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""UPDATE jobs SET job_id = '{job_id}' WHERE id = {id}""")
    connect.commit()
    connect.close()


def delete_job_id(id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""DELETE FROM jobs WHERE id = {id}""")
    connect.commit()
    connect.close()