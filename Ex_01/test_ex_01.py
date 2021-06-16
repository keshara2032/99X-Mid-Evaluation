import unittest
import ex_01 as validator

class TestValidateString(unittest.TestCase):
    
    def test_validateString_validCases(self):
        self.assertTrue(validator.validateString("test"))
        self.assertTrue(validator.validateString("()"))
        self.assertTrue(validator.validateString("{}"))
        self.assertTrue(validator.validateString("[]"))
        self.assertTrue(validator.validateString("test(func[1,2])"))
        self.assertTrue(validator.validateString("test(func{1,2})"))
        self.assertTrue(validator.validateString("[test(func{1,2}),pop[1],peek({2,3,4})]"))
        self.assertTrue(validator.validateString("[({[({})]})]"))

    def test_validateString_invalidCases(self):
        self.assertFalse(validator.validateString("test("))        
        self.assertFalse(validator.validateString("test["))        
        self.assertFalse(validator.validateString("test{"))        
        self.assertFalse(validator.validateString("("))        
        self.assertFalse(validator.validateString("{"))  
        self.assertFalse(validator.validateString("["))        
        self.assertFalse(validator.validateString(")"))        
        self.assertFalse(validator.validateString("}"))  
        self.assertFalse(validator.validateString("]"))  
        self.assertFalse(validator.validateString("test(func()]"))        
        self.assertFalse(validator.validateString("test{(func()]"))   
        self.assertFalse(validator.validateString("[({[({(})]})]"))



if __name__ == '__main__':
    unittest.main()