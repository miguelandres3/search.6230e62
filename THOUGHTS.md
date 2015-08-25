#Thought process

1. Identifying what are the most complex parts of the project. A high effort seems to be needed reaching a good performance of a proximity filtering since  external databases cannot be used.

2. Coming up with an algorithm with high performance for doing location based searches. I was curious about the topic and looked into how to calculate the distance between two coordinates, I found different algorithms created by cartographers that model the earth as a sphere and other more advanced that model it as an ellipsoid. 
3. After satisfying my curiosity I thought this is a common task so I looked for popular python libraries that had these implementations of algorithms, I found several but decided to use GeoPy. 
4. These algorithm allows to calculate the distance between two coordinates and have an accurate result. However the performance is low so I decided to pre process the data and cluster the coordinates of the shops in subgroups. I designed a way of doing this but while doing some research on I came across to the concept of geo hash and Z-order curve. I realized an accepted way of sorting geographical coordinates so decided to dig into it. 
5. I decided to go with geo hash and using it for indexing the shops by pre-calculating the hashes of 6 characters and storing the values in a dictionary. To get the shops for a particular coordinate I would calculate the geo hash of these coordinate with 6 chars and retrieve the cluster where it belongs together with the near shops. There are cases where the coordinate can be in the border of the grid so its necessary to bring the neighbors clusters. Also, for different distances the amount of neighbors clusters is increased to cover the requested area. Finally, a brute force comparison is carried out over the subset of shops in order to increase the accuracy.


#Design
For the api a service repository pattern is used. There are three layers involved. A repository layer in charged of accessing the data in the files that can be easily replaced for other types of storage without affecting the rest of the application. A service layer that contains the business logic and finally a controller layer that manages the requests from the api.

There are implemented unit tests and integration tests to ensure the quality of the code.

