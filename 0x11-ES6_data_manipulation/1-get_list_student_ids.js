export default function getListStudentIds(people) {
  if (!(Array.isArray(people))) return [];
  return people.map((ids) => ids.id);
}
