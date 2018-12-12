import twint

c = twint.Config()
c.Search="hello"
c.Store_object=True
# c.Store_csv=True
# c.Output="tweetcsv.csv"
c.Limit=10
c.Database="tweet.db"
obj=twint.run.Search(c)
print(obj)
