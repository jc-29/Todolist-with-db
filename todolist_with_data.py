import datetime
import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase


db = PostgresqlExtDatabase('todo_list')

class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime.datetime.now())
    updated_at = pw.DateTimeField(default=datetime.datetime.now())

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db
        # Check this one out here http://docs.peewee-orm.com/en/latest/peewee/models.html#table-names
        legacy_table_names = False

class User(BaseModel):
    username = pw.CharField(null=False)
    password = pw.CharField(null = False)

class Todo_list(BaseModel):
    name = pw.CharField(null=False)
    # user = pw.ForeignKeyField(User, backref='todo_lists')

    def __repr__(self):
        return f'id: {self.id} name:{self.name}'

class Todo_task(BaseModel):
    task = pw.CharField(null = False)
    completed = pw.BooleanField(default=False)
    todo_list=pw.ForeignKeyField(Todo_list, backref='tasks')

# Define your models here