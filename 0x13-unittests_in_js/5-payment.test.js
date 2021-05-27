const chai = require('chai');
const sinon = require('sinon');
const expect = chai.expect;
const chai = require('chai');
const sendPaymentRequestToApi = require('./5-payment.js');
const Utils = require('./utils');


describe('Tests sendPaymentRequestToAPI function', function() {
  let consoleSpy;
  beforeEach(() => {
  consoleSpy = sinon.spy(console, 'log');
  });
  afterEach(() => {
      consoleSpy.restore();
  })
  it('different parameters', function() {
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
  })
  it('parameters with the same value', function() {
    sendPaymentRequestToApi(10, 10);
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
  })
});
