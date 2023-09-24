<a href="https://www.npmjs.com/package/vue"><img src="https://img.shields.io/npm/l/vue.svg?sanitize=true" alt="License"></a>



# Images API
Django REST Framework API that allows any user to upload an image in PNG or JPG format.

### Preparation

1. Clone repository `git clone git@github.com:timschopinski/images-api.git` 

    (or with HTTPS `git clone https://github.com/timschopinski/images-api.git`)
 
2. Create virtualenv `python -m venv venv`
3. Upgrade setup tools `pip install --upgrade pip setuptools wheel`
4. Activate env and install libraries `pip install -r requirements.txt`
5. go to ./app and execute `python manage.py runserver`


### Running locally with docker-compose 

1. Clone repository `git clone git@github.com:timschopinski/images-api.git` 

    (or with HTTPS `git clone https://github.com/timschopinski/images-api.git`)
 
2. Install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/).
3. Run `docker compose up`


### User Tiers

There are three built-in account tiers for users: Basic, Premium, and Enterprise. The features available to users are tier-dependent:

- **Basic Tier**: Users with the Basic plan can upload images and receive a link to a thumbnail that's 200px in height.

- **Premium Tier**: Users with the Premium plan can upload images and receive the following:
  - A link to a thumbnail that's 200px in height.
  - A link to a thumbnail that's 400px in height.
  - A link to the originally uploaded image.

- **Enterprise Tier**: Users with the Enterprise plan can upload images and receive the following:
  - A link to a thumbnail that's 200px in height.
  - A link to a thumbnail that's 400px in height.
  - A link to the originally uploaded image.
  - Ability to fetch an expiring link to the image. The link expires after a specified number of seconds (between 300 and 30000 seconds).

### User Creation

Users are created via the admin panel, and by default, they are associated with the Basic Tier.

### Testing with Swagger

You can test the API using Swagger, a user-friendly interface for interacting with the endpoints. To access Swagger:

1. Start your development server.
2. Open your web browser and navigate to [http://localhost:8000/swagger/](http://localhost:8000/swagger/).
3. You can use Swagger to explore and interact with the API endpoints, making it easy to test and understand the available features.


## Admin Panel and Live Preview

### Admin Panel

You can access the admin panel to manage users and other aspects of your application. Use the following credentials to log in:

- **Username**: admin
- **Password**: password

## Existing Users

Three users with different Tiers have already been created for testing purposes. You can use the following credentials to log in as these users:

1. **User**: Tomek
   - **Login**: Tomek
   - **Password**: password123#
   - **Tier**: Basic

2. **User**: Adam
   - **Login**: Adam
   - **Password**: password123#
   - **Tier**: Premium

3. **User**: Bartek
   - **Login**: Bartek
   - **Password**: password123#
   - **Tier**: Enterprise

### Live Preview

You can explore a live preview of the application hosted on AWS by visiting the following link:

[Live Preview](http://imagesapiloadbalancer-1990742228.us-east-1.elb.amazonaws.com/api/)

Feel free to log in as one of the existing users or use the admin panel to manage your application.

### API Documentation

For detailed API documentation and examples, please refer to our [Postman workspace](https://www.postman.com/blue-eclipse-637617/workspace/images-api/).

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/blue-eclipse-637617/workspace/images-api/)
