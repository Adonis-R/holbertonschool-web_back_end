document.querySelector('#add_item').addEventListener('click', () => {
  const list = document.querySelector('.my_list');
  const item = document.createElement('li');
  item.innerText = 'Item';
  list.appendChild(item);
});