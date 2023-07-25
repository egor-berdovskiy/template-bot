from configparser import ConfigParser


parser = ConfigParser()
parser.read('config.ini')


class Telegram:
    section = 'Telegram'
    token = parser.get(section, 'token')
    support = parser.get(section, 'support')


class WebHooks:
    section = 'WebHooks'
    listen_address = parser.get(section, 'listen_address')
    listen_port = parser.getint(section, 'listen_port')
    base_url = parser.get(section, 'base_url')
    bot_path = parser.get(section, 'bot_path')


class DataBase:
    section = 'DataBase'
    host = parser.get(section, 'host')
    port = parser.getint(section, 'port')
    user = parser.get(section, 'user')
    password = parser.get(section, 'password')
    database = parser.get(section, 'database')


class Settings:
    section = 'Settings'
    currency = parser.get(section, 'currency')
    currency_code = parser.get(section, 'currency_code')
    referral_bonus = parser.getfloat(section, 'referral_bonus')
