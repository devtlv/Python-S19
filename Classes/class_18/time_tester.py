import time

def test_sleep():
    # time.sleep(x): suspend the program for x seconds
    print("And the winner is..")
    print("3..")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1..")
    time.sleep(1)
    print("Marev !")

t_before = time.time()
test_sleep()
t_after  = time.time()
print("test_sleep took {} seconds to execute".format(t_after-t_before))




