const sinon = require('sinon');
const expect = chai.expect;
const chai = require('chai');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');


describe('Tests sendPaymentRequestToApi function', function() {
    let spies;
    beforeEach(() => {
        spies = sinon.spy(console, 'log');
    });
    afterEach(() => {
        spies.restore();
    })
    it('validate the usage of the Utils function', function() {
      
      const calcStub = sinon.stub(Utils, 'calculateNumber').returns(10);

      sendPaymentRequestToApi(100, 20);

      expect(spies.calledOnce).to.be.true;
      expect(spies.calledWith('The total is: 10')).to.be.true;

      expect(calcStub.calledOnce).to.be.true;
      expect(calcStub.args[0][0]).to.equal('SUM');
      expect(calcStub.args[0][1]).to.equal(100);
      expect(calcStub.args[0][2]).to.equal(20);
   
      calcStub.restore();
    });
});
