export default class Building {
	constructor(sqft) {
		if (typeof(sqft) === 'number') {
      this._sqft = sqft;
    }
	}

	set sqft(value) {
    this._sqft = value;
  }

  get sqft() {
    return this._sqft;
  }
}
