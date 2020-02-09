#### Assignmnet to restrict-API

##### Task: 
Set of APIs to be made:


	Registration and Mgmt of User: Email and Name is sufficient for now
    An auth mechanism to restrict APIs. You can use any auth mechanism of your choice.
	An API to manage a calender schedule for the User. User should be able to create, edit and 
	delete events. User should also be able to see all his scheduled events.
	
Make sure python (preferred python3.7) is added to path.

python --version or python3.7 --version Install virtualenv using pip.
```
 pip install virtualenv 
 ```
 
First create a virtual environment for the project.

```virtualenv -p python3.7 venv or virtualenv venv
     . venv/bin/activate (Linux)
     . venv/Scripts/activate (windows using Gitbash)
 ```
#### Install dependencies
 ```
pip install -r requirements.txt
```
This will install all the dependencies (pylint, pycodestyle, flask) mentioned in the requirements 

### Run app using below command
```
python run.py
```

#### Run linter using below command
```
sh scripts/lint.sh
```

### API Key
 I have generated API key using generate_api_key.py script and kept this unique key in app.key file,While accessing the API,they need have same api key. We are validating user provided key and our provided key using src/validating_api_key.py script. In all routes we are using validating_api_key function require_api_key in all route methods .
 
 like: src/routes.py
```
@app.route('/newuser')
@require_api_key
```
user can hit new user registration api only if they have API key and ``` @require_api_key``` is validating
 same like for login api and other api also
 
 ```
@app.route('/login')
@require_api_key
@app.route('/create_event', methods=['POSt'])
@require_api_key
same with other api entry point
 ```
 
 #### Table structure
 In this assignment we have two table one for user and other for schedule_event
 ```User``` table structure:

| name          | Email         |password|
| ------------- |:-------------:| -----:|
| user_name      | user_email | user_hashed_password |
|      |      |  |
|  |       |   |

```user``` table creation query:
```
create table User (name varchar(60), email varchar(60) primary key, 
password varchar(150));
```
```Event``` table structture:


| event_id        | event_name           | event_description  |organiser_email        | start_date           | start_time  | end_date           | end_time  |
| ------------- |:-------------:| -----:|------------- |:-------------:| -----:|:-------------:| -----:|
| 1      | your_event_name| provide_event_descriptio |provide organiser_email      | event_start_date | event_start_time |event_end_date  | event_end_time |
|       |    |    |   |    |    |       |    |
|  |       |     | |       |    |      |     |

``` event``` table creation query
```
create table event_details (event_id int Not Null auto_increment, event_name varchar(80),event_description varchar(300),organiser_email varchar(45),
start_date Date,start_time Time, end_date Date, end_time Time ,primary key (event_id), foreign key (organiser_email) references user(Email));
```
```Note```:  Here Organiser email is foreign key. So organiser email will be user email id. Before creating any event make sure user has been registered. One user can create many events but that user should be registered

#### Hashing Password:
while register we are storing hash password in a user table we are hashing password using ```hashlib``` python library and using ```sha256``` algorithm

hashing password code is written in ``` src/hash_utils.py``` file


 
 
