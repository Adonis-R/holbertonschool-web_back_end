const name = 'Alice';
let age = 30;
const hobbies = ['reading', 'traveling', 'swimming'];

function introduce(personName, personAge, personHobbies) {
  console.log('Name: ' + personName);
  console.log('Age: ' + personAge);
  console.log('Hobbies: ' + personHobbies.join(', '));
}

introduce(name, age, hobbies);

