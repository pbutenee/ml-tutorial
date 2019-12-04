c = get_config()
c.CourseDirectory.db_assignments = [dict(name="1", duedate="2019-12-09 17:00:00 UTC")]
c.CourseDirectory.db_students = [
    dict(id="foo", first_name="foo", last_name="foo")
]
c.ClearSolutions.code_stub = {'python': '##### Implement this part of the code #####\nraise NotImplementedError()'}
