class Alice():
    '''Creates set of packets to send them to Bob'''
    def __init__(self, set_of_packets):
        self.set_of_packets = set_of_packets

    # def create_set(self):
    #     pass


# class InternetProcessing():
#     '''Middle procedure, checks are there some set of packets 
#     on Alice's computer and sends them to Bob
#     '''
    def deliver_set(self):
        if self.set_of_packets == True:
            return self.set_of_packets

    # def deliver_set(self):
    #     pass


class Bob():
    '''Checks are there some set of packets from Alice and delete them'''
    packets = Alice(input())

    def check_delivered(self):
        self.set_of_packets = self.packets.deliver_set()

    def delete_set(self):
        self.set_of_packets = 0