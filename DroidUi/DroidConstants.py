#
# Copyright (C) 2012-2015 Tommy Alex. All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# Symbolic constants for DroidUi

#########
# DroidUi

try:
	type(basestring)
	XML_ENCODING = 'utf-8'
except NameError:	# basestring is removed in python 3
	basestring = str
	XML_ENCODING = 'unicode'

def isstring(obj):
	return isinstance(obj, basestring)

def stringlize(obj):
	'''stringlize an object'''
	return obj if isinstance(obj, basestring) else str(obj)

def joinattr(*attrs):
	'''join many attribute together'''
	return '|'.join(attrs)

def joinflags(*flags):
	'''join many flags together'''
	result = 0
	for flag in flags:
		result |= flag
	return result

# boolean
TRUE = 'true'
FALSE = 'false'

# layout_width and layout_height
WRAP_CONTENT = 'wrap_content'
MATCH_PARENT = 'match_parent'
FILL_PARENT = 'fill_parent'

# gravity and layout_gravity
TOP = 'top'
BOTTOM = 'bottom'
LEFT = 'left'
RIGHT = 'right'
CENTER = 'center'
FILL = 'fill'
CENTER_VERTICAL = 'center_vertical'
CENTER_HORIZONTAL = 'center_horizontal'
FILL_VERTICAL = 'fill_vertical'
FILL_HORIZONTAL = 'fill_horizontal'
CLIP_VERTICAL = 'clip_vertical'
CLIP_HORIZONTAL = 'clip_horizontal'

# misc
NONE = 'none'
HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'

# visibility
VISIBLE = 'visible'
INVISIBLE = 'invisible'
GONE = 'gone'

# scrollbarStyle
INSIDE_OVERLAY = 'insideOverlay'
INSIDE_INSET = 'insideInset'
OUTSIDE_OVERLAY = 'outsideOverlay'
OUTSIDE_INSET = 'outsideInset'

# textStyle
NORMAL = 'normal'
BOLD = 'bold'
ITALIC = 'italic'

# typeface
SANS = 'sans'
SERIF = 'serif'
MONOSPACE = 'monospace'

# inputType
TEXT = 'text'
DATE = 'date'
TIME = 'time'
DATETIME = 'datetime'
PHONE = 'phone'
NUMBER = 'number'
NUMBER_SIGNED = 'numberSigned'
NUMBER_DECIMAL = 'numberDecimal'
TEXT_CAP_CHARACTERS = 'textCapCharacters'
TEXT_CAP_WORDS = 'textCapWords'
TEXT_CAP_SENTENCES = 'textCapSentences'
TEXT_AUTO_CORRECT = 'textAutoCorrect'
TEXT_AUTO_COMPLETE = 'textAutoComplete'
TEXT_MULTI_LINE = 'textMultiLine'
TEXT_IME_MULTI_LINE = 'textImeMultiLine'
TEXT_NO_SUGGESTIONS = 'textNoSuggestions'
TEXT_URI = 'textUri'
TEXT_EMAIL_ADDRESS = 'textEmailAddress'
TEXT_EMAIL_SUBJECT = 'textEmailSubject'
TEXT_SHORT_MESSAGE = 'textShortMessage'
TEXT_LONG_MESSAGE = 'textLongMessage'
TEXT_PERSON_NAME = 'textPersonName'
TEXT_POSTAL_ADDRESS = 'textPostalAddress'
TEXT_PASSWORD = 'textPassword'
TEXT_VISIBLE_PASSWORD = 'textVisiblePassword'
TEXT_WEB_EDIT_TEXT = 'textWebEditText'
TEXT_FILTER = 'textFilter'
TEXT_PHONETIC = 'textPhonetic'

#############
# DroidFacade

# SmsFacade
INBOX = 'inbox'

# Bluetooth
BLUETOOTH_UUID = '457807c0-4897-11df-9879-0800200c9a66'

# sensorNumber
SENSOR_ALL = 1
ORIENTATION = 1
ACCELEROMETER = 2
MAGNETOMETER = 3
LIGHT = 4

# axis parm
NO_AXIS = 0
X = 1
Y = 2
XY = 3
Z = 4
XZ = 5
YZ = 6
XYZ = 7

####################
# DroidFacede.Intent

# Standard Activity Actions
ACTION_MAIN = 'android.intent.action.MAIN'
ACTION_VIEW = 'android.intent.action.VIEW'
ACTION_ATTACH_DATA = 'android.intent.action.ATTACH_DATA'
ACTION_EDIT = 'android.intent.action.EDIT'
ACTION_PICK = 'android.intent.action.PICK'
ACTION_CHOOSER = 'android.intent.action.CHOOSER'
ACTION_GET_CONTENT = 'android.intent.action.GET_CONTENT'
ACTION_DIAL = 'android.intent.action.DIAL'
ACTION_CALL = 'android.intent.action.CALL'
ACTION_SEND = 'android.intent.action.SEND'
ACTION_SENDTO = 'android.intent.action.SENDTO'
ACTION_ANSWER = 'android.intent.action.ANSWER'
ACTION_INSERT = 'android.intent.action.INSERT'
ACTION_DELETE = 'android.intent.action.DELETE'
ACTION_RUN = 'android.intent.action.RUN'
ACTION_SYNC = 'android.intent.action.SYNC'
ACTION_PICK_ACTIVITY = 'android.intent.action.PICK_ACTIVITY'
ACTION_SEARCH = 'android.intent.action.SEARCH'
ACTION_WEB_SEARCH = 'android.intent.action.WEB_SEARCH'
ACTION_FACTORY_TEST = 'android.intent.action.FACTORY_TEST'

# Standard Broadcast Actions
ACTION_TIME_TICK = 'android.intent.action.TIME_TICK'
ACTION_TIME_CHANGED = 'android.intent.action.TIME_SET'
ACTION_TIMEZONE_CHANGED = 'android.intent.action.TIMEZONE_CHANGED'
ACTION_BOOT_COMPLETED = 'android.intent.action.BOOT_COMPLETED'
ACTION_PACKAGE_ADDED = 'android.intent.action.PACKAGE_ADDED'
ACTION_PACKAGE_CHANGED = 'android.intent.action.PACKAGE_CHANGED'
ACTION_PACKAGE_REMOVED = 'android.intent.action.PACKAGE_REMOVED'
ACTION_PACKAGE_RESTARTED = 'android.intent.action.PACKAGE_RESTARTED'
ACTION_PACKAGE_DATA_CLEARED = 'android.intent.action.PACKAGE_DATA_CLEARED'
ACTION_UID_REMOVED = 'android.intent.action.UID_REMOVED'
ACTION_BATTERY_CHANGED = 'android.intent.action.BATTERY_CHANGED'
ACTION_POWER_CONNECTED = 'android.intent.action.ACTION_POWER_CONNECTED'
ACTION_POWER_DISCONNECTED = 'android.intent.action.ACTION_POWER_DISCONNECTED'
ACTION_SHUTDOWN = 'android.intent.action.ACTION_SHUTDOWN'

# more action
ACTION_ADVANCED_SETTINGS_CHANGED = 'android.intent.action.ADVANCED_SETTINGS'
ACTION_AIRPLANE_MODE_CHANGED = 'android.intent.action.AIRPLANE_MODE'
ACTION_ALARM_CHANGED = 'android.intent.action.ALARM_CHANGED'
ACTION_ALL_APPS = 'android.intent.action.ALL_APPS'
ACTION_ANALOG_AUDIO_DOCK_PLUG = 'android.intent.action.ANALOG_AUDIO_DOCK_PLUG'
ACTION_APP_ERROR = 'android.intent.action.APP_ERROR'
ACTION_APP_LAUNCH_FAILURE = 'com.tmobile.intent.action.APP_LAUNCH_FAILURE'
ACTION_APP_LAUNCH_FAILURE_RESET = 'com.tmobile.intent.action.APP_LAUNCH_FAILURE_RESET'
ACTION_ASSIST = 'android.intent.action.ASSIST'
ACTION_BATTERY_LOW = 'android.intent.action.BATTERY_LOW'
ACTION_BATTERY_OKAY = 'android.intent.action.BATTERY_OKAY'
ACTION_BUG_REPORT = 'android.intent.action.BUG_REPORT'
ACTION_CALL_BUTTON = 'android.intent.action.CALL_BUTTON'
ACTION_CALL_EMERGENCY = 'android.intent.action.CALL_EMERGENCY'
ACTION_CALL_PRIVILEGED = 'android.intent.action.CALL_PRIVILEGED'
ACTION_CAMERA_BUTTON = 'android.intent.action.CAMERA_BUTTON'
ACTION_CLEAR_DNS_CACHE = 'android.intent.action.CLEAR_DNS_CACHE'
ACTION_CLOSE_SYSTEM_DIALOGS = 'android.intent.action.CLOSE_SYSTEM_DIALOGS'
ACTION_CONFIGURATION_CHANGED = 'android.intent.action.CONFIGURATION_CHANGED'
ACTION_CREATE_SHORTCUT = 'android.intent.action.CREATE_SHORTCUT'
ACTION_DATE_CHANGED = 'android.intent.action.DATE_CHANGED'
ACTION_DEFAULT = 'android.intent.action.VIEW'
ACTION_DEVICE_STORAGE_FULL = 'android.intent.action.DEVICE_STORAGE_FULL'
ACTION_DEVICE_STORAGE_LOW = 'android.intent.action.DEVICE_STORAGE_LOW'
ACTION_DEVICE_STORAGE_NOT_FULL = 'android.intent.action.DEVICE_STORAGE_NOT_FULL'
ACTION_DEVICE_STORAGE_OK = 'android.intent.action.DEVICE_STORAGE_OK'
ACTION_DIGITAL_AUDIO_DOCK_PLUG = 'android.intent.action.DIGITAL_AUDIO_DOCK_PLUG'
ACTION_DOCK_EVENT = 'android.intent.action.DOCK_EVENT'
ACTION_DREAMING_STARTED = 'android.intent.action.DREAMING_STARTED'
ACTION_DREAMING_STOPPED = 'android.intent.action.DREAMING_STOPPED'
ACTION_EXTERNAL_APPLICATIONS_AVAILABLE = 'android.intent.action.EXTERNAL_APPLICATIONS_AVAILABLE'
ACTION_EXTERNAL_APPLICATIONS_UNAVAILABLE = 'android.intent.action.EXTERNAL_APPLICATIONS_UNAVAILABLE'
ACTION_GTALK_SERVICE_CONNECTED = 'android.intent.action.GTALK_CONNECTED'
ACTION_GTALK_SERVICE_DISCONNECTED = 'android.intent.action.GTALK_DISCONNECTED'
ACTION_HDMI_AUDIO_PLUG = 'android.intent.action.HDMI_AUDIO_PLUG'
ACTION_HEADSET_PLUG = 'android.intent.action.HEADSET_PLUG'
ACTION_INPUT_METHOD_CHANGED = 'android.intent.action.INPUT_METHOD_CHANGED'
ACTION_INSERT_OR_EDIT = 'android.intent.action.INSERT_OR_EDIT'
ACTION_INSTALL_PACKAGE = 'android.intent.action.INSTALL_PACKAGE'
ACTION_LOCALE_CHANGED = 'android.intent.action.LOCALE_CHANGED'
ACTION_MANAGE_NETWORK_USAGE = 'android.intent.action.MANAGE_NETWORK_USAGE'
ACTION_MANAGE_PACKAGE_STORAGE = 'android.intent.action.MANAGE_PACKAGE_STORAGE'
ACTION_MEDIA_BAD_REMOVAL = 'android.intent.action.MEDIA_BAD_REMOVAL'
ACTION_MEDIA_BUTTON = 'android.intent.action.MEDIA_BUTTON'
ACTION_MEDIA_CHECKING = 'android.intent.action.MEDIA_CHECKING'
ACTION_MEDIA_EJECT = 'android.intent.action.MEDIA_EJECT'
ACTION_MEDIA_MOUNTED = 'android.intent.action.MEDIA_MOUNTED'
ACTION_MEDIA_NOFS = 'android.intent.action.MEDIA_NOFS'
ACTION_MEDIA_REMOVED = 'android.intent.action.MEDIA_REMOVED'
ACTION_MEDIA_SCANNER_FINISHED = 'android.intent.action.MEDIA_SCANNER_FINISHED'
ACTION_MEDIA_SCANNER_SCAN_FILE = 'android.intent.action.MEDIA_SCANNER_SCAN_FILE'
ACTION_MEDIA_SCANNER_STARTED = 'android.intent.action.MEDIA_SCANNER_STARTED'
ACTION_MEDIA_SHARED = 'android.intent.action.MEDIA_SHARED'
ACTION_MEDIA_UNMOUNTABLE = 'android.intent.action.MEDIA_UNMOUNTABLE'
ACTION_MEDIA_UNMOUNTED = 'android.intent.action.MEDIA_UNMOUNTED'
ACTION_MEDIA_UNSHARED = 'android.intent.action.MEDIA_UNSHARED'
ACTION_MY_PACKAGE_REPLACED = 'android.intent.action.MY_PACKAGE_REPLACED'
ACTION_NEW_OUTGOING_CALL = 'android.intent.action.NEW_OUTGOING_CALL'
ACTION_NEW_OUTGOING_SMS = 'android.intent.action.NEW_OUTGOING_SMS'
ACTION_PACKAGE_FIRST_LAUNCH = 'android.intent.action.PACKAGE_FIRST_LAUNCH'
ACTION_PACKAGE_FULLY_REMOVED = 'android.intent.action.PACKAGE_FULLY_REMOVED'
ACTION_PACKAGE_INSTALL = 'android.intent.action.PACKAGE_INSTALL'
ACTION_PACKAGE_NEEDS_VERIFICATION = 'android.intent.action.PACKAGE_NEEDS_VERIFICATION'
ACTION_PACKAGE_REPLACED = 'android.intent.action.PACKAGE_REPLACED'
ACTION_PACKAGE_VERIFIED = 'android.intent.action.PACKAGE_VERIFIED'
ACTION_PASTE = 'android.intent.action.PASTE'
ACTION_POWER_USAGE_SUMMARY = 'android.intent.action.POWER_USAGE_SUMMARY'
ACTION_PRE_BOOT_COMPLETED = 'android.intent.action.PRE_BOOT_COMPLETED'
ACTION_PROVIDER_CHANGED = 'android.intent.action.PROVIDER_CHANGED'
ACTION_QUERY_PACKAGE_RESTART = 'android.intent.action.QUERY_PACKAGE_RESTART'
ACTION_QUICK_CLOCK = 'android.intent.action.QUICK_CLOCK'
ACTION_REBOOT = 'android.intent.action.REBOOT'
ACTION_REMOTE_INTENT = 'com.google.android.c2dm.intent.RECEIVE'
ACTION_REQUEST_SHUTDOWN = 'android.intent.action.ACTION_REQUEST_SHUTDOWN'
ACTION_SCREEN_OFF = 'android.intent.action.SCREEN_OFF'
ACTION_SCREEN_ON = 'android.intent.action.SCREEN_ON'
ACTION_SEARCH_LONG_PRESS = 'android.intent.action.SEARCH_LONG_PRESS'
ACTION_SEND_MULTIPLE = 'android.intent.action.SEND_MULTIPLE'
ACTION_SET_WALLPAPER = 'android.intent.action.SET_WALLPAPER'
ACTION_SYNC_STATE_CHANGED = 'android.intent.action.SYNC_STATE_CHANGED'
ACTION_SYSTEM_TUTORIAL = 'android.intent.action.SYSTEM_TUTORIAL'
ACTION_UMS_CONNECTED = 'android.intent.action.UMS_CONNECTED'
ACTION_UMS_DISCONNECTED = 'android.intent.action.UMS_DISCONNECTED'
ACTION_UNINSTALL_PACKAGE = 'android.intent.action.UNINSTALL_PACKAGE'
ACTION_UPGRADE_SETUP = 'android.intent.action.UPGRADE_SETUP'
ACTION_USB_AUDIO_ACCESSORY_PLUG = 'android.intent.action.USB_AUDIO_ACCESSORY_PLUG'
ACTION_USB_AUDIO_DEVICE_PLUG = 'android.intent.action.USB_AUDIO_DEVICE_PLUG'
ACTION_USER_ADDED = 'android.intent.action.USER_ADDED'
ACTION_USER_BACKGROUND = 'android.intent.action.USER_BACKGROUND'
ACTION_USER_FOREGROUND = 'android.intent.action.USER_FOREGROUND'
ACTION_USER_INFO_CHANGED = 'android.intent.action.USER_INFO_CHANGED'
ACTION_USER_INITIALIZE = 'android.intent.action.USER_INITIALIZE'
ACTION_USER_PRESENT = 'android.intent.action.USER_PRESENT'
ACTION_USER_REMOVED = 'android.intent.action.USER_REMOVED'
ACTION_USER_STARTED = 'android.intent.action.USER_STARTED'
ACTION_USER_STARTING = 'android.intent.action.USER_STARTING'
ACTION_USER_STOPPED = 'android.intent.action.USER_STOPPED'
ACTION_USER_STOPPING = 'android.intent.action.USER_STOPPING'
ACTION_USER_SWITCHED = 'android.intent.action.USER_SWITCHED'
ACTION_VOICE_COMMAND = 'android.intent.action.VOICE_COMMAND'
ACTION_WALLPAPER_CHANGED = 'android.intent.action.WALLPAPER_CHANGED'
ACTION_WIFI_DISPLAY_AUDIO = 'qualcomm.intent.action.WIFI_DISPLAY_AUDIO'
ACTION_WIFI_DISPLAY_VIDEO = 'qualcomm.intent.action.WIFI_DISPLAY_VIDEO'

# Standard Categories
CATEGORY_DEFAULT = 'android.intent.category.DEFAULT'
CATEGORY_BROWSABLE = 'android.intent.category.BROWSABLE'
CATEGORY_TAB = 'android.intent.category.TAB'
CATEGORY_ALTERNATIVE = 'android.intent.category.ALTERNATIVE'
CATEGORY_SELECTED_ALTERNATIVE = 'android.intent.category.SELECTED_ALTERNATIVE'
CATEGORY_LAUNCHER = 'android.intent.category.LAUNCHER'
CATEGORY_INFO = 'android.intent.category.INFO'
CATEGORY_HOME = 'android.intent.category.HOME'
CATEGORY_PREFERENCE = 'android.intent.category.PREFERENCE'
CATEGORY_TEST = 'android.intent.category.TEST'
CATEGORY_CAR_DOCK = 'android.intent.category.CAR_DOCK'
CATEGORY_DESK_DOCK = 'android.intent.category.DESK_DOCK'
CATEGORY_LE_DESK_DOCK = 'android.intent.category.LE_DESK_DOCK'
CATEGORY_HE_DESK_DOCK = 'android.intent.category.HE_DESK_DOCK'
CATEGORY_CAR_MODE = 'android.intent.category.CAR_MODE'
CATEGORY_APP_MARKET = 'android.intent.category.APP_MARKET'

# more category
CATEGORY_APP_BROWSER = 'android.intent.category.APP_BROWSER'
CATEGORY_APP_CALCULATOR = 'android.intent.category.APP_CALCULATOR'
CATEGORY_APP_CALENDAR = 'android.intent.category.APP_CALENDAR'
CATEGORY_APP_CONTACTS = 'android.intent.category.APP_CONTACTS'
CATEGORY_APP_EMAIL = 'android.intent.category.APP_EMAIL'
CATEGORY_APP_GALLERY = 'android.intent.category.APP_GALLERY'
CATEGORY_APP_MAPS = 'android.intent.category.APP_MAPS'
CATEGORY_APP_MESSAGING = 'android.intent.category.APP_MESSAGING'
CATEGORY_APP_MUSIC = 'android.intent.category.APP_MUSIC'
CATEGORY_DEVELOPMENT_PREFERENCE = 'android.intent.category.DEVELOPMENT_PREFERENCE'
CATEGORY_EMBED = 'android.intent.category.EMBED'
CATEGORY_FRAMEWORK_INSTRUMENTATION_TEST = 'android.intent.category.FRAMEWORK_INSTRUMENTATION_TEST'
CATEGORY_MONKEY = 'android.intent.category.MONKEY'
CATEGORY_OPENABLE = 'android.intent.category.OPENABLE'
CATEGORY_SAMPLE_CODE = 'android.intent.category.SAMPLE_CODE'
CATEGORY_THEME_PACKAGE_INSTALLED_STATE_CHANGE = 'com.tmobile.intent.category.THEME_PACKAGE_INSTALL_STATE_CHANGE'
CATEGORY_UNIT_TEST = 'android.intent.category.UNIT_TEST'

# Standard Extra Data
EXTRA_ALARM_COUNT = 'android.intent.extra.ALARM_COUNT'
EXTRA_BCC = 'android.intent.extra.BCC'
EXTRA_CC = 'android.intent.extra.CC'
EXTRA_CHANGED_COMPONENT_NAME = 'android.intent.extra.changed_component_name'
EXTRA_DATA_REMOVED = 'android.intent.extra.DATA_REMOVED'
EXTRA_DOCK_STATE = 'android.intent.extra.DOCK_STATE'
EXTRA_DOCK_STATE_HE_DESK = 4
EXTRA_DOCK_STATE_LE_DESK = 3
EXTRA_DOCK_STATE_CAR = 2
EXTRA_DOCK_STATE_DESK = 1
EXTRA_DOCK_STATE_UNDOCKED = 0
EXTRA_DONT_KILL_APP = 'android.intent.extra.DONT_KILL_APP'
EXTRA_EMAIL = 'android.intent.extra.EMAIL'
EXTRA_INITIAL_INTENTS = 'android.intent.extra.INITIAL_INTENTS'
EXTRA_INTENT = 'android.intent.extra.INTENT'
EXTRA_KEY_EVENT = 'android.intent.extra.KEY_EVENT'
EXTRA_ORIGINATING_URI = 'android.intent.extra.ORIGINATING_URI'
EXTRA_PHONE_NUMBER = 'android.intent.extra.PHONE_NUMBER'
EXTRA_REFERRER = 'android.intent.extra.REFERRER'
EXTRA_REMOTE_INTENT_TOKEN = 'android.intent.extra.remote_intent_token'
EXTRA_REPLACING = 'android.intent.extra.REPLACING'
EXTRA_SHORTCUT_ICON = 'android.intent.extra.shortcut.ICON'
EXTRA_SHORTCUT_ICON_RESOURCE = 'android.intent.extra.shortcut.ICON_RESOURCE'
EXTRA_SHORTCUT_INTENT = 'android.intent.extra.shortcut.INTENT'
EXTRA_STREAM = 'android.intent.extra.STREAM'
EXTRA_SHORTCUT_NAME = 'android.intent.extra.shortcut.NAME'
EXTRA_SUBJECT = 'android.intent.extra.SUBJECT'
EXTRA_TEMPLATE = 'android.intent.extra.TEMPLATE'
EXTRA_TEXT = 'android.intent.extra.TEXT'
EXTRA_TITLE = 'android.intent.extra.TITLE'
EXTRA_UID = 'android.intent.extra.UID'

# more extra
EXTRA_ALLOW_REPLACE = 'android.intent.extra.ALLOW_REPLACE'
EXTRA_BUG_REPORT = 'android.intent.extra.BUG_REPORT'
EXTRA_CHANGED_COMPONENT_NAME_LIST = 'android.intent.extra.changed_component_name_list'
EXTRA_CHANGED_PACKAGE_LIST = 'android.intent.extra.changed_package_list'
EXTRA_CHANGED_UID_LIST = 'android.intent.extra.changed_uid_list'
EXTRA_CLIENT_INTENT = 'android.intent.extra.client_intent'
EXTRA_CLIENT_LABEL = 'android.intent.extra.client_label'
EXTRA_HTML_TEXT = 'android.intent.extra.HTML_TEXT'
EXTRA_INSTALLER_PACKAGE_NAME = 'android.intent.extra.INSTALLER_PACKAGE_NAME'
EXTRA_INSTALL_RESULT = 'android.intent.extra.INSTALL_RESULT'
EXTRA_KEY_CONFIRM = 'android.intent.extra.KEY_CONFIRM'
EXTRA_LOCAL_ONLY = 'android.intent.extra.LOCAL_ONLY'
EXTRA_NOT_UNKNOWN_SOURCE = 'android.intent.extra.NOT_UNKNOWN_SOURCE'
EXTRA_ORIGINATING_UID = 'android.intent.extra.ORIGINATING_UID'
EXTRA_PACKAGES = 'android.intent.extra.PACKAGES'
EXTRA_REMOVED_FOR_ALL_USERS = 'android.intent.extra.REMOVED_FOR_ALL_USERS'
EXTRA_RETURN_RESULT = 'android.intent.extra.RETURN_RESULT'
EXTRA_UNINSTALL_ALL_USERS = 'android.intent.extra.UNINSTALL_ALL_USERS'
EXTRA_USER_HANDLE = 'android.intent.extra.user_handle'

# intent flags
FLAG_GRANT_READ_URI_PERMISSION = 1
FLAG_GRANT_WRITE_URI_PERMISSION = 2
FLAG_FROM_BACKGROUND = 4
FLAG_DEBUG_LOG_RESOLUTION = 8
FLAG_EXCLUDE_STOPPED_PACKAGES = 0x10
FLAG_INCLUDE_STOPPED_PACKAGES = 0x20
FLAG_ACTIVITY_TASK_ON_HOME = 0x4000
FLAG_ACTIVITY_CLEAR_TASK = 0x8000
FLAG_ACTIVITY_NO_ANIMATION = 0x10000
FLAG_ACTIVITY_REORDER_TO_FRONT = 0x20000
FLAG_ACTIVITY_NO_USER_ACTION = 0x40000
FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET = 0x80000
FLAG_ACTIVITY_LAUNCHED_FROM_HISTORY = 0x100000
FLAG_ACTIVITY_RESET_TASK_IF_NEEDED = 0x200000
FLAG_ACTIVITY_BROUGHT_TO_FRONT = 0x400000
FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS = 0x800000
FLAG_ACTIVITY_PREVIOUS_IS_TOP = 0x1000000
FLAG_ACTIVITY_FORWARD_RESULT = 0x2000000
FLAG_ACTIVITY_CLEAR_TOP = 0x4000000
FLAG_RECEIVER_BOOT_UPGRADE = 0x4000000
FLAG_ACTIVITY_MULTIPLE_TASK = 0x8000000
FLAG_RECEIVER_REGISTERED_ONLY_BEFORE_BOOT = 0x8000000
FLAG_ACTIVITY_NEW_TASK = 0x10000000
FLAG_RECEIVER_FOREGROUND = 0x10000000
FLAG_ACTIVITY_SINGLE_TOP = 0x20000000
FLAG_RECEIVER_REPLACE_PENDING = 0x20000000
FLAG_ACTIVITY_NO_HISTORY = 0x40000000
FLAG_RECEIVER_REGISTERED_ONLY = 0x40000000

#####

# key
KEY_UNKNOWN = 0
KEY_SOFT_LEFT = 1
KEY_SOFT_RIGHT = 2
HOME = KEY_HOME = 3
BACK = KEY_BACK = 4
KEY_CALL = 5
KEY_ENDCALL = 6
KEY_0 = 7
KEY_1 = 8
KEY_2 = 9
KEY_3 = 10
KEY_4 = 11
KEY_5 = 12
KEY_6 = 13
KEY_7 = 14
KEY_8 = 15
KEY_9 = 16
KEY_STAR = 17
KEY_POUND = 18
KEY_DPAD_UP = 19
KEY_DPAD_DOWN = 20
KEY_DPAD_LEFT = 21
KEY_DPAD_RIGHT = 22
KEY_DPAD_CENTER = 23
VOLUME_UP = KEY_VOLUME_UP = 24
VOLUME_DOWN = KEY_VOLUME_DOWN = 25
KEY_POWER = 26
KEY_CAMERA = 27
KEY_CLEAR = 28
KEY_A = 29
KEY_B = 30
KEY_C = 31
KEY_D = 32
KEY_E = 33
KEY_F = 34
KEY_G = 35
KEY_H = 36
KEY_I = 37
KEY_J = 38
KEY_K = 39
KEY_L = 40
KEY_M = 41
KEY_N = 42
KEY_O = 43
KEY_P = 44
KEY_Q = 45
KEY_R = 46
KEY_S = 47
KEY_T = 48
KEY_U = 49
KEY_V = 50
KEY_W = 51
KEY_X = 52
KEY_Y = 53
KEY_Z = 54
KEY_COMMA = 55
KEY_PERIOD = 56
KEY_ALT_LEFT = 57
KEY_ALT_RIGHT = 58
KEY_SHIFT_LEFT = 59
KEY_SHIFT_RIGHT = 60
KEY_TAB = 61
KEY_SPACE = 62
KEY_SYM = 63
KEY_EXPLORER = 64
KEY_ENVELOPE = 65
KEY_ENTER = 66
KEY_DEL = 67
KEY_GRAVE = 68
KEY_MINUS = 69
KEY_EQUALS = 70
KEY_LEFT_BRACKET = 71
KEY_RIGHT_BRACKET = 72
KEY_BACKSLASH = 73
KEY_SEMICOLON = 74
KEY_APOSTROPHE = 75
KEY_SLASH = 76
KEY_AT = 77
KEY_NUM = 78
KEY_HEADSETHOOK = 79
KEY_FOCUS = 80
KEY_PLUS = 81
MENU = KEY_MENU = 82
KEY_NOTIFICATION = 83
SEARCH = KEY_SEARCH = 84
KEY_MEDIA_PLAY_PAUSE = 85
KEY_MEDIA_STOP = 86
KEY_MEDIA_NEXT = 87
KEY_MEDIA_PREVIOUS = 88
KEY_MEDIA_REWIND = 89
KEY_MEDIA_FAST_FORWARD = 90
KEY_MUTE = 91
KEY_PAGE_UP = 92
KEY_PAGE_DOWN = 93
KEY_PICTSYMBOLS = 94
KEY_SWITCH_CHARSET = 95
KEY_BUTTON_A = 96
KEY_BUTTON_B = 97
KEY_BUTTON_C = 98
KEY_BUTTON_X = 99
KEY_BUTTON_Y = 100
KEY_BUTTON_Z = 101
KEY_BUTTON_L1 = 102
KEY_BUTTON_R1 = 103
KEY_BUTTON_L2 = 104
KEY_BUTTON_R2 = 105
KEY_BUTTON_THUMBL = 106
KEY_BUTTON_THUMBR = 107
KEY_BUTTON_START = 108
KEY_BUTTON_SELECT = 109
KEY_BUTTON_MODE = 110
KEY_ESCAPE = 111
KEY_FORWARD_DEL = 112
KEY_CTRL_LEFT = 113
KEY_CTRL_RIGHT = 114
KEY_CAPS_LOCK = 115
KEY_SCROLL_LOCK = 116
KEY_META_LEFT = 117
KEY_META_RIGHT = 118
KEY_FUNCTION = 119
KEY_SYSRQ = 120
KEY_BREAK = 121
KEY_MOVE_HOME = 122
KEY_MOVE_END = 123
KEY_INSERT = 124
KEY_FORWARD = 125
KEY_MEDIA_PLAY = 126
KEY_MEDIA_PAUSE = 127
KEY_MEDIA_CLOSE = 128
KEY_MEDIA_EJECT = 129
KEY_MEDIA_RECORD = 130
KEY_F1 = 131
KEY_F2 = 132
KEY_F3 = 133
KEY_F4 = 134
KEY_F5 = 135
KEY_F6 = 136
KEY_F7 = 137
KEY_F8 = 138
KEY_F9 = 139
KEY_F10 = 140
KEY_F11 = 141
KEY_F12 = 142
KEY_NUM_LOCK = 143
KEY_NUMPAD_0 = 144
KEY_NUMPAD_1 = 145
KEY_NUMPAD_2 = 146
KEY_NUMPAD_3 = 147
KEY_NUMPAD_4 = 148
KEY_NUMPAD_5 = 149
KEY_NUMPAD_6 = 150
KEY_NUMPAD_7 = 151
KEY_NUMPAD_8 = 152
KEY_NUMPAD_9 = 153
KEY_NUMPAD_DIVIDE = 154
KEY_NUMPAD_MULTIPLY = 155
KEY_NUMPAD_SUBTRACT = 156
KEY_NUMPAD_ADD = 157
KEY_NUMPAD_DOT = 158
KEY_NUMPAD_COMMA = 159
KEY_NUMPAD_ENTER = 160
KEY_NUMPAD_EQUALS = 161
KEY_NUMPAD_LEFT_PAREN = 162
KEY_NUMPAD_RIGHT_PAREN = 163
KEY_VOLUME_MUTE = 164
KEY_INFO = 165
KEY_CHANNEL_UP = 166
KEY_CHANNEL_DOWN = 167
KEY_ZOOM_IN = 168
KEY_ZOOM_OUT = 169
KEY_TV = 170
KEY_WINDOW = 171
KEY_GUIDE = 172
KEY_DVR = 173
KEY_BOOKMARK = 174
KEY_CAPTIONS = 175
KEY_SETTINGS = 176
KEY_TV_POWER = 177
KEY_TV_INPUT = 178
KEY_STB_POWER = 179
KEY_STB_INPUT = 180
KEY_AVR_POWER = 181
KEY_AVR_INPUT = 182
KEY_PROG_RED = 183
KEY_PROG_GREEN = 184
KEY_PROG_YELLOW = 185
KEY_PROG_BLUE = 186
KEY_APP_SWITCH = 187
KEY_BUTTON_1 = 188
KEY_BUTTON_2 = 189
KEY_BUTTON_3 = 190
KEY_BUTTON_4 = 191
KEY_BUTTON_5 = 192
KEY_BUTTON_6 = 193
KEY_BUTTON_7 = 194
KEY_BUTTON_8 = 195
KEY_BUTTON_9 = 196
KEY_BUTTON_10 = 197
KEY_BUTTON_11 = 198
KEY_BUTTON_12 = 199
KEY_BUTTON_13 = 200
KEY_BUTTON_14 = 201
KEY_BUTTON_15 = 202
KEY_BUTTON_16 = 203
KEY_LANGUAGE_SWITCH = 204
KEY_MANNER_MODE = 205
KEY_3D_MODE = 206
KEY_CONTACTS = 207
KEY_CALENDAR = 208
KEY_MUSIC = 209
KEY_CALCULATOR = 210
KEY_ZENKAKU_HANKAKU = 211
KEY_EISU = 212
KEY_MUHENKAN = 213
KEY_HENKAN = 214
KEY_KATAKANA_HIRAGANA = 215
KEY_YEN = 216
KEY_RO = 217
KEY_KANA = 218
KEY_ASSIST = 219
KEY_BRIGHTNESS_DOWN = 220
KEY_BRIGHTNESS_UP = 221
KEY_MEDIA_AUDIO_TRACK = 222
