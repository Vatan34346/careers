import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()


engine = create_engine(os.getenv('CONNECTION_STRING'),
                       connect_args={
                           "ssl": {
                                "ssl_ca": "/etc/ssl/cert.pem",
                                "ssl_cert": "/home/gord/client-ssl/client-cert.pem",
                                "ssl_key": "/home/gord/client-ssl/client-key.pem"
                           }
                       })


def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        columns = result.keys()
        jobs_ = [dict(zip(columns, row)) for row in result.all()]
        return jobs_




