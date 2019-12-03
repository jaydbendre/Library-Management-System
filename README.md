# Library Management System
Library Management System using Django 2.x and MySQLDB

# Problem Statement : 
An online library management system  essentially comprises of  all the facilities a library provides and a lot more. It comprises of a large number of books, respective authors and any vital information related to it. It also keeps a record of the students issuing the books, reissing them, fines charged etc. Individuals working for the library are also given special rights. We have created a website that organises various library elements for optimal functioning of the same. In addition to the traditional library portal database, the provision of an online buying/selling service of books has also been catered to. 

# Solution : 
Offering a website capable of handling both the issuing of books  and buying books through a common portal.

# Stakeholders : 
       1.Student(Common User):
1.Login / Signup<br />
View Books available at that instant <br />
Search , filtered search and advanced search  <br />
Issue books for a period of 7 days  <br />
Instantaneous Reissue of books after 7 days for another week  <br />
Buy books , new or old  <br />
Payment API to simulate payment by means of cash, card  <br />
E-Wallet of the library to allow purchases through the available balance  <br /> 
Sell Books once verified from the library authorities  <br />
Avail balance either through e wallet or cash of the sold book  <br />
View Fine availed if failed to return the book and pay for the same as they wont be allowed to issue books if pending  <br />
View the return date of the books issued  <br />
View transaction history <br />

       2. Book Verification Incharge :
Login / Signup <br />
View books being issued according to time filters and the corresponding user issuing the same  <br />
Approve the requests of sellers to publish the ad of their book on the site for selling once verified  <br /> 
Approve Reissue Requests of the users concerning their currently issued books with the current status of the user  <br />
Put requests to the admin level 2 to restock books once out of stock  <br />
Report Generation  <br />

    
   3. Admin : 
<ul>
Login/Signup  <br />
Authorize users to be admin of level 1  <br />
Can add or remove book verification incharges  <br />
View Requests of restocking of books from admin of level 1  <br />
Update the stock of the books  <br />
Blacklisting Users  <br />
Report Generation  <br />
	
# Tech Stack : 
HTML5 <br />
CSS 3 <br />
BootStrap 4 <br />
JavaScript <br />
MySQL <br />
Django 2.x <br />
