from .PredefinedField import PredefinedField
from ..Region.Region import Region


class FluidCavityPressure(PredefinedField):
    """The FluidCavityPressure object stores the data for initial fluid cavity pressures. The
    base class*region* argument can not be specifed with this object. 
    The FluidCavityPressure object is derived from the PredefinedField object. 

    Attributes
    ----------
    region: Region
        A Region object on which the **fluidCavity** interaction is specified.

    Notes
    -----
        This object can be accessed by:
        - import load
        - mdb.models[name].predefinedFields[name]

    Corresponding analysis keywords
    -------------------------------
        - INITIAL CONDITIONS

    """

    # A Region object on which the *fluidCavity* interaction is specified. 
    region: Region = Region()

    def __init__(self, name: str, fluidCavity: str, fluidPressure: float):
        """This method creates a FluidCavityPressure object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].FluidCavityPressure

        Parameters
        ----------
        name
            A String specifying the repository key. 
        fluidCavity
            A String specifying the name of a Fluid Cavity Interaction. 
        fluidPressure
            A Float specifying the initial fluid pressure. 

        Returns
        -------
            A FluidCavityPressure object. . 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the FluidCavityPressure object.

        Parameters
        ----------
        """
        pass
