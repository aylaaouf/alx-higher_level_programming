#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name_hid in dir(hidden_4):
        if name_hid[:2] != "__":
            print("{}".format(name_hid))