# 05.EmailAPINews Project
- From Python Mega Course (by Ardit Sulce)
- Project to Send Email of Daily News from API
- Day 27-28 Project 05 EmailAPINews 

- Three separate implementations 
  - course_C is from working the lessons
  - mikeb_M is enhanced implementation based on my own ideas and those of others on the internet
  - Claude_A is experiments in generating code similiar to course.C and mikeb.M
  - (C,M,A - are the letters that proceed git commit comments and correspond to the respective implementations)

- Github repo: https://github.com/mikebstudy/PMC_05_EmailAPINews
  - each implementation is in its own folder 

## course_C

### (DayNN) Features added to Website bonus project

## mikeb_M
- Started with final version of course_C
- [ X ] Update from_data to today
- [ X ] put date into "today's news" subject line
- [ X ] add filter_by (currently 'Trump')
- [ X ] experiment with adding 'author' and 'publisher' line
  - [ X ] find out who all the 'publishers' are. Instead just count them.
- [ X ] add when published (publishedAt)
- [ X ] experiment with adding 'content' line
- [   ] explore using searchin fields (title,description,content)
- [ X ] add article_limit for output stories count
- [   ]consider setting up feature boundaries for experimenting
  - consider using a class to implement the boundaries
    - basic and enhanced
    - trigger with cli features set to basic or enhanced 
- [   ] add multiple email address(s) 
- [   ] setup defaults in settings dictionary
- [   ] add cli args using argparse
  - topic
  - filter_by
  - article_limit
  - email address(s)

## Claude_A

