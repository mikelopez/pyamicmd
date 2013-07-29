from pyamicmd import *
# import the settings locally
import settings

i, e, w = "INFO", "ERROR", "WARNING"

class AMICommand(AMIWrapper):
    """ Base class wrapper file for call originating with starpy """
    user = getattr(settings, "AMI_USER")
    pwd = getattr(settings, "AMI_PASS")
    host = getattr(settings, "PBX")
    command_txt = ""
    response = ""

    def __init__(self, **kwargs):
        # overwrite defaults frm any kwargs
        super(AMICommand, self).__init__(self, **kwargs)
        for k, v in kwargs.items():
            if k in self.allowed_keys:
                setattr(self, k, v) 

    def get_command(self):
        """ Get the command to send to AMI (if any) """
        return getattr(self, "command_txt", None)

    def set_command(self, value):
        """ Set the command text to send over AMI """
        setattr(self, "command_txt", value)

    # action methods
    def __command(self, cmd_override=None):
        """ Send a command to Asterisk, or fail """
        if cmd_override:
            self.set_command(cmd_override)
        if not self.get_command():
            self.__exception(e, "No command to send. set class.command = 'command to send'")

        def on_connect(ami):
            # on connect callback
            df = ami.command(self.get_command())

            def on_result(result):
                # do something with the result and exit
                self.response = result
                return ami.logoff()
            def on_error(error):
                # callback when any errors occur
                self.response = error
                self.__exception(error.getTraceback())
            def on_complete(result):
                # when completed, just stop the reactor cause were done
                self.__stop_reactor()

            termprint(w, self.get_command())                
            df.addCallbacks(on_result, on_error)
            df.addCallbacks(on_complete, on_complete)

        def on_error(ami):
            # if any errors with intial login, we call __exception
            self.__exception(ami)

        df = self.__set_session().login(self.host, 5038).addCallbacks(on_connect, on_error)
        if not self.session:
            self.__exception("Failed to set the session")
        if not df:
            self.__exception(df)

    def command(self):
        # start the reactor 
        self.__run_reactor(self.__command)

        



if __name__ == '__main__':
    #manager.log.setLevel(logging.DEBUG)

    # send a command
    cl = AMIWrapper(command="dialplan show from-internal")
    reactor.callWhenRunning(cl.command)
    reactor.run()


