from abaqusConstants import *
from .PropertyTableData import PropertyTableData


class PropertyTable:
    """A PropertyTable is an object that is used to define the container that encapsulates the
    PropertyTableData object. 
    The data of the PropertyTableData object is dependent on the contents of the 
    PropertyTable object. 
    After PropertyTableDatais instantiated, making changes to PropertyTable may lead to data 
    corruption. 

    Access
    ------
        - mdb.models[name].tableCollections[name].propertyTables[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - PROPERTY TABLE TYPE
        - PROPERTY TABLE

    """

    # A repository of PropertyTableData. Specifies all the propertyTableData in PropertyTable 
    propertyTableDatas: dict[str, PropertyTableData] = dict[str, PropertyTableData]()

    def __init__(self, name: str, properties: str, variables: str = ''):
        """This method creates a PropertyTable object.

        Path
        ----
            - mdb.models[name].tableCollections[name].PropertyTable

        Parameters
        ----------
        name
            A String specifying the repository key. 
        properties
            A string array specifying the multiple properties to build the parameter table type. 
        variables
            A String array specifying multiple independent variables. The default value is an empty 
            array. 

        Returns
        -------
            A PropertyTable object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self, variables: str = ''):
        """This method modifies the PropertyTable object.

        Parameters
        ----------
        variables
            A String array specifying multiple independent variables. The default value is an empty 
            array. 

        Returns
        -------

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def PropertyTableData(self, label: str = '', regularize: SymbolicConstant = None,
                          extrapolate: SymbolicConstant = None, isTemp: Boolean = OFF, fieldNums: int = None,
                          regularizeTolerance: str = '', data: str = '') -> PropertyTableData:
        """This method creates a PropertyTableData object.

        Path
        ----
            - mdb.models[name].tableCollections[name].propertyTables[name].PropertTableData

        Parameters
        ----------
        label
            A String specifying a unique label name for the current PropertyTable object.
        regularize
            A SymbolicConstant specifying the type of regularize to the user-defined property data.
        extrapolate
            A SymbolicConstant specifying the type of extrapolation of dependent variables outside
            the specified range of the independent variables.
        isTemp
            A Boolean specifying the dependency of properties on temperature.
        fieldNums
            An Int specifying the field variables on which properties are dependent.
        regularizeTolerance
            A Double specifying the tolerance to be used to regularize the property table data.
        data
            An Array of doubles specifying the values of the properties, the variables mentioned in
            PropertyTable, and the field variables mentioned in PropertyTableData.

        Returns
        -------
            A PropertyTableData object.

        Exceptions
        ----------
            RangeError.
        """
        self.propertyTableDatas[label] = propertyTableData = PropertyTableData(label, regularize, extrapolate, isTemp,
                                                                               fieldNums, regularizeTolerance, data)
        return propertyTableData
