from psychopy import visual, monitors, core, event
from random import randrange

#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(fullscr=False, monitor=mon, size=(800,800), color='black', units='pix')
win.mouseVisible = False
timer = core.CountdownTimer() #timer for trial duration
stim = visual.Rect(win, size=(10,10), color='blue') #random example stimulus
myMouse = event.Mouse(visible=True,win=win)

line = visual.Line(
    win=win,
    units="pix",
    lineColor=[1, 1, 1],
    lineWidth = 5
)
line.start = [-10, 100]
line.end = [-10, 120]

nTrials=5 #number of trials to demonstrate effect
moveAmount = 1
goalWidth = 10
#start trial sequence
for trial in range(nTrials):   
    xPos = 0;
    frameN=-1 #set frame for beginning of trial
    timer.reset() #reset timer
    timer.add(4) #2-second trial time
    offset = randrange(-20,20,2) # -10 to 10
    while timer.getTime() > 0: #until the end of trial
        frameN+=1#count frames        
        mouseLoc=myMouse.getPos()
        print(mouseLoc)
        # if keys: #if there are keypresses stored in keys
        #     sub_resp = keys[0] #only count the first keypress        
        #     if sub_resp == 'left':
        #         xPos = xPos - moveAmount
        #     if sub_resp == 'right':
        #         xPos = xPos + moveAmount
        stim.pos=(mouseLoc[0],frameN) #make stim move slowly upward from center
          
        stim.draw() #draw stim
        line.start = [-goalWidth+offset, 200]
        line.end = [-goalWidth+offset, 220]
        line.draw()
        
        line.start = [goalWidth+offset, 200]
        line.end = [goalWidth+offset, 220]
        line.draw()
        win.flip()
        
win.mouseVisible = True
win.close()
