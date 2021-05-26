import { strictEqual } from 'assert';
import { default as calculateNumber } from './0-calcul';

describe('calculateNumber', function() {
    it('Calculates given numbers', function() {
        strictEqual(calculateNumber(1, 3), 4)
        strictEqual(calculateNumber(1, 3.7), 5)
        strictEqual(calculateNumber(1.5, 3.7), 6)
    });
    
})
