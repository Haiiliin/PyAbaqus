class OdbJobTime:
    """The OdbJobTime object stores the analysis time of a job.

    Attributes
    ----------
    systemTime: str
        A float specifying the systemtime for the analysis. This attribute is read-only.
    userTime: str
        A float specifying the usertime for the analysis. This attribute is read-only.
    wallclockTime: str
        A float specifying the wallclocktime for the analysis. This attribute is read-only.

    Notes
    -----
        This object can be accessed by:
        - import visualization
        - session.odbData[name].diagnosticData.jobTime

    """

    # A float specifying the systemtime for the analysis. This attribute is read-only. 
    systemTime: str = ''

    # A float specifying the usertime for the analysis. This attribute is read-only. 
    userTime: str = ''

    # A float specifying the wallclocktime for the analysis. This attribute is read-only. 
    wallclockTime: str = ''
