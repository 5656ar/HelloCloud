from sqlalchemy import VARCHAR, create_engine, MetaData, Table, Integer, Column, String, ForeignKey, Text, insert, CHAR

metadata = MetaData()

engine = create_engine('sqlite:///test_03.sqlite3')

students = Table('Students', metadata,
    Column('student_id', CHAR(13), primary_key=True),
    Column('f_name', VARCHAR(30), nullable=False),
    Column('l_name', VARCHAR(30),  nullable=False),
    Column('e_mail', VARCHAR(30),  nullable=False),    
)

teachers = Table('Teachers', metadata,
    Column('teacher_id', CHAR(3), primary_key=True),
    Column('f_name', VARCHAR(30), nullable=False),
    Column('l_name', VARCHAR(30),  nullable=False),
    Column('e_mail', VARCHAR(30),  nullable=False),    
)

subjects = Table('Subjects', metadata,
    Column('subject_id', CHAR(15), primary_key=True),
    Column('subject_name', VARCHAR(50), nullable=False),
    Column('creadit', Integer,  nullable=False),
    Column('teacher_id', ForeignKey('Teachers.teacher_id') )   
)

registration = Table('Registration', metadata,
    Column('student_id', CHAR(13), nullable=False),
    Column('subject_id', CHAR(15), nullable=False),
    Column('year', CHAR(4),  nullable=False),
    Column('semester', CHAR(1),  nullable=False),
    Column('grade', CHAR(2))    
)

conn = engine.connect()

metadata.create_all(engine)

ins = insert(students)

ins_list_students = [{
    "student_id" : "6406022620037",
    "f_name" : "Bunnapon",
    "l_name" : "Takumwan",
    "e_mail" : "s6406022620037@email.kmutnb.ac.th"
    },
    {
    "student_id" : "6406022620011",
    "f_name" : "Jakapat",
    "l_name" : "Jodduangchan",
    "e_mail" : "s6406022620011@email.kmutnb.ac.th"
    },
    {
    "student_id" : "6406022620031",
    "f_name" : "Chalongrath",
    "l_name" : "Kodlord",
    "e_mail" : "s6406022620011@email.kmutnb.ac.th"
    },

]


ins_list_teacher = [{
    "teacher_id" : "AMK",
    "f_name" : "Anirach",
    "l_name" : "Mingkhwan",
    "e_mail" : "Anirach@email.kmutnb.ac.th"
    },
    {
    "teacher_id" : "WKN",
    "f_name" : "Watcherachai",
    "l_name" : "Kongsiriwattana",
    "e_mail" : "Watcherachai@email.kmutnb.ac.th"
    },
    {
    "teacher_id" : "STS",
    "f_name" : "Sarayoot",
    "l_name" : "Tanessakulwattana",
    "e_mail" : "Sarayoot@email.kmutnb.ac.th"
    },

]


ins_list_subject = [{
    "subject_id" : "060233112",
    "subject_name" : "DATA ENGINEERING",
    "creadit" : "3",
    "teacher_id" : "STS"
    },
    {
    "subject_id" : "060233113",
    "subject_name" : "ADVANCED COMPUTER PROGRAMMIN",
    "creadit" : "3",
    "teacher_id" : "AMK"
    },
    {
    "subject_id" : "060233205",
    "subject_name" : "ADVANCED NETWORK AND PROTOCO	",
    "creadit" : "3",
    "teacher_id" : "ANM"
    },

]

ins_list_registration = [{
    "student_id" : "6406022620037",
    "subject_id" : "060233112",
    "year" : "2565",
    "semester" : "1",
    "grade" : "A"
    },
    {
    "student_id" : "6406022620037",
    "subject_id" : "060233113",
    "year" : "2565",
    "semester" : "1",
    "grade" : "A"
    },
    {
    "student_id" : "6406022620037",
    "subject_id" : "060233205",
    "year" : "2565",
    "semester" : "1",
    "grade" : "A"
    },

    {
    "student_id" : "6406022620011",
    "subject_id" : "060233112",
    "year" : "2565",
    "semester" : "1",
    "grade" : "A"
    },
    {
    "student_id" : "6406022620011",
    "subject_id" : "060233113",
    "year" : "2565",
    "semester" : "1",
    "grade" : "A"
    },
    {
    "student_id" : "6406022620011",
    "subject_id" : "060233205",
    "year" : "2565",
    "semester" : "1",
    "grade" : "A"
    },

    {
    "student_id" : "6406022620031",
    "subject_id" : "060233112",
    "year" : "2565",
    "semester" : "1",
    "grade" : "A"
    },
    {
    "student_id" : "6406022620031",
    "subject_id" : "060233113",
    "year" : "2565",
    "semester" : "1",
    "grade" : "A"
    },
    {
    "student_id" : "6406022620031",
    "subject_id" : "060233205",
    "year" : "2565",
    "semester" : "1",
    "grade" : "A"
    },
]


r = conn.execute(insert(students), ins_list_students)
r.rowcount

r = conn.execute(insert(teachers), ins_list_teacher)
r.rowcount

r = conn.execute(insert(subjects), ins_list_subject)
r.rowcount

r = conn.execute(insert(registration), ins_list_registration)
r.rowcount