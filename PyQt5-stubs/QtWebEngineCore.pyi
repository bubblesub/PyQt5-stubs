# The PEP 484 type hints stub file for the QtWebEngineCore module.
#
# Generated by SIP 6.0.2
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQtWebEngine.
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
from PyQt5 import QtNetwork
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


class QtWebEngineCore(sip.simplewrapper): ...


class QWebEngineClientCertificateStore(sip.simplewrapper):

    def clear(self) -> None: ...
    def remove(self, certificate: QtNetwork.QSslCertificate) -> None: ...
    def certificates(self) -> typing.List[QtNetwork.QSslCertificate]: ...
    def add(self, certificate: QtNetwork.QSslCertificate, privateKey: QtNetwork.QSslKey) -> None: ...


class QWebEngineCookieStore(QtCore.QObject):

    class FilterRequest(sip.simplewrapper):

        firstPartyUrl = ... # type: QtCore.QUrl
        origin = ... # type: QtCore.QUrl
        thirdParty = ... # type: bool

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebEngineCookieStore.FilterRequest') -> None: ...

    def setCookieFilter(self, filterCallback: typing.Optional[typing.Callable[[FilterRequest], bool]] = ...) -> None: ...
    def cookieRemoved(self, cookie: QtNetwork.QNetworkCookie) -> None: ...
    def cookieAdded(self, cookie: QtNetwork.QNetworkCookie) -> None: ...
    def loadAllCookies(self) -> None: ...
    def deleteAllCookies(self) -> None: ...
    def deleteSessionCookies(self) -> None: ...
    def deleteCookie(self, cookie: QtNetwork.QNetworkCookie, origin: QtCore.QUrl = ...) -> None: ...
    def setCookie(self, cookie: QtNetwork.QNetworkCookie, origin: QtCore.QUrl = ...) -> None: ...


class QWebEngineFindTextResult(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QWebEngineFindTextResult') -> None: ...

    def activeMatch(self) -> int: ...
    def numberOfMatches(self) -> int: ...


class QWebEngineHttpRequest(sip.simplewrapper):

    class Method(int):
        Get = ... # type: QWebEngineHttpRequest.Method
        Post = ... # type: QWebEngineHttpRequest.Method

    Get = ...  # type: QWebEngineHttpRequest.Method
    Post = ...  # type: QWebEngineHttpRequest.Method

    @typing.overload
    def __init__(self, url: QtCore.QUrl = ..., method: 'QWebEngineHttpRequest.Method' = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QWebEngineHttpRequest') -> None: ...

    def unsetHeader(self, headerName: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def setHeader(self, headerName: typing.Union[QtCore.QByteArray, bytes, bytearray], value: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def header(self, headerName: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> QtCore.QByteArray: ...
    def headers(self) -> typing.List[QtCore.QByteArray]: ...
    def hasHeader(self, headerName: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> bool: ...
    def setPostData(self, postData: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def postData(self) -> QtCore.QByteArray: ...
    def setUrl(self, url: QtCore.QUrl) -> None: ...
    def url(self) -> QtCore.QUrl: ...
    def setMethod(self, method: 'QWebEngineHttpRequest.Method') -> None: ...
    def method(self) -> 'QWebEngineHttpRequest.Method': ...
    def swap(self, other: 'QWebEngineHttpRequest') -> None: ...
    @staticmethod
    def postRequest(url: QtCore.QUrl, postData: typing.Dict[str, str]) -> 'QWebEngineHttpRequest': ...


class QWebEngineNotification(QtCore.QObject):

    def closed(self) -> None: ...
    def close(self) -> None: ...
    def click(self) -> None: ...
    def show(self) -> None: ...
    def direction(self) -> QtCore.Qt.LayoutDirection: ...
    def language(self) -> str: ...
    def tag(self) -> str: ...
    def message(self) -> str: ...
    def title(self) -> str: ...
    def icon(self) -> QtGui.QImage: ...
    def origin(self) -> QtCore.QUrl: ...
    def matches(self, other: 'QWebEngineNotification') -> bool: ...


class QWebEngineQuotaRequest(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QWebEngineQuotaRequest') -> None: ...

    def requestedSize(self) -> int: ...
    def origin(self) -> QtCore.QUrl: ...
    def reject(self) -> None: ...
    def accept(self) -> None: ...


class QWebEngineRegisterProtocolHandlerRequest(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QWebEngineRegisterProtocolHandlerRequest') -> None: ...

    def scheme(self) -> str: ...
    def origin(self) -> QtCore.QUrl: ...
    def reject(self) -> None: ...
    def accept(self) -> None: ...


class QWebEngineUrlRequestInfo(sip.simplewrapper):

    class NavigationType(int):
        NavigationTypeLink = ... # type: QWebEngineUrlRequestInfo.NavigationType
        NavigationTypeTyped = ... # type: QWebEngineUrlRequestInfo.NavigationType
        NavigationTypeFormSubmitted = ... # type: QWebEngineUrlRequestInfo.NavigationType
        NavigationTypeBackForward = ... # type: QWebEngineUrlRequestInfo.NavigationType
        NavigationTypeReload = ... # type: QWebEngineUrlRequestInfo.NavigationType
        NavigationTypeRedirect = ... # type: QWebEngineUrlRequestInfo.NavigationType
        NavigationTypeOther = ... # type: QWebEngineUrlRequestInfo.NavigationType

    NavigationTypeLink = ...  # type: QWebEngineUrlRequestInfo.NavigationType
    NavigationTypeTyped = ...  # type: QWebEngineUrlRequestInfo.NavigationType
    NavigationTypeFormSubmitted = ...  # type: QWebEngineUrlRequestInfo.NavigationType
    NavigationTypeBackForward = ...  # type: QWebEngineUrlRequestInfo.NavigationType
    NavigationTypeReload = ...  # type: QWebEngineUrlRequestInfo.NavigationType
    NavigationTypeRedirect = ...  # type: QWebEngineUrlRequestInfo.NavigationType
    NavigationTypeOther = ...  # type: QWebEngineUrlRequestInfo.NavigationType

    class ResourceType(int):
        ResourceTypeMainFrame = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeSubFrame = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeStylesheet = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeScript = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeImage = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeFontResource = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeSubResource = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeObject = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeMedia = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeWorker = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeSharedWorker = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypePrefetch = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeFavicon = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeXhr = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypePing = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeServiceWorker = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeUnknown = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeCspReport = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypePluginResource = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeNavigationPreloadMainFrame = ... # type: QWebEngineUrlRequestInfo.ResourceType
        ResourceTypeNavigationPreloadSubFrame = ... # type: QWebEngineUrlRequestInfo.ResourceType

    ResourceTypeMainFrame = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeSubFrame = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeStylesheet = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeScript = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeImage = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeFontResource = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeSubResource = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeObject = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeMedia = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeWorker = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeSharedWorker = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypePrefetch = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeFavicon = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeXhr = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypePing = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeServiceWorker = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeUnknown = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeCspReport = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypePluginResource = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeNavigationPreloadMainFrame = ...  # type: QWebEngineUrlRequestInfo.ResourceType
    ResourceTypeNavigationPreloadSubFrame = ...  # type: QWebEngineUrlRequestInfo.ResourceType

    def initiator(self) -> QtCore.QUrl: ...
    def setHttpHeader(self, name: typing.Union[QtCore.QByteArray, bytes, bytearray], value: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def redirect(self, url: QtCore.QUrl) -> None: ...
    def block(self, shouldBlock: bool) -> None: ...
    def requestMethod(self) -> QtCore.QByteArray: ...
    def firstPartyUrl(self) -> QtCore.QUrl: ...
    def requestUrl(self) -> QtCore.QUrl: ...
    def navigationType(self) -> 'QWebEngineUrlRequestInfo.NavigationType': ...
    def resourceType(self) -> 'QWebEngineUrlRequestInfo.ResourceType': ...


class QWebEngineUrlRequestInterceptor(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def interceptRequest(self, info: QWebEngineUrlRequestInfo) -> None: ...


class QWebEngineUrlRequestJob(QtCore.QObject):

    class Error(int):
        NoError = ... # type: QWebEngineUrlRequestJob.Error
        UrlNotFound = ... # type: QWebEngineUrlRequestJob.Error
        UrlInvalid = ... # type: QWebEngineUrlRequestJob.Error
        RequestAborted = ... # type: QWebEngineUrlRequestJob.Error
        RequestDenied = ... # type: QWebEngineUrlRequestJob.Error
        RequestFailed = ... # type: QWebEngineUrlRequestJob.Error

    NoError = ...  # type: QWebEngineUrlRequestJob.Error
    UrlNotFound = ...  # type: QWebEngineUrlRequestJob.Error
    UrlInvalid = ...  # type: QWebEngineUrlRequestJob.Error
    RequestAborted = ...  # type: QWebEngineUrlRequestJob.Error
    RequestDenied = ...  # type: QWebEngineUrlRequestJob.Error
    RequestFailed = ...  # type: QWebEngineUrlRequestJob.Error

    def requestHeaders(self) -> typing.Dict[QtCore.QByteArray, QtCore.QByteArray]: ...
    def initiator(self) -> QtCore.QUrl: ...
    def redirect(self, url: QtCore.QUrl) -> None: ...
    def fail(self, error: 'QWebEngineUrlRequestJob.Error') -> None: ...
    def reply(self, contentType: typing.Union[QtCore.QByteArray, bytes, bytearray], device: QtCore.QIODevice) -> None: ...
    def requestMethod(self) -> QtCore.QByteArray: ...
    def requestUrl(self) -> QtCore.QUrl: ...


class QWebEngineUrlScheme(sip.simplewrapper):

    class Flag(int):
        SecureScheme = ... # type: QWebEngineUrlScheme.Flag
        LocalScheme = ... # type: QWebEngineUrlScheme.Flag
        LocalAccessAllowed = ... # type: QWebEngineUrlScheme.Flag
        NoAccessAllowed = ... # type: QWebEngineUrlScheme.Flag
        ServiceWorkersAllowed = ... # type: QWebEngineUrlScheme.Flag
        ViewSourceAllowed = ... # type: QWebEngineUrlScheme.Flag
        ContentSecurityPolicyIgnored = ... # type: QWebEngineUrlScheme.Flag
        CorsEnabled = ... # type: QWebEngineUrlScheme.Flag

    SecureScheme = ...  # type: QWebEngineUrlScheme.Flag
    LocalScheme = ...  # type: QWebEngineUrlScheme.Flag
    LocalAccessAllowed = ...  # type: QWebEngineUrlScheme.Flag
    NoAccessAllowed = ...  # type: QWebEngineUrlScheme.Flag
    ServiceWorkersAllowed = ...  # type: QWebEngineUrlScheme.Flag
    ViewSourceAllowed = ...  # type: QWebEngineUrlScheme.Flag
    ContentSecurityPolicyIgnored = ...  # type: QWebEngineUrlScheme.Flag
    CorsEnabled = ...  # type: QWebEngineUrlScheme.Flag

    class SpecialPort(int):
        PortUnspecified = ... # type: QWebEngineUrlScheme.SpecialPort

    PortUnspecified = ...  # type: QWebEngineUrlScheme.SpecialPort

    class Syntax(int):
        HostPortAndUserInformation = ... # type: QWebEngineUrlScheme.Syntax
        HostAndPort = ... # type: QWebEngineUrlScheme.Syntax
        Host = ... # type: QWebEngineUrlScheme.Syntax
        Path = ... # type: QWebEngineUrlScheme.Syntax

    HostPortAndUserInformation = ...  # type: QWebEngineUrlScheme.Syntax
    HostAndPort = ...  # type: QWebEngineUrlScheme.Syntax
    Host = ...  # type: QWebEngineUrlScheme.Syntax
    Path = ...  # type: QWebEngineUrlScheme.Syntax

    class Flags(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QWebEngineUrlScheme.Flags', 'QWebEngineUrlScheme.Flag']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebEngineUrlScheme.Flags') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QWebEngineUrlScheme.Flags': ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...

        def __and__(self, other: typing.Union['QWebEngineUrlScheme.Flags', 'QWebEngineUrlScheme.Flag']) -> 'QWebEngineUrlScheme.Flags': ...
        def __iand__(self, other: typing.Union['QWebEngineUrlScheme.Flags', 'QWebEngineUrlScheme.Flag']) -> 'QWebEngineUrlScheme.Flags': ...
        def __or__(self, other: typing.Union['QWebEngineUrlScheme.Flags', 'QWebEngineUrlScheme.Flag']) -> 'QWebEngineUrlScheme.Flags': ...
        def __ior__(self, other: typing.Union['QWebEngineUrlScheme.Flags', 'QWebEngineUrlScheme.Flag']) -> 'QWebEngineUrlScheme.Flags': ...
        def __xor__(self, other: typing.Union['QWebEngineUrlScheme.Flags', 'QWebEngineUrlScheme.Flag']) -> 'QWebEngineUrlScheme.Flags': ...
        def __ixor__(self, other: typing.Union['QWebEngineUrlScheme.Flags', 'QWebEngineUrlScheme.Flag']) -> 'QWebEngineUrlScheme.Flags': ...

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, name: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    @typing.overload
    def __init__(self, that: 'QWebEngineUrlScheme') -> None: ...

    @staticmethod
    def schemeByName(name: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> 'QWebEngineUrlScheme': ...
    @staticmethod
    def registerScheme(scheme: 'QWebEngineUrlScheme') -> None: ...
    def setFlags(self, newValue: typing.Union['QWebEngineUrlScheme.Flags', 'QWebEngineUrlScheme.Flag']) -> None: ...
    def flags(self) -> 'QWebEngineUrlScheme.Flags': ...
    def setDefaultPort(self, newValue: int) -> None: ...
    def defaultPort(self) -> int: ...
    def setSyntax(self, newValue: 'QWebEngineUrlScheme.Syntax') -> None: ...
    def syntax(self) -> 'QWebEngineUrlScheme.Syntax': ...
    def setName(self, newValue: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def name(self) -> QtCore.QByteArray: ...


class QWebEngineUrlSchemeHandler(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def requestStarted(self, a0: QWebEngineUrlRequestJob) -> None: ...
