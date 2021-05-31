const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const expect = chai.expect;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('Tests getPaymentTokenFromAPI function', function() {
  it('return a resolve promise', function(done) {
    getPaymentTokenFromAPI(true).then((res) => {
      expect(res).to.eql({data: 'Successful response from the API' })
    })
    done();
  });
});
