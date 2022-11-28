from psychopy import visual, monitors, core, event
from random import randrange

#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(fullscr=False, monitor=mon, size=(800,800), color='black', units='pix')
win.mouseVisible = False
timer = core.CountdownTimer() #timer for trial duration

stim = visual.Rect(win, size=(10,10), color='blue') #random example stimulus
stim.pos=(-100,-100)
stimText = visual.TextStim(win, units='pix')
stimText.pos=(-100, -110)
stimText.color='white'
stimText.height =10
nTrials=5 #number of trials to demonstrate effect
#start trial sequence
for trial in range(nTrials):   
    frameN=-1 #set frame for beginning of trial
    timer.reset() #reset timer
    timer.add(4) #2-second trial time
    while timer.getTime() > 0: #until the end of trial
        frameN+=1#count frames     
        stim.pos=(-100+frameN, -100+frameN)   
        stim.draw()
        stimText.pos=(-100+frameN, -110+frameN)
        stimText.text=str(frameN)
        stimText.draw()
        win.flip()
        
win.mouseVisible = True
win.close()
