import Currency from './3-currency.js';

export default  class Pricing{
  constructor(amount, currency) {
    if (typeof (amount) === 'string') {
      this._amount = amount;
    }
  
    if (typeof(currency) === 'string') {
      this._currency = currency;
    }
  }

  set amount(value) {
    if (typeof (amount) === 'string') {
      this._amount = amount;
    } else {
      throw new Error(TypeError('amount must be a String'));
    }
  }

  get amount() {
    return this._amount;
  }

  set currency(value) {
    if (typeof (currency) === 'string') {
      this._currency = currency;
    } else {
      throw new Error(TypeError('currency must be a String'));
    }
  }

  get currency() {
    return this._currency;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
