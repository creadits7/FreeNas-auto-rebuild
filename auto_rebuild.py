import subprocess, re
from time import sleep



def findWord(word, text):
    """word: word to search for in text (String)
       text: text in you wish to search for the word (String)
       returns a count of how many times the word occurs (Int)"""

    count = 0
    text_copy = text
    while text_copy.find(word) != -1:
        text_copy = text_copy[text_copy.find(word) + len(word):]
        count += 1
    return count

def checkPoolStatus(pool_name):
    """pool_name: The name of the ZFS pool being checked (String)
       Returns GOOD or BAD depending on the health or the pool"""

    #Runs command to retrieve status of pool
    command = "zpool list -o health " + pool_name

    #Test to make sure command runs successfully. Should only fail if pool name is incorrect.
    #try:
        #process = subprocess.check_call([command], stdout=subprocess.PIPE, shell=True)
    #except subprocess.CalledProcessError:
        #return "Invalid command. \"" + command + "\". Was name of pool supplied incorrectly?"

    #Uses sample output for testing
    f = open("cmd_output.txt", 'r')

    #Converts command output to String
    #output = str(process.communicate())

    output = f.read()
    f.close()


    #Successful output will look like: HEALTH ONLINE

    #Check and make sure pool is online
    if "ONLINE" in output:
        return "GOOD"

    #If not, pool is DEGRADED or OFFLINE
    else:
        return "BAD"

def checkDriveSpares(pool_name):
    """pool_name: Name of the ZFS pool we are checking (String)
       returns number of spare drives with status AVAILABLE (Int)"""
    # Runs command to retrieve status of pool
    command = "zpool status" + " " + pool_name

    # Test to make sure command runs successfully. Should only fail if pool name is incorrect.
    # try:
    # process = subprocess.check_call([command], stdout=subprocess.PIPE, shell=True)
    # except subprocess.CalledProcessError:
    # return "Invalid command. \"" + command + "\". Was name of pool supplied incorrectly?"

    # Uses sample output for testing
    f = open("cmd_output.txt", 'r')

    # Converts command output to String
    # output = str(process.communicate())

    output = f.read()
    f.close()

    spares = findWord("AVAIL", output)

    return spares

def getFailedDriveId(pool_name):




while True:
    #mainStatus = subprocess.Popen(["zpool status -x"], stdout=subprocess.PIPE, shell=True)
    #mainStatus = str(mainStatus.communicate())

    mainStatus = "all pools are healthly"

    if mainStatus == "all pools are healthy":
        sleep(60)
    else:
        #get a list of pools
        #pools = subprocess.Popen(["zpool list"], stdout=subprocess.PIPE, shell=True)
        #pools = str(pools.communicate())

        f = open("zpool list.txt", 'r')

        pools = []

        #CReates a list of the pools by name
        for i in f.readlines():
            if "NAME" not in i:
                pools.append(i)
        names = []
        for pool in pools:
            names.append(re.search(r'[\S]+', pool).group(0))

        for i in names:
            if checkPoolStatus(i) == "BAD":
                if checkDriveSpares(i) > 0:
                    #TODO Get bad drive ID
                    #TODO get spare id
                    #TODO replace drive









        break


