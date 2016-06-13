import sys
from models import *


def action_create(*args, **kwargs):
	my_models_db.create_tables([School, Batch, User, Student])


def action_print(*args, **kwargs):
	print "print"


def action_insert(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `insert`")

	if sys.argv[2] == "school":
		if len(sys.argv) <= 3:
			raise Exception("Too few arguments for `insert school`")
		name = sys.argv[3]
		school = School()
		school.name = name
		school.save()
		return

	if sys.argv[2] == "batch":
		if len(sys.argv) <= 4:
			raise Exception("Too few arguments for `insert batch`")
		school = sys.argv[3]
		name = sys.argv[4]
		batch = Batch()
		batch.name = name
		batch.school = school
		batch.save()
		return

	if sys.argv[2] == "student":
		#first_name is optional
		if len(sys.argv) <= 5:
			raise Exception("Too few arguments for `insert batch`")
		batch = sys.argv[3]
		age = sys.argv[4]
		last_name = sys.argv[5]
		if len(sys.argv) > 6:
			first_name = sys.argv[6]
		student = Student()
		student.last_name = last_name
		student.batch = batch
		student.age = age
		if "first_name" in locals():
			student.first_name = first_name
		student.save()
		return

def action_delete(*args, **kwargs):
	print "delete"

def action_schema(*args, **kwargs):
	print "schema"

if __name__ == '__main__':
	actions = {
		"create": action_create,
		"print": action_print,
		"insert": action_insert,
		"delete": action_delete,
		"schema": action_schema,
	}
	if len(sys.argv) > 1:
		action = sys.argv[1]

	if not "action" in locals():
		print "Please enter an action"
		sys.exit()

	if not action:
		#shouldn't run
		raise Exception("No action supplied")

	my_models_db.connect()

	if action in actions.keys():
		actions[action]()
	else:
		print "Undefined action " + action
