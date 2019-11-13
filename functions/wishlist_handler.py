import json

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

from utils.db_credentials import DBCredentials #place it on top
def claim_gift(event,context):
    
# 01 - Finding out how things communicate:

    # log.info(json.dumps(event))

# 02 - Manipulating objects:

    body = json.loads(event['body'])
    item_id = body['id']
    # log.info(item_id)

# 03 - Write basic test for local execution

# 04 - Connecting to database:
    import psycopg2
    
    conn = psycopg2.connect(**DBCredentials.credentials)
    cur = conn.cursor()

    cur.execute("update items set reserved = true where id = %s",(item_id,))

# 05 - Provision a cloud database:

# 06 - Provision CI/CD

# 07 - Change DBCredentials.credentials so it gets from environment variables

# 08 - Make list items method (as exercise)

# 09 - Plan further features

# 10 - Start on database modelling
    # - Data types
    # - Relationships 1:1 1:n n:n
    # - Normal formulas

# 11 - Start improving table modelling

# 12 - Implement new features

# 13 - Introduce ORM SqlAlchemy

# 14 - Refactor code

# 15 - Introduce Database Code First and Migrations - Alembic

# 16 - Improve deployment codes to execute migrations

# 17 - Introduce automated tests and a test framework


# Common closing code -----------------------

    cur.close()
    conn.commit()
    conn.close()

    response = {
        "statusCode": 200
    }
    return response