def studentNames(*args):
    print("Student names",args)

def studentsWithPrgLang(**kwargs):
    print(kwargs)


s = studentNames("Nazreen","Bhavya","pooja","Hema",65377.2,2341)
s = studentsWithPrgLang(arvind="java",Hema="python",pooja="Selenium")