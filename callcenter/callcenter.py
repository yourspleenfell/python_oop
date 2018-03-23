class Call(object):
    call_count = []
    def __init__(self, name, phone, reason):
        self.name = name
        self.phone = phone
        self.reason = reason
        Call.call_count.append(self)
        self.unique_id()
        self.call_time()
    def unique_id(self):
        import uuid
        id = uuid.uuid4().hex[:10]
        self.id = id
        return self
    def call_time(self):
        import datetime
        time = str(datetime.datetime.now().time())
        self.time = time
        return self
    def display(self):
        print "Call ID: " + self.id
        print "Caller Name: " + self.name
        print "Caller Phone Number: " + self.phone
        print "Call Time: " + self.time
        print "Reason for Call: " + self.reason
        print ""
        return self

class CallCenter(object):
    call_count = Call.call_count
    def __init__(self, location):
        self.location = location
        self.call_count = Call.call_count
        self.queue = len(self.call_count)
    def add_call(self):
        if (self.queue < len(CallCenter.call_count)):
            self.queue = len(CallCenter.call_count)
        return self
    def remove_call(self):
        self.call_count.remove(self.call_count[0])
        print "Call ended. There are", len(self.call_count), "calls remanining in the queue."
        print ""
        return self
    def remove_phone(self, str):
        for val in self.call_count:
            if (val.phone == str):
                self.call_count.remove(val)
                print "Call with " + val.name +  " Removed"
                print ""
        return self
    def call_info(self):
        for val in self.call_count:
            print "Caller Name: " + val.name
            print "Caller Phone Number: " + val.phone
            print "Queue Length:", self.queue
            print ""
        return self

center = CallCenter("Mesa, Arizona")

call1 = Call("John Hopkins", "661-867-5309", "Microwave won't work").display()
call2 = Call("Bob Ross", "661-867-5310", "Oven won't work").display()
call3 = Call("George Harrison", "661-867-5311", "Wanted to say thank you").display()
call4 = Call("Matthew Perry", "661-867-5312", "You're stealing my money").display()
call5 = Call("Old Man Toofins", "661-867-5313", "Toaster exploded").display()
call6 = Call("Brandon Sanderson", "661-867-5314", "Toaster exploded").display()
call7 = Call("Robert Jordan", "661-867-5315", "Toaster exploded").display()


center.remove_phone("661-867-5314")
center.call_info()
center.remove_call()

call8 = Call("Hiro Wash", "661-867-5555", "I am sad")
center.add_call()
center.call_info()