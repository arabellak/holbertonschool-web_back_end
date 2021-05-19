export default function updateUniqueItems(mapList) {
  if (mapList instanceof Map) {
    for (const i of mapList.entries()) {
      if (i[1] === 1) {
        mapList.set(i[0], 100);
      }
    }
    return mapList;
  } throw Error('Cannot process');
}
