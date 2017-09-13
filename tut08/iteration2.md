- Important part:
 - Authentication
 * load the auth data from 'zid, password, role' csv file
 * need authentication module
 * survey pass credential to Auth module and then auth module auth password agianst database.
 * auth return the role of the user.
 * able to add user as well

 * Based on the role, taken to different dashboard.
 * admin -> same as before
 * student dashboard -> 1. All surveys to fill 2. the results of the closed survey
 * staff -> something
 - Survey system
 * Courses.csv (just course name) and (enrolments.csv (zid, course id, semester): including both students and course staff) -> potentially import them into the database
 * able to create question to be (optional/mandatory -> optional to the course) (should be able to do MCQ or Text)
 * Visualization!
- ER design in the final exam!
- CREATE - Review - live - close
- Key changes:
 - Persistence
 - Authorization
 - Workflow process
 - Handle diff response types
 - Task 2 is identical to the exam question *
 - Submission, example for db connection (good one :))
 - Final demo is on CSE. (Something -> )

- Some other resource:
 Forms in python: https://flask-wtf.readthedocs.io/en/stable/
 
