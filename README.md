# Cambridge University Press website scraping

### Background 

This is the task that I was given in 2014 while working in the Acquitions Department at the University of Edinburgh. I was asked to get the publication data for almost 3800 ebooks from our collection. I was expected to do it manually. Input data that I received is in file CUPyear-copy.xlsx

### Initial time estimation

Time estimation for doing it all manually, i.e. going to the website and fetching the data, with the following assumptions:

1 minute per record and 7 hours workday, so:

3800 minutes = 63.3 hours = 9 workdays 

In reality it would take longer, since there is no allowance for any breaks. 

### My findings

I decided to try to find an automated way of doing it. I noticed that the link to every ebook in the CUP catalogue was a concatenation of the prefix + ISBN, where:

prefix = http://ebooks.cambridge.org/ebook.jsf?bid=CBO

example ISBN = 9780511545566

So the example link would be like this http://ebooks.cambridge.org/ebook.jsf?bid=CBO9780511545566

### My solution

I decided to use Python and Beautiful Soup library for this. The script would pull out the ISBNs from a text file isbn.txt and write the outcome to db.txt and to the console. The script is in a file called searchYear.py

### Outcome






