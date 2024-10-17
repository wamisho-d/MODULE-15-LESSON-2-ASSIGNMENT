# Task 1: Refactor the Messages List to Use a Hashmap
# Initialize message storage
message_storage = {}

# Task 2: Modify the handle_message Function
def handle_message(user, message):
    if user not in message_storage:
        message_storage[user] = [] # Initialize a list for new users
    message_storage[user].append(message) # Append the new message to the user's list

# Task 3: Update the SocketIO on('message') Event Handler
from flask_socketio import  SocketIO

# Assume you have an initialized SocketIO instance
socketio = SocketIO(app)

@socketio.on('message')
def message_recieved(data):
    user = data['user']
    message = data['message']

    # Store the message in message_storage
    handle_message(user, message)

    # Optianally , emit the message to all connected clients
    socketio.emit('message', {'user': user, 'message': message})

# Task 4: Test Socket in Postman
# Method: POST
# URL:http://localhost:5000/socket.io/?EIO=3&transport=polling
# Body: Set the body to raw JSON and use the following structure:
{
   "user":"JohnDoe",
     "message": "Hello world!"
}

# Task 5: Update Socket get_all_messages to Get Messages by User
@socketio.on('get_all_messages')
def get_all_messages(user):
    # Fetch messages for the requested user
    messages = message_storage.get(user, [])

    # Emit the message back to the user
    socketio.emit('all_messages', {'user': user, 'messages': messages })
