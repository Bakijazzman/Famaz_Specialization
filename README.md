Famaz - 
This project is an ecommerce website that helps famers connect to various customers around tthe world. It aim at facilitating automated production and distribution route to mitigate and reduce to bare minimum the losses incured by farmers.

Features

Authentication :
	Users can login, logout and signup with ease

Cart Functionality:
	users can add, remove and update items to cart and also specify quantity

Cart persistense:
	items added to cart are automatically realoaded on login, items added to cart before logging in are also automatically added to cart after login

Update User Info:
	Users additional information are also automatically saved and retrieved from the database

Update Password:
	password change functionality has also been added


Cart summary:
	cart items and prices are automatically calculated and totalled with respect to their secified quantities


Installation

Clone the repository:

Using this on bash:

git clone https://github.com/your_username/Famaz-MVP.git

Navigate to the project directory: On bash;

cd Famaz-MVP

create a virtual env by running "python -m venv env"

Install the required dependencies: On bash;

pip install -r requirements.txt

Run the application: On bash;

python manage.py runserver

Usage

Login or Signup: If you're a new user, sign up for an account. Otherwise, log in with your credentials.

Update info : after logging in, you will be required to provide additional information for your profile

Item add and remove: You can add and remove products that you desire 

generate order : check out the cart and generate your order
Contributing

Contributions are welcome! If you have any ideas, bug fixes, or feature enhancements, feel free to open an issue or submit a pull request.
