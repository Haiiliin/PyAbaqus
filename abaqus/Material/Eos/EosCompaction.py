class EosCompaction:
    """The EosCompaction object specifies material eos compaction.

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].eos.eosCompaction
        - import odbMaterial
        - session.odbs[name].materials[name].eos.eosCompaction

    Corresponding analysis keywords
    -------------------------------
        - EOS COMPACTION

    """

    def __init__(self, soundSpeed: float, porosity: float, pressure: float, compactionPressure: float):
        """This method creates an EosCompaction object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].eos.EosCompaction
            - session.odbs[name].materials[name].eos.EosCompaction
        soundSpeed
            A Float specifying reference sound speed in the porous material. 
        porosity
            A Float specifying value of the porosity of the unloaded material. 
        pressure
            A Float specifying pressure required to initialize Plastic behavior.
        compactionPressure
            A Float specifying compaction pressure at which all pores are crushed. 

        Returns
        -------
            An EosCompaction object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the EosCompaction object.

        Raises
        ------
            RangeError. 
        """
        pass
