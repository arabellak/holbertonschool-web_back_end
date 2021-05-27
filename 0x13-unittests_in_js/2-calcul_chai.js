function calculateNumber(type, a, b){
  if (type === 'SUM') Math.round(a) + Math.round(b);
  if (type === 'SUBTRACT') Math.round(a) - Math.round(b);
  if (type === 'DIVIDE') {
    if (Math.round(b) === 0) {
      return 'Eror'
    }
    Math.round(a) / Math.round(b);
  }
}

module.exports = calculateNumber;
