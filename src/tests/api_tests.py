import sys

sys.path.append("..")

from src.api.student_client import StudentClient

if __name__ == "__main__":

    #Simple login test

    c = StudentClient("********", (0,0,0))

    c.login()

    print(c.get_homework())