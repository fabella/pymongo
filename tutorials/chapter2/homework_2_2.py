import sys

import pymongo


def drop_lowest_homework_grades():
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.students
    grades = db.grades

    try:
        query = {'type': 'homework'}

        scores = grades.find(query).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

        current_user = None
        for score in scores:
            if current_user is None:
                current_user = score['student_id']
                grades.remove(score)
            if current_user != score['student_id']:
                current_user = score['student_id']
                grades.remove(score)

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


if __name__ == '__main__':
    drop_lowest_homework_grades()

