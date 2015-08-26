
#Design
For the api a repository pattern is used. There are three layers involved. A repository layer in charged of accessing the data in the files that can be easily replaced for other types of storage without affecting the rest of the application. A service layer that contains the business logic and finally a controller layer that manages the requests from the api.

Indexing based on geo hashes combined with a brute force distance comparison was used for the proximity search algorithm.
The data is pre-processed storing the geo hashes for every shop using 6 characters as index. To find the stores around a location the geo hash for the location is calculated using the same amount of characters producing a hash that is used to get the shops. For extreme cases around the boundaries of the hash the surrounding hashes are also included. After this a brute force filter is applied over the subset for accuracy. For bigger radiuses more surroundings are included in the subset.

##Concepts used
* Dependency Injection
* TDD and DDD
* Unit testing and integration testing
* Repository pattern
* Multi layered design
* Geo hashing and Indexing

##Python libraries
* GeoPy
* python-geohash

#Thought process

1. Identifying what are the most complex parts of the project. A high effort seems to be needed reaching a good performance of a proximity filtering since  external databases cannot be used.

2. Coming up with an algorithm with high performance for doing location based searches. I was curious about the topic and looked into how to calculate the distance between two coordinates.

4. These algorithm allows to calculate the distance between two coordinates and have an accurate result. However the performance is low so I decided to pre process the data and cluster the coordinates of the shops in subgroups. I designed a way of doing this but while doing some research on I came across to the concept of geo hash and Z-order curve. I realized an accepted way of sorting geographical coordinates so decided to dig into it. 

5. I decided to go with geo hash and using it for indexing the shops by pre-calculating the hashes of 6 characters and storing the values in a dictionary. To get the shops for a particular coordinate I would calculate the geo hash of these coordinate with 6 chars and retrieve the cluster where it belongs together with the near shops. There are cases where the coordinate can be in the border of the grid so its necessary to bring the neighbors clusters. Also, for different distances the amount of neighbors clusters is increased to cover the requested area. Finally, a brute force comparison is carried out over the subset of shops in order to increase the accuracy.

