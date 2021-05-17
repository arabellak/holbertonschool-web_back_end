export default class Car {
  constructor(brand, motor, color) {
		if (typeof brand === 'string') {
			this._brand = brand;
		}
		if (typeof motor === 'string') {
			this._motor = motor;
		}
		if (typeof color === 'string') {
			this._color = color;
		}
  }

	static get [Symbol.species]() {
		return this;
	}

	cloneCar() {
		const cloneC = this.constructos;
		return new cloneC[Symbol.species](this._brand, this._motor, this._color)
	}
}
