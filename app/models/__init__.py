from ._base import db
from . import article,comment,user,articleCategory,articleTag,category,tag,content,like,friend,friendRequest,follow, notification
import os,uuid
from pony.orm import db_session,commit
from app.models.user import User
from datetime import datetime
from app.controllers.auth import hashPassword
db_params = {'provider': 'postgres',
             'user': os.getenv('PGUSER'),
             'password': os.getenv('PGPASSWORD'),
             'host': os.getenv('PGHOST'),
             'database': os.getenv('PGDATABASE')}

db.bind(**db_params)
#db.bind(provider='postgres', user='postgres', password='ETEx8zYeytUk3MsfpXMh', host='containers-us-west-112.railway.app', database='railway')
db.generate_mapping(create_tables=True)



with db_session:
    try:
        User(idUser = str(uuid.uuid4()),username = "Admin",email = "Admin@adm.com", password = hashPassword("admin"),dateRegister = datetime.now() ,isActivated = True)
        commit()
    except:
        pass
