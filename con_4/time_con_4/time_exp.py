#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on 五月 30, 2023, at 10:24
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'time_exp'  # from the Builder filename that created this script
expInfo = {
    'participant': '000',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\User\\Documents\\program\\timeperception\\time_exp.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
textWelcomeMessage = visual.TextStim(win=win, name='textWelcomeMessage',
    text='歡迎來到本次的實驗\n\n請按"空白鍵"開始實驗',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyWelcome = keyboard.Keyboard()

# --- Initialize components for Routine "blank_1000" ---
textblank1000 = visual.TextStim(win=win, name='textblank1000',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_1 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# --- Initialize components for Routine "pra_img" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.95, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "estimation" ---
textreproductionstart = visual.TextStim(win=win, name='textreproductionstart',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
scale = visual.Slider(win=win, name='scale',
    startValue=None, size=(1.2, 0.04), pos=(0, -0.2), units=None,
    labels=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
key_next = keyboard.Keyboard()

# --- Initialize components for Routine "rest" ---
textrest = visual.TextStim(win=win, name='textrest',
    text='休息20秒\n\n時間結束會自動進入下一題',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textready = visual.TextStim(win=win, name='textready',
    text='即將進入下一題',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# --- Initialize components for Routine "start" ---
text = visual.TextStim(win=win, name='text',
    text='練習階段結束\n\n準備好請按"空白鍵"開始正式階段',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank_1000" ---
textblank1000 = visual.TextStim(win=win, name='textblank1000',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_1 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# --- Initialize components for Routine "pic" ---
emopic = visual.ImageStim(
    win=win,
    name='emopic', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "estimation" ---
textreproductionstart = visual.TextStim(win=win, name='textreproductionstart',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
scale = visual.Slider(win=win, name='scale',
    startValue=None, size=(1.2, 0.04), pos=(0, -0.2), units=None,
    labels=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'], ticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
key_next = keyboard.Keyboard()

# --- Initialize components for Routine "rest" ---
textrest = visual.TextStim(win=win, name='textrest',
    text='休息20秒\n\n時間結束會自動進入下一題',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textready = visual.TextStim(win=win, name='textready',
    text='即將進入下一題',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# --- Initialize components for Routine "End" ---
textEndMessage = visual.TextStim(win=win, name='textEndMessage',
    text='本次實驗到此結束\n\n感謝您的參與',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyEnd = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
_keyWelcome_allKeys = []
# keep track of which components have finished
WelcomeComponents = [textWelcomeMessage, keyWelcome]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcomeMessage* updates
    if textWelcomeMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcomeMessage.frameNStart = frameN  # exact frame index
        textWelcomeMessage.tStart = t  # local t and not account for scr refresh
        textWelcomeMessage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcomeMessage, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textWelcomeMessage.started')
        textWelcomeMessage.setAutoDraw(True)
    
    # *keyWelcome* updates
    waitOnFlip = False
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyWelcome.started')
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyWelcome.getKeys(keyList=['space'], waitRelease=False)
        _keyWelcome_allKeys.extend(theseKeys)
        if len(_keyWelcome_allKeys):
            keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
            keyWelcome.rt = _keyWelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyWelcome.keys in ['', [], None]:  # No response was made
    keyWelcome.keys = None
thisExp.addData('keyWelcome.keys',keyWelcome.keys)
if keyWelcome.keys != None:  # we had a response
    thisExp.addData('keyWelcome.rt', keyWelcome.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pra_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pink_con.xlsx'),
    seed=None, name='pra_trials')
thisExp.addLoop(pra_trials)  # add the loop to the experiment
thisPra_trial = pra_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPra_trial.rgb)
if thisPra_trial != None:
    for paramName in thisPra_trial:
        exec('{} = thisPra_trial[paramName]'.format(paramName))

for thisPra_trial in pra_trials:
    currentLoop = pra_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPra_trial.rgb)
    if thisPra_trial != None:
        for paramName in thisPra_trial:
            exec('{} = thisPra_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "blank_1000" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sound_1.setSound('sound/trueding.wav', secs=1, hamming=True)
    sound_1.setVolume(1.0, log=False)
    # keep track of which components have finished
    blank_1000Components = [textblank1000, sound_1]
    for thisComponent in blank_1000Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank_1000" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textblank1000* updates
        if textblank1000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textblank1000.frameNStart = frameN  # exact frame index
            textblank1000.tStart = t  # local t and not account for scr refresh
            textblank1000.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textblank1000, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textblank1000.started')
            textblank1000.setAutoDraw(True)
        if textblank1000.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textblank1000.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                textblank1000.tStop = t  # not accounting for scr refresh
                textblank1000.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textblank1000.stopped')
                textblank1000.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_1.started', tThisFlipGlobal)
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_1.stopped')
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_1000Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank_1000" ---
    for thisComponent in blank_1000Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "pra_img" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    image.setImage(pink)
    # keep track of which components have finished
    pra_imgComponents = [image]
    for thisComponent in pra_imgComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pra_img" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + pra_duration-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra_imgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pra_img" ---
    for thisComponent in pra_imgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "pra_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "estimation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    textreproductionstart.setText('時間估計作業\n請透過滑鼠將刺激呈現時間點在以下量尺中\n按下空白鍵進入下一題')
    scale.reset()
    key_next.keys = []
    key_next.rt = []
    _key_next_allKeys = []
    # keep track of which components have finished
    estimationComponents = [textreproductionstart, scale, key_next]
    for thisComponent in estimationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "estimation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textreproductionstart* updates
        if textreproductionstart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textreproductionstart.frameNStart = frameN  # exact frame index
            textreproductionstart.tStart = t  # local t and not account for scr refresh
            textreproductionstart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textreproductionstart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textreproductionstart.started')
            textreproductionstart.setAutoDraw(True)
        
        # *scale* updates
        if scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scale.frameNStart = frameN  # exact frame index
            scale.tStart = t  # local t and not account for scr refresh
            scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'scale.started')
            scale.setAutoDraw(True)
        
        # *key_next* updates
        waitOnFlip = False
        if key_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_next.frameNStart = frameN  # exact frame index
            key_next.tStart = t  # local t and not account for scr refresh
            key_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next.started')
            key_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next.status == STARTED and not waitOnFlip:
            theseKeys = key_next.getKeys(keyList=['space'], waitRelease=False)
            _key_next_allKeys.extend(theseKeys)
            if len(_key_next_allKeys):
                key_next.keys = _key_next_allKeys[-1].name  # just the last key pressed
                key_next.rt = _key_next_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in estimationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "estimation" ---
    for thisComponent in estimationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pra_trials.addData('scale.response', scale.getRating())
    pra_trials.addData('scale.rt', scale.getRT())
    # check responses
    if key_next.keys in ['', [], None]:  # No response was made
        key_next.keys = None
    pra_trials.addData('key_next.keys',key_next.keys)
    if key_next.keys != None:  # we had a response
        pra_trials.addData('key_next.rt', key_next.rt)
    # the Routine "estimation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "rest" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sound_2.setSound('sound/trueding.wav', secs=1.0, hamming=True)
    sound_2.setVolume(1.0, log=False)
    # keep track of which components have finished
    restComponents = [textrest, textready, sound_2]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rest" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textrest* updates
        if textrest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textrest.frameNStart = frameN  # exact frame index
            textrest.tStart = t  # local t and not account for scr refresh
            textrest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textrest, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textrest.started')
            textrest.setAutoDraw(True)
        if textrest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textrest.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                textrest.tStop = t  # not accounting for scr refresh
                textrest.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textrest.stopped')
                textrest.setAutoDraw(False)
        
        # *textready* updates
        if textready.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            textready.frameNStart = frameN  # exact frame index
            textready.tStart = t  # local t and not account for scr refresh
            textready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textready, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textready.started')
            textready.setAutoDraw(True)
        if textready.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textready.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                textready.tStop = t  # not accounting for scr refresh
                textready.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textready.stopped')
                textready.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_2.started', tThisFlipGlobal)
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_2.stopped')
                sound_2.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest" ---
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-20.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'pra_trials'


# --- Prepare to start Routine "start" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
startComponents = [text, key_resp]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start" ---
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pic_condition.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "blank_1000" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sound_1.setSound('sound/trueding.wav', secs=1, hamming=True)
    sound_1.setVolume(1.0, log=False)
    # keep track of which components have finished
    blank_1000Components = [textblank1000, sound_1]
    for thisComponent in blank_1000Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank_1000" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textblank1000* updates
        if textblank1000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textblank1000.frameNStart = frameN  # exact frame index
            textblank1000.tStart = t  # local t and not account for scr refresh
            textblank1000.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textblank1000, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textblank1000.started')
            textblank1000.setAutoDraw(True)
        if textblank1000.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textblank1000.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                textblank1000.tStop = t  # not accounting for scr refresh
                textblank1000.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textblank1000.stopped')
                textblank1000.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_1.started', tThisFlipGlobal)
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_1.stopped')
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_1000Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank_1000" ---
    for thisComponent in blank_1000Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "pic" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    emopic.setSize((0.95,0.7))
    emopic.setImage(emo_pic)
    # keep track of which components have finished
    picComponents = [emopic]
    for thisComponent in picComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pic" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *emopic* updates
        if emopic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            emopic.frameNStart = frameN  # exact frame index
            emopic.tStart = t  # local t and not account for scr refresh
            emopic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(emopic, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'emopic.started')
            emopic.setAutoDraw(True)
        if emopic.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > emopic.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                emopic.tStop = t  # not accounting for scr refresh
                emopic.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'emopic.stopped')
                emopic.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in picComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pic" ---
    for thisComponent in picComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "pic" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "estimation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    textreproductionstart.setText('時間估計作業\n請透過滑鼠將刺激呈現時間點在以下量尺中\n按下空白鍵進入下一題')
    scale.reset()
    key_next.keys = []
    key_next.rt = []
    _key_next_allKeys = []
    # keep track of which components have finished
    estimationComponents = [textreproductionstart, scale, key_next]
    for thisComponent in estimationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "estimation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textreproductionstart* updates
        if textreproductionstart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textreproductionstart.frameNStart = frameN  # exact frame index
            textreproductionstart.tStart = t  # local t and not account for scr refresh
            textreproductionstart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textreproductionstart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textreproductionstart.started')
            textreproductionstart.setAutoDraw(True)
        
        # *scale* updates
        if scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scale.frameNStart = frameN  # exact frame index
            scale.tStart = t  # local t and not account for scr refresh
            scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'scale.started')
            scale.setAutoDraw(True)
        
        # *key_next* updates
        waitOnFlip = False
        if key_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_next.frameNStart = frameN  # exact frame index
            key_next.tStart = t  # local t and not account for scr refresh
            key_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_next.started')
            key_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next.status == STARTED and not waitOnFlip:
            theseKeys = key_next.getKeys(keyList=['space'], waitRelease=False)
            _key_next_allKeys.extend(theseKeys)
            if len(_key_next_allKeys):
                key_next.keys = _key_next_allKeys[-1].name  # just the last key pressed
                key_next.rt = _key_next_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in estimationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "estimation" ---
    for thisComponent in estimationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('scale.response', scale.getRating())
    trials.addData('scale.rt', scale.getRT())
    # check responses
    if key_next.keys in ['', [], None]:  # No response was made
        key_next.keys = None
    trials.addData('key_next.keys',key_next.keys)
    if key_next.keys != None:  # we had a response
        trials.addData('key_next.rt', key_next.rt)
    # the Routine "estimation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "rest" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sound_2.setSound('sound/trueding.wav', secs=1.0, hamming=True)
    sound_2.setVolume(1.0, log=False)
    # keep track of which components have finished
    restComponents = [textrest, textready, sound_2]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rest" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textrest* updates
        if textrest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textrest.frameNStart = frameN  # exact frame index
            textrest.tStart = t  # local t and not account for scr refresh
            textrest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textrest, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textrest.started')
            textrest.setAutoDraw(True)
        if textrest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textrest.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                textrest.tStop = t  # not accounting for scr refresh
                textrest.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textrest.stopped')
                textrest.setAutoDraw(False)
        
        # *textready* updates
        if textready.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            textready.frameNStart = frameN  # exact frame index
            textready.tStart = t  # local t and not account for scr refresh
            textready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textready, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textready.started')
            textready.setAutoDraw(True)
        if textready.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textready.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                textready.tStop = t  # not accounting for scr refresh
                textready.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textready.stopped')
                textready.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_2.started', tThisFlipGlobal)
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_2.stopped')
                sound_2.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest" ---
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-20.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keyEnd.keys = []
keyEnd.rt = []
_keyEnd_allKeys = []
# keep track of which components have finished
EndComponents = [textEndMessage, keyEnd]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
while continueRoutine and routineTimer.getTime() < 30.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndMessage* updates
    if textEndMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEndMessage.frameNStart = frameN  # exact frame index
        textEndMessage.tStart = t  # local t and not account for scr refresh
        textEndMessage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEndMessage, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textEndMessage.started')
        textEndMessage.setAutoDraw(True)
    if textEndMessage.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEndMessage.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            textEndMessage.tStop = t  # not accounting for scr refresh
            textEndMessage.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textEndMessage.stopped')
            textEndMessage.setAutoDraw(False)
    
    # *keyEnd* updates
    waitOnFlip = False
    if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEnd.frameNStart = frameN  # exact frame index
        keyEnd.tStart = t  # local t and not account for scr refresh
        keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyEnd.started')
        keyEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEnd.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > keyEnd.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            keyEnd.tStop = t  # not accounting for scr refresh
            keyEnd.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyEnd.stopped')
            keyEnd.status = FINISHED
    if keyEnd.status == STARTED and not waitOnFlip:
        theseKeys = keyEnd.getKeys(keyList=['space'], waitRelease=False)
        _keyEnd_allKeys.extend(theseKeys)
        if len(_keyEnd_allKeys):
            keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
            keyEnd.rt = _keyEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyEnd.keys in ['', [], None]:  # No response was made
    keyEnd.keys = None
thisExp.addData('keyEnd.keys',keyEnd.keys)
if keyEnd.keys != None:  # we had a response
    thisExp.addData('keyEnd.rt', keyEnd.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-30.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
