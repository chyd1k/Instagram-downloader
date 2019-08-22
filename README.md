# Instagram-downloader
Tool that allows you to download Instagram Photos to your PC.

First of all you need to install this package:
* run <code>pip install requests</code>

Others packeges, like <code>re, os, json, urllib.request</code> is a standard librarys, so you don't have to install them.


In my work i try to find the way to download pictures without using instagram api.


The problem is that Instagram uses "infinite scrolling" which won't allow you to load the entire page.
It may look a bit stupid, but this problem wasn't simple to solve.

After a hour of searching at the Internet any other ways to solve this problem, i find out, that if i want to get user posts 
i need to use query_hash and use a <code>GET</code> request simular to the following:


<code>https://www.instagram.com/graphql/query/?query_hash=query_hash_value&variables={"id":"XXX","first":12,"after":"XXX"}</code>

With using this request i get only first 12 pictures from page, so i started to "play" with this and "after" value.
When count of pictures is more then 50, we need to place end_cursor value as parameter to variable "after".


# query_hash values:
<code>ff260833edf142911047af6024eb634a</code> - all photos where a person is marked.

<code>f2405b236d85e8296cf30347c9f08c2a</code> - if there are several photos in the post,
the main photo downloads first, and then it downloads all pictures in post
(wich includes the first).
This causes a repetition, but I'm too lazy to fix it LUL.

<code>472f257a40c653c64c666ce877d59d2b</code> - all photos without repetitions, but it
allows you to download only first photos in the post.
I use this value as standard.
