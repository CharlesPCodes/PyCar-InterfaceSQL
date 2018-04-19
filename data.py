from appJar import gui
import sqlite3
conn = sqlite3.connect("suspiciouscars.db")
c = conn.cursor()


#SQL DATA

table_create = "CREATE table if not exists suspiciouscars('Date' TEXT, 'Time' TEXT,  'Car Type' TEXT, 'Car Color' TEXT, 'PlateNum' TEXT, 'Number of People' TEXT, 'People Description' TEXT, 'Police Called' TEXT) ;"
c.execute(table_create)


#WINDOW
app = gui("Sus Cars", "1024x768")

app.addLabel("title", "Welcome to the car database")
app.setLabelBg("title", "blue")


# app.setStretch("both")
app.setExpand("both")
app.setPadding([20,20])


app.addLabelEntry("Date", 0,0)
app.addLabelEntry("Time", 0,1)
app.addLabelEntry("Car Type", 1, 0)
app.addLabelEntry("Color", 1,1)
app.addLabelEntry("PlateNum",2,0)
app.setEntryDefault("PlateNum", "XXX XXX")
app.setEntryUpperCase("PlateNum")
app.addLabelEntry("# of People",2,1)
app.addLabelEntry("Person(s) Description", 3, 0)
# app.addLabelOptionBox("Police Called" ,["-Options- ", "Yes", "No"], 3,1)
app.addLabelEntry("Police Called", 3,1)
app.setEntryDefault("Police Called", "Y/N")
app.setEntryUpperCase("Police Called")
app.addLabelEntry("Search Plate Number", 4,0)
app.setEntryDefault("Search Plate Number", "XXX XXX")
app.setEntryUpperCase("Search Plate Number")
####################################################################
#TESTING CODE

# def launch(win):
#     app.showSubWindow(win)
#     # app.addLabelEntry("License Number")

# # these go in the main window
# app.addButtons(["License Number"], launch)

# # this is a pop-up
# app.startSubWindow("License Number", modal=True)
# app.addMessage(all_rows)
# app.stopSubWindow()




#TESTING CODE

####################################################################

# def launch(win):
# 	app.showSubWindow(win)

def press(button):
	# app.showSubWindow(button)
	

	if button == "Cancel":
		app.stop()

	elif button =="Clear":
		app.clearEntry("Date")
		app.clearEntry("Time")
		app.clearEntry("Car Type")
		app.clearEntry("Color")
		app.clearEntry("PlateNum")
		app.clearEntry("# of People")
		app.clearEntry("Person(s) Description")
		app.clearEntry("Police Called")
	
	
	elif button == "Search":

		#TODO:
		#Pop up window with text from the search. Currently have it printing out the console

		plateSearch = app.getEntry("Search Plate Number")
		print(plateSearch)
		c.execute('SELECT * FROM suspiciouscars WHERE PlateNum= "%s"' %(plateSearch))
		all_rows = c.fetchall()
		print(all_rows)
		app.infoBox("Search Results", all_rows)
		app.startSubWindow("Search", modal=True)
	elif button == "Clear Search":
		app.clearEntry("Search Plate Number")

	else:
		userDate = app.getEntry("Date")
		userTime = app.getEntry("Time")
		userType = app.getEntry("Car Type")
		userColor= app.getEntry("Color")
		userPlate = app.getEntry("PlateNum")
		userNum = app.getEntry("# of People")
		userDes = app.getEntry("Person(s) Description")
		police = app.getEntry("Police Called")
		
		# print("Date:",date, "Time", time)
		sql_Statement = "insert into suspiciouscars values (?,?,?,?,?,?,?,?);"
		c.execute(sql_Statement, (userDate, userTime,  userType, userColor, userPlate, userNum, userDes, police))
		conn.commit()
		app .infoBox("Sus Cars", "Data succesfully entered" , parent=None)


app.addButtons(["Submit", "Clear", "Cancel"], press)
app.addButtons(["Search", "Clear Search"], press, 4,1)
app.setBg("orange")
app.setFont(16)


app.setFocus("Date")

app.go()
