# Copyright <2023> <Sadat Gresham>
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the “Software”), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# Module 1
# Double Linked List
class Stop:
    """Creates a named Node that points ahead and behind"""
    def __init__(self, name, dura):
        """
        Summary: Create Node Class
        :param name: Name of Train Stop
        :param dura: Duration to next Stop
        """
        self.next = None
        self.prev = None
        self.stationname = name
        self.duration = dura


class TrainLine:
    """Creates a Train Line comprised of doubly linked nodes,
    with traversal and editing functions"""
    def __init__(self):
        """
        Summary: Structures the Double Linked List
        with a Current Stop and Destination placeholder metric
        """
        self.head = None
        self.tail = None
        self.currentstop = None
        self.destination = None

    def addstoptohead(self, statname, dura=0):
        """
        Summary: Add a Stop to the Start of the TrainLine
        :param statname: Name of Train Stop
        :param dura: Duration to next Stop
        :return: None
        """
        node = Stop(statname, dura)
        if self.head is None:
            # Check if TrainLine is initialized
            self.head = node
            self.tail = node
            self.currentstop = node
            # Initialize by setting all parameters to the new node
        else:
            # If the TrainLine was started:
            self.head.prev = node
            node.next = self.head
            self.head = node
            # Set New Node to the head

    def addstopnexttocurrent(self, statname, dura):
        """
        Summary: Adds a Train Stop next to the Current Stop
        :param statname: Name of Train Stop
        :param dura: Duration to next Stop
        :return: None
        """
        if self.currentstop == self.tail:
            self.addstoptoend(statname, dura)
            # If the current stop is the tail, then append the new Stop
        else:
            # If current stop is not the tail
            node = Stop(statname, dura)
            # Create the new node
            self.currentstop.next.prev = node
            # Decouple currentstop from currentstop.next
            # to make room for new node
            node.next = self.currentstop.next
            self.currentstop.next = node
            node.prev = self.currentstop
            # Insert node into newly created space

    def addstoptoend(self, statname, dura):
        """
        Summary: Appends a Train Stop
        :param statname: Name of Train Stop
        :param dura: Duration to next Stop
        :return: None
        """
        node = Stop(statname, dura)
        # Create the new node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        # Set new node to Tail

    def setdestination(self, i):
        """
        Summary: Sets Destination to desired Node
        :param i: Index of Destination Node
        :return: None
        """
        count = 0
        it = self.head
        # "it" pointer indicates current position
        # and starts at 0
        while count < i:
            count += 1
            it = it.next
            # compares index number and count for a counter
            # to move "it" pointer to desired destination
        self.destination = it
        # Set destination to the pointers indicated position

    def calcduration(self):
        """
        Summary: Calculates the estimated time duration
        to the prior specified destination
        :return: the calculated duration
        """
        dur = 0
        it = self.currentstop
        # "it" pointer indicates current position
        # and starts at the current stop
        while it != self.destination:
            dur += it.duration
            it = it.next
            # Iterates through until pointer is at the destination
        print("Duration to  " + self.destination.stationname +
              " from  " + self.currentstop.stationname + ":")
        return dur


TrainLine = TrainLine()
print('Hello! Welcome to the Trainline. Please Start with Step 5 to initialize List')
# Set up User Input Menu
while True:
    print("The following trainline is: ")
    tmp = TrainLine.head
    while tmp is not None:
        print(tmp.stationname, end='<->')
        tmp = tmp.next
        # if the TrainLine exists, prints all node names in order
    print('\n')
    if TrainLine.currentstop is not None:
        print("\n Current Stop selected is: " + TrainLine.currentstop.stationname)
        # prints current stop if available
    if TrainLine.destination is not None:
        print("Destination selected is: " + TrainLine.destination.stationname)
        # prints destination if available
    choice = input(
        "Please select from the following choices: \n"
        "1. Display Trainline\n"
        "2. Move to Next Stop\n"
        "3. Move to previous Stop\n"
        "4. Add Stop after Current\n"
        "5. Add Stop to beginning\n"
        "6. Add Stop to End\n"
        "7. Set Destination\n"
        "8. Calculate total duration to destination\n")
    if choice == '2':
        if TrainLine.currentstop is not None:
            TrainLine.currentstop = TrainLine.currentstop.next
            # Function only works if current stop exists
        else:
            print("CANNOT DO! PLEASE DEFINE CURRENT STOP FIRST")
    elif choice == '3':
        if TrainLine.currentstop is not None:
            TrainLine.currentstop = TrainLine.currentstop.prev
            # Function only works if current stop exists
        else:
            print("CANNOT DO! PLEASE DEFINE CURRENT STOP FIRST")
    elif choice == '4':
        if TrainLine.currentstop is None:
            print("CANNOT DO! PLEASE DEFINE CURRENT STOP FIRST")
            # Function only works if current stop exists
        else:
            stationname = input("Please enter the station name: ")
            duration = input("Please enter the duration to the station: ")
            TrainLine.addstopnexttocurrent(stationname, int(duration))
    elif choice == '5':
        stationname = input("Please enter the station name: ")
        duration = input("Please enter the duration to the station: ")
        TrainLine.addstoptohead(stationname, int(duration))
        # Adds a Stop to the start of the Trainline
    elif choice == '6':
        if TrainLine.head is None:
            print("CANNOT DO! PLEASE DEFINE LIST")
            # Function requires the Trainline to be populated to work
            continue
        stationname = input("Please enter the station name: ")
        duration = input("Please enter the duration to the station: ")
        TrainLine.addstoptoend(stationname, int(duration))
    elif choice == '7':
        dest = input("Please input index of Destination: ")
        if dest is not True:
            # Function requires a destination to work
            print('Stop is not in Trainline.\n')
            dest = input('Please choose a Stop indexed within TrainLine: ')
        TrainLine.setdestination(int(dest))
    elif choice == '8':
        if TrainLine.destination is None:
            # Function requires a destination to work
            print("CANNOT DO! PLEASE SET THE DESTINATION FIRST")
        else:
            TrainLine.calcduration()
