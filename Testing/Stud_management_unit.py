import unittest

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

class StudentManagemnt:
    def __init__(self):
        self.students=[]
    
    def add_student(self,student):
        self.students.append(student)
    
    def remove_student(self,roll):
        for s in self.students:
            if s.roll==roll:
                self.students.remove(s)

        

    def get_count(self):
        return len(self.students)
    
    def get_stud_roll(self,roll):
        for s in self.students:
            if s.roll==roll:    
                return s
        return None   
    
class StudManagemntTest(unittest.TestCase):
    def setUp(self):
        self.smt=StudentManagemnt()
        self.stud1=Student("Prasath",1)
        self.stud2=Student("Ravalika",2)
        self.smt.add_student(self.stud1)
        self.smt.add_student(self.stud2)
    
    def test_addstudent(self):
        stud3=Student("Iranna",3)
        self.smt.add_student(stud3)
        self.assertEqual(self.smt.get_count(),3)

    def test_remove_exi_stud(self):
        res=self.smt.remove_student(2)
        
        self.assertEqual(self.smt.get_count(),1)

    def test_remove_non_exi_stud(self):
        res=self.smt.remove_student(3)
        self.assertFalse(res)
        self.assertEqual(self.smt.get_count(),2)

    def test_getStud_roll_exi(self):
        stud=self.smt.get_stud_roll(1)
        self.assertEqual(stud.name,"Prasath")

    def test_getStud_roll_non_exi(self):
        stud=self.smt.get_stud_roll(3)
        self.assertIsNone(stud)

if __name__=='__main__':
    unittest.main()