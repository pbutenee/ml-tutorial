c = get_config()
c.NbGrader.db_assignments = [dict(name="1", duedate="2017-01-01 17:00:00 UTC")]
c.NbGrader.db_students = [
    dict(id="foo", first_name="foo", last_name="foo")
]
c.ClearSolutions.code_stub = '##### Implement this part of the code #####\nraise NotImplementedError()'
