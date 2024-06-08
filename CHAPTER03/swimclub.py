import statistics
FOLDER = "swimdata/"

def read_swim_data(filename):
    """Return swim data from a file.

    Given the name of a swimmer's file (in filename), extract all the required
    data, then return it to the caller as a tuple.
    """
    
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")
    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip().split(",")
    converts = []
    for t in times:
       if ":" in t:                                 #for fix when don't exist minutes
            minutes, rest = t.split(":")
            seconds, hundredths = rest.split(".")
       else:
           minutes = 0
           seconds,hundredths = t.split(".")
       converts.append((int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths))
    average = statistics.mean(converts)
    min_secs, hundreths = str(round(average / 100, 2)).split(".")
    min_secs = int(min_secs)
    minutes = min_secs // 60
    seconds = min_secs - minutes*60
    average = str(minutes) + ":" +str(seconds) + "." + hundreths
    return swimmer, age, distance, stroke, times, average
