from abaqusConstants import *


class MeanFieldVoid:
    """The MeanFieldVoid object specifies the void inclusion property.

    Notes
    -----
        This object can be accessed by:
        - import material
        - mdb.models[name].materials[name].constituents[name]
        - import odbMaterial
        - session.odbs[name].materials[name].constituents[name]

    Table Data
    ----------
        The table data specify the following:
        - Volume fraction.
        - Aspect ratio.
        - Components of the direction vector defined in the local coordinate system when *direction*=FIXED. Components of the second-order orientation tensor in the local coordinate system when *direction*=ORIENTATION_TENSOR.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CONSTITUENT

    """

    def __init__(self, name: str, table: tuple, material: str = '', isotropizationCoefficient: float = None,
                 volumeFractionType: SymbolicConstant = UNIFORM, volumeFractionFieldName: str = '',
                 aspectRatioType: SymbolicConstant = UNIFORM, aspectRatioFieldName: str = '',
                 orientationTensorType: SymbolicConstant = UNIFORM, orientationTensorFieldName: str = '',
                 shape: SymbolicConstant = SPHERE, direction: SymbolicConstant = None,
                 strainConcentrationTensor: tuple = (),
                 temperatureGradientConcentrationTensor: tuple = ()):
        """This method creates a MeanFieldVoid object.

        Notes
        -----
            This function can be accessed by:
            - mdb.models[name].materials[name].meanFieldHomogenization.MeanFieldVoid
            - session.odbs[name].materials[name].meanFieldHomogenization.MeanFieldVoid
        name
            A String specifying the constituent repository key. 
        table
            A sequence of sequences of Floats specifying the items described below. 
        material
            A String specifying the name of the material. 
        isotropizationCoefficient
            A Float specifying the factor used for scaling the Plastic strain of the constituent
            when calculating the isotropic part of the tangent. 
        volumeFractionType
            A SymbolicConstant specifying the type of volume fraction. Possible values are UNIFORM, 
            ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM. 
        volumeFractionFieldName
            A String specifying the name of the AnalyticalField object or DiscreteField object. 
        aspectRatioType
            A SymbolicConstant specifying the type of aspect ratio. Possible values are UNIFORM, 
            ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM. 
        aspectRatioFieldName
            A String specifying the name of the AnalyticalField object or DiscreteField object. 
        orientationTensorType
            A SymbolicConstant specifying the type of orientation tensor. Possible values are 
            UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default value is UNIFORM. 
        orientationTensorFieldName
            A String specifying the name of the AnalyticalField object or DiscreteField object. 
        shape
            A SymbolicConstant specifying the type of inclusion shapes. Possible values are SPHERE, 
            PROLATE, OBLATE, CYLINDER, PENNY, and ELLIPTIC_CYLINDER. The default value is SPHERE. 
        direction
            A SymbolicConstant specifying the type of inclusion direction. Possible values are 
            FIXED, RANDOM3D, and ORIENTATION_TENSOR. 
        strainConcentrationTensor
            A sequence of Floats defining the 36 components of the strain concentration tensor. 
        temperatureGradientConcentrationTensor
            A sequence of Floats defining the 9 components of the temperature gradient concentration 
            tensor. 

        Returns
        -------
            A MeanFieldVoid object. 

        Raises
        ------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the MeanFieldVoid object.

        Raises
        ------
            RangeError. 
        """
        pass
