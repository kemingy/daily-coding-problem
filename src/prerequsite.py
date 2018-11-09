# We're given a hashmap with a key courseId and value a list of courseIds, 
# which represents that the prerequsite of courseId is courseIds. Return a 
# sorted ordering of courses such that we can finish all courses.
# Return null if there is no such ordering.


def prerequsite(courses):
    ans = []

    def pre(course):
        if course in ans:
            return None

        if not courses.get(course):
            ans.append(course)
            return None

        for cs in courses.get(course):
            pre(cs)

        ans.append(course)


    for course in courses:
        pre(course)

    return ans



if __name__ == '__main__':
    for courses in [{
        'CSC300': ['CSC200', 'CSC100'],
        'CSC200': ['CSC100'],
        'CSC100': [],
    },
    {
        'CS201': ['CS100', 'CS101'],
        'CS101': ['CS104'],
        'CS100': ['CS102', 'CS103'],
        'CS103': ['CS102'],
        'CS102': [],
        'CS104': [],
    }]:
        print(prerequsite(courses))
