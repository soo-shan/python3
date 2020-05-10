class IntroPython:
    def __init__(self):
        self.student = "Alice"
    def lesson(self):
        return f"""
            Hello {self.student}. 
            Define two variables, an integer named a with value 1 and
            a  string named b with value 'hello'.
        """

    def check(self,code):
        return code == "a = 1 \nb = 'hello'"
