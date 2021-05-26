let assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
    it('Calculates positive numbers', function() {
        assert.strictEqual(calculateNumber(1, 3), 4)
        assert.strictEqual(calculateNumber(1, 3.7), 5)
    });
    it('Calculates negative numbers', function(){
        assert.strictEqual(calculateNumber(-1, 1), 0)
        assert.strictEqual(calculateNumber(-48, 8), -40)
    });
    it('Calculates float numbers', function() {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6)
        assert.strictEqual(calculateNumber(-2.8, 9.8), 7)
    });
});
