from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

DB_USER = 'postgres'
DB_PASS = '1111'
DB_HOST = '127.0.0.1'
DB_PORT = '5432'
DB_NAME = 'db_bot'