from appJar import gui
import sqlite3
conn = sqlite3.connect("cars.db")
c = conn.cursor()


#SQL DATA

table_create = "CREATE table if not exists cars('Date' TEXT, 'Time' TEXT,  'CarType' TEXT, 'Car Color' TEXT) ;"
c.execute(table_create)


#WINDOW
app = gui("Cars database", "1024x768")

# app.setStretch("both")
app.setExpand("both")
app.setPadding([20,20])


app.addLabelEntry("Date", 0,0)
app.addLabelEntry("Time", 0,1)
app.addLabelEntry("Car Type", 1, 0)
app.addLabelEntry("Color", 1,1)
app.addLabelEntry("Search Car", 2,0)



def press(button):
	# app.showSubWindow(button)
	

	if button == "Quit":
		app.stop()

	elif button =="Clear":
		app.clearEntry("Date")
		app.clearEntry("Time")
		app.clearEntry("Car Type")
		app.clearEntry("Color")
	elif button == "Clear Search":
		app.clearEntry("Search Car")
	
	elif button == "Search":

		#TODO:
		#Pop up window with text from the search. Currently have it printing out the console

		carSearch = app.getEntry("Search Car")
		# print(plateSearch)
		c.execute('SELECT * FROM cars WHERE CarType= "%s"' %(carSearch))
		all_rows = c.fetchall()
		print(*all_rows, sep="\n")
	elif button == "Clear Search":
		app.clearEntry("Search Car")

	else:
		userDate = app.getEntry("Date")
		userTime = app.getEntry("Time")
		userType = app.getEntry("Car Type")
		userColor= app.getEntry("Color")
		
		# print("Date:",date, "Time", time)
		sql_Statement = "insert into cars values (?,?,?,?);"
		c.execute(sql_Statement, (userDate, userTime,  userType, userColor))
		conn.commit()
		app .infoBox("Sus Cars", "Data succesfully entered" , parent=None)


app.addButtons(["Submit", "Clear", "Quit"], press)
app.addButtons(["Search", "Clear Search"], press, 2,1)
app.setBg("orange")
app.setFont(16)


app.setFocus("Date")

app.go()
