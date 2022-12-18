const initialCards = [
  {
    name: "2010 music",
    link: "https://code.s3.yandex.net/web-code/yosemite.jpg",
  },
  {
    name: "2011 music",
    link: "./images/2011.jpeg",
  },
  {
    name: "2012 music",
    link: "./images/2012.jpeg",
  },
  {
    name: "2013 music",
    link: "./images/2013.jpeg",
  },
  {
    name: "2014 music",
    link: "./images/2014.jpeg",
  },
  {
    name: "2015 music",
    link: "./images/2015.jpeg",
  },
  {
    name: "2016 music",
    link: "./images/2016.jpeg",
  },
  {
    name: "2017 music",
    link: "./images/2017.jpeg",
  },
  {
    name: "2018 music",
    link: "./images/2018.jpeg",
  },
  {
    name: "2019 music",
    link: "./images/2019.jpeg",
  },
  {
    name: "2020 music",
    link: "./images/2020.jpeg",
  },
];

const cardList = document.querySelector(".card__list");
const cardTemplate =
  document.querySelector("#card-template").content.firstElementChild;

function getCards(data) {
  const cardElement = cardTemplate.cloneNode(true);
  const cardImage = cardElement.querySelector(".card__image");
  const cardName = cardElement.querySelector(".card__subtitle");

  cardImage.src = data.link;
  cardImage.src = data.name;
  cardName.src = data.name;

  return cardElement;
}

initialCards.forEach((cardData) => {
  const card = getCards(cardData);
  cardList.append(card);
});
