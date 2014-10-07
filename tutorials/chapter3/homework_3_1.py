import sys

import pymongo


def drop_lowest_homework_grade():
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.school
    students = db.students

    try:
        # get all the students, only bring the scores
        studs = students.find({}, {'scores': True})

        for student in studs:
            # get only the homework types
            homework_scores_sorted_ascending = sorted([s for s in student['scores'] if s['type'] == "homework"],
                                                      key=lambda grade: grade['score'])
            # only delete the lowest when we have multiple homework
            if len(homework_scores_sorted_ascending) > 1:
                min_score = homework_scores_sorted_ascending[0]
                # remove the min score from the student if there are mo
                student['scores'].remove(min_score)
                # update the scores list in the database
                students.update({'_id': student['_id']}, {'$set': {'scores': student['scores']}})
                # students.save(student)
            else:
                print "Student {id} has only one homework grade".format(id=student['_id'])

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


if __name__ == '__main__':
    drop_lowest_homework_grade()

