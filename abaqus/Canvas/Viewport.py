import typing

from abaqusConstants import *
from .AttributeColorMap import AttributeColorMap
from .Displayable import Displayable
from .ImageOptions import ImageOptions
from .Layer import Layer
from .MovieOptions import MovieOptions
from ..Animation.AnimationController import AnimationController
from ..Annotation.AnnotationsToPlotArray import AnnotationsToPlotArray
from ..DisplayGroup.Leaf import Leaf
from ..DisplayOptions.AssemblyDisplayOptions import AssemblyDisplayOptions
from ..DisplayOptions.LightOptions import LightOptions
from ..DisplayOptions.PartDisplayOptions import PartDisplayOptions
from ..DisplayOptions.ViewportAnnotationOptions import ViewportAnnotationOptions
from ..OdbDisplay.OdbDisplay import OdbDisplay
from ..PlotOptions.DetailPlotOptions import DetailPlotOptions
from ..UtilityAndView.Repository import Repository
from ..UtilityAndView.View import View


class Viewport:

    """A viewport is the container for the graphics generated by the application. TheViewport 
    object stores the various settings that determine how objects are displayed within that 
    viewport. 

    Access
    ------
        - session.viewports[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the display mode of the viewport. Possible values 
    # are:SINGLE, specifying a single *displayedObject*.OVERLAY, specifying one or more layers 
    # to be displayed simultaneously—each layer contains one *displayedObject*. 
    displayMode: SymbolicConstant = None

    # A SymbolicConstant specifying which layer or layers will be controlled by the view 
    # manipulation tools when *displayMode*=OVERLAY. Possible values are ALL and CURRENT. 
    viewManipLayers: SymbolicConstant = None

    # A Float specifying a factor to be used in offsetting layers in the screen Z direction. 
    # Possible values are –1 to 1. A negative value reverses the apparent order in which the 
    # layers are plotted. 
    layerOffset: float = None

    # A SymbolicConstant specifying the current state of a viewport. Possible values are 
    # NORMAL, MAXIMIZED, and MINIMIZED. 
    windowState: SymbolicConstant = None

    # A Float specifying the width in millimeters of the current viewport, regardless of the 
    # value of *windowState*. 
    currentWidth: float = None

    # A Float specifying the height in millimeters of the current viewport, regardless of the 
    # value of *windowState*, and including the title bar. 
    currentHeight: float = None

    # A Boolean specifying whether the viewport is linked for synchronization. The default 
    # value is ON. 
    applyLinkedCommands: Boolean = ON

    # A SymbolicConstant specifying the currently active color mappings. Possible values 
    # are:DEFAULT_COLORSPART_GEOM_MAP_COLORSASSEMBLY_MAP_COLORSPART_MAP_COLORSINSTANCE_MAP_COLORSINSTANCE_TYPE_MAP_COLORSSECTION_MAP_COLORSMATERIAL_MAP_COLORSLOAD_MAP_COLORSBC_MAP_COLORSINTERACTION_MAP_COLORSCONSTRAINT_MAP_COLORSSET_MAP_COLORSSURFACE_MAP_COLORSINTERNAL_SET_MAP_COLORSINTERNAL_SURFACE_MAP_COLORSDISPLAY_GRP_MAP_COLORSSELECTION_GRP_MAP_COLORSELTYPE_MAP_COLORSPLOT_MAP_COLORSMESH_MAP_COLORSThe 
    # default value is DEFAULT_COLORS. 
    activeColorModes: SymbolicConstant = DEFAULT_COLORS

    # A SymbolicConstant specifying the last applied color mapping. Possible values 
    # are:DEFAULT_COLORSPART_GEOM_MAP_COLORSASSEMBLY_MAP_COLORSPART_MAP_COLORSINSTANCE_MAP_COLORSINSTANCE_TYPE_MAP_COLORSSECTION_MAP_COLORSMATERIAL_MAP_COLORSLOAD_MAP_COLORSBC_MAP_COLORSINTERACTION_MAP_COLORSCONSTRAINT_MAP_COLORSSET_MAP_COLORSSURFACE_MAP_COLORSINTERNAL_SET_MAP_COLORSINTERNAL_SURFACE_MAP_COLORSDISPLAY_GRP_MAP_COLORSSELECTION_GRP_MAP_COLORSELTYPE_MAP_COLORSPLOT_MAP_COLORSMESH_MAP_COLORSThe 
    # default value is DEFAULT_COLORS. 
    colorMode: SymbolicConstant = DEFAULT_COLORS

    # A Float specifying the translucency that will be applied to objects colored using 
    # *initialColor* and it needs to be set along with *initialColor*. If *initialColor* is 
    # set to 'As is' then translucency will have no effect. 
    translucency: float = None

    # A Boolean specifying whether an animation is connected to the viewport. 
    animationConnect: Boolean = OFF

    # A repository of AttributeColorMap objects specifying the objects cannot be constructed 
    # but the following attribute maps are supported:"type""Element 
    # set""Material""Section""Default""Part""Part instance""Element type""Averaging 
    # region""Assembly""Property""Set""Surface""Skin""Profile""Part shape""Part status""Part 
    # geometry""Meshability""Instance type""Load""Boundary 
    # condition""Interaction""Constraint""Interaction type""Constraint type""Display 
    # group""Selection group""Interaction property""Connector""Connector type""Connector 
    # property""Internal set""Internal 
    # surface""mapColors""autoColors""overrides""defaultAutoColors""defaultOverrides""objectToCopy""colorMapping""colorMappings""colorMode""attributeColors""updateOverrides""colorCodeOverride""initialColor""Layup""Ply" 
    colorMappings: int = None

    # A String specifying the color that will be applied to all objects in the viewport at the 
    # start of color coding. The possible values are 'As is', 'Default' or a string with a 
    # hexadecimal representation of a color. 
    initialColor: str = ''

    # A String specifying which layer is affected by options settings when *displayMode* 
    # =OVERLAY. The current layer is also the only layer affected by view manipulations 
    # when*viewManipLayers* =CURRENT. 
    currentLayer: str = ''

    # A Displayable object specifying the object to be displayed. The Displayable type is an 
    # abstract generalization. The concrete possible types are Part, Assembly, 
    # ConstrainedSketch, Odb, PlyStackPlot, or XYPlot. If *displayedObject*=None, Abaqus 
    # displays an empty viewport. 
    displayedObject: Displayable = Displayable()

    # A repository of Layer objects specifying the key to the repository is a String with the 
    # name of the layer. 
    layers: Repository[str, Layer] = Repository[str, Layer]()

    # A View object specifying the object that controls viewing of the viewport content. 
    view: View = View()

    # An OdbDisplay object specifying the display options for the Odb object. 
    odbDisplay: OdbDisplay = OdbDisplay()

    # A PartDisplayOptions object specifying the display options for the Part object. 
    partDisplay: PartDisplayOptions = PartDisplayOptions()

    # An AssemblyDisplayOptions object specifying the display options for the Assembly object. 
    assemblyDisplay: AssemblyDisplayOptions = AssemblyDisplayOptions()

    # A ViewportAnnotationOptions object. 
    viewportAnnotationOptions: ViewportAnnotationOptions = ViewportAnnotationOptions()

    # A DetailPlotOptions object. 
    detailPlotOptions: DetailPlotOptions = DetailPlotOptions()

    # An AnnotationsToPlotArray object. 
    annotationsToPlot: AnnotationsToPlotArray = AnnotationsToPlotArray()

    # A tuple of Strings specifying the names of layers that will be displayed in the viewport 
    # when *displayMode* = OVERLAY. 
    visibleLayers: tuple = ()

    # A pair of Floats specifying the *X*- and *Y*-coordinates in millimeters in the canvas 
    # coordinate system of the lower left corner of the current viewport, regardless of the 
    # value of *windowState*. 
    currentOrigin: tuple[float] = ()

    # A pair of Floats specifying the *X*- and *Y*-coordinates in millimeters of the lower 
    # left corner of the current viewport from a coordinate system having its origin in the 
    # lower left corner of the drawing area. This origin refers to the viewport location when 
    # *windowState* =MINIMIZED. 
    iconOrigin: tuple[float] = ()

    # A LightOptions object. 
    lightOptions: LightOptions = LightOptions()

    # An ImageOptions object. 
    imageOptions: ImageOptions = ImageOptions()

    # A MovieOptions object. 
    movieOptions: MovieOptions = MovieOptions()

    # An AnimationController object. 
    animationController: AnimationController = AnimationController()

    # A tuple of Strings specifying keys to the session.drawings repository. The default value 
    # is an empty sequence. 
    drawings: tuple = ()

    def __init__(self, name: str, origin: tuple[float] = (), width: float = 120, height: float = 80, 
                 border: Boolean = ON, titleBar: Boolean = ON, titleStyle: SymbolicConstant = SYSTEM, 
                 customTitleString: str = ''):
        """This method creates a Viewport object with the specified origin and dimensions.

        Path
        ----
            - session.Viewport

        Parameters
        ----------
        name
            A String specifying the repository key. 
        origin
            A pair of Floats specifying the *X*- and *Y*-coordinates in millimeters in the canvas 
            coordinate system of the lower left corner of the viewport. The default origin is (0, 
            0). 
        width
            A Float specifying the width in millimeters of the viewport. Possible values are 30 ≤≤ 
            *width* ≤≤ (*maxWidth*). The default value is 120.0.Note:The maximum value of width 
            (*maxWidth*) is the width of the screen in millimeters. 
        height
            A Float specifying the height in millimeters of the viewport. This height includes the 
            title bar. Possible values are 30 ≤≤ *height* ≤≤ (*maxHeight*). The default value is 
            80.0.Note:The maximum value of height (*maxHeight*) is the height of the screen in 
            millimeters. 
        border
            A Boolean specifying whether the viewport border is visible in a printed image. The 
            default value is ON. 
        titleBar
            A Boolean specifying whether the viewport title should be displayed in a printed image. 
            The default value is ON.If *border* = OFF, the title will not be visible, even if 
            *titleBar* =ON. 
        titleStyle
            A SymbolicConstant specifying which title to use for the viewport title. Possible values 
            are CUSTOM and SYSTEM. The default value is SYSTEM.If *titleStyle* = CUSTOM, 
            *customTitleString* will be used. If *titleStyle*= SYSTEM, a system-generated string 
            will be used. 
        customTitleString
            A String specifying the viewport title when *titleStyle* =CUSTOM. The default value is 
            an empty string. 

        Returns
        -------
            A Viewport object. 

        Exceptions
        ----------
            RangeError. 
            - If the user attempts to delete the only viewport: 
              SystemError: the current viewport may not be deleted. 
            - If *width* is out of range: 
              RangeError: width must be a Float in the range: 30 <= width <= *maxWidth* 
            - If *height* is out of range: 
              RangeError: height must be a Float in the range: 30 <= width <= *maxHeight* 
        """
        pass

    def bringToFront(self):
        """This method moves the Viewport object to the front.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def disableMultipleColors(self):
        """This method disables applying multiple color mappings that was enabled using
        enableMultipleColors

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def disableRefresh(self):
        """This method disables Viewport refresh. Some methods that require the Viewport to be
        up-to-date will override this setting. It is advisable to use this method sparingly.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def disableColorCodeUpdates(self):
        """This method disables Viewport updates and internal computations triggered because of
        color coding. Performance improvement will be significant when color coding is ON and
        repeating operations are performed using a script each of which requires color code
        updates. No benefit will be had when color coding is OFF.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def enableMultipleColors(self):
        """This method enables multiple color mappings to be applied at the same time. It also
        ensures that the Viewport is updated correctly when *initialColor* is set.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def enableRefresh(self):
        """This method enables Viewport refresh disabled using disableRefresh.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def enableColorCodeUpdates(self):
        """This method enables Viewport color code updates disabled using disableColorCodeUpdates.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getActiveElementLabels(self, useCut: Boolean = OFF, printResults: Boolean = OFF):
        """This method returns the element labels currently active in the viewport based on the
        current display group. The element labels are printed only when the *displayedObject*
        member in the Viewport object is set to an Odb. The getActiveElementLabels method has
        the following arguments:

        Parameters
        ----------
        useCut
            A Boolean flag to specify if any active cutting plane is to be considered in determining 
            active elements. 
        printResults
            A Boolean flag to specify if the active element labels are to be printed to the replay 
            file. 

        Returns
        -------
            A Dictionary object of element labels, keyed by OdbInstance name. Returns None if the 
            *displayedObject* member is not an Odb object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getActiveNodeLabels(self, useCut: Boolean = OFF, printResults: Boolean = OFF):
        """This method returns the node labels currently active in the viewport based on the
        current display group. The node labels are printed only when the *displayedObject*
        member in the Viewport object is set to an Odb. The getActiveNodeLabels method has the
        following arguments:

        Parameters
        ----------
        useCut
            A Boolean flag to specify if any active cutting plane is to be considered in determining 
            active nodes. 
        printResults
            A Boolean flag to specify if the active node labels are to be printed to the replay 
            file. 

        Returns
        -------
            A Dictionary object of node labels, keyed by OdbInstance name. Returns None if the 
            *displayedObject* member is not an Odb object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getPrimVarMinMaxLoc(self):
        """This method returns a dictionary containing the minimum, maximum and their location for
        the current primary variable. A contour plot should be displayed in the current viewport
        or else the method will return *None*.

        Parameters
        ----------

        Returns
        -------
            A dictionary with keys 'minPartInstanceName', 'minElementLabel', 'minNodeLabel', 
            'minPosition', 'maxPartInstanceName', 'maxElementLabel', 'maxNodeLabel', 'maxPosition' 

        Exceptions
        ----------
            None. 
        """
        pass

    def makeCurrent(self):
        """This method makes theViewport object the current viewport.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def maximize(self):
        """This method maximizes the Viewport object to fill the drawing area.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def minimize(self):
        """This method minimizes the Viewport object to appear as an abbreviated title bar.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def offset(self, deltaX: float = 0, deltaY: float = 0):
        """This method modifies the current *X*-*Y* location of the viewport by the specified
        distance.

        Parameters
        ----------
        deltaX
            A Float specifying the offset in millimeters of the *X*-component of the viewport 
            origin. The default value is 0. 
        deltaY
            A Float specifying the offset in millimeters of the *Y*-component of the viewport 
            origin. The default value is 0. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def restore(self):
        """This method restores a maximized or minimized Viewport object to its previous size and
        location.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def sendToBack(self):
        """This method moves the Viewport object to the back.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def setColor(self, initialColor: str, translucency: str = ''):
        """This method specifies the color assignment using *initialColor* and *translucency*. If
        *initialColor* has a value of 'As is', *translucency* has no effect. The setColor method
        has the following arguments:

        Parameters
        ----------
        initialColor
            A string specifying the initial color applied to the objects. 
        translucency
            A float in the range of 0.0 to 1.0 specifying how translucent the objects drawn using 
            *initialColor* needs to be. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def setColor(self, colorMapping: AttributeColorMap):
        """This method specifies the color assignment using attributes specified by an
        AttributeColorMap object. The setColor method has the following arguments:

        Parameters
        ----------
        colorMapping
            An AttributeColorMap object. Possible values are any AttributeColorMap object. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    @typing.overload
    def setColor(self, leaf: Leaf, edgeColorWireHide: str = '', edgeColorFillShade: str = '', 
                 fillColor: str = '', nodeSymbolColor: str = '', 
                 nodeSymbolType: SymbolicConstant = HOLLOW_CIRCLE, 
                 nodeSymbolSize: SymbolicConstant = SMALL):
        """This method specifies the color of a Leaf object.

        Parameters
        ----------
        leaf
            A Leaf object. Possible values are any Leaf object. 
        edgeColorWireHide
            A String specifying the color to be used for drawing the edges of the elements contained 
            in *leaf* when the render style is wireframe or hidden. 
        edgeColorFillShade
            A String specifying the color to be used for drawing the edges of the elements contained 
            in *leaf* when the render style is filled or shaded. 
        fillColor
            A String specifying the color to be used for drawing the faces of the elements contained 
            in *leaf* when the render style is filled or shaded. 
        nodeSymbolColor
            A String specifying the color to be used for drawing the nodes contained in *leaf*. 
        nodeSymbolType
            A SymbolicConstant specifying the node symbol types for the nodes contained in *leaf*. 
            Possible values areFILLED_CIRCLE, FILLED_SQUARE, FILLED_DIAMOND, FILLED_TRI, 
            HOLLOW_CIRCLE, HOLLOW_SQUARE, HOLLOW_DIAMOND, HOLLOW_TRI, CROSS, and XMARKER. The 
            default value is HOLLOW_CIRCLE. 
        nodeSymbolSize
            A SymbolicConstant specifying the node symbol size for the nodes contained in *leaf*. 
            Possible values are SMALL, MEDIUM, and LARGE. The default value is SMALL. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setColor(self, *args, **kwargs):
        pass

    def forceRefresh(self):
        """This method causes the Viewport to refresh immediately. It is provided to allow scripts
        to refresh the Viewport before the script terminates. Normally, there would only be a
        single cumulative refresh that takes place immediately after the script completes.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self, displayedObject: Displayable = Displayable(), displayMode: SymbolicConstant = None, 
                  visibleLayers: tuple = (), viewManipLayers: SymbolicConstant = None, 
                  currentLayer: str = '', layerOffset: float = None):
        """This method modifies the Viewport object. The arguments to setValues are the same as the
        arguments to the Viewport method, except for the *name* argument. In addition, the
        setValues method has the following arguments:

        Parameters
        ----------
        displayedObject
            A Displayable object specifying the object to be displayed. The Displayable type is an 
            abstract generalization. The concrete possible types are Part, Assembly, 
            ConstrainedSketch, Odb, PlyStackPlot, or XYPlot. If *displayedObject*=None, Abaqus 
            displays an empty viewport. 
        displayMode
            A SymbolicConstant specifying the display mode of the viewport. Possible values 
            are:SINGLE, specifying a single *displayedObject*.OVERLAY, specifying one or more layers 
            to be displayed simultaneously—each layer contains one *displayedObject*. 
        visibleLayers
            A sequence of Strings specifying the names of layers that will be displayed in the 
            viewport when *displayMode* = OVERLAY. 
        viewManipLayers
            A SymbolicConstant specifying which layer or layers will be controlled by the view 
            manipulation tools when *displayMode*=OVERLAY. Possible values are ALL and CURRENT. 
        currentLayer
            A String specifying which layer is affected by options settings when *displayMode* 
            =OVERLAY. The current layer is also the only layer affected by view manipulations 
            when*viewManipLayers* =CURRENT. 
        layerOffset
            A Float specifying a factor to be used in offsetting layers in the screen Z direction. 
            Possible values are –1 to 1. A negative value reverses the apparent order in which the 
            layers are plotted. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def addDrawings(self, names: tuple = ()):
        """This method identifies the names of Drawing objects to be rendered in the Viewport.

        Parameters
        ----------
        names
            A sequence of String values identifying keys in the session.drawings repository. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            ValueError. 
        """
        pass

    def removeDrawings(self, names: tuple = ()):
        """This method identifies the names of Drawing objects to no longer be rendered in the
        Viewport.

        Parameters
        ----------
        names
            A sequence of String values identifying keys in the Viewport sequence. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            ValueError. 
        """
        pass

    def timeDisplay(self, numFrames: int = 0, numSeconds: int = 10, degreesPerFrame: float = 0):
        """This method refreshes the Viewport display *numFrames* times and then checks to see if
        *numSeconds* seconds have elapsed. If not, it will continue refreshing the Viewport
        until the time has elapsed. At completion, the actual number of refreshes (frames)
        rendered and elapsed time will be reported along with the calculated frames-per-second
        (fps).

        Parameters
        ----------
        numFrames
            An Int specifying the minimum number of times to refresh the Viewport. The default value 
            is 0. 
        numSeconds
            An Int specifying the minimum number of seconds to spend refreshing the Viewport. The 
            default value is 10. 
        degreesPerFrame
            A Float specifying the number of degrees to rotate the model view about its Z axis 
            before each refresh. The default value is 0.0. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

