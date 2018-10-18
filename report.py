#!/usr/bin/env python3
import psycopg2
from datetime import date

conn = psycopg2.connect("dbname = news")

cursor = conn.cursor()

cursor.execute("""
    select title, count(*) viewCount from log l, articles a
    where right(l.path, -9) = a.slug and left(l.path, 9) = '/article/'
    group by a.id order by viewCount desc limit 3;
""")

articles = cursor.fetchall()

print("Most popular articles:")
for article in articles:
    print('"{title}" - {views} views'.format(
        title=article[0], views=article[1]))

print("\n")

cursor.execute("""
    select auth.name, count(*) viewCount from log l, articles art,
    authors auth where right(l.path, -9) = art.slug and
    left(l.path, 9) = '/article/' and art.author = auth.id
    group by auth.id order by viewCount desc;
""")

authors = cursor.fetchall()

print("Popular authors:")
for author in authors:
    print("{author} - {views} views".format(
        author=author[0], views=author[1]))

print("\n")

cursor.execute("""
    select day, round((badrequests * 1.0) / (total * 1.0) * 100, 1)
    as percentBad from (select date_trunc('day', time) as day,
    sum(case when status <> '200 OK' then 1 end) as badrequests,
    count(*) as total from log group by day) as requests
    where (badrequests * 1.0) / (total * 1.0) > 0.01;
""")

days = cursor.fetchall()

print("Days when over 1% of requests lead to errors:")
for day in days:
    print("{dayDate} - {percent}%".format(
        dayDate=day[0].strftime("%B %d, %Y"), percent=day[1]))

conn.close()
