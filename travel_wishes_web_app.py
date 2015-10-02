from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from travel_wishes import Base, Users, Locations, Wishes


engine = create_engine('sqlite:///travel_wishes.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/locations', methods=['GET', 'POST'])
def all_locations():
    sorted_by = "alphabetically"
    locations = get_locations_ordered_alphabetically()
    if request.method == 'POST':
        if request.form['sort_by'] == 'by_state':
            return redirect(url_for('all_locations_by_state'))
    return render_template('locations.html', locations=locations, sorted_by=sorted_by)


@app.route('/locations/by_state', methods=['GET', 'POST'])
def all_locations_by_state():
    sorted_by = "by state"
    locations = get_locations_ordered_by_state()
    if request.method == 'POST':
        if request.form['sort_by'] == 'alphabetically':
            return redirect(url_for('all_locations'))
    return render_template('locations.html', locations=locations, sorted_by=sorted_by)


@app.route('/wishlists', methods=['GET', 'POST'])
def view_wishlist():
    if request.method == 'POST':
        username = request.form['username']
        user = session.query(Users).filter_by(username=username).one()
        user_wishes = get_wishes_for_user(user.username)
        return render_template('display_user_wishes.html', user_wishes=user_wishes, user=user)
    return render_template('get_wishlist.html')


@app.route('/<dir>/<file_name>')
def static_content(dir, file_name):
    return send_from_directory(dir, file_name)


def get_locations_ordered_alphabetically():
    return session.query(Locations).order_by(Locations.name).all()


def get_locations_ordered_by_state():
    return session.query(Locations).order_by(Locations.state).all()


def get_location_by_id(location_id):
    return session.query(Locations).filter(Locations.id == location_id).one()


def get_user_list():
    return session.query(Users).order_by(Users.username).all()


def add_user_wish(user_id, location_id):
    location_to_add = Wishes(user=user_id, location=location_id)
    session.add(location_to_add)
    session.commit()
    return


def delete_user_wish(user_id, location_id):
    location_to_delete = Wishes(user_id, location_id)
    session.delete(location_to_delete)
    session.commit()
    return


def get_wishes_for_user(username):
    return session.query(Wishes).filter(Wishes.user == username).all()


# #Populate users:
# user1 = Users(username="user1", password="password", fullname="Sam Cornell", email="samcornell@aol.com")
# session.add(user1)
# user2 = Users(username="funny_guy10", password="password", fullname="Jenn Salon", email="jennsalon@aol.com")
# session.add(user2)
# user3 = Users(username="other_user4", password="password", fullname="Myles Jones", email="myles@aol.com")
# session.add(user3)
# user4 = Users(username="user30594", password="password", fullname="Brittany Casto", email="brit@aol.com")
# session.add(user4)
# user5 = Users(username="SmilerGirl", password="password", fullname="Hugh Grant", email="hugh@aol.com")
# session.add(user5)
# session.commit()
#
#
# # Populate locations:
# location1 = Locations(name="Rocky Mountains", state="TN", city="sunshine", website="www.niagrafalls.com")
# session.add(location1)
# location2 = Locations(name="Jungle City", state="AL", city="Juno", website="www.alaska.com")
# session.add(location2)
# location3 = Locations(name="Swiss Village", state="MN", city="Eureka", website="www.eurekasprings.com")
# session.add(location3)
# location4 = Locations(name="Winterland", state="AK", city="no clue", website="www.grandcanyon.com")
# session.add(location4)

# # More locations:
# location1 = Locations(name="Summersville", state="FL", city="sunshine", website="www.niagrafalls.com")
# session.add(location1)
# location2 = Locations(name="Fall-town", state="VT", city="Juno", website="www.alaska.com")
# session.add(location2)
# location3 = Locations(name="Sea Coast", state="WA", city="Eureka", website="www.eurekasprings.com")
# session.add(location3)
# location4 = Locations(name="Roundtown", state="MA", city="no clue", website="www.grandcanyon.com")
# session.add(location4)
# session.commit()

# # More locations:
# location1 = Locations(name="Niagra Falls", state="NY", city="sunshine", website="www.niagrafalls.com")
# session.add(location1)
# location2 = Locations(name="Alaskan Village", state="AK", city="Juno", website="www.alaska.com")
# session.add(location2)
# location3 = Locations(name="Eureka Springs", state="AR", city="Eureka", website="www.eurekasprings.com")
# session.add(location3)
# location4 = Locations(name="Grand Canyon", state="AZ", city="no clue", website="www.grandcanyon.com")
# session.add(location4)
# session.commit()


# # Populate Wishes
# wish = Wishes(user="user1", location=12)
# session.add(wish)
# wish1 = Wishes(user="user1", location=15)
# session.add(wish1)
# wish2 = Wishes(user="funny_guy10", location=12)
# session.add(wish)
# wish3 = Wishes(user="funny_guy10", location=1)
# session.add(wish3)
# wish4 = Wishes(user="funny_guy10", location=2)
# session.add(wish4)
# wish5 = Wishes(user="user1", location=6)
# session.add(wish5)
# wish6 = Wishes(user="other_user4", location=2)
# session.add(wish6)
# wish7 = Wishes(user="other_user4", location=10)
# session.add(wish7)
# wish8 = Wishes(user="other_user4", location=16)
# session.add(wish8)
# wish9 = Wishes(user="user1", location=7)
# session.add(wish9)
# session.commit()

if __name__ == '__main__':
    app.run()