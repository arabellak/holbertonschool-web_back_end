export default function updateStudentGradeByCity(students, city, newGrades){
    return students.filter((student) => students.location === city)
}
