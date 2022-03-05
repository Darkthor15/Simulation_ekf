# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from depthGet/BboxL.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class BboxL(genpy.Message):
  _md5sum = "a686645d937a65fb5a698081320dca73"
  _type = "depthGet/BboxL"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 minx
float64 miny
float64 maxx
float64 maxy
float64 navi
float64 centerx
float64 centery
"""
  __slots__ = ['minx','miny','maxx','maxy','navi','centerx','centery']
  _slot_types = ['float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       minx,miny,maxx,maxy,navi,centerx,centery

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BboxL, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.minx is None:
        self.minx = 0.
      if self.miny is None:
        self.miny = 0.
      if self.maxx is None:
        self.maxx = 0.
      if self.maxy is None:
        self.maxy = 0.
      if self.navi is None:
        self.navi = 0.
      if self.centerx is None:
        self.centerx = 0.
      if self.centery is None:
        self.centery = 0.
    else:
      self.minx = 0.
      self.miny = 0.
      self.maxx = 0.
      self.maxy = 0.
      self.navi = 0.
      self.centerx = 0.
      self.centery = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_7d().pack(_x.minx, _x.miny, _x.maxx, _x.maxy, _x.navi, _x.centerx, _x.centery))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 56
      (_x.minx, _x.miny, _x.maxx, _x.maxy, _x.navi, _x.centerx, _x.centery,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_7d().pack(_x.minx, _x.miny, _x.maxx, _x.maxy, _x.navi, _x.centerx, _x.centery))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 56
      (_x.minx, _x.miny, _x.maxx, _x.maxy, _x.navi, _x.centerx, _x.centery,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
