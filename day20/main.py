# https://adventofcode.com/2023/day/20
import sys
from tqdm import tqdm
# bfs essentially graph
class FlipFlopModule:
    def __init__(self, name, listeners, active):
        self.name = name
        self.listeners = listeners
        self.active = active

class ConjunctionModule:

    def __init__(self, name, senders, listeners):
        self.name = name
        self.senders = senders
        self.listeners = listeners
        self.last_sender_high_s = {}

    def start(self):
        for s in self.senders:
            self.last_sender_high_s[s] = False
    
    def should_send_high(self):
        return not all(self.last_sender_high_s.values())

class Broadcaster:
    def __init__(self, listeners, send_high):
        self.name = "broacaster"
        self.listeners = listeners
        self.send_high = send_high
    
def p1():
    flip_flop_map = {}
    conjunction_map = {}
    for line in input:
        m, _ = line.split("->")
        m = m.strip()    
        broadcaster = Broadcaster([], False)
        name = m[1:]
        if m[0] == "%":
            module = FlipFlopModule(name, [], False)
            flip_flop_map[name] = module
        elif m[0] == "&":
            module = ConjunctionModule(name, [], [])
            conjunction_map[name] = module
        else:
            pass
    
    for line in input:
        m, receivers = line.split("->")
        m = m.strip()
        receivers_arr = receivers.strip().split(", ")
        # print(m, receivers_arr)
        name = m[1:]

        if m[0] == "%":
            module = flip_flop_map[name]
            for r in receivers_arr:
                if r in conjunction_map:
                    conjunction_map[r].senders.append(name)
                module.listeners.append(r)
        elif m[0] == "&":
            module = conjunction_map[name]
            for r in receivers_arr:
                if r in conjunction_map:
                    conjunction_map[r].senders.append(name)
                module.listeners.append(r)
        else:
            for r in receivers_arr:
                if r in flip_flop_map:
                    broadcaster.listeners.append(r)
                elif r in conjunction_map:
                    broadcaster.listeners.append(r)
        
    for cm in conjunction_map.values():
        cm.start()
    # for _, cm in conjunction_map.items():
    #     print(f"{cm.name}, senders: {cm.senders}, listeners: {cm.listeners}, sender_remember: {cm.last_sender_high_s}")
    # for _, ffm in flip_flop_map.items():
    #     print(f"{ffm.name}, listeners: {ffm.listeners}, active: {ffm.active}")
    # print(f"broadcaster, listeners:{broadcaster.listeners}")

    BUTTON_PUSHES = 1000
    # for _ in range(BUTTON_PUSHES):
    # cn_senders = conjunction_map["cn"].senders
    num_hi = 0
    num_lo = 0
    for i in tqdm(range(BUTTON_PUSHES)):
        q = []
        for bl in broadcaster.listeners:
            q.append((broadcaster.name, bl, False))
        while len(q) != 0:
            curr_size = len(q)
            last_added = 0
            # print(q)
            for _ in range(curr_size - last_added):
                last_sender, rec_signal, high_signal = q.pop(0)
                signal_sent = "high" if high_signal else "low"
                if rec_signal == "rx" and signal_sent == "low":
                    print(f"{i}: {rec_signal}, {signal_sent}")
                if high_signal:
                    num_hi += 1
                else:
                    num_lo += 1
                # print(f"{last_sender} -> sends {signal_sent} to {rec_signal}")
                if rec_signal in flip_flop_map:
                    rm = flip_flop_map[rec_signal]
                    if not high_signal:
                        send_high = True if not rm.active else False
                        rm.active = not rm.active
                        for rml in rm.listeners:
                            q.append((rec_signal, rml, send_high))
                            last_added += 1
                        break
                elif rec_signal in conjunction_map:
                    cm = conjunction_map[rec_signal]
                    if cm.name == "cn":
                        pass
                        # print(f"{cm.name}, senders: {cm.senders}, listeners: {cm.listeners}, sender_remember: {cm.last_sender_high_s}")
                    if high_signal:
                        cm.last_sender_high_s[last_sender] = True
                    else:
                        cm.last_sender_high_s[last_sender] = False

                    for cml in cm.listeners:
                        q.append((rec_signal, cml, cm.should_send_high()))
                        last_added += 1
                    break
        # print("\n\n\n")
        # for _, cm in conjunction_map.items():
        #     print(f"{i + 1}: {cm.name}, senders: {cm.senders}, listeners: {cm.listeners}, sender_remember: {cm.last_sender_high_s}")
        # for _, ffm in flip_flop_map.items():
        #     print(f"{i + 1}: {ffm.name}, listeners: {ffm.listeners}, active: {ffm.active}")
        # print("\n\n\n")
    print(num_hi * (num_lo + BUTTON_PUSHES))
if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    p1()
