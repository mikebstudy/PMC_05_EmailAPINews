# Course Notes 05.EmailAPINews Project
- From Python Mega Course (by Ardit Sulce)
- Day 27-28 Project 5 Send Email of Daily News from API 

### Day 27
- newsapi.org: API Key: 7b0a6d7450aa4fa9b8af0632a4e1b827
- send_email.py used from PMC_02_Showcase.
  - See PMC_02_Showcase/CourseNotes.md L219 for setup of app passwords

### Day 28
- add 5 refinements
- add bonus_B Nasa sky photo webpage with streamlit

#### Lnnn 

### source for newsapi.com 

https://newsapi.org/v2/top-headlines/sources?country=us&apiKey=7b0a6d7450aa4fa9b8af0632a4e1b827

{
  "status": "ok",
  "sources": [
    {
      "id": "abc-news",
      "name": "ABC News",
      "description": "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
      "url": "https://abcnews.go.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "al-jazeera-english",
      "name": "Al Jazeera English",
      "description": "News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.",
      "url": "https://www.aljazeera.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "ars-technica",
      "name": "Ars Technica",
      "description": "The PC enthusiast's resource. Power users and the tools they love, without computing religion.",
      "url": "https://arstechnica.com",
      "category": "technology",
      "language": "en",
      "country": "us"
    },
    {
      "id": "associated-press",
      "name": "Associated Press",
      "description": "The AP delivers in-depth coverage on the international, politics, lifestyle, business, and entertainment news.",
      "url": "https://apnews.com/",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "axios",
      "name": "Axios",
      "description": "Axios are a new media company delivering vital, trustworthy news and analysis in the most efficient, illuminating and shareable ways possible.",
      "url": "https://www.axios.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "bleacher-report",
      "name": "Bleacher Report",
      "description": "Sports journalists and bloggers covering NFL, MLB, NBA, NHL, MMA, college football and basketball, NASCAR, fantasy sports and more. News, photos, mock drafts, game scores, player profiles and more!",
      "url": "http://www.bleacherreport.com",
      "category": "sports",
      "language": "en",
      "country": "us"
    },
    {
      "id": "bloomberg",
      "name": "Bloomberg",
      "description": "Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring stories from Businessweek and Bloomberg News.",
      "url": "http://www.bloomberg.com",
      "category": "business",
      "language": "en",
      "country": "us"
    },
    {
      "id": "breitbart-news",
      "name": "Breitbart News",
      "description": "Syndicated news and opinion website providing continuously updated headlines to top news and analysis sources.",
      "url": "http://www.breitbart.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "business-insider",
      "name": "Business Insider",
      "description": "Business Insider is a fast-growing business site with deep financial, media, tech, and other industry verticals. Launched in 2007, the site is now the largest business news site on the web.",
      "url": "http://www.businessinsider.com",
      "category": "business",
      "language": "en",
      "country": "us"
    },
    {
      "id": "buzzfeed",
      "name": "Buzzfeed",
      "description": "BuzzFeed is a cross-platform, global network for news and entertainment that generates seven billion views each month.",
      "url": "https://www.buzzfeed.com",
      "category": "entertainment",
      "language": "en",
      "country": "us"
    },
    {
      "id": "cbs-news",
      "name": "CBS News",
      "description": "CBS News: dedicated to providing the best in journalism under standards it pioneered at the dawn of radio and television and continue in the digital age.",
      "url": "http://www.cbsnews.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "cnn",
      "name": "CNN",
      "description": "View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN",
      "url": "http://us.cnn.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "cnn-es",
      "name": "CNN Spanish",
      "description": "Lee las últimas noticias e información sobre Latinoamérica, Estados Unidos, mundo, entretenimiento, política, salud, tecnología y deportes en CNNEspañol.com.",
      "url": "http://cnnespanol.cnn.com/",
      "category": "general",
      "language": "es",
      "country": "us"
    },
    {
      "id": "crypto-coins-news",
      "name": "Crypto Coins News",
      "description": "Providing breaking cryptocurrency news - focusing on Bitcoin, Ethereum, ICOs, blockchain technology, and smart contracts.",
      "url": "https://www.ccn.com",
      "category": "technology",
      "language": "en",
      "country": "us"
    },
    {
      "id": "engadget",
      "name": "Engadget",
      "description": "Engadget is a web magazine with obsessive daily coverage of everything new in gadgets and consumer electronics.",
      "url": "https://www.engadget.com",
      "category": "technology",
      "language": "en",
      "country": "us"
    },
    {
      "id": "entertainment-weekly",
      "name": "Entertainment Weekly",
      "description": "Online version of the print magazine includes entertainment news, interviews, reviews of music, film, TV and books, and a special area for magazine subscribers.",
      "url": "http://www.ew.com",
      "category": "entertainment",
      "language": "en",
      "country": "us"
    },
    {
      "id": "espn",
      "name": "ESPN",
      "description": "ESPN has up-to-the-minute sports news coverage, scores, highlights and commentary for NFL, MLB, NBA, College Football, NCAA Basketball and more.",
      "url": "https://www.espn.com",
      "category": "sports",
      "language": "en",
      "country": "us"
    },
    {
      "id": "espn-cric-info",
      "name": "ESPN Cric Info",
      "description": "ESPN Cricinfo provides the most comprehensive cricket coverage available including live ball-by-ball commentary, news, unparalleled statistics, quality editorial comment and analysis.",
      "url": "http://www.espncricinfo.com/",
      "category": "sports",
      "language": "en",
      "country": "us"
    },
    {
      "id": "fortune",
      "name": "Fortune",
      "description": "Fortune 500 Daily and Breaking Business News",
      "url": "http://fortune.com",
      "category": "business",
      "language": "en",
      "country": "us"
    },
    {
      "id": "fox-news",
      "name": "Fox News",
      "description": "Breaking News, Latest News and Current News from FOXNews.com. Breaking news and video. Latest Current News: U.S., World, Entertainment, Health, Business, Technology, Politics, Sports.",
      "url": "http://www.foxnews.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "fox-sports",
      "name": "Fox Sports",
      "description": "Find live scores, player and team news, videos, rumors, stats, standings, schedules and fantasy games on FOX Sports.",
      "url": "http://www.foxsports.com",
      "category": "sports",
      "language": "en",
      "country": "us"
    },
    {
      "id": "google-news",
      "name": "Google News",
      "description": "Comprehensive, up-to-date news coverage, aggregated from sources all over the world by Google News.",
      "url": "https://news.google.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "hacker-news",
      "name": "Hacker News",
      "description": "Hacker News is a social news website focusing on computer science and entrepreneurship. It is run by Paul Graham's investment fund and startup incubator, Y Combinator. In general, content that can be submitted is defined as \"anything that gratifies one's intellectual curiosity\".",
      "url": "https://news.ycombinator.com",
      "category": "technology",
      "language": "en",
      "country": "us"
    },
    {
      "id": "ign",
      "name": "IGN",
      "description": "IGN is your site for Xbox One, PS4, PC, Wii-U, Xbox 360, PS3, Wii, 3DS, PS Vita and iPhone games with expert reviews, news, previews, trailers, cheat codes, wiki guides and walkthroughs.",
      "url": "http://www.ign.com",
      "category": "entertainment",
      "language": "en",
      "country": "us"
    },
    {
      "id": "mashable",
      "name": "Mashable",
      "description": "Mashable is a global, multi-platform media and entertainment company.",
      "url": "https://mashable.com",
      "category": "entertainment",
      "language": "en",
      "country": "us"
    },
    {
      "id": "medical-news-today",
      "name": "Medical News Today",
      "description": "Medical news and health news headlines posted throughout the day, every day.",
      "url": "http://www.medicalnewstoday.com",
      "category": "health",
      "language": "en",
      "country": "us"
    },
    {
      "id": "msnbc",
      "name": "MSNBC",
      "description": "Breaking news and in-depth analysis of the headlines, as well as commentary and informed perspectives from The Rachel Maddow Show, Morning Joe & more.",
      "url": "http://www.msnbc.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "mtv-news",
      "name": "MTV News",
      "description": "The ultimate news source for music, celebrity, entertainment, movies, and current events on the web. It's pop culture on steroids.",
      "url": "http://www.mtv.com/news",
      "category": "entertainment",
      "language": "en",
      "country": "us"
    },
    {
      "id": "national-geographic",
      "name": "National Geographic",
      "description": "Reporting our world daily: original nature and science news from National Geographic.",
      "url": "http://news.nationalgeographic.com",
      "category": "science",
      "language": "en",
      "country": "us"
    },
    {
      "id": "national-review",
      "name": "National Review",
      "description": "National Review: Conservative News, Opinion, Politics, Policy, & Current Events.",
      "url": "https://www.nationalreview.com/",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "nbc-news",
      "name": "NBC News",
      "description": "Breaking news, videos, and the latest top stories in world news, business, politics, health and pop culture.",
      "url": "http://www.nbcnews.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "new-scientist",
      "name": "New Scientist",
      "description": "Breaking science and technology news from around the world. Exclusive stories and expert analysis on space, technology, health, physics, life and Earth.",
      "url": "https://www.newscientist.com/section/news",
      "category": "science",
      "language": "en",
      "country": "us"
    },
    {
      "id": "newsweek",
      "name": "Newsweek",
      "description": "Newsweek provides in-depth analysis, news and opinion about international issues, technology, business, culture and politics.",
      "url": "https://www.newsweek.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "new-york-magazine",
      "name": "New York Magazine",
      "description": "NYMAG and New York magazine cover the new, the undiscovered, the next in politics, culture, food, fashion, and behavior nationally, through a New York lens.",
      "url": "https://nymag.com/",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "next-big-future",
      "name": "Next Big Future",
      "description": "Coverage of science and technology that have the potential for disruption, and analysis of plans, policies, and technology that enable radical improvement.",
      "url": "https://www.nextbigfuture.com",
      "category": "science",
      "language": "en",
      "country": "us"
    },
    {
      "id": "nfl-news",
      "name": "NFL News",
      "description": "The official source for NFL news, schedules, stats, scores and more.",
      "url": "https://www.nfl.com",
      "category": "sports",
      "language": "en",
      "country": "us"
    },
    {
      "id": "nhl-news",
      "name": "NHL News",
      "description": "The most up-to-date breaking hockey news from the official source including interviews, rumors, statistics and schedules.",
      "url": "https://www.nhl.com/news",
      "category": "sports",
      "language": "en",
      "country": "us"
    },
    {
      "id": "politico",
      "name": "Politico",
      "description": "Political news about Congress, the White House, campaigns, lobbyists and issues.",
      "url": "https://www.politico.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "polygon",
      "name": "Polygon",
      "description": "Polygon is a gaming website in partnership with Vox Media. Our culture focused site covers games, their creators, the fans, trending stories and entertainment news.",
      "url": "http://www.polygon.com",
      "category": "entertainment",
      "language": "en",
      "country": "us"
    },
    {
      "id": "recode",
      "name": "Recode",
      "description": "Get the latest independent tech news, reviews and analysis from Recode with the most informed and respected journalists in technology and media.",
      "url": "http://www.recode.net",
      "category": "technology",
      "language": "en",
      "country": "us"
    },
    {
      "id": "reddit-r-all",
      "name": "Reddit /r/all",
      "description": "Reddit is an entertainment, social news networking service, and news website. Reddit's registered community members can submit content, such as text posts or direct links.",
      "url": "https://www.reddit.com/r/all",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "reuters",
      "name": "Reuters",
      "description": "Reuters.com brings you the latest news from around the world, covering breaking news in business, politics, entertainment, technology, video and pictures.",
      "url": "https://www.reuters.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "techcrunch",
      "name": "TechCrunch",
      "description": "TechCrunch is a leading technology media property, dedicated to obsessively profiling startups, reviewing new Internet products, and breaking tech news.",
      "url": "https://techcrunch.com",
      "category": "technology",
      "language": "en",
      "country": "us"
    },
    {
      "id": "techradar",
      "name": "TechRadar",
      "description": "The latest technology news and reviews, covering computing, home entertainment systems, gadgets and more.",
      "url": "https://www.techradar.com",
      "category": "technology",
      "language": "en",
      "country": "us"
    },
    {
      "id": "the-american-conservative",
      "name": "The American Conservative",
      "description": "Realism and reform. A new voice for a new generation of conservatives.",
      "url": "http://www.theamericanconservative.com/",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "the-hill",
      "name": "The Hill",
      "description": "The Hill is a top US political website, read by the White House and more lawmakers than any other site -- vital for policy, politics and election campaigns.",
      "url": "https://thehill.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "the-huffington-post",
      "name": "The Huffington Post",
      "description": "The Huffington Post is a politically liberal American online news aggregator and blog that has both localized and international editions founded by Arianna Huffington, Kenneth Lerer, Andrew Breitbart, and Jonah Peretti, featuring columnists.",
      "url": "http://www.huffingtonpost.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "the-next-web",
      "name": "The Next Web",
      "description": "The Next Web is one of the world’s largest online publications that delivers an international perspective on the latest news about Internet technology, business and culture.",
      "url": "http://thenextweb.com",
      "category": "technology",
      "language": "en",
      "country": "us"
    },
    {
      "id": "the-verge",
      "name": "The Verge",
      "description": "The Verge covers the intersection of technology, science, art, and culture.",
      "url": "http://www.theverge.com",
      "category": "technology",
      "language": "en",
      "country": "us"
    },
    {
      "id": "the-wall-street-journal",
      "name": "The Wall Street Journal",
      "description": "WSJ online coverage of breaking news and current headlines from the US and around the world. Top stories, photos, videos, detailed analysis and in-depth reporting.",
      "url": "https://www.wsj.com",
      "category": "business",
      "language": "en",
      "country": "us"
    },
    {
      "id": "the-washington-post",
      "name": "The Washington Post",
      "description": "Breaking news and analysis on politics, business, world national news, entertainment more. In-depth DC, Virginia, Maryland news coverage including traffic, weather, crime, education, restaurant reviews and more.",
      "url": "https://www.washingtonpost.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "the-washington-times",
      "name": "The Washington Times",
      "description": "The Washington Times delivers breaking news and commentary on the issues that affect the future of our nation.",
      "url": "https://www.washingtontimes.com/",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "time",
      "name": "Time",
      "description": "Breaking news and analysis from TIME.com. Politics, world news, photos, video, tech reviews, health, science and entertainment news.",
      "url": "http://time.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "usa-today",
      "name": "USA Today",
      "description": "Get the latest national, international, and political news at USATODAY.com.",
      "url": "http://www.usatoday.com/news",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "vice-news",
      "name": "Vice News",
      "description": "Vice News is Vice Media, Inc.'s current affairs channel, producing daily documentary essays and video through its website and YouTube channel. It promotes itself on its coverage of \"under - reported stories\".",
      "url": "https://news.vice.com",
      "category": "general",
      "language": "en",
      "country": "us"
    },
    {
      "id": "wired",
      "name": "Wired",
      "description": "Wired is a monthly American magazine, published in print and online editions, that focuses on how emerging technologies affect culture, the economy, and politics.",
      "url": "https://www.wired.com",
      "category": "technology",
      "language": "en",
      "country": "us"
    }
  ]
}