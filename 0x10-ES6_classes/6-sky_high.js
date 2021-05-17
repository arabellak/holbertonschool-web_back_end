import Building from './5-building.js';

export default class SkyHighBuilding {
	constructor(sqtf, floors) {
		if (typeof(sqft) === 'number') {
      this._sqft = sqft;
    }

		if (typeof(floors) === 'number') {
      this._floors = floors;
    }
	}

	set sqft(value) {
    this._sqft = value;
  }

  get sqft() {
    return this.__sqft;
  }

	set floors(value) {
    this._floors = value;
  }

  get floors() {
    return this._floors;
  }

	evacuationWarningMessage() {
		return `Evacuate slowly the ${this.floors} floors`;
	}
}
