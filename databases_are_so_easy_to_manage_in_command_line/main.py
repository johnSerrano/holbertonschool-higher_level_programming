import sys
from models import *

def action_create(*args, **kwargs):
	my_models_db.create_tables([School, Batch, User, Student])

def action_print(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `print`")

	tables = {
		"school": School,
		"batch": Batch,
		"student": Student,
		"user": User
	}

	if sys.argv[2] not in tables.keys():
		return
	for item in tables[sys.argv[2]].select():
		print item

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

def action_delete(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `delete`")

	if sys.argv[2] == "school":
		if len(sys.argv) <= 3:
			raise Exception("No ID supplied")
		todel = int(sys.argv[3])
		for school in School.select().where(School.id == todel):
			print "DELETE: " + str(school)
		delete_q = School.delete().where(School.id == todel)
		if delete_q.execute() == 0:
			print "Nothing to delete"
		return

	if sys.argv[2] == "batch":
		if len(sys.argv) <= 3:
			raise Exception("No ID supplied")
		todel = int(sys.argv[3])
		for batch in Batch.select().where(Batch.id == todel):
			print "DELETE: " + str(batch)
		delete_q = Batch.delete().where(Batch.id == todel)
		if delete_q.execute() == 0:
			print "Nothing to delete"
		return

	if sys.argv[2] == "student":
		if len(sys.argv) <= 3:
			raise Exception("No ID supplied")
		todel = int(sys.argv[3])
		for student in Student.select().where(Student.id == todel):
			print "DELETE: " + str(student)
		delete_q = Student.delete().where(Student.id == todel)
		if delete_q.execute() == 0:
			print "Nothing to delete"

def action_print_batch_by_school(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `print_batch_by_school`")

	schoolid = int(sys.argv[2])
	#make sure school exists
	if not School.select().where(School.id == schoolid):
		print "School not found"
		return

	#print all batches associated with school
	for item in Batch.select().where(Batch.school == schoolid):
		print item

def action_print_student_by_batch(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `print_student_by_batch`")

	batchid = int(sys.argv[2])
	if not Batch.select().where(Batch.id == batchid):
		print "Batch not found"
		return

	for item in Student.select().where(Student.batch == batchid):
		print item

def action_print_student_by_school(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `print_student_by_school`")

	schoolid = int(sys.argv[2])
	if not School.select().where(School.id == schoolid):
		print "School not found"
		return

	for batch in Batch.select().where(Batch.school == schoolid):
		for student in Student.select().where(Student.batch == batch):
			print student

def action_print_family(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `print_family`")

	family_name = sys.argv[2]

	for student in Student.select().where(Student.last_name == family_name):
		print student

def action_age_average(*args, **kwargs):
	total = 0
	count = 0
	batch_id = None
 	if len(sys.argv) > 2:
		batch_id == int(sys.argv[2])
	if batch_id:
		for student in Student.select().where(Student.batch == batch_id):
			total += student.age
			count += 1
		print int(total/count)
		return
	for student in Student.select():
		total += student.age
		count += 1
	print int(total/count)

def action_change_batch(*args, **kwargs):
	if len(sys.argv) <= 3:
		raise Exception("Too few arguments for `change_batch`")
	student_id = int(sys.argv[2])
	batch_id = int(sys.argv[3])
	students = Student.select().where(Student.id == student_id)
	batches = Batch.select().where(Batch.id == batch_id)
	if not students:
		print "Student not found"
	elif not batches:
		print "Batch not found"
	elif students[0].batch == batches[0]:
		print str(students[0]) + " already in " + str(batches[0])
	else:
		students[0].batch = batches[0].id
		students[0].save()
		print str(students[0]) + " has been move to " + str(batches[0])

def action_print_all(*args, **kwargs):
	for school in School.select():
		print school
		for batch in Batch.select().where(Batch.school == school):
			print "\t" + str(batch)
			for student in Student.select().where(Student.batch == batch):
				print "\t\t" + str(student)


if __name__ == '__main__':
	actions = {
		"create": action_create,
		"print": action_print,
		"insert": action_insert,
		"delete": action_delete,
		"print_batch_by_school": action_print_batch_by_school,
		"print_student_by_batch": action_print_student_by_batch,
		"print_student_by_school": action_print_student_by_school,
		"print_family": action_print_family,
		"age_average": action_age_average,
		"change_batch": action_change_batch,
		"print_all": action_print_all,
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
