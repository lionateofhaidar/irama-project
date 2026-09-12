# TraCI4Traffic Lights - SUMO Documentation

Sumber file: SUMO_Docs_TraCI4Traffic_Lights.html
Diunduh: 2026-09-12 (arsip teks otomatis)

---

possibility to control a running road traffic simulation. TraCI uses a

TCP-based client/server architecture where SUMO acts as a server and the

external script (the “controller”) is the client. In this tutorial the

“controller” is a python script which receives information about the

simulation state from the server and then sends instructions back.

It is assumed that road network building and routes definition is known

All files mentioned here can also be found in the

/docs/tutorial/traci_tls directory of your installation. The most

recent version can be found in the repository at

Our example plays on a simple signalized intersection with four

approaches. We only have traffic on the horizontal axis and important

vehicles (like trams, trains, fire engines, ...) on the vertical axis

from north to south. On the approach in the north we have an induction

loop to recognize entering vehicles. As long as no vehicle enters from the

north, we give green on the horizontal axis all the time; but when a

vehicle enters the induction loop we switch the signal immediately so

the vehicle can cross the intersection without stopping.

To run the example you need to execute the script

You need to press start in the simulation gui to run the tutorial.

The net-definition can be found in the files

generated randomly by the script. The vehicles leave the source

according to a Poisson process approximated here by a binomial

vehicle is generated every 30 seconds in average.

The control logic resides in the python script

the routes, acts with the server and controls the traffic light. It

makes use of the TraCI python API bundled with SUMO. A description of

For a detailed list of available functions see the

The main program is implemented in the script

first generate the routes as described above. Then

. The start call also connects our script with the

Then we start to control the simulation. We let the server simulate one

simulation step, read the induction loop and switch the phase of the

traffic light until the end is reached where no vehicle exists on the

road anymore. If we find a vehicle on the induction loop the phase is

switched such that the north-south direction gets green. If no vehicle

is on the detector, and we are not already in the process of switching

(so EW has still green), we try to keep this phase by simply setting it

again. In the end, we close the connection.

We want to run this simulation in SUMO, acting as a server, and control

the signal dependent on the actual simulation state. For this task TraCI

offers commands which are described in the corresponding article

in detail. For this example we will use only

The commands are embedded in TCP messages but the direct client server

communication is opaque to the user. The four commands needed in this

traci.inductionloop.getLastStepVehicleNumber(IndLoopID)

The methods for sending and receiving the messages,

and there is no need to call them directly. In this

section we will show the composition of a command using the example of

traci.trafficlight.setRedYellowGreenState

This method sets the phase of a traffic light, so it gets the ID of the

traffic light and the new phase as parameter. The phase definitions can

be read from the sumo network and are described in

If the phase is already the current one, it is restarted from the