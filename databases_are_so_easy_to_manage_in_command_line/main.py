import sys
from models import *

def action_create(*args, **kwargs):
	my_models_db.create_tables([School, Batch, User, Student, Exercise])

def action_print(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `print`")

	tables = {
		"school": School,
		"batch": Batch,
		"student": Student,
		"user": User,
		"exercise": Exercise,
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

	if sys.argv[2] == "exercise":
		if len(sys.argv) < 6:
			raise Exception("Too few arguments for `insert exercise`")
		student_id = sys.argv[3]
		subject = sys.argv[4]

		res = False
		for sub in Exercise.SUBJECTS:
			if sub[0] == subject:
				subject = sub[1]
				res = True

		if not res:
			raise Exception("Invalid subject")

		note = sys.argv[5]
		ex = Exercise()
		ex.student = student_id
		ex.subject = subject
		ex.note = note
		ex.save()

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

	if sys.argv[2] == "exercise":
		if len(sys.argv) <= 3:
			raise Exception("No ID supplied")
		todel = int(sys.argv[3])
		for ex in Exercise.select().where(Exercise.id == todel):
			print "DELETE: " + str(ex)
		delete_q = Exercise.delete().where(Exercise.id == todel)
		if delete_q.execute() == 0:
			print "Nothing to delete"

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
				for ex in Exercise.select().where(Exercise.student == student):
					print "\t\t\t" + str(ex)

def action_note_average_by_student(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `note_average_by_student`")
	student_id = sys.argv[2]
	if not Student.select().where(Student.id == student_id):
		print "Student not found"
		return
	for subject in Exercise.SUBJECTS:
		total = 0
		count = 0
		for ex in Exercise.select().where(Exercise.student == student_id, Exercise.subject == subject[1]):
			total += ex.note
			count += 1
		if count == 0:
			count += 1
		print str(subject[1]) + ": " + str(total/float(count))

def action_note_average_by_batch(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `note_average_by_batch`")
	batch_id = sys.argv[2]
	if not Batch.select().where(Batch.id == batch_id):
		print "Batch not found"
		return
	for subject in Exercise.SUBJECTS:
		total = 0
		count = 0
		for student in Student.select().where(Student.batch == batch_id):
			for ex in Exercise.select().where(Exercise.student == student, Exercise.subject == subject[1]):
				total += ex.note
				count += 1
		if count == 0:
			continue;
		print str(subject[1]) + ": " + str(total/float(count))

def action_note_average_by_school(*args, **kwargs):
	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `note_average_by_school`")
	school_id = sys.argv[2]
	if not School.select().where(School.id == school_id):
		print "School not found"
		return
	for subject in Exercise.SUBJECTS:
		total = 0
		count = 0
		for batch in Batch.select().where(Batch.school == school_id):
			for student in Student.select().where(Student.batch == batch):
				for ex in Exercise.select().where(Exercise.student == student, Exercise.subject == subject[1]):
					total += ex.note
					count += 1
		if count == 0:
			continue;
		print str(subject[1]) + ": " + str(total/float(count))

def action_top_batch(*args, **kwargs):
	def get_top_batch_for_subject(subject, batch_id):
		best = None
		best_score = -1
		students = Student.select().where(Student.batch == batch_id)
		if not students:
			print "No students in batch"
			return
		for student in students:
			total = 0
			count = 0
			for ex in Exercise.select().where(Exercise.student == student, Exercise.subject == subject[1]):
				total += ex.note
				count += 1
			if count == 0:
				count += 1
			avg = total/float(count)
			if avg > best_score:
				best = student
				best_score = avg
		return (best_score, str(best))

	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `top_batch`")
	batch_id = sys.argv[2]
	if not Batch.select().where(Batch.id == batch_id):
		print "Batch not found"
		return
	if len(sys.argv) > 3:
		subject = sys.argv[3]
		best = get_top_batch_for_subject(subject, batch_id)
		if best:
			print best[1]
	else:
		winners = []
		for subject in Exercise.SUBJECTS:
			best = get_top_batch_for_subject(subject, batch_id)
			if best:
				winners.append(best)
		best = max(winners, key=lambda x: x[0])
		if best:
			print best[1]

def action_top_school(*args, **kwargs):
	def get_top_school_for_subject(subject, school_id):
		best = None
		best_score = -1
		batches = Batch.select().where(Batch.school == school_id)
		if not batches:
			print "No batches in school"
			return
		for batch in batches:
			students = Student.select().where(Student.batch == batch)
			for student in students:
				total = 0
				count = 0
				for ex in Exercise.select().where(Exercise.student == student, Exercise.subject == subject[1]):
					total += ex.note
					count += 1
				if count == 0:
					count += 1
				avg = total/float(count)
				if avg > best_score:
					best = student
					best_score = avg
		return (best_score, str(best))

	if len(sys.argv) <= 2:
		raise Exception("Too few arguments for `top_school`")
	school_id = sys.argv[2]
	if not School.select().where(School.id == school_id):
		print "School not found"
		return
	if len(sys.argv) > 3:
		subject = sys.argv[3]
		best = get_top_school_for_subject(subject, school_id)
		if best:
			print best[1]
	else:
		winners = []
		for subject in Exercise.SUBJECTS:
			best = get_top_school_for_subject(subject, school_id)
			if best:
				winners.append(best)
		best = max(winners, key=lambda x: x[0])
		if best:
			print best[1]

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
		"note_average_by_student": action_note_average_by_student,
		"note_average_by_batch": action_note_average_by_batch,
		"note_average_by_school": action_note_average_by_school,
		"top_batch": action_top_batch,
		"top_school": action_top_school,
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
