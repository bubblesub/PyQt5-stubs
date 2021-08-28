# The PEP 484 type hints stub file for the QtPrintSupport module.
#
# Generated by SIP 6.0.2
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
#
# This file is part of PyQt5.
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

from PyQt5 import sip

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QAbstractPrintDialog(QtWidgets.QDialog):

    class PrintDialogOption(int):
        None_ = ... # type: QAbstractPrintDialog.PrintDialogOption
        PrintToFile = ... # type: QAbstractPrintDialog.PrintDialogOption
        PrintSelection = ... # type: QAbstractPrintDialog.PrintDialogOption
        PrintPageRange = ... # type: QAbstractPrintDialog.PrintDialogOption
        PrintCollateCopies = ... # type: QAbstractPrintDialog.PrintDialogOption
        PrintShowPageSize = ... # type: QAbstractPrintDialog.PrintDialogOption
        PrintCurrentPage = ... # type: QAbstractPrintDialog.PrintDialogOption

    None_ = ...  # type: QAbstractPrintDialog.PrintDialogOption
    PrintToFile = ...  # type: QAbstractPrintDialog.PrintDialogOption
    PrintSelection = ...  # type: QAbstractPrintDialog.PrintDialogOption
    PrintPageRange = ...  # type: QAbstractPrintDialog.PrintDialogOption
    PrintCollateCopies = ...  # type: QAbstractPrintDialog.PrintDialogOption
    PrintShowPageSize = ...  # type: QAbstractPrintDialog.PrintDialogOption
    PrintCurrentPage = ...  # type: QAbstractPrintDialog.PrintDialogOption

    class PrintRange(int):
        AllPages = ... # type: QAbstractPrintDialog.PrintRange
        Selection = ... # type: QAbstractPrintDialog.PrintRange
        PageRange = ... # type: QAbstractPrintDialog.PrintRange
        CurrentPage = ... # type: QAbstractPrintDialog.PrintRange

    AllPages = ...  # type: QAbstractPrintDialog.PrintRange
    Selection = ...  # type: QAbstractPrintDialog.PrintRange
    PageRange = ...  # type: QAbstractPrintDialog.PrintRange
    CurrentPage = ...  # type: QAbstractPrintDialog.PrintRange

    class PrintDialogOptions(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QAbstractPrintDialog.PrintDialogOptions', 'QAbstractPrintDialog.PrintDialogOption']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QAbstractPrintDialog.PrintDialogOptions') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QAbstractPrintDialog.PrintDialogOptions': ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...

        def __xor__(self, other: typing.Union['QAbstractPrintDialog.PrintDialogOptions', 'QAbstractPrintDialog.PrintDialogOption']) -> 'QAbstractPrintDialog.PrintDialogOptions': ...
        def __ixor__(self, other: typing.Union['QAbstractPrintDialog.PrintDialogOptions', 'QAbstractPrintDialog.PrintDialogOption']) -> 'QAbstractPrintDialog.PrintDialogOptions': ...
        def __iand__(self, other: typing.Union['QAbstractPrintDialog.PrintDialogOptions', 'QAbstractPrintDialog.PrintDialogOption']) -> 'QAbstractPrintDialog.PrintDialogOptions': ...
        def __or__(self, other: typing.Union['QAbstractPrintDialog.PrintDialogOptions', 'QAbstractPrintDialog.PrintDialogOption']) -> 'QAbstractPrintDialog.PrintDialogOptions': ...
        def __ior__(self, other: typing.Union['QAbstractPrintDialog.PrintDialogOptions', 'QAbstractPrintDialog.PrintDialogOption']) -> 'QAbstractPrintDialog.PrintDialogOptions': ...
        def __and__(self, other: typing.Union['QAbstractPrintDialog.PrintDialogOptions', 'QAbstractPrintDialog.PrintDialogOption']) -> 'QAbstractPrintDialog.PrintDialogOptions': ...

    def __init__(self, printer: 'QPrinter', parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def enabledOptions(self) -> 'QAbstractPrintDialog.PrintDialogOptions': ...
    def setEnabledOptions(self, options: typing.Union['QAbstractPrintDialog.PrintDialogOptions', 'QAbstractPrintDialog.PrintDialogOption']) -> None: ...
    def setOptionTabs(self, tabs: typing.Iterable[QtWidgets.QWidget]) -> None: ...
    def printer(self) -> 'QPrinter': ...
    def toPage(self) -> int: ...
    def fromPage(self) -> int: ...
    def setFromTo(self, fromPage: int, toPage: int) -> None: ...
    def maxPage(self) -> int: ...
    def minPage(self) -> int: ...
    def setMinMax(self, min: int, max: int) -> None: ...
    def printRange(self) -> 'QAbstractPrintDialog.PrintRange': ...
    def setPrintRange(self, range: 'QAbstractPrintDialog.PrintRange') -> None: ...
    def exec(self) -> int: ...
    def exec_(self) -> int: ...


class QPageSetupDialog(QtWidgets.QDialog):

    @typing.overload
    def __init__(self, printer: 'QPrinter', parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def printer(self) -> 'QPrinter': ...
    def done(self, result: int) -> None: ...
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    def open(self, slot: PYQT_SLOT) -> None: ...
    def exec(self) -> int: ...
    def exec_(self) -> int: ...
    def setVisible(self, visible: bool) -> None: ...


class QPrintDialog(QAbstractPrintDialog):

    @typing.overload
    def __init__(self, printer: 'QPrinter', parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    @typing.overload  # type: ignore[override]
    def accepted(self) -> None: ...
    @typing.overload
    def accepted(self, printer: 'QPrinter') -> None: ...
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    def open(self, slot: PYQT_SLOT) -> None: ...
    def setVisible(self, visible: bool) -> None: ...
    def options(self) -> QAbstractPrintDialog.PrintDialogOptions: ...
    def setOptions(self, options: typing.Union[QAbstractPrintDialog.PrintDialogOptions, QAbstractPrintDialog.PrintDialogOption]) -> None: ...
    def testOption(self, option: QAbstractPrintDialog.PrintDialogOption) -> bool: ...
    def setOption(self, option: QAbstractPrintDialog.PrintDialogOption, on: bool = ...) -> None: ...
    def done(self, result: int) -> None: ...
    def accept(self) -> None: ...
    def exec(self) -> int: ...
    def exec_(self) -> int: ...


class QPrintEngine(sip.simplewrapper):

    class PrintEnginePropertyKey(int):
        PPK_CollateCopies = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_ColorMode = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_Creator = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_DocumentName = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_FullPage = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_NumberOfCopies = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_Orientation = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_OutputFileName = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PageOrder = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PageRect = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PageSize = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperRect = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperSource = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PrinterName = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PrinterProgram = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_Resolution = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_SelectionOption = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_SupportedResolutions = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_WindowsPageSize = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_FontEmbedding = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_Duplex = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperSources = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_CustomPaperSize = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PageMargins = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperSize = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_CopyCount = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_SupportsMultipleCopies = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_PaperName = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_QPageSize = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_QPageMargins = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_QPageLayout = ... # type: QPrintEngine.PrintEnginePropertyKey
        PPK_CustomBase = ... # type: QPrintEngine.PrintEnginePropertyKey

    PPK_CollateCopies = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_ColorMode = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_Creator = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_DocumentName = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_FullPage = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_NumberOfCopies = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_Orientation = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_OutputFileName = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PageOrder = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PageRect = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PageSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PaperRect = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PaperSource = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PrinterName = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PrinterProgram = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_Resolution = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_SelectionOption = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_SupportedResolutions = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_WindowsPageSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_FontEmbedding = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_Duplex = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PaperSources = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_CustomPaperSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PageMargins = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PaperSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_CopyCount = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_SupportsMultipleCopies = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_PaperName = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_QPageSize = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_QPageMargins = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_QPageLayout = ...  # type: QPrintEngine.PrintEnginePropertyKey
    PPK_CustomBase = ...  # type: QPrintEngine.PrintEnginePropertyKey

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QPrintEngine') -> None: ...

    def printerState(self) -> 'QPrinter.PrinterState': ...
    def metric(self, a0: QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def abort(self) -> bool: ...
    def newPage(self) -> bool: ...
    def property(self, key: 'QPrintEngine.PrintEnginePropertyKey') -> typing.Any: ...
    def setProperty(self, key: 'QPrintEngine.PrintEnginePropertyKey', value: typing.Any) -> None: ...


class QPrinter(QtGui.QPagedPaintDevice):

    class DuplexMode(int):
        DuplexNone = ... # type: QPrinter.DuplexMode
        DuplexAuto = ... # type: QPrinter.DuplexMode
        DuplexLongSide = ... # type: QPrinter.DuplexMode
        DuplexShortSide = ... # type: QPrinter.DuplexMode

    DuplexNone = ...  # type: QPrinter.DuplexMode
    DuplexAuto = ...  # type: QPrinter.DuplexMode
    DuplexLongSide = ...  # type: QPrinter.DuplexMode
    DuplexShortSide = ...  # type: QPrinter.DuplexMode

    class Unit(int):
        Millimeter = ... # type: QPrinter.Unit
        Point = ... # type: QPrinter.Unit
        Inch = ... # type: QPrinter.Unit
        Pica = ... # type: QPrinter.Unit
        Didot = ... # type: QPrinter.Unit
        Cicero = ... # type: QPrinter.Unit
        DevicePixel = ... # type: QPrinter.Unit

    Millimeter = ...  # type: QPrinter.Unit
    Point = ...  # type: QPrinter.Unit
    Inch = ...  # type: QPrinter.Unit
    Pica = ...  # type: QPrinter.Unit
    Didot = ...  # type: QPrinter.Unit
    Cicero = ...  # type: QPrinter.Unit
    DevicePixel = ...  # type: QPrinter.Unit

    class PrintRange(int):
        AllPages = ... # type: QPrinter.PrintRange
        Selection = ... # type: QPrinter.PrintRange
        PageRange = ... # type: QPrinter.PrintRange
        CurrentPage = ... # type: QPrinter.PrintRange

    AllPages = ...  # type: QPrinter.PrintRange
    Selection = ...  # type: QPrinter.PrintRange
    PageRange = ...  # type: QPrinter.PrintRange
    CurrentPage = ...  # type: QPrinter.PrintRange

    class OutputFormat(int):
        NativeFormat = ... # type: QPrinter.OutputFormat
        PdfFormat = ... # type: QPrinter.OutputFormat

    NativeFormat = ...  # type: QPrinter.OutputFormat
    PdfFormat = ...  # type: QPrinter.OutputFormat

    class PrinterState(int):
        Idle = ... # type: QPrinter.PrinterState
        Active = ... # type: QPrinter.PrinterState
        Aborted = ... # type: QPrinter.PrinterState
        Error = ... # type: QPrinter.PrinterState

    Idle = ...  # type: QPrinter.PrinterState
    Active = ...  # type: QPrinter.PrinterState
    Aborted = ...  # type: QPrinter.PrinterState
    Error = ...  # type: QPrinter.PrinterState

    class PaperSource(int):
        OnlyOne = ... # type: QPrinter.PaperSource
        Lower = ... # type: QPrinter.PaperSource
        Middle = ... # type: QPrinter.PaperSource
        Manual = ... # type: QPrinter.PaperSource
        Envelope = ... # type: QPrinter.PaperSource
        EnvelopeManual = ... # type: QPrinter.PaperSource
        Auto = ... # type: QPrinter.PaperSource
        Tractor = ... # type: QPrinter.PaperSource
        SmallFormat = ... # type: QPrinter.PaperSource
        LargeFormat = ... # type: QPrinter.PaperSource
        LargeCapacity = ... # type: QPrinter.PaperSource
        Cassette = ... # type: QPrinter.PaperSource
        FormSource = ... # type: QPrinter.PaperSource
        MaxPageSource = ... # type: QPrinter.PaperSource
        Upper = ... # type: QPrinter.PaperSource
        CustomSource = ... # type: QPrinter.PaperSource
        LastPaperSource = ... # type: QPrinter.PaperSource

    OnlyOne = ...  # type: QPrinter.PaperSource
    Lower = ...  # type: QPrinter.PaperSource
    Middle = ...  # type: QPrinter.PaperSource
    Manual = ...  # type: QPrinter.PaperSource
    Envelope = ...  # type: QPrinter.PaperSource
    EnvelopeManual = ...  # type: QPrinter.PaperSource
    Auto = ...  # type: QPrinter.PaperSource
    Tractor = ...  # type: QPrinter.PaperSource
    SmallFormat = ...  # type: QPrinter.PaperSource
    LargeFormat = ...  # type: QPrinter.PaperSource
    LargeCapacity = ...  # type: QPrinter.PaperSource
    Cassette = ...  # type: QPrinter.PaperSource
    FormSource = ...  # type: QPrinter.PaperSource
    MaxPageSource = ...  # type: QPrinter.PaperSource
    Upper = ...  # type: QPrinter.PaperSource
    CustomSource = ...  # type: QPrinter.PaperSource
    LastPaperSource = ...  # type: QPrinter.PaperSource

    class ColorMode(int):
        GrayScale = ... # type: QPrinter.ColorMode
        Color = ... # type: QPrinter.ColorMode

    GrayScale = ...  # type: QPrinter.ColorMode
    Color = ...  # type: QPrinter.ColorMode

    class PageOrder(int):
        FirstPageFirst = ... # type: QPrinter.PageOrder
        LastPageFirst = ... # type: QPrinter.PageOrder

    FirstPageFirst = ...  # type: QPrinter.PageOrder
    LastPageFirst = ...  # type: QPrinter.PageOrder

    class Orientation(int):
        Portrait = ... # type: QPrinter.Orientation
        Landscape = ... # type: QPrinter.Orientation

    Portrait = ...  # type: QPrinter.Orientation
    Landscape = ...  # type: QPrinter.Orientation

    class PrinterMode(int):
        ScreenResolution = ... # type: QPrinter.PrinterMode
        PrinterResolution = ... # type: QPrinter.PrinterMode
        HighResolution = ... # type: QPrinter.PrinterMode

    ScreenResolution = ...  # type: QPrinter.PrinterMode
    PrinterResolution = ...  # type: QPrinter.PrinterMode
    HighResolution = ...  # type: QPrinter.PrinterMode

    @typing.overload
    def __init__(self, mode: 'QPrinter.PrinterMode' = ...) -> None: ...
    @typing.overload
    def __init__(self, printer: 'QPrinterInfo', mode: 'QPrinter.PrinterMode' = ...) -> None: ...

    def pdfVersion(self) -> QtGui.QPagedPaintDevice.PdfVersion: ...
    def setPdfVersion(self, version: QtGui.QPagedPaintDevice.PdfVersion) -> None: ...
    def paperName(self) -> str: ...
    def setPaperName(self, paperName: str) -> None: ...
    def setEngines(self, printEngine: QPrintEngine, paintEngine: QtGui.QPaintEngine) -> None: ...
    def metric(self, a0: QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def getPageMargins(self, unit: 'QPrinter.Unit') -> typing.Tuple[float, float, float, float]: ...
    def setPageMargins(self, left: float, top: float, right: float, bottom: float, unit: 'QPrinter.Unit') -> None: ...  # type: ignore[override]
    def setMargins(self, m: QtGui.QPagedPaintDevice.Margins) -> None: ...
    def printRange(self) -> 'QPrinter.PrintRange': ...
    def setPrintRange(self, range: 'QPrinter.PrintRange') -> None: ...
    def toPage(self) -> int: ...
    def fromPage(self) -> int: ...
    def setFromTo(self, fromPage: int, toPage: int) -> None: ...
    def printEngine(self) -> QPrintEngine: ...
    def paintEngine(self) -> QtGui.QPaintEngine: ...
    def printerState(self) -> 'QPrinter.PrinterState': ...
    def abort(self) -> bool: ...
    def newPage(self) -> bool: ...
    def setPrinterSelectionOption(self, a0: str) -> None: ...
    def printerSelectionOption(self) -> str: ...
    @typing.overload
    def pageRect(self) -> QtCore.QRect: ...
    @typing.overload
    def pageRect(self, a0: 'QPrinter.Unit') -> QtCore.QRectF: ...
    @typing.overload
    def paperRect(self) -> QtCore.QRect: ...
    @typing.overload
    def paperRect(self, a0: 'QPrinter.Unit') -> QtCore.QRectF: ...
    def doubleSidedPrinting(self) -> bool: ...
    def setDoubleSidedPrinting(self, enable: bool) -> None: ...
    def fontEmbeddingEnabled(self) -> bool: ...
    def setFontEmbeddingEnabled(self, enable: bool) -> None: ...
    def supportedResolutions(self) -> typing.List[int]: ...
    def duplex(self) -> 'QPrinter.DuplexMode': ...
    def setDuplex(self, duplex: 'QPrinter.DuplexMode') -> None: ...
    def paperSource(self) -> 'QPrinter.PaperSource': ...
    def setPaperSource(self, a0: 'QPrinter.PaperSource') -> None: ...
    def supportsMultipleCopies(self) -> bool: ...
    def copyCount(self) -> int: ...
    def setCopyCount(self, a0: int) -> None: ...
    def fullPage(self) -> bool: ...
    def setFullPage(self, a0: bool) -> None: ...
    def collateCopies(self) -> bool: ...
    def setCollateCopies(self, collate: bool) -> None: ...
    def colorMode(self) -> 'QPrinter.ColorMode': ...
    def setColorMode(self, a0: 'QPrinter.ColorMode') -> None: ...
    def resolution(self) -> int: ...
    def setResolution(self, a0: int) -> None: ...
    def pageOrder(self) -> 'QPrinter.PageOrder': ...
    def setPageOrder(self, a0: 'QPrinter.PageOrder') -> None: ...
    @typing.overload
    def paperSize(self) -> QtGui.QPagedPaintDevice.PageSize: ...
    @typing.overload
    def paperSize(self, unit: 'QPrinter.Unit') -> QtCore.QSizeF: ...
    @typing.overload
    def setPaperSize(self, a0: QtGui.QPagedPaintDevice.PageSize) -> None: ...
    @typing.overload
    def setPaperSize(self, paperSize: QtCore.QSizeF, unit: 'QPrinter.Unit') -> None: ...
    def setPageSizeMM(self, size: QtCore.QSizeF) -> None: ...
    def orientation(self) -> 'QPrinter.Orientation': ...
    def setOrientation(self, a0: 'QPrinter.Orientation') -> None: ...
    def creator(self) -> str: ...
    def setCreator(self, a0: str) -> None: ...
    def docName(self) -> str: ...
    def setDocName(self, a0: str) -> None: ...
    def printProgram(self) -> str: ...
    def setPrintProgram(self, a0: str) -> None: ...
    def outputFileName(self) -> str: ...
    def setOutputFileName(self, a0: str) -> None: ...
    def isValid(self) -> bool: ...
    def printerName(self) -> str: ...
    def setPrinterName(self, a0: str) -> None: ...
    def outputFormat(self) -> 'QPrinter.OutputFormat': ...
    def setOutputFormat(self, format: 'QPrinter.OutputFormat') -> None: ...


class QPrinterInfo(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: 'QPrinterInfo') -> None: ...
    @typing.overload
    def __init__(self, printer: QPrinter) -> None: ...

    def supportedColorModes(self) -> typing.List[QPrinter.ColorMode]: ...
    def defaultColorMode(self) -> QPrinter.ColorMode: ...
    def supportedDuplexModes(self) -> typing.List[QPrinter.DuplexMode]: ...
    def defaultDuplexMode(self) -> QPrinter.DuplexMode: ...
    @staticmethod
    def defaultPrinterName() -> str: ...
    @staticmethod
    def availablePrinterNames() -> typing.List[str]: ...
    def supportedResolutions(self) -> typing.List[int]: ...
    def maximumPhysicalPageSize(self) -> QtGui.QPageSize: ...
    def minimumPhysicalPageSize(self) -> QtGui.QPageSize: ...
    def supportsCustomPageSizes(self) -> bool: ...
    def defaultPageSize(self) -> QtGui.QPageSize: ...
    def supportedPageSizes(self) -> typing.List[QtGui.QPageSize]: ...
    def state(self) -> QPrinter.PrinterState: ...
    def isRemote(self) -> bool: ...
    @staticmethod
    def printerInfo(printerName: str) -> 'QPrinterInfo': ...
    def makeAndModel(self) -> str: ...
    def location(self) -> str: ...
    def description(self) -> str: ...
    @staticmethod
    def defaultPrinter() -> 'QPrinterInfo': ...
    @staticmethod
    def availablePrinters() -> typing.List['QPrinterInfo']: ...
    def supportedSizesWithNames(self) -> typing.List[typing.Tuple[str, QtCore.QSizeF]]: ...
    def supportedPaperSizes(self) -> typing.List[QtGui.QPagedPaintDevice.PageSize]: ...
    def isDefault(self) -> bool: ...
    def isNull(self) -> bool: ...
    def printerName(self) -> str: ...


class QPrintPreviewDialog(QtWidgets.QDialog):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...
    @typing.overload
    def __init__(self, printer: QPrinter, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    paintRequested: typing.ClassVar[QtCore.pyqtSignal]

    def done(self, result: int) -> None: ...
    def printer(self) -> QPrinter: ...
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    def open(self, slot: PYQT_SLOT) -> None: ...
    def setVisible(self, visible: bool) -> None: ...


class QPrintPreviewWidget(QtWidgets.QWidget):

    class ZoomMode(int):
        CustomZoom = ... # type: QPrintPreviewWidget.ZoomMode
        FitToWidth = ... # type: QPrintPreviewWidget.ZoomMode
        FitInView = ... # type: QPrintPreviewWidget.ZoomMode

    CustomZoom = ...  # type: QPrintPreviewWidget.ZoomMode
    FitToWidth = ...  # type: QPrintPreviewWidget.ZoomMode
    FitInView = ...  # type: QPrintPreviewWidget.ZoomMode

    class ViewMode(int):
        SinglePageView = ... # type: QPrintPreviewWidget.ViewMode
        FacingPagesView = ... # type: QPrintPreviewWidget.ViewMode
        AllPagesView = ... # type: QPrintPreviewWidget.ViewMode

    SinglePageView = ...  # type: QPrintPreviewWidget.ViewMode
    FacingPagesView = ...  # type: QPrintPreviewWidget.ViewMode
    AllPagesView = ...  # type: QPrintPreviewWidget.ViewMode

    @typing.overload
    def __init__(self, printer: QPrinter, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...
    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    def pageCount(self) -> int: ...
    previewChanged: typing.ClassVar[QtCore.pyqtSignal]
    paintRequested: typing.ClassVar[QtCore.pyqtSignal]
    def updatePreview(self) -> None: ...
    def setAllPagesViewMode(self) -> None: ...
    def setFacingPagesViewMode(self) -> None: ...
    def setSinglePageViewMode(self) -> None: ...
    def setPortraitOrientation(self) -> None: ...
    def setLandscapeOrientation(self) -> None: ...
    def fitInView(self) -> None: ...
    def fitToWidth(self) -> None: ...
    def setCurrentPage(self, pageNumber: int) -> None: ...
    def setZoomMode(self, zoomMode: 'QPrintPreviewWidget.ZoomMode') -> None: ...
    def setViewMode(self, viewMode: 'QPrintPreviewWidget.ViewMode') -> None: ...
    def setOrientation(self, orientation: QPrinter.Orientation) -> None: ...
    def setZoomFactor(self, zoomFactor: float) -> None: ...
    def zoomOut(self, factor: float = ...) -> None: ...
    def zoomIn(self, factor: float = ...) -> None: ...
    def print(self) -> None: ...
    def print_(self) -> None: ...
    def setVisible(self, visible: bool) -> None: ...
    def currentPage(self) -> int: ...
    def zoomMode(self) -> 'QPrintPreviewWidget.ZoomMode': ...
    def viewMode(self) -> 'QPrintPreviewWidget.ViewMode': ...
    def orientation(self) -> QPrinter.Orientation: ...
    def zoomFactor(self) -> float: ...
