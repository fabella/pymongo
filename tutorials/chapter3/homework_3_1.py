import sys

import pymongo


def drop_lowest_homework_grade():
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.school
    students = db.students

    try:
        query = {}

        # get all the students
        stds = students.find(query)

        for student in stds:
            # get only the homework types
            min_score = sorted([s for s in student['scores'] if s['type'] == "homework"], key=lambda s: s['score'])[0]
            # remove the min score from the student
            student['scores'].remove(min_score)
            print "Removed Lowest homework grade from", student['name'], "of", min_score['score']
            # update the student in the database
            students.save(student)

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


if __name__ == '__main__':
    drop_lowest_homework_grade()

