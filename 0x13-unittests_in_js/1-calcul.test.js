const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('Tests calculateNumber function', () => {
    it("Calculates the sum", () => {
        it('Sum', () => {
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        });
    })
    it("Calculates the subtract", () => {
        it('Subtract', () => {
        
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        });
    })
    it("Calculate the division", () => {
        it('Divide', () => {
            assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.3);
            assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        });
    it("Arguments", () => {
        it('No arguments', () => {
            assert(isNaN(calculateNumber()));
            assert(isNaN(calculateNumber(8)));
        });
    });
    });
});
