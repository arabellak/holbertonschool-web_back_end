export default function getStudentIdsSum(studentId){
    let reducer = (accumulator, currentValue) => accumulator + currentValue.id;
    return studentId.reduce(reducer, 0);
}
