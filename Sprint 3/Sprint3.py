import tkinter
import matplotlib.pyplot as plt
import json
import tkinter as tk
import numpy as np
import pymongo
from pymongo import MongoClient
from tkinter import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_wid()

    def create_wid(self):
        self.btnInsert = tk.Button(
            self, command=self.InsertDB, text="Insert Data", height=2, width=14)
        self.btngraph = tk.Button(
            self, command=self.graph, text="Totalcases", height=2, width=14)
        self.btndeaths = tk.Button(
            self, command=self.deaths, text="Deaths", height=2, width=14)
        self.btntest = tk.Button(
            self, command=self.test, text="Screen test", height=2, width=14)

        self.btnInsert.pack()
        self.btngraph.pack()
        self.btndeaths.pack()
        self.btntest.pack()

    def InsertDB(self):

        self.cluster = MongoClient(
            "mongodb+srv://admin:adimn@data.x5nnu.mongodb.net/Data?retryWrites=true&w=majority")
        self.db = self.cluster["Data"]
        self.collection = self.db["WHO"]

        with open('WHO.json') as self.f:
            self.file_data = json.load(self.f)

        self.collection.insert_many(self.file_data)
        print("Data Inserted")

    def graph(self):
        self.cluster = MongoClient(
            "mongodb+srv://admin:adimn@data.x5nnu.mongodb.net/Data?retryWrites=true&w=majority")
        self.db = self.cluster["Data"]
        self.collection = self.db["WHO"]
        temp = "Afghanistan"

        name = []
        tcases = []

        for x in self.collection.find():
            string = x["COUNTRY_NAME"]
            cases = x["TotalCase"]

            if string != temp:

                name.append(temp)
                tcases.append(cases)
                # print(name)

                temp = x["COUNTRY_NAME"]

        plt.bar(name, tcases)
        plt.xticks(rotation=90)
        plt.show()

    def deaths(self):
        self.cluster = MongoClient(
            "mongodb+srv://admin:adimn@data.x5nnu.mongodb.net/Data?retryWrites=true&w=majority")
        self.db = self.cluster["Data"]
        self.collection = self.db["WHO"]
        temp = "Afghanistan"

        name = []
        tdeaths = []

        for x in self.collection.find():
            string = x["COUNTRY_NAME"]
            cases = x["TotalDeath"]

            if string != temp:

                name.append(temp)
                tdeaths.append(cases)
                # print(name)

                temp = x["COUNTRY_NAME"]

        plt.bar(name, tdeaths)
        plt.show()

    def test(self):
        newWindow = tk.Toplevel(app)
        newWindow.title("Screen test")

        Label = tk.Label(newWindow,
                         text=" Test to see if you are Covid-19 positive").pack()
        Label = tk.Label(newWindow,
                         text="Name ").pack()
        namesurname = tk.Entry(newWindow, ).pack()
        party = tkinter.IntVar()
        cough = tkinter.IntVar()
        sorethroat = tkinter.IntVar()
        Partycheck = tk.Checkbutton(newWindow, variable=party,
                                    text='Have you been to gathering of more than 14 people').pack()
        coughcheck = tk.Checkbutton(newWindow, variable=cough,
                                    text='Did you cough in the last weeks').pack()
        sorethroatcheck = tk.Checkbutton(newWindow, variable=sorethroat,
                                         text=' Do you have sore throat').pack()
        positive = tk.Label(newWindow, text=" You need to see the doctor")
        Negative = tk.Label(newWindow,
                            text=" You are safe from Covid-19")

        total = 0
        if Partycheck.select() == "Yes":
            total = total+1

        else:
            total = total
        if coughcheck.select() == "Yes":
            total = total+1

        else:
            total = total
        if sorethroatcheck.select() == "Yes":

            total = total+1
        else:
            total = total

        def covid():
            if total > 2:
                positive.pack()
                print(total)
            else:
                Negative.pack()
                print(total)

        btnPos = tk.Button(
            newWindow, command=covid(), text="test",)
        btnPos.pack()


root = tk.Tk()
app = Application(master=root)
app.mainloop()

root.mainloop()
