export default function getStudentIdsSum(studentId) {
  const reducer = (accumulator, currentValue) => accumulator + currentValue.id;
  return studentId.reduce(reducer, 0);
}
