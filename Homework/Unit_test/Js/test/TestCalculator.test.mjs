import { Calculator } from '../Calculator.mjs';

describe('Calculator', () => {
    let calculator;

    beforeEach(() => {
        calculator = new Calculator();
    });

    test('should return the sum of two numbers', () => {
        expect(calculator.sum(10, 5)).toBe(15);
        expect(calculator.sum(-1, 1)).toBe(0);
        expect(calculator.sum(-1, -1)).toBe(-2);
    });

    test('should return the difference of two numbers', () => {
        expect(calculator.subtract(10, 5)).toBe(5);
        expect(calculator.subtract(-1, 1)).toBe(-2);
        expect(calculator.subtract(-1, -1)).toBe(0);
    });

    test('should return the product of two numbers', () => {
        expect(calculator.multiply(10, 5)).toBe(50);
        expect(calculator.multiply(-1, 1)).toBe(-1);
        expect(calculator.multiply(-1, -1)).toBe(1);
    });

    test('should return the quotient of two numbers', () => {
        expect(calculator.divide(10, 5)).toBe(2);
        expect(calculator.divide(-1, 1)).toBe(-1);
        expect(calculator.divide(-1, -1)).toBe(1);
        expect(() => calculator.divide(10, 0)).toThrow("Cannot divide by zero");
    });
});
