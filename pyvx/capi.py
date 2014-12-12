""" 
:mod:`pyvx.capi` --- C API
==========================================

This module allows the use of this python implementation as an `OpenVX`_ backend 
from a C program. A shared library is provided that embeds python and exports a C API
following the `OpenVX`_ specification. That way the C program does not need to
be aware of the fact that python is used. Also, any C program following the
`OpenVX`_ specification should be compilable with this backend.

.. code-block:: bash

  sudo python -mpyvx.capi build /usr/local/

This will install `libopenvx.so*` into `/usr/local/lib` and place the
`OpenVX`_ headers in `/usr/local/include/VX`.

.. _`OpenVX`: https://www.khronos.org/openvx

"""

from codegen import PythonApi, Enum, Reference
import codegen
from pyvx import vx

from pyvx import __version_info__, __version__
major, minor, _ = __version_info__
soversion = '%d.%d' % (major, minor)

def export(signature, add_ret_to_arg=0, **kwargs):
    return codegen.export(signature, add_ret_to_arg, **kwargs)



class OpenVxApi(object):
    wrapped_reference_types = ['vx_context', 'vx_image', 'vx_graph', 
                               'vx_node', 'vx_parameter', 'vx_reference']
    setup = ["import sys",
             "sys.path = ['.'] + sys.path",
             "import pyvx",
             "if pyvx.__version__ != %r:" % __version__,
             "    print 'Version mismatch. Please reinstall pyvx and/or recompile your binary. Exiting...'",
             "    exit()",
             "from pyvx.capi import OpenVxApi",
             "from pyvx.codegen import PythonApi",
             "from pyvx.inc.vx import ffi",
             "api = PythonApi(OpenVxApi, ffi).load()"]

    @export("vx_context()", add_ret_to_arg=None)
    def vxCreateContext():
        return vx.CreateContext()

    @export("vx_image(vx_context, uint32_t, uint32_t, vx_df_image)")
    def vxCreateImage(context, width, height, color):
        return vx.CreateImage(context, width, height, color)

    @export("vx_graph(vx_context)")
    def vxCreateGraph(context):
        return vx.CreateGraph(context, early_verify=False)

    @export("vx_image(vx_graph, uint32_t, uint32_t, vx_df_image)")
    def vxCreateVirtualImage(graph, width, height, color):
        return vx.CreateVirtualImage(graph, width, height, color)

    @export("vx_status(vx_graph)")
    def vxVerifyGraph(graph):
        return vx.VerifyGraph(graph)

    @export("vx_status(vx_graph)")
    def vxProcessGraph(graph):
        return vx.ProcessGraph(graph)
    
    @export("vx_status(vx_context *)")
    def vxReleaseContext(context):
        context_obj = OpenVxApi.pyapi.retrive(context[0])
        for r in context_obj.references:
            OpenVxApi.pyapi.discard(r)
        context_obj.clear_references()
        OpenVxApi.pyapi.discard(context[0])
        context[0] = OpenVxApi.pyapi.ffi.NULL
        return vx.SUCCESS

    @export("vx_node(vx_graph, vx_image, vx_enum, vx_image)")
    def vxChannelExtractNode(graph, input, channel, output):
        return vx.ChannelExtractNode(graph, input, channel, output)

    @export("vx_node(vx_graph, vx_image, vx_image)")
    def vxGaussian3x3Node(graph, input, output):
        return vx.Gaussian3x3Node(graph, input, output)

    @export("vx_node(vx_graph, vx_image, vx_image, vx_image)")
    def vxSobel3x3Node(graph, input, output_x, output_y):
        return vx.Sobel3x3Node(graph, input, output_x, output_y)

    @export("vx_node(vx_graph, vx_image, vx_image, vx_image)")
    def vxMagnitudeNode(graph, grad_x, grad_y, mag):
        return vx.MagnitudeNode(graph, grad_x, grad_y, mag)

    @export("vx_node(vx_graph, vx_image, vx_image, vx_image)")
    def vxPhaseNode(graph, grad_x, grad_y, orientation):
        return vx.PhaseNode(graph, grad_x, grad_y, orientation)

    @export("vx_node(vx_graph, char *, vx_image)")
    def vxPlayNode(graph, fn, output):
        return vx.PlayNode(graph, fn, output)

    @export("vx_node(vx_graph, vx_image, char *)")
    def vxShowNode(graph, input, name):
        return vx.ShowNode(graph, input, name)

    # ========================================================================
    # PARAMETER
    # ========================================================================
    @export("vx_parameter(vx_node, vx_uint32 index)")
    def vxGetParameterByIndex(node, index):
        return vx.GetParameterByIndex(node, index)
    
    @export("vx_status(vx_parameter *)")
    def vxReleaseParameter(param):
        param_obj = OpenVxApi.pyapi.retrive(param[0])
        OpenVxApi.pyapi.discard(param[0])
        param[0] = OpenVxApi.pyapi.ffi.NULL
        return vx.ReleaseParameter(param_obj)

    @export("vx_status(vx_parameter, vx_enum, void *, vx_size)")
    def vxQueryParameter(param, attribute, ptr, size):
        attr_type = {vx.PARAMETER_ATTRIBUTE_INDEX: 'vx_uint32',
                     vx.PARAMETER_ATTRIBUTE_DIRECTION: 'vx_enum',
                     vx.PARAMETER_ATTRIBUTE_TYPE: 'vx_enum',
                     vx.PARAMETER_ATTRIBUTE_STATE: 'vx_enum',
                     vx.PARAMETER_ATTRIBUTE_REF: 'vx_reference'}

        if attribute not in attr_type:
            return vx.FAILURE
        if size != OpenVxApi.pyapi.ffi.sizeof(attr_type[attribute]):
            return vx.FAILURE
        status, value = vx.QueryParameter(param, attribute)
        ptr = OpenVxApi.pyapi.ffi.cast(attr_type[attribute] + "*", ptr)
        if attr_type[attribute] == 'vx_reference':
            ptr[0] = OpenVxApi.pyapi.store(value)
        else:
            ptr[0] = value
        return status

    # ========================================================================
    # FOR TESTS
    # ========================================================================
    @export("int(vx_reference, vx_reference)")
    def same_pyobj(ref1, ref2):
        return ref1 is ref2



def build(prefix='/usr/local'):
    from pyvx.inc.vx import ffi
    import os
    from distutils.dir_util import copy_tree

    libdir = os.path.join(prefix, 'lib')
    incdir = os.path.join(prefix, 'include', 'VX')
    if not os.path.exists(libdir):
        os.makedirs(libdir)
    if not os.path.exists(incdir):
        os.makedirs(incdir)

    api = PythonApi(OpenVxApi, ffi)
    api.build('openvx', __version__, soversion, libdir)
    srcdir = os.path.join(os.path.dirname(__file__), 'inc', 'headers', 'VX')
    copy_tree(srcdir, incdir)
    os.system('ldconfig')

    return api.library_names

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'build' and len(sys.argv) in (2,3):
        build(*sys.argv[2:])
    else:
        print 'Usage: %s build [<prefix>]' % sys.argv[0]
