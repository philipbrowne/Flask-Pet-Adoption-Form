from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "helloworld99"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)


@app.route('/')
def home_page():
    """Front Page displaying Pets"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/pets/add', methods=['GET', 'POST'])
def add_pet():
    """Form for adding pets"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        # Inserts placeholder IMG if url is blank in form
        if form.photo_url.data:
            photo_url = form.photo_url.data
        else:
            photo_url = '/static/placeholder.jpg'
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/pets/<int:pet_id>')
def display_pet_info(pet_id):
    """Displays information on Pet"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)


@app.route('/pets/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet_info(pet_id):
    """Change Pet Information"""
    pet = Pet.query.get_or_404(pet_id)
    # Inserts placeholder IMG if url is blank in form
    if pet.photo_url == '/static/placeholder.jpg':
        pet.photo_url = ''
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        if form.photo_url.data:
            pet.photo_url = form.photo_url.data
        else:
            pet.photo_url = '/static/placeholder.jpg'
        pet.age = form.age.data
        pet.species = form.species.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', pet=pet, form=form)
