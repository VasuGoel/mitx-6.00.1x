def grader(marks):
    """
    marks: list of marks of students in integer

    Return average marks of students
    """

    # raise AssertionError if list is empty
    try:
        assert not len(marks) == 0, 'list cannot be empty'
    except AssertionError as ae:
        print(f'AssertionError: {ae}')
        return 0.0
    else:
        sum = 0
        for m in marks:
            sum += m
        return sum/len(marks)

# marks = [98, 87, 94, 85, 100]
marks = []
print(grader(marks))
