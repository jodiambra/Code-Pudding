const ctx = document.getElementById("myChart");

const artistArray = [];

const imageSoul = new Image();
imageSoul.src = "./albumCovers/2010/soulSister.png";

var xmalhttp = new XMLHttpRequest();
var url = "Code-Pudding/figures/interactive/popartists.json";
xmalhttp.open("GET", url, true);
xmalhttp.send();
xmalhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    var data = JSON.parse(this.responseText);
    //console.log(data);
    title = data.top_10_of_2010.map(function (elem) {
      return elem.title;
    });
    popularity = data.top_10_of_2010.map(function (elem) {
      return elem.popularity;
    });

    artist = data.top_10_of_2010.map(function (elem) {
      artistArray.push(elem.artist);
      return elem.artist;
    });
    console.log(artistArray);

    new Chart(ctx, {
      type: "bar",
      data: {
        labels: title,
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
        plugins: {
          tooltip: {
            callbacks: {
              afterTitle: function (context) {
                return `${artistArray[context[0].dataIndex]}`;
              },
              beforeBody: function (context) {
                return "________________";
              },
            },
          },
        },
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  }
};
