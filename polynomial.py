import operator
import math

class Polynomial(object):
    def __init__(self, coeffs):
        if not isinstance(coeffs, list):
            raise TypeError("Incorrect type of argument")
        if len(coeffs) == 0:
            raise TypeError("coeffs is empty")
        if not all(isinstance(c, (int, float)) for c in coeffs):
            raise TypeError("Some of constants have incorrect type")
        senior_degree = next((i for i, c in enumerate(coeffs) if c != 0), -1)
        self.coeffs = coeffs[senior_degree:]

    @property
    def degree(self):
        return len(self.coeffs) - 1

    def __check_inf_values(self, array):
        if isinstance(array, list):
            if not all(not math.isinf(c) for c in array):
                raise TypeError("Value of some coefficients are overflow")
        else:
            if math.isinf(array):
                raise TypeError("Value of coefficient is overflow")

    def __eq_inf_values(self, other):
        for i, (self_coef, other_coef) in enumerate(zip(self.coeffs, other.coeffs)):
            if math.isinf(self_coef):
                if math.isinf(other_coef):
                    continue
                else:
                    return False
            else:
                if math.isinf(self_coef):
                    return False
                else:
                    if self_coef == other_coef:
                         continue
                    else:
                        return False
        return True

    def __sign_float(self, value):
        if value > 0:
            return '+x'
        elif value < 0:
            return '-x'
        else:
            return '0'

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if self.degree > other.degree:
                a1 = self.coeffs
                a2 = [0] * (self.degree - other.degree) + other.coeffs
            elif other.degree > self.degree:
                a1 = [0] * (other.degree - self.degree) + self.coeffs
                a2 = other.coeffs
            else:
                a1 = self.coeffs
                a2 = other.coeffs
            self.__check_inf_values(self.coeffs)
            self.__check_inf_values(other.coeffs)
            return Polynomial(list(map(operator.add, a1, a2)))
        elif isinstance(other, (int, float)):
            result = Polynomial(self.coeffs)
            result.coeffs[-1] += other
            self.__check_inf_values(self.coeffs)
            self.__check_inf_values(other)
            return result
        else:
            raise TypeError("Some of constants have incorrect type")

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            if len(self.coeffs) == 1:
                if math.isinf(other):
                    if math.isinf(self.coeffs):
                        return True
                    else:
                        return False
                else:
                    if math.isinf(self.coeffs):
                        return False
                    else:
                        return self.coeffs[0] == other
            else:
                return False
        elif isinstance(other, Polynomial):
            return self.__eq_inf_values(other)
        else:
            raise TypeError("Some of constants have incorrect type")

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            self.__check_inf_values(self.coeffs)
            self.__check_inf_values(other.coeffs)
            result = [0] * (self.degree + other.degree + 1)
            for i, self_coef in enumerate(self.coeffs):
                for j, other_coef in enumerate(other.coeffs):
                    result[i + j] += self_coef * other_coef
            return Polynomial(result)
        elif isinstance(other, (int, float)):
            self.__check_inf_values(self.coeffs)
            self.__check_inf_values(other)
            result = Polynomial([coef * other for coef in self.coeffs])
            return result
        else:
            raise TypeError("Some of constants have incorrect type")

    def __str__(self):
        result = ""
        for i, coef in enumerate(self.coeffs):
            if coef != 0:
                if self.degree == 0:
                    result += str(coef)
                elif i == self.degree:
                    result += "{:+}".format(coef)
                elif i == self.degree - 1:
                    if abs(coef) == 1:
                        result += self.__sign_float(coef)
                    else:
                        result += "{:+}x".format(coef)
                else:
                    if abs(coef) == 1:
                        result += self.__sign_float(coef) + str(self.degree - i)
                    else:
                        result += "{:+}x{}".format(coef, str(self.degree - i))
        return result.lstrip("+") if result else "0"