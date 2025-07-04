/* eslint-disable */
export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;

    if (typeof name !== 'string') {
      throw new Error('Name is required');
    }

    if (typeof code !== 'string') {
      throw new Error('Code is required');
    }
  }

  getName() {
    return this._name;
  }

  getCode() {
    return this._code;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
