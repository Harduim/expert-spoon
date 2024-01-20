import logging as log
from .users import generate_users
from redis_om import get_redis_connection


def nuke():
    redis_conn = get_redis_connection()
    redis_keys = list(redis_conn.scan_iter("*"))
    log.info(f"Removing {len(redis_keys)} keys from cache")
    for k in redis_keys:
        redis_conn.delete(k)


def run():
    generate_users()
