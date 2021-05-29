export default class Airport {
  constructor(name, code) {
    if (typeof (name) === 'string') {
      this._name = name;
    }

    if (typeof (code) === 'string') {
      this._code = code;
    }
  }

  get [Symbol.toString]() {
    return this._code;
  }
}
