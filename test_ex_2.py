<body>
    <div class="container theme-showcase" role="main">
        <div class="page-header">
            <tr>
                <th>student-id</th>
                <th>student first name</th>
                <th>student last name</th>
                <th>subject id</th>
                <th>subject name</th>
                <th>teacher first name</th>
                <th>teacher last name</th>
            </tr>

            {% for r in result %}
            <tr>
                <th>{{ r.student_id }}</th>
                <th>{{ r.f_name }}</th>
                <th>{{ r.l_name }}</th>
                <th>{{ r.subject_id }}</th>
                <th>{{ r.grade}}</th>
                <th>{{ r.f_tname}}</th>
                <th>{{ r.l_tname}}</th>
            </tr>
        </div>
        {% endfor %}
    </div> <!--/container -->
</body>

 result = session.query(Students_table.student_id,Students_table.f_name,Students_table.l_name,Registration_table.subject_id,Subject_table.subject_name,Registration_table.grade,Teachers_table.f_tname,Teachers_table.l_tname).outerjoin(Registration_table,Students_table.student_id == Registration_table.student_id).outerjoin(Subject_table,Registration_table.subject_id == Subject_table.subject_id).join(Teachers_table,Subject_table.teacher_id == Teachers_table.teacher_id).all()