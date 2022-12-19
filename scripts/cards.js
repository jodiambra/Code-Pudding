const initialCards = [
  {
    name: "2010 music",
    image: "images/2010.png",
    description: "i love 2010 yo!",
    link: "http://127.0.0.1:5500/playlist.html",
  },
  {
    name: "2011 music",
    image: "./images/2011.jpeg",
    description: "help!",
    link: "http://127.0.0.1:5500/2011.html",
  },
  {
    name: "2012 music",
    image: "./images/2012.jpeg",
    description: "longer longr longersdf it never ends sww!!!!!!!!!!!!!",
    link: "http://127.0.0.1:5500/2012.html",
  },
  {
    name: "2013 music",
    image: "./images/2013.jpeg",
    description: "i love 2013 yo!",
    link: "http://127.0.0.1:5500/2013.html",
  },
  {
    name: "2014 music",
    image: "./images/2014.jpeg",
    description: "lol",
    link: "http://127.0.0.1:5500/2014.html",
  },
  {
    name: "2015 music",
    image: "./images/2015.jpeg",
    description: "i love 2010 yo!",
    link: "http://127.0.0.1:5500/2015.html",
  },
  {
    name: "2016 music",
    image: "./images/2016.jpeg",
    description: "i love 2010 yo!",
    link: "http://127.0.0.1:5500/2016.html",
  },
  {
    name: "2017 music",
    image: "./images/2017.jpeg",
    description: "i love 2010 yo!",
    link: "http://127.0.0.1:5500/2017.html",
  },
  {
    name: "2018 music",
    image: "./images/2018.jpeg",
    description: "i love 2010 yo!",
    link: "http://127.0.0.1:5500/2018.html",
  },

  {
    name: "2019 music",
    image: "./images/2019.jpeg",
    description: "i love 2010 yo!",
    link: "http://127.0.0.1:5500/2019.html",
  },
  {
    name: "2020 music",
    image: "./images/2020.jpeg",
    description: "i love 2010 yo!",
    link: "http://127.0.0.1:5500/2020.html",
  },
];

/*
                      Selectors
############################################################
*/
const cardsContainer = document.querySelector(".cards");

const cardSelector = "#card__template";

console.log(cardsContainer);

/*
                      Card Class
############################################################
*/
class Card {
  constructor(data, selector) {
    this._name = data.name;
    this._image = data.image;
    this._description = data.description;
    this._link = data.link;
    this._selector = selector;
  }
  _getTemplate() {
    //prettier-ignore
    return document.querySelector(this._selector).content.querySelector(".card").cloneNode(true);
  }

  getElement() {
    this._element = this._getTemplate();

    this._element.querySelector(
      ".card__image"
    ).style.backgroundImage = `url(${this._image})`;

    this._element.querySelector(".card__subtitle").textContent = this._name;

    this._element.querySelector(".card__description").textContent =
      this._description;

    this._element.querySelector(".card__link").href = this._link;

    return this._element;
  }
}

initialCards.forEach(function (cardElement) {
  const card = new Card(cardElement, cardSelector);
  cardsContainer.append(card.getElement());
});

/*
                      Card Rendering 
############################################################
*/

/*

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
*/
