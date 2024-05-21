export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  let str = '';
  for (const elem of set) {
    if (elem.startsWith(startString)) {
      const newElem = elem.slice(startString.length);
      if (str.length > 0) {
        str += '-';
      }
      str += newElem;
    }
  }
  return str;
}
