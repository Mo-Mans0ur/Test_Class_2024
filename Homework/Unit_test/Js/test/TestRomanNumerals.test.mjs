import { RomanNumerals } from '../RomanNumerals.mjs';

describe('RomanNumerals', () => {
    let romanNumerals;

    beforeEach(() => {
        romanNumerals = new RomanNumerals();
    });

    test('should convert Roman numerals to decimal', () => {
        expect(romanNumerals.romanToDecimal('I')).toBe(1);
        expect(romanNumerals.romanToDecimal('IV')).toBe(4);
        expect(romanNumerals.romanToDecimal('IX')).toBe(9);
        expect(romanNumerals.romanToDecimal('LVIII')).toBe(58);
        expect(romanNumerals.romanToDecimal('MCMXCIV')).toBe(1994);
        expect(romanNumerals.romanToDecimal('MDCCCLXVII')).toBe(1867);
        expect(romanNumerals.romanToDecimal('XCIV')).toBe(94);
    });
});
