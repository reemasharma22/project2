# project2


#Project brief 

-


#Requirments 

Kanban Board: Asana or an equivalent Kanban Board
Version Control: Git
CI Server: Jenkins
Configuration Management: Ansible
Cloud server: GCP virtual machines
Containerisation: Docker
Orchestration Tool: Docker Swarm
Reverse Proxy: NGINX

#My project

I created an application that generated a phone deal using 4 services that interacted with eachkther. The services communicated to generate a random deal dependant on the phone and the colour of the phone. 

service 1: This was the front end of the application which communicated with the other services 
service 2: This generated a random phone 
service 3: This generated a random colour
service 4: This generated a price dependant on the phone and the colour

#Trello board





#Risk assessment 

The full risk assessment can be viewed here: https://docs.google.com/spreadsheets/d/1LR_VZsmfVByZFJA3BPvN0WsaQbGsw9JgBUsQIkRJd3s/edit?usp=sharing


#Testing

For testing, I used the pytest to run unit testing on the services. I was able to get 100% testing for both service 2 and 3 which meant to code was able to run exactly as planned for the application to run. 

Service 1 and 4 I was unable to get working. 


#Improvements 

- Create a generate button
- Make the page more aesthetically pleasing 
- Better test coverage 


#Front end

The front end of the application is simple but meets the MVP requirements. The generator will use the services to generate a phone, colour and a price to produce a phone deal for the user. 
