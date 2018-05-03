import sqlite3

#make new database file

default_dir = "C:/Users/Grazillionaire/Documents/GitHub/News-analyzer/"
folder = "Databases/"
filename = "test2.db"

#concatenate 'file:///', default directory, folder, and db filename
path = 'file:///{}{}{}'.format(default_dir, folder, filename)

conn = sqlite3.connect(path, uri=True)


c = conn.cursor()

# Create table
c.execute('''CREATE TABLE news
             (publishedAt text, source_id text, source_name text, author text, title text, description text, url text)''')

  #publishedAt text, source_id text, source_name text, author text, title text, description text, url text
  #'publishedAt': '2018-05-03T19:23:19Z'
  #'source_id': 'cnn',
  #'source_name': 'CNN',
  #'author':'Clare Foran, CNN',
  #'title': "Sanders can't 'verify the validity' of NBC report Michael Cohen was wiretapped",
  #'description': 'White House press secretary Sarah Sanders said Thursday that...',
  #'url': 'https://www.cnn.com/2018/05/03/politics/trump-lawyer-michael-cohen-wiretap/index.html',


# Insert a row of data
c.execute("INSERT INTO news VALUES ('1100 hrs', 'CNN', 'CNN', 'Claire McFadden', 'Boy loses his marbles', 'no one knows what to do', 'http://url')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
