# StrawberryFields
a study project at Lappland university of appliec sciences.
This is a study project, purpose of which is to learn practices currently being used in industry
This is used over several cources.

Docker compose file is made for database and phpmyadmin.
To start it you need to install docker firs.
Then open the folder in powershell and:
    docker-compose -f "StrawberryFields\docker-compose.yml" up -d --build
After this the phpmyadmin is accesible on localhost:8000
username: root
password: qwerty
the port is redirected to 12356 because of an error in my network

**Corpses table:**
|Cell name       |Type                           |Example                      |
|----------------|-------------------------------|-----------------------------|
|id 			 |INT, Auto increment            |0      				       |
|date            |universal date format          |2020-07-01    	           |
|value           |Float (kg)					 |123.456789				   |

**weather table**
|Cell name       |Type                           |Example                      |
|----------------|-------------------------------|-----------------------------|
|date 			 |date, current_date()           |2020-07-01      			   |
|current_temp	 |Float (°c)                     |123.456789    	           |
|min_temp        |Float	(°c)					 |123.456789				   |
|max_temp        |Float	(°c)					 |123.456789				   |
|pressure        |Float (hPa)					 |123.456789				   |
|humidity        |Float	(%)						 |123.456789				   |
