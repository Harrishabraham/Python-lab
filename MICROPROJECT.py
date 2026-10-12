import heapq
from datetime import datetime
class CampusNode:
    def __init__(self,name):
        self.name=name
        self.children=[]
    def add_child(self,node):
        self.children.append(node)
class CampusTree:
    def __init__(self):
        self.root=CampusNode("Campus")
        self.location_map={"1":"CSE Ground Floor","2":"CSE First Floor","3":"CSE Second Floor","4":"ECE Ground Floor","5":"ECE First Floor","6":"Mechanical Ground Floor","7":"Mechanical First Floor","8":"Hostel Block A","9":"Hostel Block B","10":"Principal Office","11":"Security Office","12":"Reception"}
        self.location_numbers={v:k for k,v in self.location_map.items()}
        self.build_tree()
    def build_tree(self):
        academic=CampusNode("Academic Block")
        cse=CampusNode("CSE Department")
        ece=CampusNode("ECE Department")
        mechanical=CampusNode("Mechanical Department")
        cse.add_child(CampusNode("CSE Ground Floor"))
        cse.add_child(CampusNode("CSE First Floor"))
        cse.add_child(CampusNode("CSE Second Floor"))
        ece.add_child(CampusNode("ECE Ground Floor"))
        ece.add_child(CampusNode("ECE First Floor"))
        mechanical.add_child(CampusNode("Mechanical Ground Floor"))
        mechanical.add_child(CampusNode("Mechanical First Floor"))
        academic.add_child(cse)
        academic.add_child(ece)
        academic.add_child(mechanical)
        hostel=CampusNode("Hostel")
        hostel.add_child(CampusNode("Hostel Block A"))
        hostel.add_child(CampusNode("Hostel Block B"))
        administration=CampusNode("Administration")
        administration.add_child(CampusNode("Principal Office"))
        administration.add_child(CampusNode("Security Office"))
        administration.add_child(CampusNode("Reception"))
        self.root.add_child(academic)
        self.root.add_child(hostel)
        self.root.add_child(administration)
    def display(self,node=None,level=0):
        if node is None:
            node=self.root
        if node.name in self.location_numbers:
            print("  "*level+"└── ["+self.location_numbers[node.name]+"] "+node.name)
        else:
            print("  "*level+"└── "+node.name)
        for child in node.children:
            self.display(child,level+1)
class Emergency:
    def __init__(self,emergency_id,roll_number,emergency_type,location,description):
        self.emergency_id=emergency_id
        self.roll_number=roll_number
        self.emergency_type=emergency_type
        self.location=location
        self.description=description
        self.status="Pending"
        self.responder=None
        self.time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.response_time=None
        self.resolved_at=None
        self.feedback=None
    def display(self):
        print("Emergency ID:",self.emergency_id)
        print("Roll Number:",self.roll_number)
        print("Emergency Type:",self.emergency_type)
        print("Location:",self.location)
        print("Description:",self.description)
        print("Status:",self.status)
        print("Responder:",self.responder if self.responder else "Not Assigned")
        print("Response Time:",self.response_time if self.response_time else "Not Available")
        print("Reported At:",self.time)
        print("Resolved At:",self.resolved_at if self.resolved_at else "Not Resolved")
        print("Feedback:",self.feedback if self.feedback else "Not Given")
class Responder:
    def __init__(self,responder_id,name,role):
        self.responder_id=responder_id
        self.name=name
        self.role=role
        self.available=True
        self.current_emergency=None
    def display(self):
        print("ID:",self.responder_id,"Name:",self.name,"Role:",self.role,"Status:","Available" if self.available else "Busy")
class EmergencyCoordinator:
    def __init__(self):
        self.campus=CampusTree()
        self.emergencies={}
        self.emergency_queue=[]
        self.responders=[Responder(1,"Arun","Medical"),Responder(2,"Bala","Fire"),Responder(3,"Karthik","Security"),Responder(4,"Vijay","General Response")]
        self.next_emergency_id=1
        self.history=[]
    def report_emergency(self):
        self.campus.display()
        roll_number=input("Enter Roll Number: ")
        print("1. Medical")
        print("2. Fire")
        print("3. Security")
        print("4. Accident")
        print("5. Other")
        type_choice=input("Enter Emergency Type: ")
        type_map={"1":"Medical","2":"Fire","3":"Security","4":"Accident","5":"Other"}
        if type_choice not in type_map:
            print("Invalid Emergency Type")
            return
        location_choice=input("Enter Location Number: ")
        if location_choice not in self.campus.location_map:
            print("Invalid Location")
            return
        location=self.campus.location_map[location_choice]
        description=input("Enter Description: ")
        emergency=Emergency(self.next_emergency_id,roll_number,type_map[type_choice],location,description)
        self.emergencies[self.next_emergency_id]=emergency
        heapq.heappush(self.emergency_queue,(emergency.time,self.next_emergency_id))
        self.history.append(self.next_emergency_id)
        print("Emergency Reported Successfully")
        print("Emergency ID:",self.next_emergency_id)
        self.next_emergency_id+=1
    def find_responder(self,emergency_type):
        required_role={"Medical":"Medical","Fire":"Fire","Security":"Security","Accident":"General Response","Other":"General Response"}
        role=required_role.get(emergency_type,"General Response")
        for responder in self.responders:
            if responder.role==role and responder.available:
                return responder
        return None
    def calculate_response_time(self,location):
        if "Office" in location:
            return "2 minutes"
        if "Hostel" in location:
            return "3 minutes"
        if "Ground Floor" in location:
            return "4 minutes"
        if "First Floor" in location:
            return "5 minutes"
        if "Second Floor" in location:
            return "6 minutes"
        return "5 minutes"
    def process_next_emergency(self):
        if not self.emergency_queue:
            print("No Pending Emergencies")
            return
        time,emergency_id=heapq.heappop(self.emergency_queue)
        emergency=self.emergencies[emergency_id]
        if emergency.status!="Pending":
            self.process_next_emergency()
            return
        responder=self.find_responder(emergency.emergency_type)
        if responder is None:
            print("No Responder Available")
            heapq.heappush(self.emergency_queue,(time,emergency_id))
            return
        responder.available=False
        responder.current_emergency=emergency_id
        emergency.responder=responder.name
        emergency.status="In Progress"
        emergency.response_time=self.calculate_response_time(emergency.location)
        print("Emergency Processed")
        print("Emergency ID:",emergency.emergency_id)
        print("Responder:",responder.name)
        print("Response Time:",emergency.response_time)
    def complete_emergency(self):
        emergency_id=input("Enter Emergency ID: ")
        if not emergency_id.isdigit():
            print("Invalid Emergency ID")
            return
        emergency_id=int(emergency_id)
        if emergency_id not in self.emergencies:
            print("Emergency Not Found")
            return
        emergency=self.emergencies[emergency_id]
        if emergency.status!="In Progress":
            print("Emergency is not in progress")
            return
        emergency.status="Resolved"
        emergency.resolved_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for responder in self.responders:
            if responder.name==emergency.responder:
                responder.available=True
                responder.current_emergency=None
                break
        feedback=input("Enter Feedback: ")
        emergency.feedback=feedback
        print("Emergency Completed Successfully")
    def view_all_emergencies(self):
        if not self.emergencies:
            print("No Emergencies Found")
            return
        for emergency in self.emergencies.values():
            emergency.display()
    def view_responders(self):
        if not self.responders:
            print("No Responders Found")
            return
        for responder in self.responders:
            responder.display()
    def view_history(self):
        if not self.history:
            print("No Emergency History")
            return
        for emergency_id in self.history:
            emergency=self.emergencies[emergency_id]
            print("ID:",emergency.emergency_id,"Roll Number:",emergency.roll_number,"Type:",emergency.emergency_type,"Status:",emergency.status)
    def search_emergency(self):
        value=input("Enter Emergency ID or Roll Number: ")
        found=False
        for emergency in self.emergencies.values():
            if str(emergency.emergency_id)==value or emergency.roll_number==value:
                emergency.display()
                found=True
        if not found:
            print("Emergency Not Found")
    def dashboard(self):
        total=len(self.emergencies)
        pending=sum(1 for e in self.emergencies.values() if e.status=="Pending")
        progress=sum(1 for e in self.emergencies.values() if e.status=="In Progress")
        resolved=sum(1 for e in self.emergencies.values() if e.status=="Resolved")
        available=sum(1 for r in self.responders if r.available)
        print("Total Emergencies:",total)
        print("Pending:",pending)
        print("In Progress:",progress)
        print("Resolved:",resolved)
        print("Available Responders:",available)
    def filter_emergencies(self):
        print("1. Pending")
        print("2. In Progress")
        print("3. Resolved")
        choice=input("Enter Filter: ")
        status_map={"1":"Pending","2":"In Progress","3":"Resolved"}
        if choice not in status_map:
            print("Invalid Filter")
            return
        status=status_map[choice]
        found=False
        for emergency in self.emergencies.values():
            if emergency.status==status:
                emergency.display()
                found=True
        if not found:
            print("No Emergencies Found")
    def run(self):
        while True:
            print("1. Display Campus Tree")
            print("2. Report Emergency")
            print("3. View All Emergencies")
            print("4. Process Next Emergency")
            print("5. Complete Emergency")
            print("6. View Responders")
            print("7. View Emergency History")
            print("8. Search Emergency")
            print("9. Emergency Dashboard")
            print("10. Filter Emergencies")
            print("11. Exit")
            choice=input("Enter Choice: ")
            if choice=="1":
                self.campus.display()
            elif choice=="2":
                self.report_emergency()
            elif choice=="3":
                self.view_all_emergencies()
            elif choice=="4":
                self.process_next_emergency()
            elif choice=="5":
                self.complete_emergency()
            elif choice=="6":
                self.view_responders()
            elif choice=="7":
                self.view_history()
            elif choice=="8":
                self.search_emergency()
            elif choice=="9":
                self.dashboard()
            elif choice=="10":
                self.filter_emergencies()
            elif choice=="11":
                print("Thank You")
                break
            else:
                print("Invalid Choice")
coordinator=EmergencyCoordinator()
coordinator.run()
