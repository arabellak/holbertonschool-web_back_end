const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('Tests calculateNumber function', () => {
    it('Sum', () => {
        assert.strictEqual(calculateNumber('SUM', 11, 11), 22);
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('Subtract', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('Divide', () => {
            assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
            assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
    it('No arguments', () => {
            assert(isNaN(calculateNumber()));
            assert(isNaN(calculateNumber(8)));
    });
});
