from tkinter import *
adult = 15
child = 10
senior = 10

class Ticket_Booth:
    def __innit__(self, tickets=0, total=0):
        self.tickets = tickets
        self.total = total

    def validation(self):
        print()
        if self.tickets >= 100:
            display_msg = "Invalid purchase! There is a buy limit of 100 tickets per person."
        elif self.tickets >0 and self.tickets <100:
            display_msg = f"Approved! \nCollect your tickets at the ticket booth!"
            for x in tickets:
                x.calc_price()
        else:
            display_msg = "Sorry! an error occured."
        display_text = Label(root, text=display_msg, fg="white", bg="cyan",
                font = ("Calibri", "15", "bold")).grid(column=0, row=5)

    def calc_price():
        return self.total * self.tickets
    
    def get_totals():
        child_tickets = child_ticket_num.get() 
        adult_tickets = adult_ticket_num.get()
        senior_tickets = senior_ticket_num.get()
        student_tickets = student_ticket_num.get()
        tickets.append(child_tickets, adult_tickets, senior_tickets, student_tickets)
        for x in tickets:
            x.validation()    
    
def quit(confirm_window):
    confirm_window.destroy()
    
def confirm(confirm_window):
    confirm_window.destroy()
    return calc_price()

def purchase_confirmation():
    confirm_window = Tk()
    confirm_window.title("Purchase Confirmation")
    confirm_window.geometry("300x200")
    confirm_window.configure(background="cyan")
    confirm_label = Label(confirm_window, text="Please confirm your purchase.", fg="white", bg="cyan",
                    font=("Calibri", "15", "bold")).grid(column=1, row=0)
    confirm_btn = Button(confirm_window, text="Confirm", width=20,
                         font=("Calibri", "15", "bold"), command=lambda:confirm(confirm_window)).grid(column=1, row=2)
    return_btn = Button(confirm_window, text="Cancel", width=20,
                         font=("Calibri", "15", "bold"), command=lambda:quit(confirm_window)).grid(column=1, row=3)
    confirm_window.mainloop()

# G.U.I
root = Tk()
root.title("Ticket Booth - By Evan Lightfoot")
root.geometry("600x400")
root.configure(background='cyan')
child_ticket_num = IntVar()
child_tickets_input = Entry(root, textvariable=child_ticket_num).grid(column=1, row=0)
child_tickets_label = Label(root, text="Child Tickets: $5 Each", fg="white", bg="cyan",
                                font=("Calibri", "15", "bold")).grid(column=0, row=0)
adult_ticket_num = IntVar()
adult = Entry(root, textvariable=adult_ticket_num).grid(column=1, row=1)
adult_tickets_label = Label(root, text="Adult Tickets: $15 Each", fg="white", bg="cyan",
                                font=("Calibri", "15", "bold")).grid(column=0, row=1)
student_ticket_num = IntVar()
student = Entry(root, textvariable=student_ticket_num).grid(column=1, row=2)
student_tickets_label = Label(root, text="Student Tickets: $10 Each", fg="white", bg="cyan",
                                     font=("Calibri", "15", "bold")).grid(column=0, row=2)
senior_ticket_num = IntVar()
senior_tickets = Entry(root, textvariable=senior_ticket_num).grid(column=1, row=3)
senior_tickets_label = Label(root, text="Senior Tickets: $10 Each", fg="white", bg="cyan",
                                font=("Calibri", "15", "bold")).grid(column=0, row=3)
confirm_btn = Button(root, text="Confirm", bd="1", width="13",
                         font=("Calibri", "15", "bold"),command=lambda:purchase_confirmation()).grid(column=1, row=4)
display_message = Label(root, text="Output:", fg="white", bg="cyan",
                        font=("Calibri", "15", "bold")).grid(column=0, row=5)
total = Label(root, text="Total:", fg="white", bg="cyan", font=("Calibri", "15", "bold")).grid(column=0, row=6)
root.mainloop()

for object in objects():
    print(object)
def objects():
    tickets_list = []
    adults = tickets(adults(15, 2))
    children = tickets(children(10, 3))
    seniors = tickets(seniors(10, 1))