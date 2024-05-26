from tkinter import *
adult = 15
child = 10
senior = 10

class Ticket_Booth:
    def __innit__(self, tickets=0, price=0):
        self.tickets = tickets
        self.price = price

    def validation(self):
        if self.tickets >= 100:
            display_msg = "Invalid purchase! There is a buy limit of 100 tickets per person."
        elif self.tickets >0 and self.tickets <100:
            display_msg = f"Approved! \nCollect your tickets at the ticket booth!"
            x.calc_price()
        else:
            display_msg = "Sorry! an error occured."
        display_text = Label(root, text=display_msg, fg="white", bg="cyan",
                font = ("Calibri", "15", "bold")).grid(column=0, row=5)

    def calc_price(self):
        return self.total * self.tickets

def get_totals():
    child_tickets = child_ticket_num.get() 
    adult_tickets = adult_ticket_num.get()
    senior_tickets = senior_ticket_num.get()
    student_tickets = student_ticket_num.get()
    tickets_list.append(Ticket_Booth(child_tickets, child))
    tickets_list.append(Ticket_Booth(adult_tickets, adult))
    tickets_list.append(Ticket_Booth(senior_tickets, senior))
    tickets_list.append(Ticket_Booth(student_tickets, student))
    for x in tickets_list:
        x.validation()
    return tickets_list

tickets_list = []
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
                         font=("Calibri", "15", "bold"),command=lambda:get_totals()).grid(column=1, row=4)
display_message = Label(root, text="Output:", fg="white", bg="cyan",
                        font=("Calibri", "15", "bold")).grid(column=0, row=5)
total = Label(root, text="Total:", fg="white", bg="cyan", font=("Calibri", "15", "bold")).grid(column=0, row=6)
root.mainloop()