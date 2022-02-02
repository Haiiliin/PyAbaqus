from abaqusConstants import *


class MohrCoulombHardening:
    """The MohrCoulombHardening object specifies hardening for the Mohr-Coulomb plasticity
    model. 

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].mohrCoulombPlasticity.mohrCoulombHardening
        - import odbMaterial
        - session.odbs[name].materials[name].mohrCoulombPlasticity.mohrCoulombHardening

    Table Data
    ----------
        - Cohesion yield stress.
        - The absolute value of the corresponding Plastic strain.(The first tabular value entered must always be zero.)
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - MOHR COULOMB HARDENING

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a MohrCoulombHardening object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].mohrCoulombPlasticity\
            - .MohrCoulombHardening
            - session.odbs[name].materials[name].mohrCoulombPlasticity\
            - .MohrCoulombHardening
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A MohrCoulombHardening object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the MohrCoulombHardening object.

        Raises
        ------
            RangeError. 
        """
        pass
