import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  set amount(value) {
    if (typeof (value) === 'number') {
      this._amount = value;
    }
  }

  get amount() {
    return this._amount;
  }

  set currency(value) {
    if (value instanceof Currency) {
      this._currency = value;
    }
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
