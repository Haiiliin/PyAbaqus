from abaqus.TableCollection.ParameterColumn import ParameterColumn
from abaqus.TableCollection.ParameterColumnArray import ParameterColumnArray
from abaqusConstants import *


class ParameterTable:
    """A ParameterTable is an object that is used to define the containers that encapsulate
    ParameterColumn and DataTable objects. The data of DataTable is dependent on the 
    contents of ParameterColumn. After DataTable is instantiated, making changes to 
    ParameterColumn may lead to data corruption. 

    Access
    ------
        - mdb.models[name].tableCollections[name].parameterTables[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - *PARAMETER TABLE TYPE
        - *PARAMETER TABLE

    """

    # A ParameterColumnArray specifying all the columns in the ParameterTable. 
    columns: ParameterColumnArray = ParameterColumnArray()

    # A DataTableArray specifying all the dataTables in the ParameterTable. 
    dataTables: str = ''

    def __init__(self, name: str):
        """This method creates a ParameterTable object and places it in the parameterTables
        repository.

        Path
        ----
            - mdb.models[name].tableCollections[name].ParameterTable

        Parameters
        ----------
        name
            A String specifying the repository key. 

        Returns
        -------
            A ParameterTable object. . 
        """
        pass

    def Column(self, type: SymbolicConstant, unit: str = '', description: str = '', default: str = '',
               allowedValues: str = '') -> ParameterColumn:
        """ParameterColumn is a constructor method that creates a ParameterColumn object and stores
        it in the array data structure. It is accessible from the ParameterTable object using a
        column member.

        Path
        ----
            - mdb.models[name].tableCollections[name].parameterTables[name].Column

        Parameters
        ----------
        type
            A SymbolicConstant specifying the data type of the parameter. Possible values are
            STRING, INTEGER, and FLOAT.
        unit
            A String specifying the unit of the parameter.
        description
            A String specifying the description of the parameter.
        default
            The default value of the first parameter. The data type of the value depends on the
            value of *type* argument.
        allowedValues
            A Set of allowed values for the parameter.

        Returns
        -------
            A ParameterTable object.

        Exceptions
        ----------
            Incompatible data are given.
        """
        parameterColumn = ParameterColumn(type, unit, description, default, allowedValues)
        self.columns.append(parameterColumn)
        return parameterColumn
