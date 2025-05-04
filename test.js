const fetchData = async () => {
  const url = 'http://127.0.0.1:8000/api/note/';
  const data = await fetch(url);
  const response = await data.json();
  console.log(response);
};
console.log('hehehe');
console.log('Michael is a fool!!!');
fetchData();
