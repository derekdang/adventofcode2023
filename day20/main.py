# https://adventofcode.com/2023/day/20
import sys
from tqdm import tqdm
import math

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

def generate_graph(flip_flop_map, conjunction_map, broadcaster):
    for line in input:
        m, _ = line.split("->")
        m = m.strip()    
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

def p1(BUTTON_PUSHES: int) -> int:
    flip_flop_map = {}
    conjunction_map = {}
    broadcaster = Broadcaster([], False)
    generate_graph(flip_flop_map, conjunction_map, broadcaster)
        
    for cm in conjunction_map.values():
        cm.start()

    cn_senders = conjunction_map["cn"].senders
    num_hi, num_lo = simulate_button_pushes(flip_flop_map, conjunction_map, broadcaster, BUTTON_PUSHES)
    return (num_hi * (num_lo + BUTTON_PUSHES))

def simulate_button_pushes(flip_flop_map, conjunction_map, broadcaster, BUTTON_PUSHES) -> (int, int):
    num_hi = 0
    num_lo = 0
    for i in tqdm(range(BUTTON_PUSHES)):
        q = []
        for bl in broadcaster.listeners:
            q.append((broadcaster.name, bl, False))
        while len(q) != 0:
            curr_size = len(q)
            last_added = 0
            for _ in range(curr_size - last_added):
                last_sender, rec_signal, high_signal = q.pop(0)
                signal_sent = "high" if high_signal else "low"
                if high_signal:
                    num_hi += 1
                else:
                    num_lo += 1
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
                    if high_signal:
                        cm.last_sender_high_s[last_sender] = True
                    else:
                        cm.last_sender_high_s[last_sender] = False

                    for cml in cm.listeners:
                        q.append((rec_signal, cml, cm.should_send_high()))
                        last_added += 1
                    break
    return num_hi,num_lo

if __name__ == "__main__":
    input = open(sys.argv[1]).read().splitlines()
    print (p1(1000))
