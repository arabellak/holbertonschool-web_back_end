import Building from './5-building';

export default class SkyHighBuilding {
	constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

	set floors(value) {
    if (typeof floors === 'number'){ 
      this._floors = value;
    }
  }

  get floors() {
    return this._floors;
  }

	evacuationWarningMessage() {
		return `Evacuate slowly the ${this.floors} floors`;
	}
}
