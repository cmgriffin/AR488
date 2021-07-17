from time import sleep
import pyvisa
from pyvisa.constants import BufferOperation

rm = pyvisa.ResourceManager()


class Ar488:
    """
    Ar488(address)

    Creats an instance of a low level driver for the Open Source AR488 USB
    to GPIB adapter. This driver should also be mostly compatible with the
    Prologix USB to GPIB. This class is intended to be initialized
    automatically when an instance of Ar488Inst is created.
    """

    READ_TERMINATION = "\r\n"
    WRITE_TERMINATION = "\r\n"
    BAUD_RATE = 115200
    instance = None

    def __init__(self, address, **kwargs):
        """
        Creats an instance of a low level driver for the Open Source AR488 USB
        to GPIB adapter. This driver should also be mostly compatible with the
        Prologix USB to GPIB. This class is intended to be initialized
        automatically when an instrument address with a specific prefix is opened.

        Args:
            address (str): VISA style ASRL address
        """
        self.address = address
        self.instrument = rm.open_resource(address)
        # sleep(2)  # time for the arduino bootloader to timeout
        self.instrument.read_termination = self.READ_TERMINATION
        self.instrument.write_termination = self.WRITE_TERMINATION
        self.instrument.baud_rate = self.BAUD_RATE
        self.timeout = kwargs.get("timeout", 5000)
        self.mode = 1  # configure as the bus controller
        self.auto = 0  # configure for manual reads
        type(self).instance = self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(address='{self.address}')"

    def query(self, msg, cast_func=None, delay=0.0):
        self.instrument.flush(BufferOperation.discard_receive_buffer)
        self.instrument.write(msg)
        sleep(delay)
        if cast_func is None:
            return self.instrument.read_raw()
        else:
            return cast_func(self.instrument.read())

    @property
    def timeout(self):
        """
        Specifies the timeout for the pyvisa serial instrument and also the
        AR488
        """
        return self.instrument.timeout

    @timeout.setter
    def timeout(self, timeout):
        if not (0 <= int(timeout) <= 32000):
            raise ValueError("timeout must be 0 - 32000")
        self.read_tmo_ms = timeout
        self.instrument.timeout = timeout

    def close(self):
        self.instrument.close()
        type(self).instance = None

    @property
    def version(self):
        return self.query("++ver", str)

    @property
    def target_addr(self):
        """
        This is used to set or query the GPIB address. At present, only
        primary addresses are supported. In controller mode, the address
        refers to the GPIB address of the instrument that the operator
        desires to communicate with. The address of the controller is 0.
        In device mode, the address represents the address of the interface
        which is now acting as a device.
        ++addr [1-29]
        where 1-29 is a decimal number representing the primary GPIB address of
        the device.
        """
        return self.query("++addr", int)

    @target_addr.setter
    def target_addr(self, target_addr):
        if int(target_addr) not in range(1, 29 + 1):
            raise ValueError("target_addr must be 1-29")
        return self.instrument.write(f"++addr {target_addr}")

    @property
    def mode(self):
        """
        This command configures the AR488 to serve as a controller or a device.
        In controller mode the AR488 acts as the Controller-in-Charge (CIC) on
        the GPIB bus, receiving commands terminated with CRLF over USB and
        sending them to the currently addressed instrument via the GPIB bus.
        The controller then passes the received data back over USB to the host.
        In device mode, the AR488 can act as another device on the GPIB bus.
        Modes: controller, device
        valid settings: 0=device, 1=controller
        """
        return self.query("++mode", int)

    @mode.setter
    def mode(self, mode: int):
        if int(mode) not in (0, 1):
            raise ValueError("mode must be either 0 or 1")
        return self.instrument.write(f"++mode {mode}")

    @property
    def auto(self):
        """
        Configure the instrument to automatically send data back to the
        controller. When auto is enabled, the user does not have to issue
        ++read commands repeatedly. This command has additional options
        when compared with the Prologix version. When set to zero, auto is
        disabled. When set to 1, auto is designed to emulate the Prologix
        setting.
        It is not advisable to enable auto when using this driver since
        serial data is only expected to follow an explicit read command.
        ++auto [0|1|2|3]
        where 0 disables and 1 enables automatically sending data to the
        controller
        """
        return self.query("++auto", int)

    @auto.setter
    def auto(self, auto):
        if int(auto) not in range(0, 3 + 1):
            raise ValueError("auto must be 0 - 3")
        return self.instrument.write(f"++auto {auto}")

    @property
    def eoi(self):
        """
        Enables or disables the assertion of the EOI signal. When a
        data message is sent in binary format, the CR/LF terminators cannot be
        differentiated from the binary data bytes. In this circumstance, the
        EOI signal can be used as a message terminator. When ATN is not
        asserted and EOI is enabled, the EOI signal will be briefly asserted to
        indicate the last character sent in a multibyte sequence. Some
        instruments require their command strings to be terminated with an EOI
        signal in order to properly detect the command.
        ++eoi [0|1]
        where 0 disables and 1 enables asserting EOI to signal the last
        character sent
        """
        return self.query("++eoi", int)

    @eoi.setter
    def eoi(self, eoi):
        if int(eoi) not in (0, 1):
            raise ValueError("eoi must be either 0 or 1")
        return self.instrument.write(f"++eoi {eoi}")

    @property
    def eos(self):
        """
        Specifies the GPIB termination character. When data from the host (e.g.
        a command sequence) is received over USB, all non-escaped LF, CR or Esc
        characters are removed and replaced by the GPIB termination character,
        which is appended to the data sent to the instrument. This command does
        not affect data being received from the instrument.
        0=CR+LF, 1=CR, 2=LF, 3=none
        """
        return self.query("++eos", int)

    @eos.setter
    def eos(self, eos):
        if int(eos) not in range(0, 3 + 1):
            raise ValueError("eos must be 0 - 3")
        return self.instrument.write(f"++eos {eos}")

    @property
    def eot_enable(self):
        """
        This command enables or disables the appending of a user specified
        character to the USB output from the interface to the host whenever EOI
        is detected while reading data from the GPIB port. The character to
        send is specified using the ++eot_char command.
        ++eot_enable [0|1]
        where 0 disables and 1 enables sending the EOT character to the USB
        output
        """
        return self.query("++eot_enable", int)

    @eot_enable.setter
    def eot_enable(self, eot_enable):
        if int(eot_enable) not in (0, 1):
            raise ValueError("eot_enable must be either 0 or 1")
        return self.instrument.write(f"++eot_enable {eot_enable}")

    @property
    def eot_char(self):
        """
        This command specifies the character to be appended to the USB output
        from the interface to the host whenever an EOI signal is detected while
        reading data from the GPIB bus. The character is a decimal ASCII
        character value that is less than 256.
        ++eot_char [<char>]
        where <char> is a decimal number that is less than 256.
        """
        return self.query("++eot_char", int)

    @eot_char.setter
    def eot_char(self, eot_char):
        if int(eot_char) not in range(0, 256):
            raise ValueError("eot_char must be 0 - 255")
        return self.instrument.write(f"++eot_char {eot_char}")

    @property
    def lon(self):
        """
        The ++lon command configures the controller to listen only to traffic
        on the GPIB bus. In this mode the interface does require to have a GPIB
        address assigned so the assigned GPIB address is ignored. Traffic is
        received irrespective of the currently set GPIB address. The interface
        can receive but not send, so effectively becomes a “listen-only”
        device. When issued without a parameter, the command returns the
        current state of “lon” mode.
        ++lon [0 |1]
        where 0=disabled; 1=enabled
        """
        return self.query("++lon", int)

    @lon.setter
    def lon(self, lon):
        if int(lon) not in (0, 1):
            raise ValueError("lon must be either 0 or 1")
        return self.instrument.write(f"++lon {lon}")

    @property
    def read_tmo_ms(self):
        """
        This specifies the timeout value, in milliseconds, that is used by the
        ++read (and ++spoll) commands to wait for a character to be transmitted
        while reading data from the GPIB bus. The timeout value may be set
        between 0 and 32,000 milliseconds (32 seconds).
        ++read_tmo_ms <time>
        where <time> is a decimal number between 0 and 32000 representing
        milliseconds
        """
        return self.query("++read_tmo_ms", int)

    @read_tmo_ms.setter
    def read_tmo_ms(self, read_tmo_ms):
        if not (0 <= int(read_tmo_ms) <= 32000):
            raise ValueError("read_tmo_ms must be 0 - 32000")
        return self.instrument.write(f"++read_tmo_ms {read_tmo_ms}")

    @property
    def sqr(self):
        """
        This command returns the present status of the SRQ signal line. It
        returns 0 if SRQ is not asserted and 1 if SRQ is asserted.
        """
        return self.query("++sqr", int)

    def send_clr(self):
        """
        This command sends a Selected Device Clear (SDC) to the currently
        addressed instrument. Details of how the instrument should respond may
        be found in the instrument manual.
        """
        self.instrument.write("++clr")

    def send_ifc(self):
        """
        Assert the GPIB IFC signal for 150 microseconds, making the AR488 the
        Controller-in-Charge on the GPIB bus.
        """
        self.instrument.write("++ifc")

    def send_llo(self, all=False):
        """
        Local Lock Out
        Disable front panel operation on the currently addressed instrument.
        In the original HPIB specification, sending the LLO signal to the GPIB
        bus would lock the LOCAL control on ALL instruments on the bus. In the
        Prologix specification, this command disables front panel operation
        of the addressed instrument only, in effect taking control of that
        instrument. The AR488 follows the Prologix specification, but adds a
        parameter to allow the simultaneous assertion of remote control over
        all instruments on the GPIB bus as per the HPIB specification.

        This command requires the Remote Enable (REN) line to be asserted
        otherwise it will be ignored. In controller mode, the REN signal is
        asserted by default unless its status is changed by the ++ren command.

        When the ++llo command is issued without a parameter, it behaves the
        same as it does on the Prologix controller. The LLO signal is sent to
        the currently addressed instrument and this locks out the LOCAL key on
        the instrument control panel. Because the instrument has been addressed
        and REN is already asserted, the command automatically takes remote
        control of the instrument. Most instruments will display REM on their
        display or control panel to indicate that remote control is active and
        front/rear panel controls will be disabled.

        If the ++llo command is issued with the ‘all’ parameter, this will send
        the LLO signal to the bus, putting every instrument into remote control
        mode simultaneously. At this point, instruments will not yet show the
        REM indicator and it may still be possible to operate the front panel
        controls. On some instruments the LOCAL key may be locked out. However,
        as soon as an instrument has been addressed and sent a command
        (assuming that a LOC signal has not been sent yet first), the
        controller will automatically lock in remote control of that
        instrument, the REM indicator will be displayed and front/rear panel
        controls will be disabled.
        ++llo [all]
        """
        arg = " all" if all else ""
        self.instrument.write(f"++llo{arg}")

    def send_loc(self, all=False):
        """
        Relinquish remote control and re-enable front panel operation of the
        currently addressed instrument. This command relinquishes remote
        control of the instrument by de-asserting REN and sending the GTL
        signal. The Remote Enable (REN) line must be asserted and the
        instrument must already be under remote control otherwise the command
        has no effect. In the original HPIB specification, this command would
        place all instuments back into local mode, re-enabling the LOCAL key
        and panel controls on ALL instruments currently connected to the GPIB
        bus. In the Prologix specification, this command relinquishes remote
        control of the currently addressed instrument only. The AR488 follows
        the Prologix specification, but adds a parameter to allow the
        simultaneous release of remote control over all instruments currently
        addressed as listeners on the GPIB bus as per the HPIB specification.
        If the command is issued without a parameter, it will re-enable the
        LOCAL key on the control panel on the currently addressed instrument
        and relinquish remote control of the instrument. If issued with the
        ‘all’ parameter, it puts all devices on the GPIB bus in local control
        state. The REM indicator should no longer be visible when the
        instrument has returned to local control state.
        ++loc [all]
        """
        arg = " all" if all else ""
        self.instrument.write(f"++loc{arg}")

    def send_trg(self, *target_addrs):
        """
        Sends a Group Execute Trigger to selected devices. Up to 15 addresses
        may be specified and must be separated by spaces. If no address is
        specified, then the command is sent to the currently addressed
        instrument. The instrument needs to be set to single trigger mode and
        remotely controlled by the GPIB controller. Using ++trg, the instrument
        can be manually triggered and the result read with ++read.
        Args:
            *target_addrs (int): Addr(s) to be triggered
        """
        addr_str = " ".join(addr for addr in target_addrs)
        if len(addr_str) > 0:
            addr_str = " " + addr_str
        self.instrument.write(f"++trg{addr_str}")

    def rst(self):
        """
        Performs reset of the controller
        """
        self.instrument.write("++rst")

    def savecfg(self):
        """
        This command saves the current interface configuration.
        """
        self.instrument.write("++savecfg")

    def write(self, cmd_str):
        """
        Writes the specified string onto the GPIB bus

        Args:
            cmd_str (str): string to be written to bus
        """
        self.instrument.write(cmd_str)

    def read(self):
        """
        This command can be used to read data from the currently addressed instrument. Data is read
        until:
        - the EOI signal is detected
        - a specified character is read
        - timeout expires
        Timeout is set using the read_tmo_ms command and is the maximum permitted delay for a single
        character to be read. It is not related to the time taken to read all of the data. For details see the
        description of the read_tmo_ms command.

        Returns:
            str: [description]
        """

        return self.query("++read")


class Ar488Inst:
    """
    Ar488Inst(_, address)

    Not intended to be initialized directly, instead use pyvisa.ResourceManager

    >> import ar488py
    >> inst = rm.open_resource(
            "+PROLOGIX::ASRL8+GPIB::23", resource_pyclass=ar488py.Ar488Inst)

    Creates an instance similar to the pyvisa resource to allow for
    communication with a GPIB instrument via the AR488/Prologix USB to
    GPIB adapter. This will create the resource instance but also connect
    and initialize with the AR488/Prologix adapter if necessary.

    There are some aspects still pretty hacky to get this class to work with
    pyvisa.ResourceManager.open_resource.
    """

    def __init__(self, _, address):
        """
        Creates an instance similar to the pyvisa resource to allow for
        communication with a GPIB instrument via the AR488/Prologix USB to
        GPIB adapter. This will create the resource instance but also connect
        and initialize with the AR488/Prologix adapter if necessary.

        Args:
            address (str): A resource name string similar to standard VISA
                naming. One difference here is the string must contain both
                the GPIB instrument address and also the AR488/Prologix COM
                port info. The format used is from pyvisa issue #112.
                +<NAME OF THE ADAPTER>::<REAL RESOURCE NAME>+<FAKE RESOURCE NAME>
                Examples:
                +PROLOGIX::ASRL1+GPIB::2
                +AR488::ASRL1+GPIB::2
        """
        addr_split = address.split("+")
        self._ar488_port = addr_split[1].split("::")[1]
        inst_gpib_addr = int(addr_split[2].split("::")[1])
        self.interface = None
        self._address = inst_gpib_addr

    def open(self, *args, **kwargs):
        """
        An open method for pyvisa.ResourceManager
        Initilizes the Ar488 if necessary then gets the instance.
        """
        if Ar488.instance is None:  # need to initialize the adapter
            Ar488(self._ar488_port)
        self.interface = Ar488.instance

    def close(self):
        """
        Close out the serial port for the adapter
        """
        self.interface.close()

    @property
    def address(self):
        return f"GPIB::{self._address}"

    def write(self, cmd_str):
        self.interface.target_addr = self._address
        self.interface.write(cmd_str)

    def read(self):
        self.interface.target_addr = self._address
        return self.interface.read().decode()

    def read_raw(self):
        self.interface.target_addr = self._address
        return self.interface.read()

    def query(self, message: str, delay: float = None):
        self.write(message)
        delay(0 if delay is None else delay)
        return self.read()

    def trigger(self, *trigger_addresses):
        self.interface.send_trg(*trigger_addresses)
