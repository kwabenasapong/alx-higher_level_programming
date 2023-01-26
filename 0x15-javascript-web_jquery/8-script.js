$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
function(data) {
  let titles = data.results.map(function(film) {
    return film.title;
  });
  for (let title of titles) {
    $('#list_movies').append(`<li>${title}</li>`);
  }

});
