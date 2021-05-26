export default function calculateNumber(type, a, b){
    if (type === 'SUM') Math.round(a) + Math.round(b);
    if (type === 'SUBTRACT') Math.round(a) - Math.round(b);
    if (type === 'DIVIDE') Math.round(a) / Math.round(b);
}
