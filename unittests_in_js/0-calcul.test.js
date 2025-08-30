const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('somme sans arrondi', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('arrondi vers le haut du deuxième nombre', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('arrondi vers le bas des deux nombres', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('arrondi vers le haut des deux nombres', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('arrondi des nombres négatifs', () => {
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
  });

  it('arrondi à .5 monte', () => {
    assert.strictEqual(calculateNumber(2.5, 2.5), 6);
  });
});
