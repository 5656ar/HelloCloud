SELECT Students.student_id, Students.f_name, Students.l_name, Subjects.subject_id, Subjects.subject_name, Registration.grade, Teachers.f_name, Teachers.l_name FROM Students
JOIN Registration 
ON Registration.student_id = Students.student_id
JOIN Subjects
ON Registration.subject_id = Subjects.subject_id
JOIN Teachers
on Teachers.teacher_id = Subjects.teacher_id



