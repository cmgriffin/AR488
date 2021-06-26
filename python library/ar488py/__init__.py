"""
A python module to add support for the AR488 and Prologix USB to GPIB adapter 
to pyvisa.

The current structure functions in the following way:
- ASRL of the AR488 is opened with pyvisa and set as handle in the Ar488 class
    * The Ar488 is the interface level class that implements all the commands 
      for communicating with the adapter via serial.
- The resource level class is Ar488Instr
    * This class handles a single GPIB instrument within the scope of the Ar488
    * Methods similar to other pyvisa.resource classes are implemented

>> rm = pyvisa.ResourceManager()
>> inst = rm.open_resource(
    "+PROLOGIX::ASRL8+GPIB::23", resource_pyclass=Ar488Inst
    )
"""


from ._core import Ar488, Ar488Inst

__all__ = ("Ar488", "Ar488Inst")
