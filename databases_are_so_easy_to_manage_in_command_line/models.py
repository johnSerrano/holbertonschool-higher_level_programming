import peewee as pw

my_models_db = pw.SqliteDatabase('my_models.db', pragmas=(('foreign_keys', True),))

class BaseModel(pw.Model):
	id = pw.PrimaryKeyField(primary_key=True, unique=True)

	class Meta:
		database = my_models_db
		order_by = ('id',)

class School(BaseModel):
	name = pw.FixedCharField(max_length=128)
	def __str__(self):
		return self.name + " " + str(self.id)

class Batch(BaseModel):
	school = pw.ForeignKeyField(School, related_name="batches", on_delete="cascade")
	name = pw.FixedCharField(max_length=128)
	def __str__(self):
		return self.name + " " + str(self.id)

class User(BaseModel):
	first_name = pw.FixedCharField(max_length=128, default="")
	last_name = pw.FixedCharField(max_length=128)
	age = pw.IntegerField()
	def __str__(self):
		print self.first_name, self.last_name, self.id

class Student(User):
	batch = pw.ForeignKeyField(Batch, related_name="students", on_delete="cascade")
	def __str__(self):
		return "" + self.first_name + " " + self.last_name + " " + str(self.id) + " " + "part of batch: " + str(self.batch)
