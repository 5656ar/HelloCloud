result = session.query(Student.student_id,Student.f_name,Registration.subject_id,Subjects.subject_name,Registration.grade,Teachers.f_tname,Teachers.l_tname)\
        .outerjoin(Registration,Student.student_id == Registration.student_id)\
        .outerjoin(Subjects,Registration.subject_id == Subjects.subject_id).join(Teachers,Subjects.teacher_id == Teachers.teacher_id).all()