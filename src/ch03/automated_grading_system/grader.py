import abc
import uuid


class Assignment(metaclass=abc.ABCMeta):
    """
    Abstract Base Class for Assignments.
    """
    @abc.abstractmethod
    def lesson(self, student):
        pass

    @abc.abstractmethod
    def check(self, code):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented


class AssignmentGrader:
    """Manages attempts made by students for Assignments
    """
    def __init__(self, student, AssignmentClass):
        self.assignment = AssignmentClass()
        self.assignment.student = student
        self.attempts = 0
        self.correct_attempts = 0

    def check(self, code):
        self.attempts += 1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts += 1

        return result

    def lesson(self):
        return self.assignment.lesson()


class Grader:
    """
    Manages assignments available to students and their status
    """
    def __init__(self):
        self.student_graders = {}
        self.assignment_classes = {}

    def register(self, assignment_class):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError(
                "Your class does not have the right methods"
            )

        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id

    def start_assignment(self, student, id):
        """
        Allows student to start an Assignment when provided 
        with the id of assignment
        """
        self.student_graders[student] = AssignmentGrader(student, self.assignment_classes[id])
        
    def get_lesson(self, student):
        """
        Provide with students with lesson to work on
        """
        assignment = self.student_graders[student]
        return assignment.lesson()
    
    def check_assignment(self, student, code):
        """
        Checks student's answer for the assignment
        """
        assignment = self.student_graders[student]
        return assignment.check(code)

    def assignment_summary(self, student):
        """
        Provides a summary of a student's current assignment progress
        """
        grader = self.student_graders[student]
        return f"""{student}'s attempts at {grader.assignment.__class__.__name__}:
        attempts: {grader.attempts}
        correct: {grader.correct_attempts}
        passed: {grader.correct_attempts}
        """