class _VXAuto(object):
    def __init__(self, ffi, lib):
        self.ACTION_ABANDON = lib.VX_ACTION_ABANDON
        self.ACTION_CONTINUE = lib.VX_ACTION_CONTINUE
        self.ARRAY_ATTRIBUTE_CAPACITY = lib.VX_ARRAY_ATTRIBUTE_CAPACITY
        self.ARRAY_ATTRIBUTE_ITEMSIZE = lib.VX_ARRAY_ATTRIBUTE_ITEMSIZE
        self.ARRAY_ATTRIBUTE_ITEMTYPE = lib.VX_ARRAY_ATTRIBUTE_ITEMTYPE
        self.ARRAY_ATTRIBUTE_NUMITEMS = lib.VX_ARRAY_ATTRIBUTE_NUMITEMS
        self.ATTRIBUTE_ID_MASK = lib.VX_ATTRIBUTE_ID_MASK
        self.BIDIRECTIONAL = lib.VX_BIDIRECTIONAL
        self.BORDER_MODE_CONSTANT = lib.VX_BORDER_MODE_CONSTANT
        self.BORDER_MODE_REPLICATE = lib.VX_BORDER_MODE_REPLICATE
        self.BORDER_MODE_UNDEFINED = lib.VX_BORDER_MODE_UNDEFINED
        self.CHANNEL_0 = lib.VX_CHANNEL_0
        self.CHANNEL_1 = lib.VX_CHANNEL_1
        self.CHANNEL_2 = lib.VX_CHANNEL_2
        self.CHANNEL_3 = lib.VX_CHANNEL_3
        self.CHANNEL_A = lib.VX_CHANNEL_A
        self.CHANNEL_B = lib.VX_CHANNEL_B
        self.CHANNEL_G = lib.VX_CHANNEL_G
        self.CHANNEL_R = lib.VX_CHANNEL_R
        self.CHANNEL_RANGE_FULL = lib.VX_CHANNEL_RANGE_FULL
        self.CHANNEL_RANGE_RESTRICTED = lib.VX_CHANNEL_RANGE_RESTRICTED
        self.CHANNEL_U = lib.VX_CHANNEL_U
        self.CHANNEL_V = lib.VX_CHANNEL_V
        self.CHANNEL_Y = lib.VX_CHANNEL_Y
        self.COLOR_SPACE_BT601_525 = lib.VX_COLOR_SPACE_BT601_525
        self.COLOR_SPACE_BT601_625 = lib.VX_COLOR_SPACE_BT601_625
        self.COLOR_SPACE_BT709 = lib.VX_COLOR_SPACE_BT709
        self.COLOR_SPACE_DEFAULT = lib.VX_COLOR_SPACE_DEFAULT
        self.COLOR_SPACE_NONE = lib.VX_COLOR_SPACE_NONE
        self.CONTEXT_ATTRIBUTE_CONVOLUTION_MAXIMUM_DIMENSION = lib.VX_CONTEXT_ATTRIBUTE_CONVOLUTION_MAXIMUM_DIMENSION
        self.CONTEXT_ATTRIBUTE_EXTENSIONS = lib.VX_CONTEXT_ATTRIBUTE_EXTENSIONS
        self.CONTEXT_ATTRIBUTE_EXTENSIONS_SIZE = lib.VX_CONTEXT_ATTRIBUTE_EXTENSIONS_SIZE
        self.CONTEXT_ATTRIBUTE_IMMEDIATE_BORDER_MODE = lib.VX_CONTEXT_ATTRIBUTE_IMMEDIATE_BORDER_MODE
        self.CONTEXT_ATTRIBUTE_IMPLEMENTATION = lib.VX_CONTEXT_ATTRIBUTE_IMPLEMENTATION
        self.CONTEXT_ATTRIBUTE_MODULES = lib.VX_CONTEXT_ATTRIBUTE_MODULES
        self.CONTEXT_ATTRIBUTE_OPTICAL_FLOW_WINDOW_MAXIMUM_DIMENSION = lib.VX_CONTEXT_ATTRIBUTE_OPTICAL_FLOW_WINDOW_MAXIMUM_DIMENSION
        self.CONTEXT_ATTRIBUTE_REFERENCES = lib.VX_CONTEXT_ATTRIBUTE_REFERENCES
        self.CONTEXT_ATTRIBUTE_UNIQUE_KERNELS = lib.VX_CONTEXT_ATTRIBUTE_UNIQUE_KERNELS
        self.CONTEXT_ATTRIBUTE_UNIQUE_KERNEL_TABLE = lib.VX_CONTEXT_ATTRIBUTE_UNIQUE_KERNEL_TABLE
        self.CONTEXT_ATTRIBUTE_VENDOR_ID = lib.VX_CONTEXT_ATTRIBUTE_VENDOR_ID
        self.CONTEXT_ATTRIBUTE_VERSION = lib.VX_CONTEXT_ATTRIBUTE_VERSION
        self.CONVERT_POLICY_SATURATE = lib.VX_CONVERT_POLICY_SATURATE
        self.CONVERT_POLICY_WRAP = lib.VX_CONVERT_POLICY_WRAP
        self.CONVOLUTION_ATTRIBUTE_COLUMNS = lib.VX_CONVOLUTION_ATTRIBUTE_COLUMNS
        self.CONVOLUTION_ATTRIBUTE_ROWS = lib.VX_CONVOLUTION_ATTRIBUTE_ROWS
        self.CONVOLUTION_ATTRIBUTE_SCALE = lib.VX_CONVOLUTION_ATTRIBUTE_SCALE
        self.CONVOLUTION_ATTRIBUTE_SIZE = lib.VX_CONVOLUTION_ATTRIBUTE_SIZE
        self.DELAY_ATTRIBUTE_SLOTS = lib.VX_DELAY_ATTRIBUTE_SLOTS
        self.DELAY_ATTRIBUTE_TYPE = lib.VX_DELAY_ATTRIBUTE_TYPE
        self.DF_IMAGE_IYUV = lib.VX_DF_IMAGE_IYUV
        self.DF_IMAGE_NV12 = lib.VX_DF_IMAGE_NV12
        self.DF_IMAGE_NV21 = lib.VX_DF_IMAGE_NV21
        self.DF_IMAGE_RGB = lib.VX_DF_IMAGE_RGB
        self.DF_IMAGE_RGBX = lib.VX_DF_IMAGE_RGBX
        self.DF_IMAGE_S16 = lib.VX_DF_IMAGE_S16
        self.DF_IMAGE_S32 = lib.VX_DF_IMAGE_S32
        self.DF_IMAGE_U16 = lib.VX_DF_IMAGE_U16
        self.DF_IMAGE_U32 = lib.VX_DF_IMAGE_U32
        self.DF_IMAGE_U8 = lib.VX_DF_IMAGE_U8
        self.DF_IMAGE_UYVY = lib.VX_DF_IMAGE_UYVY
        self.DF_IMAGE_VIRT = lib.VX_DF_IMAGE_VIRT
        self.DF_IMAGE_YUV4 = lib.VX_DF_IMAGE_YUV4
        self.DF_IMAGE_YUYV = lib.VX_DF_IMAGE_YUYV
        self.DIRECTIVE_DISABLE_LOGGING = lib.VX_DIRECTIVE_DISABLE_LOGGING
        self.DIRECTIVE_ENABLE_LOGGING = lib.VX_DIRECTIVE_ENABLE_LOGGING
        self.DISTRIBUTION_ATTRIBUTE_BINS = lib.VX_DISTRIBUTION_ATTRIBUTE_BINS
        self.DISTRIBUTION_ATTRIBUTE_DIMENSIONS = lib.VX_DISTRIBUTION_ATTRIBUTE_DIMENSIONS
        self.DISTRIBUTION_ATTRIBUTE_OFFSET = lib.VX_DISTRIBUTION_ATTRIBUTE_OFFSET
        self.DISTRIBUTION_ATTRIBUTE_RANGE = lib.VX_DISTRIBUTION_ATTRIBUTE_RANGE
        self.DISTRIBUTION_ATTRIBUTE_SIZE = lib.VX_DISTRIBUTION_ATTRIBUTE_SIZE
        self.DISTRIBUTION_ATTRIBUTE_WINDOW = lib.VX_DISTRIBUTION_ATTRIBUTE_WINDOW
        self.ENUM_ACCESSOR = lib.VX_ENUM_ACCESSOR
        self.ENUM_ACTION = lib.VX_ENUM_ACTION
        self.ENUM_BORDER_MODE = lib.VX_ENUM_BORDER_MODE
        self.ENUM_CHANNEL = lib.VX_ENUM_CHANNEL
        self.ENUM_COLOR_RANGE = lib.VX_ENUM_COLOR_RANGE
        self.ENUM_COLOR_SPACE = lib.VX_ENUM_COLOR_SPACE
        self.ENUM_COMPARISON = lib.VX_ENUM_COMPARISON
        self.ENUM_CONVERT_POLICY = lib.VX_ENUM_CONVERT_POLICY
        self.ENUM_DIRECTION = lib.VX_ENUM_DIRECTION
        self.ENUM_DIRECTIVE = lib.VX_ENUM_DIRECTIVE
        self.ENUM_HINT = lib.VX_ENUM_HINT
        self.ENUM_IMPORT_MEM = lib.VX_ENUM_IMPORT_MEM
        self.ENUM_INTERPOLATION = lib.VX_ENUM_INTERPOLATION
        self.ENUM_MASK = lib.VX_ENUM_MASK
        self.ENUM_NORM_TYPE = lib.VX_ENUM_NORM_TYPE
        self.ENUM_OVERFLOW = lib.VX_ENUM_OVERFLOW
        self.ENUM_PARAMETER_STATE = lib.VX_ENUM_PARAMETER_STATE
        self.ENUM_ROUND_POLICY = lib.VX_ENUM_ROUND_POLICY
        self.ENUM_TERM_CRITERIA = lib.VX_ENUM_TERM_CRITERIA
        self.ENUM_THRESHOLD_TYPE = lib.VX_ENUM_THRESHOLD_TYPE
        self.ENUM_TYPE_MASK = lib.VX_ENUM_TYPE_MASK
        self.ERROR_GRAPH_ABANDONED = lib.VX_ERROR_GRAPH_ABANDONED
        self.ERROR_GRAPH_SCHEDULED = lib.VX_ERROR_GRAPH_SCHEDULED
        self.ERROR_INVALID_DIMENSION = lib.VX_ERROR_INVALID_DIMENSION
        self.ERROR_INVALID_FORMAT = lib.VX_ERROR_INVALID_FORMAT
        self.ERROR_INVALID_GRAPH = lib.VX_ERROR_INVALID_GRAPH
        self.ERROR_INVALID_LINK = lib.VX_ERROR_INVALID_LINK
        self.ERROR_INVALID_MODULE = lib.VX_ERROR_INVALID_MODULE
        self.ERROR_INVALID_NODE = lib.VX_ERROR_INVALID_NODE
        self.ERROR_INVALID_PARAMETERS = lib.VX_ERROR_INVALID_PARAMETERS
        self.ERROR_INVALID_REFERENCE = lib.VX_ERROR_INVALID_REFERENCE
        self.ERROR_INVALID_SCOPE = lib.VX_ERROR_INVALID_SCOPE
        self.ERROR_INVALID_TYPE = lib.VX_ERROR_INVALID_TYPE
        self.ERROR_INVALID_VALUE = lib.VX_ERROR_INVALID_VALUE
        self.ERROR_MULTIPLE_WRITERS = lib.VX_ERROR_MULTIPLE_WRITERS
        self.ERROR_NOT_ALLOCATED = lib.VX_ERROR_NOT_ALLOCATED
        self.ERROR_NOT_COMPATIBLE = lib.VX_ERROR_NOT_COMPATIBLE
        self.ERROR_NOT_IMPLEMENTED = lib.VX_ERROR_NOT_IMPLEMENTED
        self.ERROR_NOT_SUFFICIENT = lib.VX_ERROR_NOT_SUFFICIENT
        self.ERROR_NOT_SUPPORTED = lib.VX_ERROR_NOT_SUPPORTED
        self.ERROR_NO_MEMORY = lib.VX_ERROR_NO_MEMORY
        self.ERROR_NO_RESOURCES = lib.VX_ERROR_NO_RESOURCES
        self.ERROR_OPTIMIZED_AWAY = lib.VX_ERROR_OPTIMIZED_AWAY
        self.ERROR_REFERENCE_NONZERO = lib.VX_ERROR_REFERENCE_NONZERO
        self.FAILURE = lib.VX_FAILURE
        self.GRAPH_ATTRIBUTE_NUMNODES = lib.VX_GRAPH_ATTRIBUTE_NUMNODES
        self.GRAPH_ATTRIBUTE_NUMPARAMETERS = lib.VX_GRAPH_ATTRIBUTE_NUMPARAMETERS
        self.GRAPH_ATTRIBUTE_PERFORMANCE = lib.VX_GRAPH_ATTRIBUTE_PERFORMANCE
        self.GRAPH_ATTRIBUTE_STATUS = lib.VX_GRAPH_ATTRIBUTE_STATUS
        self.HINT_SERIALIZE = lib.VX_HINT_SERIALIZE
        self.ID_AMD = lib.VX_ID_AMD
        self.ID_ARM = lib.VX_ID_ARM
        self.ID_AXIS = lib.VX_ID_AXIS
        self.ID_BDTI = lib.VX_ID_BDTI
        self.ID_BROADCOM = lib.VX_ID_BROADCOM
        self.ID_CEVA = lib.VX_ID_CEVA
        self.ID_COGNIVUE = lib.VX_ID_COGNIVUE
        self.ID_DEFAULT = lib.VX_ID_DEFAULT
        self.ID_FREESCALE = lib.VX_ID_FREESCALE
        self.ID_IMAGINATION = lib.VX_ID_IMAGINATION
        self.ID_INTEL = lib.VX_ID_INTEL
        self.ID_ITSEEZ = lib.VX_ID_ITSEEZ
        self.ID_KHRONOS = lib.VX_ID_KHRONOS
        self.ID_MARVELL = lib.VX_ID_MARVELL
        self.ID_MAX = lib.VX_ID_MAX
        self.ID_MEDIATEK = lib.VX_ID_MEDIATEK
        self.ID_MOVIDIUS = lib.VX_ID_MOVIDIUS
        self.ID_NVIDIA = lib.VX_ID_NVIDIA
        self.ID_QUALCOMM = lib.VX_ID_QUALCOMM
        self.ID_RENESAS = lib.VX_ID_RENESAS
        self.ID_SAMSUNG = lib.VX_ID_SAMSUNG
        self.ID_ST = lib.VX_ID_ST
        self.ID_SYNOPSYS = lib.VX_ID_SYNOPSYS
        self.ID_TI = lib.VX_ID_TI
        self.ID_VIDEANTIS = lib.VX_ID_VIDEANTIS
        self.ID_VIVANTE = lib.VX_ID_VIVANTE
        self.ID_XILINX = lib.VX_ID_XILINX
        self.IMAGE_ATTRIBUTE_FORMAT = lib.VX_IMAGE_ATTRIBUTE_FORMAT
        self.IMAGE_ATTRIBUTE_HEIGHT = lib.VX_IMAGE_ATTRIBUTE_HEIGHT
        self.IMAGE_ATTRIBUTE_PLANES = lib.VX_IMAGE_ATTRIBUTE_PLANES
        self.IMAGE_ATTRIBUTE_RANGE = lib.VX_IMAGE_ATTRIBUTE_RANGE
        self.IMAGE_ATTRIBUTE_SIZE = lib.VX_IMAGE_ATTRIBUTE_SIZE
        self.IMAGE_ATTRIBUTE_SPACE = lib.VX_IMAGE_ATTRIBUTE_SPACE
        self.IMAGE_ATTRIBUTE_WIDTH = lib.VX_IMAGE_ATTRIBUTE_WIDTH
        self.IMPORT_TYPE_HOST = lib.VX_IMPORT_TYPE_HOST
        self.IMPORT_TYPE_NONE = lib.VX_IMPORT_TYPE_NONE
        self.INPUT = lib.VX_INPUT
        self.INTERPOLATION_TYPE_AREA = lib.VX_INTERPOLATION_TYPE_AREA
        self.INTERPOLATION_TYPE_BILINEAR = lib.VX_INTERPOLATION_TYPE_BILINEAR
        self.INTERPOLATION_TYPE_NEAREST_NEIGHBOR = lib.VX_INTERPOLATION_TYPE_NEAREST_NEIGHBOR
        self.KERNEL_ABSDIFF = lib.VX_KERNEL_ABSDIFF
        self.KERNEL_ACCUMULATE = lib.VX_KERNEL_ACCUMULATE
        self.KERNEL_ACCUMULATE_SQUARE = lib.VX_KERNEL_ACCUMULATE_SQUARE
        self.KERNEL_ACCUMULATE_WEIGHTED = lib.VX_KERNEL_ACCUMULATE_WEIGHTED
        self.KERNEL_ADD = lib.VX_KERNEL_ADD
        self.KERNEL_AND = lib.VX_KERNEL_AND
        self.KERNEL_ATTRIBUTE_ENUM = lib.VX_KERNEL_ATTRIBUTE_ENUM
        self.KERNEL_ATTRIBUTE_LOCAL_DATA_PTR = lib.VX_KERNEL_ATTRIBUTE_LOCAL_DATA_PTR
        self.KERNEL_ATTRIBUTE_LOCAL_DATA_SIZE = lib.VX_KERNEL_ATTRIBUTE_LOCAL_DATA_SIZE
        self.KERNEL_ATTRIBUTE_NAME = lib.VX_KERNEL_ATTRIBUTE_NAME
        self.KERNEL_ATTRIBUTE_PARAMETERS = lib.VX_KERNEL_ATTRIBUTE_PARAMETERS
        self.KERNEL_BOX_3x3 = lib.VX_KERNEL_BOX_3x3
        self.KERNEL_CANNY_EDGE_DETECTOR = lib.VX_KERNEL_CANNY_EDGE_DETECTOR
        self.KERNEL_CHANNEL_COMBINE = lib.VX_KERNEL_CHANNEL_COMBINE
        self.KERNEL_CHANNEL_EXTRACT = lib.VX_KERNEL_CHANNEL_EXTRACT
        self.KERNEL_COLOR_CONVERT = lib.VX_KERNEL_COLOR_CONVERT
        self.KERNEL_CONVERTDEPTH = lib.VX_KERNEL_CONVERTDEPTH
        self.KERNEL_CUSTOM_CONVOLUTION = lib.VX_KERNEL_CUSTOM_CONVOLUTION
        self.KERNEL_DILATE_3x3 = lib.VX_KERNEL_DILATE_3x3
        self.KERNEL_EQUALIZE_HISTOGRAM = lib.VX_KERNEL_EQUALIZE_HISTOGRAM
        self.KERNEL_ERODE_3x3 = lib.VX_KERNEL_ERODE_3x3
        self.KERNEL_FAST_CORNERS = lib.VX_KERNEL_FAST_CORNERS
        self.KERNEL_GAUSSIAN_3x3 = lib.VX_KERNEL_GAUSSIAN_3x3
        self.KERNEL_GAUSSIAN_PYRAMID = lib.VX_KERNEL_GAUSSIAN_PYRAMID
        self.KERNEL_HALFSCALE_GAUSSIAN = lib.VX_KERNEL_HALFSCALE_GAUSSIAN
        self.KERNEL_HARRIS_CORNERS = lib.VX_KERNEL_HARRIS_CORNERS
        self.KERNEL_HISTOGRAM = lib.VX_KERNEL_HISTOGRAM
        self.KERNEL_INTEGRAL_IMAGE = lib.VX_KERNEL_INTEGRAL_IMAGE
        self.KERNEL_INVALID = lib.VX_KERNEL_INVALID
        self.KERNEL_MAGNITUDE = lib.VX_KERNEL_MAGNITUDE
        self.KERNEL_MASK = lib.VX_KERNEL_MASK
        self.KERNEL_MAX_1_0 = lib.VX_KERNEL_MAX_1_0
        self.KERNEL_MEAN_STDDEV = lib.VX_KERNEL_MEAN_STDDEV
        self.KERNEL_MEDIAN_3x3 = lib.VX_KERNEL_MEDIAN_3x3
        self.KERNEL_MINMAXLOC = lib.VX_KERNEL_MINMAXLOC
        self.KERNEL_MULTIPLY = lib.VX_KERNEL_MULTIPLY
        self.KERNEL_NOT = lib.VX_KERNEL_NOT
        self.KERNEL_OPTICAL_FLOW_PYR_LK = lib.VX_KERNEL_OPTICAL_FLOW_PYR_LK
        self.KERNEL_OR = lib.VX_KERNEL_OR
        self.KERNEL_PHASE = lib.VX_KERNEL_PHASE
        self.KERNEL_REMAP = lib.VX_KERNEL_REMAP
        self.KERNEL_SCALE_IMAGE = lib.VX_KERNEL_SCALE_IMAGE
        self.KERNEL_SOBEL_3x3 = lib.VX_KERNEL_SOBEL_3x3
        self.KERNEL_SUBTRACT = lib.VX_KERNEL_SUBTRACT
        self.KERNEL_TABLE_LOOKUP = lib.VX_KERNEL_TABLE_LOOKUP
        self.KERNEL_THRESHOLD = lib.VX_KERNEL_THRESHOLD
        self.KERNEL_WARP_AFFINE = lib.VX_KERNEL_WARP_AFFINE
        self.KERNEL_WARP_PERSPECTIVE = lib.VX_KERNEL_WARP_PERSPECTIVE
        self.KERNEL_XOR = lib.VX_KERNEL_XOR
        self.LIBRARY_KHR_BASE = lib.VX_LIBRARY_KHR_BASE
        self.LIBRARY_MASK = lib.VX_LIBRARY_MASK
        self.LUT_ATTRIBUTE_COUNT = lib.VX_LUT_ATTRIBUTE_COUNT
        self.LUT_ATTRIBUTE_SIZE = lib.VX_LUT_ATTRIBUTE_SIZE
        self.LUT_ATTRIBUTE_TYPE = lib.VX_LUT_ATTRIBUTE_TYPE
        self.MATRIX_ATTRIBUTE_COLUMNS = lib.VX_MATRIX_ATTRIBUTE_COLUMNS
        self.MATRIX_ATTRIBUTE_ROWS = lib.VX_MATRIX_ATTRIBUTE_ROWS
        self.MATRIX_ATTRIBUTE_SIZE = lib.VX_MATRIX_ATTRIBUTE_SIZE
        self.MATRIX_ATTRIBUTE_TYPE = lib.VX_MATRIX_ATTRIBUTE_TYPE
        self.MAX_IMPLEMENTATION_NAME = lib.VX_MAX_IMPLEMENTATION_NAME
        self.MAX_KERNEL_NAME = lib.VX_MAX_KERNEL_NAME
        self.MAX_LOG_MESSAGE_LEN = lib.VX_MAX_LOG_MESSAGE_LEN
        self.META_FORMAT_ATTRIBUTE_DELTA_RECTANGLE = lib.VX_META_FORMAT_ATTRIBUTE_DELTA_RECTANGLE
        self.NODE_ATTRIBUTE_BORDER_MODE = lib.VX_NODE_ATTRIBUTE_BORDER_MODE
        self.NODE_ATTRIBUTE_LOCAL_DATA_PTR = lib.VX_NODE_ATTRIBUTE_LOCAL_DATA_PTR
        self.NODE_ATTRIBUTE_LOCAL_DATA_SIZE = lib.VX_NODE_ATTRIBUTE_LOCAL_DATA_SIZE
        self.NODE_ATTRIBUTE_PERFORMANCE = lib.VX_NODE_ATTRIBUTE_PERFORMANCE
        self.NODE_ATTRIBUTE_STATUS = lib.VX_NODE_ATTRIBUTE_STATUS
        self.NORM_L1 = lib.VX_NORM_L1
        self.NORM_L2 = lib.VX_NORM_L2
        self.OUTPUT = lib.VX_OUTPUT
        self.PARAMETER_ATTRIBUTE_DIRECTION = lib.VX_PARAMETER_ATTRIBUTE_DIRECTION
        self.PARAMETER_ATTRIBUTE_INDEX = lib.VX_PARAMETER_ATTRIBUTE_INDEX
        self.PARAMETER_ATTRIBUTE_REF = lib.VX_PARAMETER_ATTRIBUTE_REF
        self.PARAMETER_ATTRIBUTE_STATE = lib.VX_PARAMETER_ATTRIBUTE_STATE
        self.PARAMETER_ATTRIBUTE_TYPE = lib.VX_PARAMETER_ATTRIBUTE_TYPE
        self.PARAMETER_STATE_OPTIONAL = lib.VX_PARAMETER_STATE_OPTIONAL
        self.PARAMETER_STATE_REQUIRED = lib.VX_PARAMETER_STATE_REQUIRED
        self.PYRAMID_ATTRIBUTE_FORMAT = lib.VX_PYRAMID_ATTRIBUTE_FORMAT
        self.PYRAMID_ATTRIBUTE_HEIGHT = lib.VX_PYRAMID_ATTRIBUTE_HEIGHT
        self.PYRAMID_ATTRIBUTE_LEVELS = lib.VX_PYRAMID_ATTRIBUTE_LEVELS
        self.PYRAMID_ATTRIBUTE_SCALE = lib.VX_PYRAMID_ATTRIBUTE_SCALE
        self.PYRAMID_ATTRIBUTE_WIDTH = lib.VX_PYRAMID_ATTRIBUTE_WIDTH
        self.READ_AND_WRITE = lib.VX_READ_AND_WRITE
        self.READ_ONLY = lib.VX_READ_ONLY
        self.REF_ATTRIBUTE_COUNT = lib.VX_REF_ATTRIBUTE_COUNT
        self.REF_ATTRIBUTE_TYPE = lib.VX_REF_ATTRIBUTE_TYPE
        self.REMAP_ATTRIBUTE_DESTINATION_HEIGHT = lib.VX_REMAP_ATTRIBUTE_DESTINATION_HEIGHT
        self.REMAP_ATTRIBUTE_DESTINATION_WIDTH = lib.VX_REMAP_ATTRIBUTE_DESTINATION_WIDTH
        self.REMAP_ATTRIBUTE_SOURCE_HEIGHT = lib.VX_REMAP_ATTRIBUTE_SOURCE_HEIGHT
        self.REMAP_ATTRIBUTE_SOURCE_WIDTH = lib.VX_REMAP_ATTRIBUTE_SOURCE_WIDTH
        self.ROUND_POLICY_TO_NEAREST_EVEN = lib.VX_ROUND_POLICY_TO_NEAREST_EVEN
        self.ROUND_POLICY_TO_ZERO = lib.VX_ROUND_POLICY_TO_ZERO
        self.SCALAR_ATTRIBUTE_TYPE = lib.VX_SCALAR_ATTRIBUTE_TYPE
        self.SCALE_UNITY = lib.VX_SCALE_UNITY
        self.STATUS_MIN = lib.VX_STATUS_MIN
        self.SUCCESS = lib.VX_SUCCESS
        self.TERM_CRITERIA_BOTH = lib.VX_TERM_CRITERIA_BOTH
        self.TERM_CRITERIA_EPSILON = lib.VX_TERM_CRITERIA_EPSILON
        self.TERM_CRITERIA_ITERATIONS = lib.VX_TERM_CRITERIA_ITERATIONS
        self.THRESHOLD_ATTRIBUTE_DATA_TYPE = lib.VX_THRESHOLD_ATTRIBUTE_DATA_TYPE
        self.THRESHOLD_ATTRIBUTE_FALSE_VALUE = lib.VX_THRESHOLD_ATTRIBUTE_FALSE_VALUE
        self.THRESHOLD_ATTRIBUTE_THRESHOLD_LOWER = lib.VX_THRESHOLD_ATTRIBUTE_THRESHOLD_LOWER
        self.THRESHOLD_ATTRIBUTE_THRESHOLD_UPPER = lib.VX_THRESHOLD_ATTRIBUTE_THRESHOLD_UPPER
        self.THRESHOLD_ATTRIBUTE_THRESHOLD_VALUE = lib.VX_THRESHOLD_ATTRIBUTE_THRESHOLD_VALUE
        self.THRESHOLD_ATTRIBUTE_TRUE_VALUE = lib.VX_THRESHOLD_ATTRIBUTE_TRUE_VALUE
        self.THRESHOLD_ATTRIBUTE_TYPE = lib.VX_THRESHOLD_ATTRIBUTE_TYPE
        self.THRESHOLD_TYPE_BINARY = lib.VX_THRESHOLD_TYPE_BINARY
        self.THRESHOLD_TYPE_RANGE = lib.VX_THRESHOLD_TYPE_RANGE
        self.TYPE_ARRAY = lib.VX_TYPE_ARRAY
        self.TYPE_BOOL = lib.VX_TYPE_BOOL
        self.TYPE_CHAR = lib.VX_TYPE_CHAR
        self.TYPE_CONTEXT = lib.VX_TYPE_CONTEXT
        self.TYPE_CONVOLUTION = lib.VX_TYPE_CONVOLUTION
        self.TYPE_COORDINATES2D = lib.VX_TYPE_COORDINATES2D
        self.TYPE_COORDINATES3D = lib.VX_TYPE_COORDINATES3D
        self.TYPE_DELAY = lib.VX_TYPE_DELAY
        self.TYPE_DF_IMAGE = lib.VX_TYPE_DF_IMAGE
        self.TYPE_DISTRIBUTION = lib.VX_TYPE_DISTRIBUTION
        self.TYPE_ENUM = lib.VX_TYPE_ENUM
        self.TYPE_ERROR = lib.VX_TYPE_ERROR
        self.TYPE_FLOAT32 = lib.VX_TYPE_FLOAT32
        self.TYPE_FLOAT64 = lib.VX_TYPE_FLOAT64
        self.TYPE_GRAPH = lib.VX_TYPE_GRAPH
        self.TYPE_IMAGE = lib.VX_TYPE_IMAGE
        self.TYPE_INT16 = lib.VX_TYPE_INT16
        self.TYPE_INT32 = lib.VX_TYPE_INT32
        self.TYPE_INT64 = lib.VX_TYPE_INT64
        self.TYPE_INT8 = lib.VX_TYPE_INT8
        self.TYPE_INVALID = lib.VX_TYPE_INVALID
        self.TYPE_KERNEL = lib.VX_TYPE_KERNEL
        self.TYPE_KEYPOINT = lib.VX_TYPE_KEYPOINT
        self.TYPE_LUT = lib.VX_TYPE_LUT
        self.TYPE_MASK = lib.VX_TYPE_MASK
        self.TYPE_MATRIX = lib.VX_TYPE_MATRIX
        self.TYPE_META_FORMAT = lib.VX_TYPE_META_FORMAT
        self.TYPE_NODE = lib.VX_TYPE_NODE
        self.TYPE_OBJECT_MAX = lib.VX_TYPE_OBJECT_MAX
        self.TYPE_PARAMETER = lib.VX_TYPE_PARAMETER
        self.TYPE_PYRAMID = lib.VX_TYPE_PYRAMID
        self.TYPE_RECTANGLE = lib.VX_TYPE_RECTANGLE
        self.TYPE_REFERENCE = lib.VX_TYPE_REFERENCE
        self.TYPE_REMAP = lib.VX_TYPE_REMAP
        self.TYPE_SCALAR = lib.VX_TYPE_SCALAR
        self.TYPE_SCALAR_MAX = lib.VX_TYPE_SCALAR_MAX
        self.TYPE_SIZE = lib.VX_TYPE_SIZE
        self.TYPE_STRUCT_MAX = lib.VX_TYPE_STRUCT_MAX
        self.TYPE_THRESHOLD = lib.VX_TYPE_THRESHOLD
        self.TYPE_UINT16 = lib.VX_TYPE_UINT16
        self.TYPE_UINT32 = lib.VX_TYPE_UINT32
        self.TYPE_UINT64 = lib.VX_TYPE_UINT64
        self.TYPE_UINT8 = lib.VX_TYPE_UINT8
        self.TYPE_USER_STRUCT_END = lib.VX_TYPE_USER_STRUCT_END
        self.TYPE_USER_STRUCT_START = lib.VX_TYPE_USER_STRUCT_START
        self.TYPE_VENDOR_OBJECT_END = lib.VX_TYPE_VENDOR_OBJECT_END
        self.TYPE_VENDOR_OBJECT_START = lib.VX_TYPE_VENDOR_OBJECT_START
        self.TYPE_VENDOR_STRUCT_END = lib.VX_TYPE_VENDOR_STRUCT_END
        self.TYPE_VENDOR_STRUCT_START = lib.VX_TYPE_VENDOR_STRUCT_START
        self.VENDOR_MASK = lib.VX_VENDOR_MASK
        self.VERSION = lib.VX_VERSION
        self.VERSION_1_0 = lib.VX_VERSION_1_0
        self.WRITE_ONLY = lib.VX_WRITE_ONLY
        self.false_e = lib.vx_false_e
        self.true_e = lib.vx_true_e