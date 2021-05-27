const chai = require("chai");
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai.js');

describe("Tests for calculateNumber with chai", () => {
    it("SUM", () => {
        it('Sum', function() {
            assert.strictEqual(calculateNumber('SUM', 2, 2)).to.equal(4);
            assert.strictEqual(calculateNumber('SUM', 18, 40)).to.equal(58);
            assert.strictEqual(calculateNumber('SUM', -2.0, 4)).to.equal(2);
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        });
    });
    it("SUBSTRACT", () => {
        it('Subtract', () => {
            assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -4.5)).to.equal(3.1);
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        });
    });
    it("DIVIDE", () => {
        it('Divide', () => {
            assert.equal(calculateNumber('DIVIDE', 1.4, 4.5)),to.equal(0.2);
            assert.equal(calculateNumber('DIVIDE', 4, 2)),to.equal(2);
            assert.equal(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
        });
    });
});
