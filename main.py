from tkinter import*
import requests
import json

class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        def submit():
            try:
                cityinput = self.cityname.get()
                if len(cityinput) == 0:
                    self.cityhead.config(text="")
                    self.citycondition.config(text="")
                    self.citytemp.config(text="")

                else:
                    url = f'https://api.weatherapi.com/v1/current.json?key=fe47d845ace04af19d244440220701&q={cityinput}&aqi=no'
                    data = requests.get(url).text
                    data_to_dict = json.loads(data)
                    print(data)
                    if "error" in data_to_dict:
                        self.cityhead.config(text="")
                        self.citycondition.config(text="")
                        self.citytemp.config(text="")
                        error = str(data_to_dict['error']['message'])
                        self.exceptionlabel.config(text=f"{error}")
                    else:
                        self.exceptionlabel.config(text="")
                        cityname = str(
                            data_to_dict['location']['name']) + ', ' + str(data_to_dict['location']['region'])
                        citycondition = data_to_dict['current']['condition']['text']
                        citytemp = data_to_dict['current']['temp_c']
                        self.cityhead.config(text=f"{cityname}")
                        self.citycondition.config(text=f"{citycondition}")
                        self.citytemp.config(text=f"{citytemp}॰C")
            except:
                self.exceptionlabel.config(
                    text="Your Internet connection is off.")

        self.title("Weather App by Souvik Roy")
        self.config(bg="#fff")
        self.resizable(False, False)

        self.heading = Label(text="Weather App by Souvik Roy", font=(
            'Segoe Print', 20), bg="#fff", fg="blue", pady=10, padx=10)
        self.heading.pack(pady=10)

        self.city = Label(text="Enter your City", font=(
            'Arial', 15, 'bold'), bg="#fff")
        self.city.pack(pady=5)

        self.cityname = Entry(width=20, font=('Helvetica', 15), bd=2)
        self.cityname.pack(pady=10)

        self.submit = Button(text="Submit", padx=20, bg="#389fff", fg="#fff", font=(
            'Consolas', 16, 'bold'), command=submit)
        self.submit.pack(pady=10)

        self.cityinfo = Frame(bg="#fff")
        self.cityinfo.pack(pady=30, side=TOP, fill=BOTH)

        self.weathericon = Label(self.cityinfo, bg="#fff")
        self.weathericon.pack()

        self.cityhead = Label(self.cityinfo, text="",
                              font=('Fira Sans', 20), bg="#fff")
        self.cityhead.pack(pady=5, side=TOP)

        self.citycondition = Label(
            self.cityinfo, text="", font=('Candera', 15), bg="#fff")
        self.citycondition.pack(side=TOP)

        self.citytemp = Label(self.cityinfo, text="",
                              font=('Consolas', 30), bg="#fff")
        self.citytemp.pack(side=TOP)

        self.exceptionlabel = Label(text="", font=('Cambola', 20), bg="#fff")
        self.exceptionlabel.pack(side=TOP)


if __name__ == '__main__':
    MainWindow().mainloop()
