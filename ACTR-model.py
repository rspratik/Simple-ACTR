#################### Parallel/Distributed Artificial Brain Model ###################

# this brain model has in total four production systems : vision, audio, smell, touch.
# this brain model performs sensing, thinking, acting.
# this brain model performs every activity in parallel.

# 
import ccm      
log=ccm.log(html=True)   

from ccm.lib.actr import *  

# Environment
class Controller(ccm.Model):  # items in the environment look and act like chunks - but note the syntactic differences
    vision_system = ccm.Model(name='vision', state='resting')
    audio_system = ccm.Model(name='audio', state='resting')
    smell_system = ccm.Model(name='smell', state='resting')
    touch_system = ccm.Model(name='touch', state='resting')


# transduction problem
class Sensing_Unit(ccm.Model):  # create a motor module do the actions
    def sense_from_vision(self):
        print "sense the vision stimulus"
        self.parent.parent.vision_system.state = 'sensing'  # self=sensing_unit, parent=ArtificialBrain, parent of parent=Controller

    def sense_from_audio(self):
        print "sense the audio stimulus"
        self.parent.parent.audio_system.state = 'sensing'

    def sense_from_smell(self):
        print "sense the smell stimulus"
        self.parent.parent.smell_system.state = 'sensing'

    def sense_from_touch(self):
        print "sense the touch stimulus"
        self.parent.parent.touch_system.state = 'sensing'

class Thinking_Unit(ccm.Model):  # create a motor module do the actions
    def thinking_for_vision(self):
        print "Think/Analyze the vision stimulus"
        self.parent.parent.vision_system.state = 'thinking'   

    def thinking_for_audio(self):
        print "Think/Analyze the audio stimulus"
        self.parent.parent.audio_system.state = 'thinking'

    def thinking_for_smell(self):
        print "Think/Analyze the smell stimulus"
        self.parent.parent.smell_system.state = 'thinking'

    def thinking_for_touch(self):
        print "Think/Analyze the touch stimulus"
        self.parent.parent.touch_system.state = 'thinking'

class Action_Unit(ccm.Model):  # create a motor module do the actions
    def acting_for_vision(self):
        print "Act on the vision stimulus"
        self.parent.parent.vision_system.state = 'acting'   

    def acting_for_audio(self):
        print "Act on the audio stimulus"
        self.parent.parent.audio_system.state = 'acting'

    def acting_for_smell(self):
        print "Act on the smell stimulus"
        self.parent.parent.smell_system.state = 'acting'

    def acting_for_touch(self):
        print "Act on the touch stimulus"
        self.parent.parent.touch_system.state = 'acting'


# create an act-r agent
# Agent
class ArtificialBrain(ACTR):
    visualbuffer = Buffer()
    visualbuffer.set('name:vision')

    audiobuffer = Buffer()
    audiobuffer.set('name:audio')

    smellbuffer = Buffer()
    smellbuffer.set('name:smell')

    touchbuffer = Buffer()
    touchbuffer.set('name:touch')

    sensing = Sensing_Unit()  # add sensing unit to agent
    thinking = Thinking_Unit()   # add thinking unit to agent
    action = Action_Unit()   # add acting unit to agent

    production_time = 0.05  # production parameter settings
    production_sd = 0.01
    production_threshold = -20

    # All methods are productions
    def eyes_s1(visualbuffer='name:vision', vision_system='state:resting'):
        print "1.1 sensing from eyes #"
        sensing.sense_from_vision()     # direct the sensing module
    def eyes_s2(visualbuffer='name:vision', vision_system='state:sensing'):
        print "1.2 analyzing from eyes #"
        thinking.thinking_for_vision()
    def eyes_s3(visualbuffer='name:vision', vision_system='state:thinking'):
        print "1.3 act over your eyes #"
        action.acting_for_vision()
    def eyes_s4(visualbuffer='name:vision', vision_system='state:acting'):
        print "1.1 sensing from eyes #"
        sensing.sense_from_vision()


    def ears_s1(audiobuffer='name:audio', audio_system='state:resting'):
        print "2.1 sense from ears #"
        sensing.sense_from_audio()     # direct the sensing module
    def ears_s2(audiobuffer='name:audio', audio_system='state:sensing'):
        print "2.2 analyze from ears #"
        thinking.thinking_for_audio()
    def ears_s3(audiobuffer='name:audio', audio_system='state:thinking'):
        print "2.3 act over your ears #"
        action.acting_for_audio()
    def ears_s4(audiobuffer='name:audio', audio_system='state:acting'):
        print "2.1 sense from ears #"
        sensing.sense_from_audio()  # direct the sensing module

    def nose_s1(smellbuffer='name:smell', smell_system='state:resting'):
        print "3.1 sense from nose #"
        sensing.sense_from_smell()
    def nose_s2(smellbuffer='name:smell', smell_system='state:sensing'):
        print "3.2 analyze from nose #"
        thinking.thinking_for_smell()
    def nose_s3(smellbuffer='name:smell', smell_system='state:thinking'):
        print "3.3 act over your nose #"
        action.acting_for_smell()
    def nose_s4(smellbuffer='name:smell', smell_system='state:acting'):
        print "3.1 sense from nose #"
        sensing.sense_from_smell()


    def skin_s1(touchbuffer='name:touch', touch_system='state:resting'):
        print "4.1 sense from skin #"
        sensing.sense_from_touch()
    def skin_s2(touchbuffer='name:touch', touch_system='state:sensing'):
        print "4.2 analyze from skin #"
        thinking.thinking_for_touch()
    def skin_s3(touchbuffer='name:touch', touch_system='state:thinking'):
        print "4.3 act over your skin #"
        action.acting_for_touch()
    def skin_s4(touchbuffer='name:touch', touch_system='state:acting'):
        print "4.1 sense from skin #"
        sensing.sense_from_touch()


    def stop_production(touchbuffer='name:none'):
        print "Brain is hibernated"
        self.stop()  # stop the agent


brain_object = ArtificialBrain()  # name the agent
controller = Controller()  # name the environment
controller.agent = brain_object  # put the agent in the environment
ccm.log_everything(controller)  # print out what happens in the environment
controller.run(5)  # run the environment
ccm.finished()  # stop the environment
