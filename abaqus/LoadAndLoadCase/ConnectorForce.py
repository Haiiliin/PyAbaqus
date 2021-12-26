import typing

from abaqusConstants import *
from .Load import Load
from ..Region.Region import Region


class ConnectorForce(Load):

    """The ConnectorForce object defines a connector force. 
    The ConnectorForce object is derived from the Load object. 

    Access
    ------
        - import load
        - mdb.models[name].loads[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the load repository key. 
    name: str = ''

    # A String specifying the name of the assembled fastener to which the load will be 
    # applied. This argument is not valid when *region* is specified. When this argument is 
    # specified, *fastenerSetName* must also be specified. The default value is an empty 
    # string. 
    fastenerName: str = ''

    # A String specifying the assembled fastener template model set to which the load will be 
    # applied. This argument is not valid when *region* is specified. When this argument is 
    # specified, *fastenerName* must also be specified. The default value is an empty string. 
    fastenerSetName: str = ''

    # A Region object specifying the region to which the load is applied. 
    region: Region = Region()

    def __init__(self, name: str, createStepName: str, region: str = '', fastenerName: str = '', 
                 fastenerSetName: str = '', f1: float = None, f2: float = None, f3: float = None, 
                 amplitude: str = UNSET):
        """This method creates a ConnectorForce object on a wire region. Alternatively, the load
        may also be applied to a wire set referenced from an assembled fastener template model.

        Path
        ----
            - mdb.models[name].ConnectorForce

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            The wire region to which the load is applied. This argument is not valid when 
            *fastenerName* and *fastenerSetName* are specified. 
        fastenerName
            A String specifying the name of the assembled fastener to which the load will be 
            applied. This argument is not valid when *region* is specified. When this argument is 
            specified, *fastenerSetName* must also be specified. The default value is an empty 
            string. 
        fastenerSetName
            A String specifying the assembled fastener template model set to which the load will be 
            applied. This argument is not valid when *region* is specified. When this argument is 
            specified, *fastenerName* must also be specified. The default value is an empty string. 
        f1
            A Float or a Complex specifying the connector force component in the connector's local 
            1-direction.Note:Although *f1*, *f2*, and *f3* are optional arguments, at least one of 
            them must be nonzero. 
        f2
            A Float or a Complex specifying the connector force component in the connector's local 
            2-direction. 
        f3
            A Float or a Complex specifying the connector force component in the connector's local 
            3-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A ConnectorForce object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, region: str = '', fastenerName: str = '', fastenerSetName: str = '', f1: float = None, 
                  f2: float = None, f3: float = None, amplitude: str = UNSET):
        """This method modifies the data for an existing ConnectorForce object in the step where it
        is created.

        Parameters
        ----------
        region
            The wire region to which the load is applied. This argument is not valid when 
            *fastenerName* and *fastenerSetName* are specified. 
        fastenerName
            A String specifying the name of the assembled fastener to which the load will be 
            applied. This argument is not valid when *region* is specified. When this argument is 
            specified, *fastenerSetName* must also be specified. The default value is an empty 
            string. 
        fastenerSetName
            A String specifying the assembled fastener template model set to which the load will be 
            applied. This argument is not valid when *region* is specified. When this argument is 
            specified, *fastenerName* must also be specified. The default value is an empty string. 
        f1
            A Float or a Complex specifying the connector force component in the connector's local 
            1-direction.Note:Although *f1*, *f2*, and *f3* are optional arguments, at least one of 
            them must be nonzero. 
        f2
            A Float or a Complex specifying the connector force component in the connector's local 
            2-direction. 
        f3
            A Float or a Complex specifying the connector force component in the connector's local 
            3-direction. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValuesInStep(self, stepName: str, 
                        f1: typing.Union[SymbolicConstant,float] = typing.Union[SymbolicConstant,float](), 
                        f2: typing.Union[SymbolicConstant,float] = typing.Union[SymbolicConstant,float](), 
                        f3: typing.Union[SymbolicConstant,float] = typing.Union[SymbolicConstant,float](), 
                        amplitude: str = ''):
        """This method modifies the propagating data for an existing ConnectorForce object in the
        specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the load is modified. 
        f1
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the connector force 
            component in the connector's local 1-direction. UNCHANGED should be used if the 
            connector force component is propagated from the previous analysis step. 
        f2
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the connector force 
            component in the connector's local 2-direction. UNCHANGED should be used if the 
            connector force component is propagated from the previous analysis step. 
        f3
            A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the connector force 
            component in the connector's local 3-direction. UNCHANGED should be used if the 
            connector force component is propagated from the previous analysis step. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous analysis step. FREED should be used if the 
            load is changed to have no amplitude reference. You should provide the *amplitude* 
            argument only if it is valid for the specified step. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

