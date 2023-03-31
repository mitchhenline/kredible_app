import os
from flask import Flask
from model import db, connect_to_db, User, Advocate, UserAdv

app = Flask(__name__)

connect_to_db(app)

# Drop existing database
try:
    os.system("dropdb -U postgres kredible_app")
    os.system("createdb -U postgres kredible_app")

# Recreate the kredible database
except:
    os.system("createdb kredible_app")

db.create_all()

# Users

user1 = User(email = "mitch@grannys.com", password = "goaggies", first_name = "Mitch", last_name = "Henline", company = "Granny's Gourmet Grilled Cheese", admin = True)
user2 = User(email = "tanner@grannys.com", password = "goaggies", first_name = "Tanenr", last_name = "Randall", company = "Granny's Gourmet Grilled Cheese", admin = True)

db.session.add_all([
    user1,
    user2
])

# Advocates

adv1 = Advocate(email = "testadv1@test.com", first_name = "Gary", last_name = "Lopez", company = "Wasatch Touring", industry = "Hospitality", company_size = "medium", product = "finance software" )
adv2 = Advocate(email="testadv2@test.com", first_name="Mary", last_name="Smith", company="Acme Inc.", industry="Finance", company_size="Large", product="Sales CRM")
adv3 = Advocate(email="testadv3@test.com", first_name="John", last_name="Doe", company="ABC Corp.", industry="Retail", company_size="Small", product="Marketing Automation")
adv4 = Advocate(email="testadv4@test.com", first_name="Sarah", last_name="Lee", company="XYZ Corp.", industry="Technology", company_size="Small", product="HR Management")
adv5 = Advocate(email="testadv5@test.com", first_name="Jack", last_name="Johnson", company="Maple Inc.", industry="Transportation", company_size="Large", product="Supply Chain Management")
adv6 = Advocate(email="testadv6@test.com", first_name="Linda", last_name="Brown", company="Brown Industries", industry="Manufacturing", company_size="Medium", product="Inventory Management")
adv7 = Advocate(email="testadv7@test.com", first_name="David", last_name="Kim", company="Skyline Corp.", industry="Real Estate", company_size="Large", product="Property Management")
adv8 = Advocate(email="testadv8@test.com", first_name="Lisa", last_name="Nguyen", company="Nguyen Enterprises", industry="Consulting", company_size="Small", product="Project Management")
adv9 = Advocate(email="testadv9@test.com", first_name="James", last_name="Anderson", company="Anderson Co.", industry="Energy", company_size="Medium", product="Billing Software")
adv10 = Advocate(email="testadv10@test.com", first_name="Anna", last_name="Garcia", company="Garcia Group", industry="Retail", company_size="Small", product="E-commerce Platform")
adv11 = Advocate(email="testadv11@test.com", first_name="Alex", last_name="Martinez", company="Martinez Inc.", industry="Marketing", company_size="Large", product="Digital Advertising")
adv12 = Advocate(email="testadv12@test.com", first_name="Emily", last_name="Taylor", company="Taylor Corp.", industry="Education", company_size="Small", product="Learning Management")
adv13 = Advocate(email="testadv13@test.com", first_name="Robert", last_name="Miller", company="Miller Group", industry="Hospitality", company_size="Medium", product="Reservation System")
adv14 = Advocate(email="testadv14@test.com", first_name="Daniel", last_name="Gonzalez", company="Gonzalez Corp.", industry="Finance", company_size="Large", product="Wealth Management")
adv15 = Advocate(email="testadv15@test.com", first_name="Christine", last_name="Wong", company="Wong Enterprises", industry="Technology", company_size="Small", product="Data Analytics")
adv16 = Advocate(email="testadv16@test.com", first_name="Michael", last_name="Johnson", company="Johnson Co.", industry="Retail", company_size="Medium", product="POS System")
adv17 = Advocate(email="testadv17@test.com", first_name="Karen", last_name="Nguyen", company="Nguyen Group", industry="Consulting", company_size="Large", product="CRM Software")
adv18 = Advocate(email="testadv18@test.com", first_name="William", last_name="Brown", company="Brown Industries", industry="Manufacturing", company_size="Small", product="Procurement System")
adv19 = Advocate(email="testadv19@test.com", first_name="Jessica", last_name="Kim", company="Kim Corp.", industry="Real Estate", company_size="Medium", product="Real Estate CRM")
adv20 = Advocate(email="testadv20@test.com", first_name="Jonathan", last_name="Lee", company="Lee Enterprises", industry="Transportation", company_size="Small", product="Fleet Management")
adv21 = Advocate(email="testadv21@test.com", first_name="Jennifer", last_name="Smith", company="Smith Co.", industry="Marketing", company_size="Large", product="Marketing Analytics")
adv22 = Advocate(email="testadv22@test.com", first_name="David", last_name="Martinez", company="Martinez Group", industry="Education", company_size="Medium", product="Student Information System")
adv23 = Advocate(email="testadv23@test.com", first_name="Emily", last_name="Taylor", company="Taylor Inc.", industry="Energy", company_size="Small", product="Energy Management")
adv24 = Advocate(email="testadv24@test.com", first_name="Samuel", last_name="Garcia", company="Garcia Enterprises", industry="Hospitality", company_size="Large", product="Hotel Management")
adv25 = Advocate(email="testadv25@test.com", first_name="Olivia", last_name="Johnson", company="Johnson Corp.", industry="Retail", company_size="Small", product="Inventory Tracking")
adv26 = Advocate(email="testadv26@test.com", first_name="Charles", last_name="Nguyen", company="Nguyen Industries", industry="Manufacturing", company_size="Medium", product="Manufacturing Execution System")
adv27 = Advocate(email="testadv27@test.com", first_name="Sophia", last_name="Brown", company="Brown Co.", industry="Consulting", company_size="Large", product="Accounting Software")
adv28 = Advocate(email="testadv28@test.com", first_name="Daniel", last_name="Lee", company="Lee Corp.", industry="Technology", company_size="Small", product="Cybersecurity")


db.session.add_all([adv1, adv2, adv3, adv4, adv5, adv6, adv7, adv8, adv9, adv10, adv11, adv12, adv13, adv14, adv15, adv16, adv17, adv18, adv19, adv20, adv21, adv22, adv23, adv24, adv25, adv26, adv27, adv28])


#UserAdv

# UserAdv
useradv1 = UserAdv(id=1, adv_id=1)
useradv2 = UserAdv(id=1, adv_id=2)
useradv3 = UserAdv(id=1, adv_id=3)
useradv4 = UserAdv(id=1, adv_id=4)
useradv5 = UserAdv(id=1, adv_id=5)
useradv6 = UserAdv(id=1, adv_id=6)
useradv7 = UserAdv(id=1, adv_id=7)
useradv8 = UserAdv(id=1, adv_id=8)
useradv9 = UserAdv(id=1, adv_id=9)
useradv10 = UserAdv(id=1, adv_id=10)
useradv11 = UserAdv(id=1, adv_id=11)
useradv12 = UserAdv(id=1, adv_id=12)
useradv13 = UserAdv(id=1, adv_id=13)
useradv14 = UserAdv(id=1, adv_id=14)
useradv15 = UserAdv(id=1, adv_id=15)
useradv16 = UserAdv(id=1, adv_id=16)
useradv17 = UserAdv(id=1, adv_id=17)
useradv18 = UserAdv(id=1, adv_id=18)
useradv19 = UserAdv(id=1, adv_id=19)
useradv20 = UserAdv(id=1, adv_id=20)
useradv21 = UserAdv(id=1, adv_id=21)
useradv22 = UserAdv(id=1, adv_id=22)
useradv23 = UserAdv(id=1, adv_id=23)
useradv24 = UserAdv(id=1, adv_id=24)
useradv25 = UserAdv(id=1, adv_id=25)

useradv26 = UserAdv(id=2, adv_id=4)
useradv27 = UserAdv(id=2, adv_id=5)
useradv28 = UserAdv(id=2, adv_id=26)
useradv29 = UserAdv(id=2, adv_id=27)
useradv30 = UserAdv(id=2, adv_id=28)
useradv31 = UserAdv(id=2, adv_id=6)
useradv32 = UserAdv(id=2, adv_id=7)
useradv33 = UserAdv(id=2, adv_id=8)
useradv34 = UserAdv(id=2, adv_id=9)
useradv35 = UserAdv(id=2, adv_id=10)
useradv36 = UserAdv(id=2, adv_id=11)
useradv37 = UserAdv(id=2, adv_id=12)
useradv38 = UserAdv(id=2, adv_id=13)
useradv39 = UserAdv(id=2, adv_id=14)
useradv40 = UserAdv(id=2, adv_id=15)
useradv41 = UserAdv(id=2, adv_id=16)
useradv42 = UserAdv(id=2, adv_id=17)
useradv43 = UserAdv(id=2, adv_id=18)
useradv44 = UserAdv(id=2, adv_id=19)
useradv45 = UserAdv(id=2, adv_id=20)
useradv46 = UserAdv(id=2, adv_id=21)
useradv47 = UserAdv(id=2, adv_id=22)
useradv48 = UserAdv(id=2, adv_id=23)
useradv49 = UserAdv(id=2, adv_id=24)
useradv50 = UserAdv(id=2, adv_id=25)

useradvs = [useradv1, useradv2, useradv3, useradv4, useradv5, useradv6, useradv7, useradv8, useradv9, useradv10, useradv11, useradv12, useradv13, useradv14, useradv15, useradv16, useradv17, useradv18, useradv19, useradv20, useradv21, useradv22, useradv23, useradv24, useradv25, useradv26, useradv27, useradv28]

db.session.add_all(useradvs)


db.session.commit()

