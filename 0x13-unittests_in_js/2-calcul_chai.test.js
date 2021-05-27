const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('Tests calculateNumber function', () => {
    it('Sum', () => {
        expect(calculateNumber('SUM', 11, 11)).to.equal(22);
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('Subtract', () => {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('Divide', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
});
