from abaqusConstants import *


class PlanarTestData:
    """The PlanarTestData object specifies planar test (or pure shear) data (compression and/or
    tension). 

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import material
            mdb.models[name].materials[name].hyperelastic.planarTestData
            mdb.models[name].materials[name].hyperfoam.planarTestData
            mdb.models[name].materials[name].mullinsEffect.planarTests[i]
            import odbMaterial
            session.odbs[name].materials[name].hyperelastic.planarTestData
            session.odbs[name].materials[name].hyperfoam.planarTestData
            session.odbs[name].materials[name].mullinsEffect.planarTests[i]

        The table data for this object are:
        For a hyperelastic material model, the table data specify the following:
            - Nominal stress, TS.
            - Nominal strain in the direction of loading, ϵS.
        For a hyperfoam material model, the table data specify the following:
            - Nominal stress, TL.
            - Nominal strain in the direction of loading, ϵp.
            - Nominal transverse strain, ϵ3. The default value is 0.

    The corresponding analysis keywords are:
        - PLANAR TEST DATA

    """

    def __init__(self, table: tuple, smoothing: int = None, lateralNominalStrain: Boolean = OFF,
                 temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a PlanarTestData object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].hyperelastic.PlanarTestData
                mdb.models[name].materials[name].hyperfoam.PlanarTestData
                mdb.models[name].materials[name].mullinsEffect.PlanarTestData
                session.odbs[name].materials[name].hyperelastic.PlanarTestData
                session.odbs[name].materials[name].hyperfoam.PlanarTestData
                session.odbs[name].materials[name].mullinsEffect.PlanarTestData
        
        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        smoothing
            None or an Int specifying the value for smoothing. If *smoothing*=None, no smoothing is 
            employed. The default value is None. 
        lateralNominalStrain
            A Boolean specifying whether to include lateral nominal strain. The default value is 
            OFF. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A PlanarTestData object.
        """
        pass

    def setValues(self):
        """This method modifies the PlanarTestData object.
        """
        pass
