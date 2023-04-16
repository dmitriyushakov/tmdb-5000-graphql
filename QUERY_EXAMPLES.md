### 1. Query most rated movies

**Query:**
```gql
{
  movies(orderBy: "voteAverage", descending: true, limit: 20) {
    title
    voteAverage
    voteCount
    originalTitle
    tagline
    budget
    releaseDate
  }
}
```
**Response:**
```json
{
  "data": {
    "movies": [
      {
        "title": "Me You and Five Bucks",
        "voteAverage": 10,
        "voteCount": 2,
        "originalTitle": "Me You and Five Bucks",
        "tagline": "A story about second, second chances",
        "budget": 1,
        "releaseDate": "2015-07-07"
      },
      {
        "title": "Stiff Upper Lips",
        "voteAverage": 10,
        "voteCount": 1,
        "originalTitle": "Stiff Upper Lips",
        "tagline": "",
        "budget": 0,
        "releaseDate": "1998-06-12"
      },
      {
        "title": "Dancer, Texas Pop. 81",
        "voteAverage": 10,
        "voteCount": 1,
        "originalTitle": "Dancer, Texas Pop. 81",
        "tagline": "in the middle of nowhere they had everything",
        "budget": 0,
        "releaseDate": "1998-05-01"
      },
      {
        "title": "Little Big Top",
        "voteAverage": 10,
        "voteCount": 1,
        "originalTitle": "Little Big Top",
        "tagline": "",
        "budget": 0,
        "releaseDate": "2006-01-01"
      },
      {
        "title": "Sardaarji",
        "voteAverage": 9.5,
        "voteCount": 2,
        "originalTitle": "Sardaarji",
        "tagline": "",
        "budget": 0,
        "releaseDate": "2015-06-26"
      },
      {
        "title": "One Man's Hero",
        "voteAverage": 9.3,
        "voteCount": 2,
        "originalTitle": "One Man's Hero",
        "tagline": "One man's hero is another man's traitor.",
        "budget": 0,
        "releaseDate": "1999-08-02"
      },
      {
        "title": "There Goes My Baby",
        "voteAverage": 8.5,
        "voteCount": 2,
        "originalTitle": "There Goes My Baby",
        "tagline": "",
        "budget": 10500000,
        "releaseDate": "1994-09-02"
      },
      {
        "title": "The Shawshank Redemption",
        "voteAverage": 8.5,
        "voteCount": 8205,
        "originalTitle": "The Shawshank Redemption",
        "tagline": "Fear can hold you prisoner. Hope can set you free.",
        "budget": 25000000,
        "releaseDate": "1994-09-23"
      },
      {
        "title": "The Prisoner of Zenda",
        "voteAverage": 8.4,
        "voteCount": 11,
        "originalTitle": "The Prisoner of Zenda",
        "tagline": "The most thrilling swordfight ever filmed...",
        "budget": 0,
        "releaseDate": "1937-09-03"
      },
      {
        "title": "The Godfather",
        "voteAverage": 8.4,
        "voteCount": 5893,
        "originalTitle": "The Godfather",
        "tagline": "An offer you can't refuse.",
        "budget": 6000000,
        "releaseDate": "1972-03-14"
      },
      {
        "title": "Counting",
        "voteAverage": 8.3,
        "voteCount": 3,
        "originalTitle": "Counting",
        "tagline": "",
        "budget": 50000,
        "releaseDate": "2015-02-09"
      },
      {
        "title": "Whiplash",
        "voteAverage": 8.3,
        "voteCount": 4254,
        "originalTitle": "Whiplash",
        "tagline": "The road to greatness can take you to the edge.",
        "budget": 3300000,
        "releaseDate": "2014-10-10"
      },
      {
        "title": "Pulp Fiction",
        "voteAverage": 8.3,
        "voteCount": 8428,
        "originalTitle": "Pulp Fiction",
        "tagline": "Just because you are a character doesn't mean you have character.",
        "budget": 8000000,
        "releaseDate": "1994-10-08"
      },
      {
        "title": "Fight Club",
        "voteAverage": 8.3,
        "voteCount": 9413,
        "originalTitle": "Fight Club",
        "tagline": "Mischief. Mayhem. Soap.",
        "budget": 63000000,
        "releaseDate": "1999-10-15"
      },
      {
        "title": "Schindler's List",
        "voteAverage": 8.3,
        "voteCount": 4329,
        "originalTitle": "Schindler's List",
        "tagline": "Whoever saves one life, saves the world entire.",
        "budget": 22000000,
        "releaseDate": "1993-11-29"
      },
      {
        "title": "The Godfather: Part II",
        "voteAverage": 8.3,
        "voteCount": 3338,
        "originalTitle": "The Godfather: Part II",
        "tagline": "I don't feel I have to wipe everybody out, Tom. Just my enemies.",
        "budget": 13000000,
        "releaseDate": "1974-12-20"
      },
      {
        "title": "Spirited Away",
        "voteAverage": 8.3,
        "voteCount": 3840,
        "originalTitle": "千と千尋の神隠し",
        "tagline": "The tunnel led Chihiro to a mysterious town...",
        "budget": 15000000,
        "releaseDate": "2001-07-20"
      },
      {
        "title": "The Visual Bible: The Gospel of John",
        "voteAverage": 8.2,
        "voteCount": 12,
        "originalTitle": "The Visual Bible: The Gospel of John",
        "tagline": "For God loved the world So much...",
        "budget": 10000000,
        "releaseDate": "2003-09-11"
      },
      {
        "title": "Anne of Green Gables",
        "voteAverage": 8.2,
        "voteCount": 68,
        "originalTitle": "Anne of Green Gables",
        "tagline": "",
        "budget": 0,
        "releaseDate": "1985-12-01"
      },
      {
        "title": "Howl's Moving Castle",
        "voteAverage": 8.2,
        "voteCount": 1991,
        "originalTitle": "ハウルの動く城",
        "tagline": "The two lived there",
        "budget": 24000000,
        "releaseDate": "2004-11-19"
      }
    ]
  }
}
```

### 2. Query "Matrix" movie overview

**Query:**
```gql
{
  movies(title: "The Matrix") {
    title
    voteAverage
    voteCount
    originalTitle
    tagline
    budget
    releaseDate
    overview
    cast {
      actor {
        name
      }
      character
    }
  }
}
```
**Response:**
```json
{
  "data": {
    "movies": [
      {
        "title": "The Matrix",
        "voteAverage": 7.9,
        "voteCount": 8907,
        "originalTitle": "The Matrix",
        "tagline": "Welcome to the Real World.",
        "budget": 63000000,
        "releaseDate": "1999-03-30",
        "overview": "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.",
        "cast": [
          {
            "actor": {
              "name": "Keanu Reeves"
            },
            "character": "Thomas \"Neo\" Anderson"
          },
          {
            "actor": {
              "name": "Laurence Fishburne"
            },
            "character": "Morpheus"
          },
          {
            "actor": {
              "name": "Carrie-Anne Moss"
            },
            "character": "Trinity"
          },
          {
            "actor": {
              "name": "Hugo Weaving"
            },
            "character": "Agent Smith"
          },
          {
            "actor": {
              "name": "Gloria Foster"
            },
            "character": "Oracle"
          },
          {
            "actor": {
              "name": "Joe Pantoliano"
            },
            "character": "Cypher"
          },
          {
            "actor": {
              "name": "Marcus Chong"
            },
            "character": "Tank"
          },
          {
            "actor": {
              "name": "Paul Goddard"
            },
            "character": "Agent Brown"
          },
          {
            "actor": {
              "name": "Robert Taylor"
            },
            "character": "Agent Jones"
          },
          {
            "actor": {
              "name": "Julian Arahanga"
            },
            "character": "Apoc"
          },
          {
            "actor": {
              "name": "Matt Doran"
            },
            "character": "Mouse"
          },
          {
            "actor": {
              "name": "Belinda McClory"
            },
            "character": "Switch"
          },
          {
            "actor": {
              "name": "Anthony Ray Parker"
            },
            "character": "Dozer"
          },
          {
            "actor": {
              "name": "David Aston"
            },
            "character": "Rhineheart"
          },
          {
            "actor": {
              "name": "Marc Aden"
            },
            "character": "Choi"
          },
          {
            "actor": {
              "name": "Ada Nicodemou"
            },
            "character": "Dujour"
          },
          {
            "actor": {
              "name": "Deni Gordon"
            },
            "character": "Priestess"
          },
          {
            "actor": {
              "name": "Rowan Witt"
            },
            "character": "Spoon Boy"
          },
          {
            "actor": {
              "name": "Eleanor Witt"
            },
            "character": "Potential"
          },
          {
            "actor": {
              "name": "Tamara Brown"
            },
            "character": "Potential"
          },
          {
            "actor": {
              "name": "Janaya Pender"
            },
            "character": "Potential"
          },
          {
            "actor": {
              "name": "Adryn White"
            },
            "character": "Potential"
          },
          {
            "actor": {
              "name": "Natalie Tjen"
            },
            "character": "Potential"
          },
          {
            "actor": {
              "name": "Bill Young"
            },
            "character": "Lieutenant"
          },
          {
            "actor": {
              "name": "David O'Connor"
            },
            "character": "FedEx Man"
          },
          {
            "actor": {
              "name": "Jeremy Ball"
            },
            "character": "Businessman"
          },
          {
            "actor": {
              "name": "Fiona Johnson"
            },
            "character": "Woman in Red"
          },
          {
            "actor": {
              "name": "Harry Lawrence"
            },
            "character": "Old Man"
          },
          {
            "actor": {
              "name": "Steve Dodd"
            },
            "character": "Blind Man"
          },
          {
            "actor": {
              "name": "Luke Quinton"
            },
            "character": "Security Guard"
          },
          {
            "actor": {
              "name": "Lawrence Woodward"
            },
            "character": "Guard"
          },
          {
            "actor": {
              "name": "Michael Butcher"
            },
            "character": "Cop Who Captures Neo"
          },
          {
            "actor": {
              "name": "Bernard Ledger"
            },
            "character": "Big Cop"
          },
          {
            "actor": {
              "name": "Robert Simper"
            },
            "character": "Cop"
          },
          {
            "actor": {
              "name": "Chris Pattinson"
            },
            "character": "Cop"
          },
          {
            "actor": {
              "name": "Nigel Harbach"
            },
            "character": "Parking Cop"
          }
        ]
      }
    ]
  }
}
```

### 3. Query movies where Keanu Reeves was filmed

**Query:**
```gql
{
  cast(actor: "Keanu Reeves") {
    character
    movie {
      title
      tagline
    }
  }
}
```
**Response:**
```json
{
  "data": {
    "cast": [
      {
        "character": "Kai",
        "movie": {
          "title": "47 Ronin",
          "tagline": "For courage. For loyalty. For honor."
        }
      },
      {
        "character": "Thomas \"Neo\" Anderson",
        "movie": {
          "title": "The Matrix Revolutions",
          "tagline": "Everything that has a beginning has an end."
        }
      },
      {
        "character": "Thomas \"Neo\" Anderson",
        "movie": {
          "title": "The Matrix Reloaded",
          "tagline": "Free your mind."
        }
      },
      {
        "character": "Julian Mercer",
        "movie": {
          "title": "Something's Gotta Give",
          "tagline": "Schmucks are people too."
        }
      },
      {
        "character": "Klaatu",
        "movie": {
          "title": "The Day the Earth Stood Still",
          "tagline": "12.12.08 is the Day the Earth Stood Still"
        }
      },
      {
        "character": "Thomas \"Neo\" Anderson",
        "movie": {
          "title": "The Matrix",
          "tagline": "Welcome to the Real World."
        }
      },
      {
        "character": "Kevin Lomax",
        "movie": {
          "title": "The Devil's Advocate",
          "tagline": "Evil has its winning ways."
        }
      },
      {
        "character": "Eddie Kasalivich",
        "movie": {
          "title": "Chain Reaction",
          "tagline": "Reaction Time 8-4-96"
        }
      },
      {
        "character": "Shane Falco",
        "movie": {
          "title": "The Replacements",
          "tagline": "Throw the ball. Catch the girl. Keep it simple."
        }
      },
      {
        "character": "Jonathan Harker",
        "movie": {
          "title": "Dracula",
          "tagline": "Love never dies."
        }
      },
      {
        "character": "Alex Wyler",
        "movie": {
          "title": "The Lake House",
          "tagline": "How do you hold on to someone you've never met?"
        }
      },
      {
        "character": "Nelson",
        "movie": {
          "title": "Sweet November",
          "tagline": "She Just Needed A Month To Change His Life For Ever."
        }
      },
      {
        "character": "David Allen Griffin",
        "movie": {
          "title": "The Watcher",
          "tagline": "Don't go home alone."
        }
      },
      {
        "character": "Jack Traven",
        "movie": {
          "title": "Speed",
          "tagline": "Get ready for rush hour"
        }
      },
      {
        "character": "Le Chevalier Raphael Danceny",
        "movie": {
          "title": "Dangerous Liaisons",
          "tagline": "Lust. Seduction. Revenge. The Game As You've Never Seen It Played Before."
        }
      },
      {
        "character": "Conor O'Neill",
        "movie": {
          "title": "Hardball",
          "tagline": "The most important thing in life is showing up"
        }
      },
      {
        "character": "Ted Logan",
        "movie": {
          "title": "Bill & Ted's Bogus Journey",
          "tagline": "Once... they made history. Now... they are history."
        }
      },
      {
        "character": "Detective Tom Ludlow",
        "movie": {
          "title": "Street Kings",
          "tagline": "Their city. Their rules. No prisoners."
        }
      },
      {
        "character": "Fred/Bob Arctor",
        "movie": {
          "title": "A Scanner Darkly",
          "tagline": "Everything Is Not Going To Be OK"
        }
      },
      {
        "character": "Keanu (voice)",
        "movie": {
          "title": "Keanu",
          "tagline": "Kitten, please."
        }
      },
      {
        "character": "Ted Logan",
        "movie": {
          "title": "Bill & Ted's Excellent Adventure",
          "tagline": "History is about to be rewritten by two guys who can't spell."
        }
      },
      {
        "character": "Don Juan",
        "movie": {
          "title": "Much Ado About Nothing",
          "tagline": "Romance. Mischief. Seduction. Revenge. Remarkable."
        }
      },
      {
        "character": "Hank",
        "movie": {
          "title": "The Neon Demon",
          "tagline": "Beauty is vicious."
        }
      },
      {
        "character": "Perry",
        "movie": {
          "title": "Thumbsucker",
          "tagline": ""
        }
      },
      {
        "character": "Harry",
        "movie": {
          "title": "The Last Time I Committed Suicide",
          "tagline": "Life is what happens when you're busy making plans"
        }
      },
      {
        "character": "Scott Favor",
        "movie": {
          "title": "My Own Private Idaho",
          "tagline": "It's not where you go, it's how you get there."
        }
      },
      {
        "character": "Matt",
        "movie": {
          "title": "River's Edge",
          "tagline": "The most controversial film you will see this year."
        }
      }
    ]
  }
}
```

### 4. Find movies directed by Christopher Nolan

**Query:**
```gql
{
  crew(person: "Christopher Nolan", job: "Director") {
    movie {
      title
      tagline
      budget
      voteAverage
    }
  }
}
```
**Response:**
```json
{
  "data": {
    "crew": [
      {
        "movie": {
          "title": "The Dark Knight Rises",
          "tagline": "The Legend Ends",
          "budget": 250000000,
          "voteAverage": 7.6
        }
      },
      {
        "movie": {
          "title": "The Dark Knight",
          "tagline": "Why So Serious?",
          "budget": 185000000,
          "voteAverage": 8.2
        }
      },
      {
        "movie": {
          "title": "Interstellar",
          "tagline": "Mankind was born on Earth. It was never meant to die here.",
          "budget": 165000000,
          "voteAverage": 8.1
        }
      },
      {
        "movie": {
          "title": "Inception",
          "tagline": "Your mind is the scene of the crime.",
          "budget": 160000000,
          "voteAverage": 8.1
        }
      },
      {
        "movie": {
          "title": "Batman Begins",
          "tagline": "Evil fears the knight.",
          "budget": 150000000,
          "voteAverage": 7.5
        }
      },
      {
        "movie": {
          "title": "Insomnia",
          "tagline": "A tough cop. A brilliant killer. An unspeakable crime.",
          "budget": 46000000,
          "voteAverage": 6.8
        }
      },
      {
        "movie": {
          "title": "The Prestige",
          "tagline": "Are You Watching Closely?",
          "budget": 40000000,
          "voteAverage": 8
        }
      },
      {
        "movie": {
          "title": "Memento",
          "tagline": "Some memories are best forgotten.",
          "budget": 9000000,
          "voteAverage": 8.1
        }
      }
    ]
  }
}
```

### 5. Find movies filmed in Russia

**Query:**
```gql
{
  productionCountries(id:"RU") {
    movies {
      title
      originalTitle
      tagline
      voteAverage
    }
  }
}
```
**Response:**
```json
{
  "data": {
    "productionCountries": [
      {
        "movies": [
          {
            "title": "Match Point",
            "originalTitle": "Match Point",
            "tagline": "Passion Temptation Obsession",
            "voteAverage": 7.3
          },
          {
            "title": "Solaris",
            "originalTitle": "Солярис",
            "tagline": "",
            "voteAverage": 7.7
          },
          {
            "title": "Night Watch",
            "originalTitle": "Ночной дозор",
            "tagline": "All That Stands Between Light And Darkness Is The Night Watch.",
            "voteAverage": 6.3
          },
          {
            "title": "The Return",
            "originalTitle": "Возвращение",
            "tagline": "",
            "voteAverage": 7.4
          },
          {
            "title": "Get Smart",
            "originalTitle": "Get Smart",
            "tagline": "Saving The World...And Loving It!",
            "voteAverage": 6
          },
          {
            "title": "Mongol: The Rise of Genghis Khan",
            "originalTitle": "Монгол",
            "tagline": "Greatness comes to those who take it.",
            "voteAverage": 6.5
          },
          {
            "title": "The Inhabited Island",
            "originalTitle": "Obitaemyy Ostrov",
            "tagline": "",
            "voteAverage": 5.3
          },
          {
            "title": "The White Countess",
            "originalTitle": "The White Countess",
            "tagline": "",
            "voteAverage": 6.9
          },
          {
            "title": "Waterloo",
            "originalTitle": "Waterloo",
            "tagline": "",
            "voteAverage": 7
          },
          {
            "title": "Space Dogs",
            "originalTitle": "Белка и Стрелка. Звёздные собаки",
            "tagline": "",
            "voteAverage": 6.3
          },
          {
            "title": "The Last Station",
            "originalTitle": "The Last Station",
            "tagline": "Intoxicating. Infuriating. Impossible. Love.",
            "voteAverage": 6.7
          },
          {
            "title": "The Darkest Hour",
            "originalTitle": "The Darkest Hour",
            "tagline": "Survive The Holidays",
            "voteAverage": 4.8
          },
          {
            "title": "Hard to Be a God",
            "originalTitle": "Трудно быть богом",
            "tagline": "",
            "voteAverage": 6.7
          },
          {
            "title": "Jack Ryan: Shadow Recruit",
            "originalTitle": "Jack Ryan: Shadow Recruit",
            "tagline": "Trust no one.",
            "voteAverage": 5.9
          },
          {
            "title": "The Snow Queen",
            "originalTitle": "Снежная королева",
            "tagline": "Cold can freeze your heart, love can set you free",
            "voteAverage": 5.1
          },
          {
            "title": "Forbidden Kingdom",
            "originalTitle": "Viy",
            "tagline": "The truth is in you",
            "voteAverage": 4.9
          },
          {
            "title": "The Geographer Drank His Globe Away",
            "originalTitle": "Географ глобус пропил",
            "tagline": "",
            "voteAverage": 7.3
          },
          {
            "title": "Red Sky",
            "originalTitle": "Red Sky",
            "tagline": "Go Rogue",
            "voteAverage": 4.1
          },
          {
            "title": "Savva. Heart of the Warrior",
            "originalTitle": "Савва. Сердце воина",
            "tagline": "You need only wish with all of your heart!",
            "voteAverage": 6.4
          }
        ]
      }
    ]
  }
}
```