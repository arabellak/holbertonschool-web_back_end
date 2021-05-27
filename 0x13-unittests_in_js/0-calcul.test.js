const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('Tests calculateNumber function', () => {
    it('Calculates positive numbers', function() {
        assert.equal(calculateNumber(1, 3), 4)
        assert.equal(calculateNumber(1, 3.7), 5)
    });
    it('Calculates negative numbers', () => {
        assert.equal(calculateNumber(-1, 1), 0)
        assert.equal(calculateNumber(-48, 8), -40)
        assert.equal(calculateNumber(-26, -77), -103)
    });
    it('Calculates float numbers', () => {
        assert.equal(calculateNumber(1.5, 3.7), 6)
        assert.equal(calculateNumber(-2.8, 9.8), 7)
    });
    it('No arguments', () => {
        assert(isNaN(calculateNumber()));
    })
});
