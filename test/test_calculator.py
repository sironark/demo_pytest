from src.calculator import Calculator
import pytest



#Oracle
class TestCalculator():

    skipComplexTest = True

    def setup_class(self):
        #print("\n Setup executado uma unica vez")
        pass

    def setup_method(self):
        self.calc = Calculator()
        #print("\n Setup executado antes de cada teste")

    def teardown_class(self):
        #print("\n Teardown executado uma unica vez")
        pass

    def teardown_method(self):
        #print("\n Teardown executado apos cada teste ")
        pass

    @pytest.mark.parametrize(("a", "b", "expected"), [(1,2,3), (1,1,2), (2,3,5), (1,0,1)])
    def test_addition_generic(self, a, b, expected):
        assert self.calc.addition(a,b) == expected

    def test_addition(self):
        #self.calc = Calculator()
        assert self.calc.addition(2,2) == 4

    @pytest.mark.skip(reason="Duplicated test case")
    def test_addition2(self):
        #self.calc = Calculator()
        assert self.calc.addition(10,10) == 20

    def test_subtraction(self):
        #self.calc = Calculator()
        assert self.calc.subtraction(2,2) == 0

    def test_multiplication(self):
        #self.calc = Calculator()
        assert self.calc.multiplication(10,2) == 20
    
    def test_division(self):
        #self.calc = Calculator()
        assert self.calc.division(10,2) == 5

    @pytest.mark.skipif(skipComplexTest, reason="Skipping complex test")
    def test_division_by_zero (self):
        #self.calc = Calculator()
        with pytest.raises(ZeroDivisionError):
            self.calc.division(2/0)