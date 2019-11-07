#Group 5 
#Project CHATIT

##Instructions to run: Navigate to the directory containing the repository for the app. Locate chatit.py and run it in the terminal. Then, open a browser and type 127.0.0.1:5000/index to reach the website.

##Feature Description:
*Register: Register to the website using a unique username, email, and password. Creates a User model with those attributes. To verify, run the app and navigate to 127.0.0.1:5000/register and fill out the form.

*Log in: Log in to the website using the username and password created from registering. To verify, after registering, navigate to 127.0.0.1:5000/login and type in the username and password.

*Log out: Log out of the website after having been logged in. To verify, after logging in, click on the log out link at the top and it will log you out.

*Send message: Creates a directMessage model between two users, one being the recipient, one being the sender, with the body of the message being defined as well. This can be verified by navigating to the app directory in Python Idle, importing app.db and everything in app.models, and initializing a directMessage model with a body, a user defined as the sender, and another user being defined as the receiver.

*Delete message: Deletes a direct message from the database. This can be verified by creating a directMessage model as described above, then from app.datamanagement importing deleteDirectMessage, and calling the deleteDirectMessage function with the message to be deleted as the parameter.

*Search for message: Queries the database to locate a message based on the user who sent it and the body of the message. To verify, create a directMessage model in the database, and import the searchForMessage function from app.datamanagement. Then, call the searchForMessage function with the user that sent the message as the first parameter, and the body of the message as the second.

*Add friend: Creates a Friend model with a relationship to the original user as friendsList, with the username variable of the Friend model being the username of the other User model that is the friend. Can be verified by doing from app.models import User, Friend, creating two User models, and creating a Friend model with the parameters username = User2.username, and requestee = User1, and then typing print(User1.friendsList).

*Remove friend: Deletes a Friend model from the database. This can be verified by importing the deleteFriend function from app.datamanagement and calling it with the Friend model to be deleted as the parameter.