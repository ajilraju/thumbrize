#https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBHjFtGpFX1b3ljX0MNXsD0o0qv3trd7Gw
#key = AIzaSyBHjFtGpFX1b3ljX0MNXsD0o0qv3trd7Gw

# import the necessary packages
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))