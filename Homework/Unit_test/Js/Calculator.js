export class Calculator {
    sum(number1, number2) {
        return number1 + number2;
    }

    subtract(number1, number2) {
        return number1 - number2;
    }

    multiply(number1, number2) {
        return number1 * number2;
    }

    divide(number1, number2) {
        if (number2 === 0) {
            throw new Error("Cannot divide by zero");
        }
        return number1 / number2;
    }
}
