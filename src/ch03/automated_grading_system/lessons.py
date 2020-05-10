from grader import Assignment, Grader


class IntroPython:
    def lesson(self):
        return f"""
            Hello {self.student}. Define two variables, an integer named 'a' with value 1 and a string named 'b' with value 'hello'.
        """

    def check(self,code):
        return code == "a = 1 \nb = 'hello'"

class Statistics(Assignment):
    """
    Explicitly extend Assignment class
    """
    def lesson(self):
        return(
            "Good work so far,"
            + self.student
            + ". Now calculate the average of the numbers "
            + " 1, 5, 18, -3 and assign to a variable named 'avg'"
            )

    def check(self, code):
        import statistics

        code = "import statistics\n" + code

        local_vars = {}
        global_vars = {}
        exec(code , global_vars, local_vars)

        return local_vars.get("avg") == statistics.mean([1, 5, 18, -3])

# Check IntroPython 
print("issubclass(IntroPython,Assignment):",issubclass(IntroPython,Assignment))

# Register IntroPython without instantiating
grader = Grader()
itp_id = grader.register(IntroPython)
stat_id = grader.register(Statistics)

grader.start_assignment("Tammy",itp_id)
print("Tammy's Lesson:", grader.get_lesson("Tammy"))
print("Tammy's Check:",grader.check_assignment("Tammy","a = 1 ; b = 'hello'"))
print("Tammy's another Check:", grader.check_assignment("Tammy","a = 1 \nb = 'hello'"))
print(grader.assignment_summary("Tammy"))

grader.start_assignment("Tammy",stat_id)
print("Tammy's Lesson:", grader.get_lesson("Tammy"))
print("Tammy's check:", grader.check_assignment("Tammy","avg=5.25"))
print("Tammy's another check:", grader.check_assignment("Tammy","avg = statistics.mean([1, 5, 18, -3])"))
print(grader.assignment_summary("Tammy"))

