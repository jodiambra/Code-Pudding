const ctx = document.getElementById("myChart");

var xmalhttp = new XMLHttpRequest();
var url = "Code-Pudding/figures/interactive/popartists.json";
xmalhttp.open("GET", url, true);
xmalhttp.send();
xmalhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    var data = JSON.parse(this.responseText);
    //console.log(data);
    artist = data.popular_artists.map(function (elem) {
      return elem.artist;
    });
    popularity = data.popular_artists.map(function (elem) {
      return elem.popularity;
    });
    // console.log(popularity);

    new Chart(ctx, {
      type: "bar",
      data: {
        labels: artist,
        datasets: [
          {
            label: "Level of popularity",
            data: popularity,
            backgroundColor: "rgb(30,215,96)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  }
};
