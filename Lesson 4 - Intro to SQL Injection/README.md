# Lesson 4 - SQL Injection
There are many different types of SQL injection, including:

* Retrieving hidden data
* Subverting application logic
* UNION attacks
* Examining the database
* Blind SQL injection
* SQL truncation attack
* And many more!

## How SQL Injection Works
SQL injection is based on **providing input that manipulates the query** run on the server. Understanding *how* the SQL query is set up is essential to understanding how to manipulate it. Let's take this query that you can see on authentication_bypass.html (you can try this yourself on the HTML page):

<img src="sql1.png">

If we insert the username `user` and the password `123456`, this SQL query will be run:

```
SELECT * 
FROM users 
WHERE username = 'user'
AND password = '123456'
LIMIT 1     
```

If that's not a valid username and password combination, then you will not get any results back and you won't be authenticated. However, look at what happens if we insert `user'` and `123456`:

```
SELECT * 
FROM users 
WHERE username = 'user''
AND password = '123456'
LIMIT 1     
```

Our SQL query will throw an error because after 'user', you have an additional apostrophe ' that ends before 123456 and it doesn't know what to do with this double string. There are different types of comments in SQL queries, one of which is a double dash `--`. Note what happens if we input `user'--` and no password:

```
SELECT * 
FROM users 
WHERE username = 'user'--'
AND password = ''
LIMIT 1     
```

Everything after `'user'` doesn't matter since there's a comment, so the SQL query *will* return a result, and you'll be authenticated. You didn't even need to know the password! This is one example of **subverting application logic**.

## How to Identify SQL Injectable pages
There are many different ways, but one way is by simply putting an apostrophe `'` in a field - if you are returned an error, that's a strong indication that it's SQL injectable. 

## Retrieving Hidden Data
A great example of retrieving hidden data is explained on [portswigger.net](https://portswigger.net/web-security/sql-injection). Let's imagine that you're on a website and when you click on a button that says "Gifts", it brings you here to show you all the products that are gifts (you can try this yourself at hidden_data.html):

```
https://insecure-website.com/products?category=Gifts
```

This is the SQL query run on the database when you go to that link:

```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

Released as `1` means that it only shows products that are currently released. If you decided to go to `https://insecure-website.com/products?category=Gifts'--`, then this query would be run:

```
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```

This would bypass the `released` argument and all products would be shown, whether they should be or not.

Also consider this input: `https://insecure-website.com/products?category=Gifts'+OR+1=1--`

```
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
```

This SQL query would return all products in **all** categories, since the boolean statement `category = 'Gifts' OR 1=1` will **always** return true.

## UNION Attacks
* Union-based (https://redtiger.labs.overthewire.org/level1.php)
    * Username and password don't give us an error
    * ?cat=1 ORDER BY 5 shows us there are 4
* https://www.programmersought.com/article/15413667438/
* https://medium.com/@nyomanpradipta120/sql-injection-union-attack-9c10de1a5635
* Burp Suite
* SQLmap

## Challenges